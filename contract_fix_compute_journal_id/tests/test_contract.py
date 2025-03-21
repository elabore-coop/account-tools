from odoo.addons.contract.tests.test_contract import TestContractBase


class TestContract(TestContractBase):
    def test_compute_journal_id(self):
        self.contract.contract_template_id = self.template
        self.contract._compute_journal_id()
        self.assertEqual(self.contract.journal_id, self.template.journal_id)

        new_journal = self.env["account.journal"].create(
            {
                "name": "Test journal",
                "code": "foo",
                "type": "sale",
            }
        )
        new_template = self.env["contract.template"].create(
            {
                "name": "Test Contract Template Journal ID",
                "journal_id": new_journal.id,
            }
        )
        self.contract.contract_template_id = new_template
        self.contract._compute_journal_id()
        self.assertEqual(self.contract.journal_id, new_template.journal_id)
