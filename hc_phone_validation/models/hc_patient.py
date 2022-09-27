from odoo import api, models


class Patient(models.Model):
    _name = 'hc.patient'
    _inherit = ['hc.patient', 'phone.validation.mixin']

    @api.onchange('phone', 'country_id')
    def _onchange_phone_validation(self):
        if self.phone:
            self.phone = self.phone_format(self.phone)

    @api.onchange('mobile', 'country_id')
    def _onchange_mobile_validation(self):
        if self.mobile:
            self.mobile = self.phone_format(self.mobile)
