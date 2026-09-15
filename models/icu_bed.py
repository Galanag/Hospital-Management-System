from odoo import models, fields, api, _

class IcuBed(models.Model):
    _name = 'hm.icu.bed'
    _description = 'ICU Bed'
    _inherit = ['hm.base.mixin']

    name = fields.Char(string='Bed Number', required=True)
    room = fields.Char(string='Room')
    is_isolation = fields.Boolean(string='Isolation Room')
    state = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance')
    ], default='available', tracking=True)
    department_id = fields.Many2one('hm.department', string='Department')
    current_admission_id = fields.Many2one('hm.icu.admission', string='Current Admission')
    notes = fields.Text(string='Notes')