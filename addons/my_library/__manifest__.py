# -*- coding: utf-8 -*-
{
    'name': "my_library",

    'summary': """
        Testing Module created by Tiago Martins""",

    'description': """
        My First Module of library created for odoo for testing purporses.
    """,

    'author': "Tiago Martins Andrade",
    'website': "https://www.linkedin.com/in/tiago-martins-andrade/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/library_book.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
