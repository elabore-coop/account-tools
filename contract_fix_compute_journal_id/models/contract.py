from odoo import models, api


class Contract(models.Model):
    _inherit = 'contract.contract'

    @api.depends("contract_type", "company_id")
    def _compute_journal_id(self):
        AccountJournal = self.env["account.journal"]
        for contract in self:
            contract_template = contract.contract_template_id
            if (
                    contract_template
                    and contract_template.journal_id
                    and contract_template.contract_type
                    and contract.contract_type
                    and contract.contract_type == contract_template.contract_type
                    and contract.company_id == contract_template.company_id
            ):
                contract.journal_id = contract_template.journal_id
            else:
                domain = [
                    ("type", "=", contract.contract_type),
                    ("company_id", "=", contract.company_id.id),
                ]
                journal = AccountJournal.search(domain, limit=1)
                if journal:
                    contract.journal_id = journal.id
                else:
                    contract.journal_id = None
