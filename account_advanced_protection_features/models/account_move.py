from odoo import models, api, fields, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def button_draft(self):
        if self.is_move_sent and self.journal_id.prevent_reset_to_draft_sent_invoice:
            raise UserError(_(
                "You cannot reset to draft this invoice because it has been sent by email."
            ))
        return super(AccountMove, self).button_draft()

    @api.ondelete(at_uninstall=False)
    def _check_posted(self):
        """ Prevent deletion of an account move if it has already been posted and
        journal parameter prevent_deletion_of_posted_account_move is activated
        """
        for rec in self:
            if rec.posted_before and rec.journal_id.prevent_deletion_of_posted_account_move:
                raise UserError(_(
                    "You cannot delete this account move because it has already been posted."
                ))
