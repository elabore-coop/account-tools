from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    sub_account_customer = fields.Char(string="Custommer sub-account")
    sub_account_supplier = fields.Char(string="Supplier sub-account")
