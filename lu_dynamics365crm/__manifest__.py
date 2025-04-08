# -*- coding: utf-8 -*-
{
    'name': 'Dynamics 365 CRM Connector',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Integrate Microsoft Dynamics 365 CRM with Odoo',
    'description': """
Dynamics 365 CRM Connector
===========================
This module allows you to connect and synchronize data between Odoo and Microsoft Dynamics 365 CRM. 
It provides the following key features:
- Authentication using OAuth2 client credentials.
- Fetch and manage Contacts, Accounts, Leads, Opportunities, and Campaigns from Dynamics 365 CRM.
- Dynamic scope and region support for global compatibility.
- Logging and chatter notifications for data retrieval success.
- Secure management of sensitive credentials.
    """,
    'author': 'Linkup Infotech Inc.',
    'website': 'https://www.link-up.co.kr',
    'depends': ['base', 'mail'],
    'external_dependencies': {'python': ['dynamics365crm-python']},
    'data': [
        'security/ir.model.access.csv',
        'views/dynamics_crm_views.xml',
    ],
    'application': True,
    'images': ['static/description/banner.png'],
    'license': 'Other proprietary',
}
