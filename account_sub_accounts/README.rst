====================
account_sub_accounts
====================

Add sub-account fields in res.partners and account.move.line, and sync them.

Installation
============

Use Odoo normal module installation procedure to install
``account_sub_account``.

Description
===========

- adds sub_account_customer and sub_account_supplier to res.partner model
- adds sub_account_customer and sub_account_supplier to account.move.line model
- when a account.move.line is created, sub_account_customer and sub_account_supplier fields are sync with the parner_id corresponding values

Known issues / Roadmap
======================

None yet.

Bug Tracker
===========

Bugs are tracked on `our issues website <https://github.com/elabore-coop/account-tools/issues>`_. In case of
trouble, please check there if your issue has already been
reported. If you spotted it first, help us smashing it by providing a
detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Stéphan Sainléger - https://github.com/stephansainleger

Funders
-------

The development of this module has been financially supported by:
* Elabore (https://elabore.coop)


Maintainer
----------

This module is maintained by Elabore.
