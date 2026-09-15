from odoo import models, fields, api

class IcuClinicalNote(models.Model):
    _name = 'hm.icu.clinical.note'
    _description = 'ICU Clinical Note'
    _inherit = ['hm.base.mixin', 'mail.thread']

    patient_id = fields.Many2one('hm.patient', string='Patient', required=True)
    admission_id = fields.Many2one('hm.icu.admission', string='ICU Admission')
    note_type = fields.Selection([
        ('daily_progress', 'Daily Progress'),
        ('consultant', 'Consultant Note'),
        ('resident', 'Resident Note'),
        ('nutrition', 'Nutrition Note'),
        ('respiratory', 'Respiratory Therapy Note'),
        ('care_plan', 'Care Plan')
    ], string='Type', required=True)
    date_time = fields.Datetime(string='Date/Time', default=fields.Datetime.now)
    doctor_id = fields.Many2one('res.users', string='Doctor')
    content = fields.Html(string='Note', required=True)