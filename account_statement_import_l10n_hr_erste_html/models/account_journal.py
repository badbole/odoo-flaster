# @author: Davor Bojkić <bole@dajmi5.com>
# Licence LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import _, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def _get_bank_statements_available_import_formats(self):
        res = super(AccountJournal, self). \
            _get_bank_statements_available_import_formats()
        res.extend([('l10n_hr_erste_html'), _('Croatia-Erste-html')])
        return res
