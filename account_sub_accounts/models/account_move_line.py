from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    sub_account_customer = fields.Char(
        string="Custommer sub-account",
        related="partner_id.sub_account_customer"
    )

    sub_account_supplier = fields.Char(
        string="Supplier sub-account",
        related="partner_id.sub_account_supplier"
    )
