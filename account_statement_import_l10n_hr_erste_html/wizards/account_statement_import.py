# Copyright 2023 DAJ MI 5, Croatia (http://www.dajmi5.com/)
# @author: Davor Bojkić <bole@dajmi5.com>
# Licence AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from lxml import etree
from datetime import datetime
import logging
from odoo import models
from .erste_parser import ErsteParser as Parser

_logger = logging.getLogger(__name__)

class AccountStatementImport(models.TransientModel):
    _inherit = "account.statement.import"

    def _parse_file(self, data_file):
        """Parse a CROATIA-ERSTE html file."""
        try:
            parser = Parser()
            _logger.debug("Try parsing with l10n_hr_erste.")
            res = parser.parse(data_file.decode("utf-8"))
            # check multi currency journals
            return res

        except Exception as E:
            # Not a erste html file, returning super will call next candidate:
            _logger.debug("Statement file was not a ERSTE html file.",
                          exc_info=True)
        return super(AccountStatementImport, self)._parse_file(data_file)
