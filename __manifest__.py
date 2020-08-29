# -*- coding: utf-8 -*-
{
    'name': "DIU Regulations",

    'summary': """
        This repository contains all policies, guidelines etc. of Daffodil International University. Any faculty, student and administrative employee will be able to easily access to his/her required DIU regulations from this module """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Mahfuz",
    'website': "http://research.daffodilvarsity.edu.bd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/diu_regulations_security.xml',
        'security/ir.model.access.csv',
        'views/diu_regulations.xml',
        'views/menus.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
