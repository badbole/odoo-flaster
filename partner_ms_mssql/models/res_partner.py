from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    icrc_identifier = fields.Char()


    def _get_db_server(self):
        # implenment any server search logic if more than one
        srv = self.env[("base.external.dbsource")].search([], limit=1)[0]
        return srv


    def mssql_test_orm(self):
        db_server = self._get_db_server()

    def mssql_sync_partners(self):
        db_server = self._get_db_server()
        qry = """
        select id, first_name, last_name from partner
        """
        param = None
        meta = ("first_name", "last_name", "id")
        res = db_server.execute_mssql(qry, param, meta)
        res_json = db_server.execute_mssql_json(qry, param, meta)

        print(res)
        print(res_json)

