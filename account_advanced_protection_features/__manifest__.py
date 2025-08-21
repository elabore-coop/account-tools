# Copyright 2025 Boris Gallet, Clément Thomas, Quentin Mondot
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "account_advanced_protection_features",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Quentin Mondot",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Add several protection features about accounting",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "account"
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
