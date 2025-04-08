# -*- coding: utf-8 -*-

import logging
import requests

from dynamics365crm.client import Client
from werkzeug.urls import url_quote_plus

from odoo import api, fields, models, _
from odoo.http import request
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DynamicsCrm(models.Model):
    _name = 'lu.dynamics.crm'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Dynamics CRM"
    _order = 'id desc'

    name = fields.Char(required=True, index=True)
    domain = fields.Char('Domain')
    region = fields.Char('Region')
    client_id = fields.Char('Client ID')
    client_secret = fields.Char('Client Secret')
    tenant_id = fields.Char('Tenant Id', default="common")
    scope = fields.Char('Scope')

    def _get_state(self, redirect=None):
        redirect = redirect or 'web'
        if not redirect.startswith(('//', 'http://', 'https://')):
            redirect = '%s%s' % (request.httprequest.url_root, redirect[1:] if redirect[0] == '/' else redirect)
        state = dict(
            d=request.session.db,
            p=self.id,
            r=url_quote_plus(redirect),
        )
        return state

    def _get_scope(self):
        scope = f'https://{self.domain}.api.{self.region}.dynamics.com/.default'
        if self.scope:
            scope += " %s" % self.scope
        return scope

    def _get_token_url(self):
        return f'https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token'

    def get_access_token(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': self._get_scope()
        }
        access_token = None
        try:
            response = requests.post(self._get_token_url(), headers=headers, data=data)
            if response.status_code == 200:
                response_dict = response.json()
                access_token = response_dict['access_token']
            elif response.status_code == 401:
                raise ValidationError(_('Error with one or several invalid parameters on the POST request during authentication. Please contact an administrator. (%s)', response.text))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ValidationError(_('Cannot connect with the servers. Please contact an administrator. (%s)', e))
        return access_token

    def _get_client(self):
        access_token = self.get_access_token()
        client = Client(
            f'https://{self.domain}.api.{self.region}.dynamics.com',
            client_id=self.client_id,
            client_secret=self.client_secret,
            access_token=access_token
        )
        return client

    def action_get_contacts(self):
        client = self._get_client()
        try:
            contacts = client.get_contacts()
        except requests.exceptions.ConnectionError as e:
            raise ValidationError(_("Could not establish the connection to the API.\n%s", e))
        except requests.exceptions.HTTPError as e:
            raise ValidationError(_("The communication with the API failed: %s") % e)
        except Exception as e:
            raise ValidationError(e)
        _logger.debug(contacts)
        self.message_post(body=_("Get Contacts Success: %s") % contacts.get('@odata.context'))

    def action_get_accounts(self):
        client = self._get_client()
        try:
            accounts = client.get_accounts()
        except requests.exceptions.ConnectionError as e:
            raise ValidationError(_("Could not establish the connection to the API.\n%s", e))
        except requests.exceptions.HTTPError as e:
            raise ValidationError(_("The communication with the API failed: %s") % e)
        except Exception as e:
            raise ValidationError(e)
        _logger.debug(accounts)
        self.message_post(body=_("Get Accounts Success: %s") % accounts.get('@odata.context'))

    def action_get_opportunities(self):
        client = self._get_client()
        try:
            opportunities = client.get_opportunities()
        except requests.exceptions.ConnectionError as e:
            raise ValidationError(_("Could not establish the connection to the API.\n%s", e))
        except requests.exceptions.HTTPError as e:
            raise ValidationError(_("The communication with the API failed: %s") % e)
        except Exception as e:
            raise ValidationError(e)
        _logger.debug(opportunities)
        self.message_post(body=_("Get Opportunities Success: %s") % opportunities.get('@odata.context'))

    def action_get_leads(self):
        client = self._get_client()
        try:
            leads = client.get_leads()
        except requests.exceptions.ConnectionError as e:
            raise ValidationError(_("Could not establish the connection to the API.\n%s", e))
        except requests.exceptions.HTTPError as e:
            raise ValidationError(_("The communication with the API failed: %s") % e)
        except Exception as e:
            raise ValidationError(e)
        _logger.debug(leads)
        self.message_post(body=_("Get Leads Success: %s") % leads.get('@odata.context'))

    def action_get_campaigns(self):
        client = self._get_client()
        try:
            campaigns = client.get_campaigns()
        except requests.exceptions.ConnectionError as e:
            raise ValidationError(_("Could not establish the connection to the API.\n%s", e))
        except requests.exceptions.HTTPError as e:
            raise ValidationError(_("The communication with the API failed: %s") % e)
        except Exception as e:
            raise ValidationError(e)
        _logger.debug(campaigns)
        self.message_post(body=_("Get Campaigns Success: %s") % campaigns.get('@odata.context'))
