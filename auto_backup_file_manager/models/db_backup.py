import os
from odoo import _, api, exceptions, fields, models, tools
from odoo.exceptions import UserError



class DbBackup(models.Model):
    _inherit = "db.backup"

    backup_files = fields.Text(
        compute="_get_available_files",
        string="Available files"
    )

    def _get_local_files(self):
        """
        :return: list of file names form folder configured for backup
        """
        self.ensure_one()
        res = []
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                res.append((file, size))
        return res

    @api.depends("folder", "method")
    def _get_available_files(self):
        for record in self:
            if record.method == "sftp":
                record.backup_files = "Not yet covered - sftp"
                continue
            if not record.folder or not os.path.exists(record.folder):
                record.backup_files = "Backup folder not yet configured!"
                continue
            files = record._get_local_files()
            if files:
                files.sort()
                res = ""
                for file, size in files:
                    res += "\n" + " - ".join((file, str(size)))
                record.backup_files = res
            else:
                record.backup_files = "No backup files found!"

    def action_file_manager(self):
        self.ensure_one()
        if self.method == "sftp":
            raise UserError(_("Not yet implemented"))

        # now local files only
        files = self._get_local_files()
        if not files:
            raise UserError(_("No files found on backup location"))

        file_lines = [(0, 0, {'name': f, "size": s}) for (f, s) in files]
        manager = self.env["db.backup.manager"].create({
            "backup_id": self.id,
            "file_ids": file_lines
        })
        view = self.env.ref("auto_backup_file_manager.db_file_manager_wizard")
        return {
            "res_model": "db.backup.manager",
            "res_id": manager.id,
            "target": "new",
            "type": "ir.actions.act_window",
            "view_mode": "form",
        }
