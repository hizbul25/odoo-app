# -*- coding: utf-8 -*-
{
    'name': "Database Backup",

    'summary': """
        Backup Your database as your defined time.
        """,

    'description': """
        =======================
        Database Backup
        =======================
        
        This module allows you to backup your database at your defined directory in your defined time.
        
        Configuration
        =============
        
        * Active developer mode.
        * Go Settings > General Settings > Database Backup
        * Set your database name and path where you want to save your database.
        
        Usage
        =====
        
        Set scheduler
        -------------------------------
        
        #. Go to 'Settings / Automation / Scheduler Actions'
        #. Find out 'Database Backup' and set Execute Every and Next Execution Date as per you
        Preference.
        
        Contributors
        ------------
        
        * Hizbul Bahar <hizbul25@gmail.com>
        
        Notice
        ----------
        For any kind of module customization feel free to knock me:
        Email: hizbul25@gmail.com
        Skype: hizbul_ku
        Whatsapp: +8801918019179
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