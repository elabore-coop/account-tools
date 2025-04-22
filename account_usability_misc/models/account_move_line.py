from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    reconcile_filter = fields.Boolean(
        string='Reconcile Filter', default=True, compute='_compute_reconcile_filter', store=True
    )

    @api.depends('date', 'date_maturity')
    def _compute_reconcile_filter(self):
        for rec in self:
            rec.reconcile_filter = rec.date.day % 2 == 0
