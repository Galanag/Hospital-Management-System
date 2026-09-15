from odoo import models, fields, api

class IcuNursingNote(models.Model):
    _name = 'hm.icu.nursing.note'
    _description = 'ICU Nursing Note'
    _inherit = ['hm.base.mixin', 'mail.thread']
    _order = 'note_date desc'

    patient_id = fields.Many2one('hm.patient', string='Patient', required=True)
    admission_id = fields.Many2one('hm.icu.admission', string='ICU Admission')
    note_date = fields.Datetime(string='Date/Time', default=fields.Datetime.now, required=True)
    shift = fields.Selection([
        ('day', 'Day'),
        ('night', 'Night')
    ], string='Shift', required=True)
    nurse_id = fields.Many2one('res.users', string='Nurse', default=lambda self: self.env.user)
    observations = fields.Text(string='Observations', required=True)
    medication_administered = fields.Text(string='Medications Given')
    fluid_balance = fields.Text(string='Fluid Balance')
    pain_assessment = fields.Text(string='Pain Assessment')
    tasks_performed = fields.Text(string='Tasks Performed')
    handover_notes = fields.Text(string='Handover Notes')