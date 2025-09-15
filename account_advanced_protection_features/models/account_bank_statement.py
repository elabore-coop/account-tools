from odoo import models, _
from odoo.exceptions import UserError

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    def unlink(self):
        for statement in self:
            if not statement.journal_id.allow_bank_statement_deletion:
                raise UserError(
                    _("The deletion of bank statements is not allowed for the journal %s.") % statement.journal_id.display_name
                )
            # we delete all the statement lines before deleting the statement itself
            for line in statement.line_ids:
                line.unlink()
        return super(AccountBankStatement, self).unlink()


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    def unlink(self):
        for line in self:
            if not line.journal_id.allow_bank_statement_deletion:
                raise UserError(
                    _("The deletion of bank statement lines is not allowed for the journal %s.") % line.journal_id.display_name
                )
        return super(AccountBankStatementLine, self).unlink()
