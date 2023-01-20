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
            if  not record.folder or not os.path.exists(record.folder):
                record.backup_files = "Backup folder not yet configured!"
                continue
            files = [a for a in os.listdir(record.folder) if a not in [".", ".."]]
            if files:
                files.sort()
                record.backup_files = "\n".join(files)
            else:
                record.backup_files = "No backup files found!"
