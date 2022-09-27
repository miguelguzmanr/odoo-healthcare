{
    "name": "Patient Tags",
    "summary": "Organize and manage your patients using tags",
    "category": "Health Care/Health Care",
    "author": "Miguel Alejandro Guzmán Rodríguez",

    "version": "14.0.1.0",

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
