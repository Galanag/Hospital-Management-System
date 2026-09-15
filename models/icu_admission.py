from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class IcuAdmission(models.Model):
    _name = 'hm.icu.admission'
    _description = 'ICU Admission'
    _inherit = ['hm.base.mixin', 'mail.thread']
    _order = 'admission_date desc'

    name = fields.Char(string='ICU Admission #', readonly=True, copy=False, default=lambda self: _('New'))
    patient_id = fields.Many2one('hm.patient', string='Patient', required=True, tracking=True)
    admission_date = fields.Datetime(string='Admission Date', default=fields.Datetime.now, tracking=True)
    bed_id = fields.Many2one('hm.icu.bed', string='Bed', required=True)
    consultant_id = fields.Many2one('res.users', string='Consultant', domain=[('groups_id', '=', 'hm_icu.group_icu_doctor')])
    admission_diagnosis = fields.Text(string='Admission Diagnosis', required=True)
    severity = fields.Selection([
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
        ('critical', 'Critical')
    ], string='Severity', required=True, default='moderate')
    notes = fields.Text(string='Admission Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged')
    ], default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hm.icu.admission') or _('New')
        return super().create(vals_list)

    def action_admit(self):
        self.state = 'admitted'
        self.bed_id.state = 'occupied'
        self.bed_id.current_admission_id = self.id

    def action_discharge(self):
        self.state = 'discharged'
        self.bed_id.state = 'available'
        self.bed_id.current_admission_id = False