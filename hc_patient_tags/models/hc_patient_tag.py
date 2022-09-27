from random import randint
from odoo import models, fields, api


class Tag(models.Model):
    _name = 'hc.patient.tag'
    _description = "Patient Tag"
    _order = 'name'

    _sql_constraints = [('hc_patient_tag_name_unique', 'unique(name)', "Tag already exists!")]

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Tag Name", required=True, index=True)

    def get_default_color(self):
        return randint(1, 15)

    color = fields.Integer(string="Color Index (0-15)", default=lambda self: self.get_default_color())

    code = fields.Char(string="Code")

    patient_ids = fields.Many2many(
        comodel_name='hc.patient', relation='hc_patient_tags_rel',
        column1='tag_id', column2='patient_id',
        string="Patients",
    )

    patient_count = fields.Integer(
        compute='_compute_patient_count',
        string="Patient Count",
    )

    @api.depends('patient_ids')
    def _compute_patient_count(self):
        for tag in self:
            tag.patient_count = len(tag.patient_ids)
        return
