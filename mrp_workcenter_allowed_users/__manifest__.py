# © 2018 Davor Bojkić - Bole <bole@dajmi5.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP Workcenter - allowed users",
    "summary": "Alow users to see only operations from selected workcenters",
    "category": "Manufacture",
    "images": [],
    "version": "16.0.1.0.0",
    "application": False,
    "author": "Davor Bojkić (DAJ MI 5)",
    "license": "AGPL-3",
    "depends": [
        "mrp",
    ],
    "data": [
        "security/security.xml",
        "views/mrp_workcenter_views.xml",
        "views/mrp_workorder_views.xml",
        "views/res_user_views.xml",
    ],
    "qweb": [],
    "demo": [],
    "auto_install": False,
    "installable": True,
}
