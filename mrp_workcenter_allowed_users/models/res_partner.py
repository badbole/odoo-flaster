from odoo import api, fields, models, _

class Users(models.Model):
    _inherit = "res.users"

    allowed_workcenter_ids = fields.Many2many(
        comodel_name='mrp.workcenter',
        relation='mrp_workcenter_users_rel',
        column1="user_id", column2="workcenter_id",
        string="Allowed Workcenters"
    )
