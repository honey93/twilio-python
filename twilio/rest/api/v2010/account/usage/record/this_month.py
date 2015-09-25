# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class ThisMonthList(ListResource):

    def __init__(self, version, account_sid):
        super(ThisMonthList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Usage/Records/ThisMonth".format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            ThisMonthInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            ThisMonthInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self):
        return ThisMonthContext(self._version, **self._kwargs)

    def __repr__(self):
        return '<Twilio.Api.V2010.ThisMonthList>'


class ThisMonthContext(InstanceContext):

    def __init__(self, version):
        super(ThisMonthContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = "None".format(**self._kwargs)


class ThisMonthInstance(InstanceResource):

    def __init__(self, version, payload, account_sid):
        super(ThisMonthInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'category': payload['category'],
            'count': payload['count'],
            'count_unit': payload['count_unit'],
            'description': payload['description'],
            'end_date': deserialize.rfc2822_datetime(payload['end_date']),
            'price': payload['price'],
            'price_unit': payload['price_unit'],
            'start_date': deserialize.rfc2822_datetime(payload['start_date']),
            'subresource_uris': payload['subresource_uris'],
            'uri': payload['uri'],
            'usage': payload['usage'],
            'usage_unit': payload['usage_unit'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = ThisMonthContext(
                self._version,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def category(self):
        """ The category """
        return self._properties['category']

    @property
    def count(self):
        """ The count """
        return self._properties['count']

    @property
    def count_unit(self):
        """ The count_unit """
        return self._properties['count_unit']

    @property
    def description(self):
        """ The description """
        return self._properties['description']

    @property
    def end_date(self):
        """ The end_date """
        return self._properties['end_date']

    @property
    def price(self):
        """ The price """
        return self._properties['price']

    @property
    def price_unit(self):
        """ The price_unit """
        return self._properties['price_unit']

    @property
    def start_date(self):
        """ The start_date """
        return self._properties['start_date']

    @property
    def subresource_uris(self):
        """ The subresource_uris """
        return self._properties['subresource_uris']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    @property
    def usage(self):
        """ The usage """
        return self._properties['usage']

    @property
    def usage_unit(self):
        """ The usage_unit """
        return self._properties['usage_unit']
