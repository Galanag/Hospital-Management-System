from odoo import models, fields, api

class IcuVentilator(models.Model):
    _name = 'hm.icu.ventilator'
    _description = 'Ventilator'
    _inherit = ['hm.base.mixin']

    name = fields.Char(string='Ventilator ID', required=True)
    model = fields.Char(string='Model')
    assignment_id = fields.Many2one('hm.icu.ventilator.assignment', string='Current Assignment')

class IcuVentilatorAssignment(models.Model):
    _name = 'hm.icu.ventilator.assignment'
    _description = 'Ventilator Assignment'
    _inherit = ['hm.base.mixin', 'mail.thread']

    patient_id = fields.Many2one('hm.patient', string='Patient', required=True)
    admission_id = fields.Many2one('hm.icu.admission', string='ICU Admission')
    ventilator_id = fields.Many2one('hm.icu.ventilator', string='Ventilator', required=True)
    start_date = fields.Datetime(string='Start Date', default=fields.Datetime.now)
    end_date = fields.Datetime(string='End Date')
    mode = fields.Selection([
        ('ac', 'Assist-Control'),
        ('simv', 'SIMV'),
        ('psv', 'Pressure Support'),
        ('cpap', 'CPAP')
    ], string='Mode', required=True)
    peep = fields.Float(string='PEEP (cmH₂O)')
    fio2 = fields.Float(string='FiO₂ (%)')
    rate = fields.Integer(string='Rate (breaths/min)')
    tidal_volume = fields.Integer(string='Tidal Volume (ml)')
    pressure_support = fields.Integer(string='Pressure Support (cmH₂O)')
    notes = fields.Text(string='Notes')