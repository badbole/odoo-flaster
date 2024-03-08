from odoo import fields, models, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tmpl_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        relation="product_template_partner_rel",
        column1="product_id", column2="partner_id",
        string='Template Customers'
    )

class Product(models.Model):
    _inherit = 'product.product'

    prod_partner_ids = fields.Many2many(
        comodel_name='res.partner',
        relation="product_product_partner_rel",
        column1="product_id", column2="partner_id",
        string='Variant Customers'
    )
