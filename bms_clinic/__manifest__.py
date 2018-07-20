# -*- coding: utf-8 -*-
{
    'name': "Quản lý phòng khám",

    'summary': """
        Module quản lý phòng khám của BMS TECHNOLOGY""",

    'description': """
        Module quản lý phòng khám của BMS TECHNOLOGY
    """,

    'author': "BMS TECHNOLOGY",
    'website': "http://www.bmstech.io",
    #support for show when filter App
    'installable': True,
    'application': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'BMS Clinic',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'views/bms_hr_employee_view.xml',
    ],
}
