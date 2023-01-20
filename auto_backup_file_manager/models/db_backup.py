from odoo import _, api, exceptions, fields, models, tools
import os


class DbBackup(models.Model):
    _inherit = "db.backup"

    backup_files = fields.Text(
        compute="_get_available_files",
        string="Available files"
    )

    @api.depends("folder", "method")
    def _get_available_files(self):
        for record in self:
            if record.method == "sftp":
                record.backup_files = "Not yet covered - sftp"
                continue
            files = [a for a in os.listdir(record.folder) if a not in [".", ".."]]
            record.backup_files = "\n".join(files)
