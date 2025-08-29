from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = "account.journal"

    prevent_reset_to_draft_sent_invoice = fields.Boolean("Prevent to reset to draft a sent invoice")
    prevent_deletion_of_posted_account_move = fields.Boolean("Prevent to delete an already posted account move")
    allow_bank_statement_deletion = fields.Boolean(
        "Allow bank statements deletion",
        help="Users with group Show Full Accounting Features (id: group_account_user) will be allowed to delete account bank statements "
             "and bank statement lines."
    )
