# -*- coding: utf-8 -*-
{
    'name': "Contacts pour commerciaux",

    'summary': """ """,

    'description': """ """,

    'author': "My Company",
    'website': " ",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
