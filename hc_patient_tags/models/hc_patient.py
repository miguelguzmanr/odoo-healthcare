from odoo import models, fields


class Patient(models.Model):
    _inherit = 'hc.patient'

    tag_ids = fields.Many2many(
        comodel_name='hc.patient.tag', relation='hc_patient_tags_rel',
        column1='patient_id', column2='tag_id',
        string="Tags",
    )
