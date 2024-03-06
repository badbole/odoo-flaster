from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_template_ids = fields.Many2many(comodel_name='product.template', string='Allowed Products')
