from odoo import api, fields, models, _

class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    allowed_user_ids = fields.Many2many(
        comodel_name='res.users',
        relation='mrp_workcenter_users_rel',
        column1="workcenter_id", column2="user_id",
        string="Allowed users",
        domain=lambda self: [("groups_id", "=",
                              self.env.ref("mrp.group_mrp_user").id)]
    )
