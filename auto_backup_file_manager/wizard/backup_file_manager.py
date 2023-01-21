import os
from odoo import _, api, exceptions, fields, models, tools



class DbBackupManager(models.TransientModel):
    _name = "db.backup.manager"
    _description = "Manager for backup files"


    backup_id = fields.Many2one(
        comodel_name="db.backup",
        required=True
    )
    folder = fields.Char(related="backup_id.folder", readonly=True)
    method = fields.Selection(related="backup_id.method", readonly=True)
    file_ids = fields.One2many(
        comodel_name="db.backup.manager.file",
        inverse_name="manager_id",
    )



class DbBackupManagerFile(models.TransientModel):
    _name = "db.backup.manager.file"
    _description = "Available backup files"



    manager_id = fields.Many2one(comodel_name="db.backup.manager")
    name = fields.Char(string="File name")
    size = fields.Integer(readonly=1)
    size_kb = fields.Float(compute="_compute_size")
    size_mb = fields.Float(compute="_compute_size")
    size_gb = fields.Float(compute="_compute_size")

    @api.depends("size")
    def _compute_size(self):
        for file in self:
            file.size_kb = file.size / 1024
            file.size_mb = file.size_kb / 1024
            file.size_gb = file.size_mb / 1024


    def action_delete_file(self):
        for file in self:
            path = "/".join([file.manager_id.folder, file.name])
            try:
                os.remove(path)
            except Exception as E:
                raise E
            file.manager_id.backup_id._get_available_files()
            file.unlink()
        #return {"type": "ir.actions.do_nothing"}
