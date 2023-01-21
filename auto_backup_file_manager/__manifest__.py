
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Auto backup - file manager",
    "version": "16.0.1.0.0",
    "author": "Daj mi 5",
    "category": "Tools",
    "website": "https://github.com/OCA/server-tools",
    "license": "AGPL-3",
    "summary": "Backups file manager",
    "depends": [
        'auto_backup',
    ],
    'data': [
        "views/db_backup_views.xml",
        "wizard/db_file_manager_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
