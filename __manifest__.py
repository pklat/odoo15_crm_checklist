# -*- coding: utf-8 -*-
{
    'name': "crm_checklist",
    'summary': """
       CRM-Erweiterung - Checklisten""",
    'description': """
        CRM-Erweiterung welche im CRM-Modul eine Checkliste als Notebook mit Progressbar hinzufügt.
    """,
    'author': "Paul Klat",
    'website': "https://www.manatec.de/",
    'category': 'Productivity',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/checklist.xml',
        # 'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [           
            "crm_checklist/static/src/js/update_progress.js",
        ],
        },
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
