{
    'name': 'HM ICU',
    'version': '18.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'Intensive Care Unit Management',
    'description': 'Manages ICU admissions, beds, monitoring, ventilators, nursing notes, procedures, and discharge.',
    'author': 'Galana G.',
    'depends': ['base', 'mail', 'hmis', 'hm_patient', 'web'],
    'data': [
        'security/hm_icu_groups.xml',
        'security/ir.model.access.csv',
        'data/icu_sequence.xml',
        'data/icu_config_data.xml',
        # ---- ACTION-DEFINING VIEWS (load before menus) ----
        'views/icu_admission_views.xml',      # defines action_icu_admission
        'views/icu_bed_views.xml',            # defines action_icu_bed
        'views/icu_monitoring_views.xml',     # defines action_icu_monitoring
        'views/icu_ventilator_views.xml',     # defines action_icu_ventilator
        'views/icu_nursing_note_views.xml',   # defines action_icu_nursing_note
        'views/icu_procedure_views.xml',      # defines action_icu_procedure
        'views/icu_clinical_note_views.xml',  # defines action_icu_clinical_note
        'views/icu_discharge_views.xml',      # defines action_icu_discharge
        'views/icu_dashboard_views.xml',      # defines action_icu_dashboard
        'views/icu_reports_views.xml',        # defines action_icu_reports
        # ---- MENUS (now all actions exist) ----
        'views/icu_menus.xml',
        'reports/icu_reports.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}