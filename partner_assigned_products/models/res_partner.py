from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_template_ids = fields.Many2many(
        comodel_name='product.template',
        relation="product_template_partner_rel",
        column1="partner_id", column2="product_id",
        string='Allowed Products')
    product_variant_ids = fields.Many2many(
        comodel_name='product.product',
        relation="product_product_partner_rel",
        column1="partner_id", column2="product_id",
        string='Allowed Variants')
