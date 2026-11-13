HM ICU – Intensive Care Unit Management for Odoo 18

Odoo License
🏥 Overview

HM ICU is a comprehensive Odoo 18 module designed to manage all aspects of an Intensive Care Unit.

It provides full‑cycle ICU workflows — from admission and bed management, through continuous monitoring and ventilator tracking, to discharge and reporting — while integrating seamlessly with the existing hmis core and hm_patient modules.
✨ Features
Feature 	Description
ICU Dashboard 	At‑a‑glance KPIs: occupancy, admissions, discharges, ventilator usage, critical patients
Admissions 	Full ICU admission process with bed assignment, consultant, severity classification, and admission notes
Bed Management 	Track beds, isolation rooms, occupancy, cleaning, and maintenance status
Continuous Monitoring 	Capture vitals (BP, pulse, SpO₂), GCS, pain score, fluid balance, and hourly observations
Ventilator Management 	Assign ventilators, track modes (AC, SIMV, PSV, CPAP), PEEP, FiO₂, and alarm history
Nursing Notes 	Shift‑based notes, medication administration, fluid balance, pain assessment, and handover
Procedures 	Log intubations, central lines, chest tubes, transfusions, dialysis, and more
Clinical Notes 	Daily progress, consultant/resident notes, nutrition, and respiratory therapy notes
Discharge 	Transfer to ward, referral, or death summary with final diagnosis and follow‑up
Reports 	Interactive pivot/graph views + printable PDF reports for admissions and discharges
🔗 Dependencies

    base
    mail
    hmis (core mixin & departments)
    hm_patient (patient records)

    All optional integrations (lab, radiology, pharmacy, billing, HR, etc.) are prepared and will be activated when the corresponding modules are installed.

🚀 Installation

    Place the hm_icu folder in your Odoo addons path.
    Restart your Odoo server.
    Go to Apps → Update Apps List.
    Search for HM ICU and click Install.

    Make sure hmis and hm_patient are installed first.

🧪 Quick Start

After installation, you will see a new ICU top‑level menu with the following entries:

    Dashboard
    Admissions
    Beds
    Monitoring
    Ventilators
    Nursing Notes
    Procedures
    Clinical Notes
    Discharge
    Reports

Start by creating a Bed (Configuration is not required – beds are created from the Beds menu), then admit a patient, and begin tracking their care.
🛠️ Development
Structure
Odoo 18 Compliance

    No attrs or states – fully compatible with Odoo 18’s view validation.
    Uses hm.base.mixin from the hmis core module.
    All sequences generated via ir.sequence.
    Role‑based access: ICU Nurse, ICU Doctor, ICU Manager.

📊 Reports

Two interactive reports are available from the Reports menu:

    ICU Occupancy Report – pivot and graph views by severity, state, and admission date.
    ICU Discharge Report – pivot and graph views by discharge type and date.

You can also print detailed PDF reports from any admission or discharge record.
🤝 Contributing

    Fork the repository.
    Create a feature branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -am 'Add some feature').
    Push to the branch (git push origin feature/your-feature).
    Open a Pull Request.

📄 License

This module is distributed under the LGPL‑3 license. See the LICENSE file for more details.
🙏 Acknowledgements

Built as part of the HMIS project for BelTech Solutions.

Happy coding! 🚀
