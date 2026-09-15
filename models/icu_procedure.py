from odoo import models, fields, api

class IcuProcedure(models.Model):
    _name = 'hm.icu.procedure'
    _description = 'ICU Procedure'
    _inherit = ['hm.base.mixin', 'mail.thread']

    name = fields.Char(string='Procedure', required=True)
    patient_id = fields.Many2one('hm.patient', string='Patient', required=True)
    admission_id = fields.Many2one('hm.icu.admission', string='ICU Admission')
    procedure_type = fields.Selection([
        ('intubation', 'Intubation'),
        ('extubation', 'Extubation'),
        ('central_line', 'Central Line'),
        ('chest_tube', 'Chest Tube'),
        ('blood_transfusion', 'Blood Transfusion'),
        ('dialysis', 'Dialysis'),
        ('tracheostomy', 'Tracheostomy'),
        ('other', 'Other')
    ], string='Type', required=True)
    performed_by = fields.Many2one('res.users', string='Performed By')
    date_performed = fields.Datetime(string='Date Performed', default=fields.Datetime.now)
    outcome = fields.Text(string='Outcome')
    notes = fields.Text(string='Notes')