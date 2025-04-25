{
    'name': 'Account Sub-accounts',
    'version': '16.0.1.0.0',
    'summary': 'Add sub-account fields in res.partners and account.move.line, and sync them.',
    'author': 'Elabore',
    'website': 'https://elabore.coop/',
    'license': 'AGPL-3',
    'category': 'Accounting',
    'depends': [
        'account',
        'base',
    ],
    'data': [
        'views/res_partner_views.xml',
        'views/account_move_line_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {},
}
