from odoo import models, _
from odoo.exceptions import UserError

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    def unlink(self):
        for statement in self:
            if not statement.journal_id.allow_bank_statement_deletion:
                raise UserError(
                    _(f"The deletion of bank statements is not allowed for the journal {statement.journal_id.display_name}.")
                )
        return super(AccountBankStatement, self).unlink()
