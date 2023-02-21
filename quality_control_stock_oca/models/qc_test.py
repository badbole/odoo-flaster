# Copyright 2010 NaN Projectes de Programari Lliure, S.L.
# Copyright 2014 Serv. Tec. Avanzados - Pedro M. Baeza
# Copyright 2014 Oihane Crucelaegui - AvanzOSC
# Copyright 2017 ForgeFlow S.L.
# Copyright 2017 Simone Rubino - Agile Business Group
# Copyright 2022 ICRC
# Copyright 2022 Davor Bojkić - Daj Mi 5
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, exceptions, fields, models


class QcTest(models.Model):
    _inherit = "qc.test"


    def object_selection_values(self):
        res = super().object_selection_values()
        if isinstance(res, set):
            res = []
        res.extend([
            ("stock.picking", 'Stock Picking'),
            ('stock.lot', 'Stock  production Lot')
        ])
        return res
