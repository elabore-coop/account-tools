from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = "account.journal"

    prevent_reset_to_draft_sent_invoice = fields.Boolean("Prevent to reset to draft a sent invoice")
