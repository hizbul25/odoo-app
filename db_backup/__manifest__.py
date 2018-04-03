# -*- coding: utf-8 -*-
{
    'name': "Database Backup",

    'summary': """
        Backup Your database as your defined time.
        """,

    'description': """
        This module allows you to backup your database at your defined directory in your defined time.
        
        For any kind of module customization feel free to knock me:
        Email: hizbul25@gmail.com
        Skype: hizbul_ku
        Whatsapp: +8801918019179
        Configuration
    """,

    'author': "Molla IT",
    'website': "https://stackoverflow.com/cv/hizbul",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/db_backup_scheduler_views.xml',
        'views/res_config_settings_db_backup_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}