from odoo import models, fields, api, _
from datetime import datetime, timedelta

class IcuDashboard(models.TransientModel):
    _name = 'hm.icu.dashboard'
    _description = 'ICU Dashboard'
    _transient = True

    total_patients = fields.Integer(string='Total ICU Patients', compute='_compute_stats')
    admitted_today = fields.Integer(string='Admitted Today', compute='_compute_stats')
    discharged_today = fields.Integer(string='Discharged Today', compute='_compute_stats')
    occupancy_rate = fields.Float(string='Occupancy Rate (%)', compute='_compute_stats')

    # Dummy fields to hold graph data – we'll use them to display graphs
    graph_data = fields.Char(compute='_compute_stats', string='Graph Data')

    def _compute_stats(self):
        today = fields.Date.today()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = start_of_day + timedelta(days=1)

        Admission = self.env['hm.icu.admission']
        Discharge = self.env['hm.icu.discharge']
        Bed = self.env['hm.icu.bed']

        total_admitted = Admission.search_count([('state', '=', 'admitted')])
        admitted_today = Admission.search_count([
            ('admission_date', '>=', start_of_day),
            ('admission_date', '<', end_of_day)
        ])
        discharged_today = Discharge.search_count([
            ('discharge_date', '>=', start_of_day),
            ('discharge_date', '<', end_of_day)
        ])
        total_beds = Bed.search_count([])
        occupied_beds = Bed.search_count([('state', '=', 'occupied')])
        occupancy = (occupied_beds / total_beds * 100) if total_beds else 0

        for rec in self:
            rec.total_patients = total_admitted
            rec.admitted_today = admitted_today
            rec.discharged_today = discharged_today
            rec.occupancy_rate = round(occupancy, 1)
            rec.graph_data = 'dummy'  # just to have a field