from odoo import models, fields, api

class IcuMonitoring(models.Model):
    _name = 'hm.icu.monitoring'
    _description = 'ICU Monitoring'
    _inherit = ['hm.base.mixin', 'mail.thread']
    _order = 'timestamp desc'

    patient_id = fields.Many2one('hm.patient', string='Patient', required=True)
    admission_id = fields.Many2one('hm.icu.admission', string='ICU Admission')
    timestamp = fields.Datetime(string='Time', default=fields.Datetime.now, required=True)
    temperature = fields.Float(string='Temperature (°C)')
    blood_pressure_systolic = fields.Integer(string='Systolic BP')
    blood_pressure_diastolic = fields.Integer(string='Diastolic BP')
    pulse = fields.Integer(string='Pulse (bpm)')
    respiratory_rate = fields.Integer(string='Respiratory Rate')
    oxygen_saturation = fields.Float(string='SpO₂ (%)')
    ecg_summary = fields.Text(string='ECG Summary')
    fluid_intake = fields.Float(string='Fluid Intake (ml)')
    fluid_output = fields.Float(string='Fluid Output (ml)')
    urine_output = fields.Float(string='Urine Output (ml)')
    weight = fields.Float(string='Weight (kg)')
    pain_score = fields.Selection([
        ('0', '0 - No pain'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5 - Moderate'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10 - Worst pain')
    ], string='Pain Score')
    gcs = fields.Integer(string='Glasgow Coma Scale', help='Sum of eye, verbal, motor (3-15)')
    notes = fields.Text(string='Notes')