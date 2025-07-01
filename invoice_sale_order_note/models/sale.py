# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.sale.models.sale_order import LOCKED_FIELD_STATES


class SaleOrder(models.Model):
    _inherit = "sale.order"

    report_note = fields.Html("Note", states=LOCKED_FIELD_STATES,)

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res["report_note"] = self.report_note
        return res
    
    @api.onchange('sale_order_template_id')
    def _onchange_sale_order_template_id_report_note(self):
        if self.sale_order_template_id and self.sale_order_template_id.report_note:
            self.report_note = self.sale_order_template_id.report_note
