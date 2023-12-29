# © 2023 DAJ MI 5 <https://www.dajmi5.hr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from lxml import etree
from datetime import datetime

class ErsteParser(object):
    """Parser for Croatia ERSTE html bank statement import files."""


    def _get_amount(self, amount):
        try:
            amount = amount.replace('.', '').replace(',', '.')
            amount = float(amount)
        except:
            amount = None
        return amount

    def convert_date(self, date):
        try:
            date = datetime.strptime(date, "%d.%m.%Y.").strftime("%Y-%m-%d")
        except:
            date = date
        return date

    def parse(self, data):
        """Parse a erste html file."""
        try:
            root = etree.fromstring(
                data.replace('<br>', '[|]'), parser=etree.XMLParser(recover=True))

        except Exception as E:
            root = None
        if root is None:
            raise ValueError(
                'Not a valid erste html file, or not an xml file at all.')

        statements = []
        currency_code = None
        account_number = None
        #speeddict =
        for el in root.xpath(".//div[@id='Generalno']"):
            spans = el.xpath(".//span")
            if len(spans) < 3:
                continue
            if "IBAN:" in spans[0].text:
                account_number = spans[2].text
            elif "Oznaka valute:" in spans[0].text:
                currency_code = spans[2].text
            elif "Broj izvoda:" in spans[0].text:
                broj_izvoda = spans[2].text


        for stanje in root.xpath(".//table[@class='tbHeadDown']"):
            st = stanje.xpath(".//tr/td")
            amount = self._get_amount(st[5].text)
            if "etno" in st[0].text:    # Početno
                balance_start = amount
            elif "Kona" in st[0].text:  # Konačno
                balance_end_real = amount
        transactions = []
        for item in root.findall(".//tr[@class='trItems']"):
            trans = {}
            lines = item.findall('td')  # item.xpath("./td")
            #trans['name'] = lines[2].text
            trans['date'] = self.convert_date(lines[0].text.split('[|]')[1])
            trans['account_number'] = lines[1].text.split('[|]')[1]
            trans['partner_name'] = lines[1].text.split('[|]')[0]
            ref = lines[3].text.split('[|]')
            trans['ref'] = ref[1] != 'HR99' and ref[1] or None
            trans['payment_ref'] = ref[2]
            trans['unique_import_id'] = trans['account_number'] + currency_code + ref[2]
            trans['amount'] = lines[5].text is None and - self._get_amount(lines[4].text) or self._get_amount(lines[5].text)
            trans['raw_data'] = etree.tostring(item)
            if trans:
                transactions.append(trans)
        statements.append({
            'name': 'Izvod Erste-%s-%s' % (currency_code, broj_izvoda),
            'date': trans['date'], #TODO: bolje ... ne biti ljen!
            'balance_start': balance_start,
            'balance_end_real': balance_end_real,
            'transactions': transactions

        })
        return currency_code, account_number, statements
