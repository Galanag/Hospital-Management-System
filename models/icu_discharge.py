from odoo import models, fields, api

class IcuDischarge(models.Model):
    _name = 'hm.icu.discharge'
    _description = 'ICU Discharge'
    _inherit = ['hm.base.mixin', 'mail.thread']

    admission_id = fields.Many2one('hm.icu.admission', string='ICU Admission', required=True)
    patient_id = fields.Many2one('hm.patient', string='Patient', related='admission_id.patient_id', store=True)
    discharge_date = fields.Datetime(string='Discharge Date', default=fields.Datetime.now)
    discharge_type = fields.Selection([
        ('transfer_ward', 'Transfer to Ward'),
        ('referral', 'Referral'),
        ('death', 'Death')
    ], string='Discharge Type', required=True)
    final_diagnosis = fields.Text(string='Final Diagnosis', required=True)
    discharge_summary = fields.Text(string='Discharge Summary')
    follow_up_recommendations = fields.Text(string='Follow-up Recommendations')
    notes = fields.Text(string='Notes')