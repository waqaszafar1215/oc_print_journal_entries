# -*- coding: utf-8 -*-
{
    'name': 'Print Journal Entries Report in Odoo',
    'version': '0.0.1',
    'category': 'Accounting',
    'license': 'OPL-1',
    'summary': 'Allow to print pdf report of Journal Entries.',
    'description': """
    Allow to print pdf report of Journal Entries.
    journal entry
    print journal entry 
    journal entries
    print journal entry reports
    account journal entry reports
    journal reports
    account entry reports
    
""",
    'author': 'Odoo Circle',
    'depends': ['base','account'],
    'data': [
            'report/report_journal_entries.xml',
            'report/report_journal_entries_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    "images":["static/description/Banner.jpg"],
}

