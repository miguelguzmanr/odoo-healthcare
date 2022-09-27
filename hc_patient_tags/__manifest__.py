{
    "name": "Patient Tags",
    "version": "14.0.1.0",
    "category": "Health Care/Health Care",

    "summary": "Organize and manage your patients using tags",
    "author": "Miguel Alejandro Guzmán Rodríguez",

    "website": "https://github.com/miguelguzmanr/odoo-healthcare",
    "license": "GPL-3",

    "depends": [
        "hc",
    ],

    "data": [
        # --------
        # Security
        # ========
        "security/ir_model_access_data.xml",

        # -----
        # Views
        # =====
        "views/hc_patient_tag_views.xml",
        "views/hc_patient_views.xml",
    ],
    "demo": [],

    "installable": True,
    "application": False,
}
