from odoo import api, fields, models, _

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    allowed_user_ids = fields.Many2many(
        related='workcenter_id.allowed_user_ids',
        relation='workorder_user_rel',
        column1="workorder_id", column2="user_id",
        readonly=True, store=True
    )
