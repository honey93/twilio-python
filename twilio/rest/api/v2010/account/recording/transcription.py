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


class TranscriptionList(ListResource):

    def __init__(self, version, account_sid, recording_sid):
        super(TranscriptionList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'recording_sid': recording_sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions.json".format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            TranscriptionInstance,
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
            TranscriptionInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        return TranscriptionContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        return '<Twilio.Api.V2010.TranscriptionList>'


class TranscriptionContext(InstanceContext):

    def __init__(self, version, account_sid, recording_sid, sid):
        super(TranscriptionContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'recording_sid': recording_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            TranscriptionInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)


class TranscriptionInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, recording_sid, sid=None):
        super(TranscriptionInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'duration': payload['duration'],
            'owner_account_sid': payload['owner_account_sid'],
            'price': payload['price'],
            'price_unit': payload['price_unit'],
            'recording_sid': payload['recording_sid'],
            'sid': payload['sid'],
            'status': payload['status'],
            'transcription_text': payload['transcription_text'],
            'type': payload['type'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'recording_sid': recording_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TranscriptionContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['recording_sid'],
                self._context_properties['sid'],
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
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def duration(self):
        """ The duration """
        return self._properties['duration']

    @property
    def owner_account_sid(self):
        """ The owner_account_sid """
        return self._properties['owner_account_sid']

    @property
    def price(self):
        """ The price """
        return self._properties['price']

    @property
    def price_unit(self):
        """ The price_unit """
        return self._properties['price_unit']

    @property
    def recording_sid(self):
        """ The recording_sid """
        return self._properties['recording_sid']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def status(self):
        """ The status """
        return self._properties['status']

    @property
    def transcription_text(self):
        """ The transcription_text """
        return self._properties['transcription_text']

    @property
    def type(self):
        """ The type """
        return self._properties['type']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
