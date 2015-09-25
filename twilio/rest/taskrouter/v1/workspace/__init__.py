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
from twilio.rest.taskrouter.v1.workspace.activity import ActivityList
from twilio.rest.taskrouter.v1.workspace.event import EventList
from twilio.rest.taskrouter.v1.workspace.statistics import StatisticsContext
from twilio.rest.taskrouter.v1.workspace.task import TaskList
from twilio.rest.taskrouter.v1.workspace.task_queue import TaskQueueList
from twilio.rest.taskrouter.v1.workspace.worker import WorkerList
from twilio.rest.taskrouter.v1.workspace.workflow import WorkflowList


class WorkspaceList(ListResource):

    def __init__(self, version):
        super(WorkspaceList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = "/Workspaces".format(**self._kwargs)

    def read(self, friendly_name=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "FriendlyName": friendly_name,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            "FriendlyName": friendly_name,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, event_callback_url=values.unset,
               template=values.unset):
        data = values.of({
            "FriendlyName": friendly_name,
            "EventCallbackUrl": event_callback_url,
            "Template": template,
        })
        
        return self._version.create(
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        return WorkspaceContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        return '<Twilio.Taskrouter.V1.WorkspaceList>'


class WorkspaceContext(InstanceContext):

    def __init__(self, version, sid):
        super(WorkspaceContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = "/Workspaces/{sid}".format(**self._kwargs)
        
        # Dependents
        self._activities = None
        self._events = None
        self._tasks = None
        self._task_queues = None
        self._workers = None
        self._workflows = None
        self._statistics = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, friendly_name=values.unset,
               timeout_activity_sid=values.unset):
        data = values.of({
            "DefaultActivitySid": default_activity_sid,
            "EventCallbackUrl": event_callback_url,
            "FriendlyName": friendly_name,
            "TimeoutActivitySid": timeout_activity_sid,
        })
        
        return self._version.update(
            WorkspaceInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)

    @property
    def activities(self):
        if self._activities is None:
            self._activities = ActivityList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._activities

    @property
    def events(self):
        if self._events is None:
            self._events = EventList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._events

    @property
    def tasks(self):
        if self._tasks is None:
            self._tasks = TaskList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._tasks

    @property
    def task_queues(self):
        if self._task_queues is None:
            self._task_queues = TaskQueueList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._task_queues

    @property
    def workers(self):
        if self._workers is None:
            self._workers = WorkerList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._workers

    @property
    def workflows(self):
        if self._workflows is None:
            self._workflows = WorkflowList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._workflows

    @property
    def statistics(self):
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._statistics


class WorkspaceInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        super(WorkspaceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'default_activity_name': payload['default_activity_name'],
            'default_activity_sid': payload['default_activity_sid'],
            'event_callback_url': payload['event_callback_url'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'timeout_activity_name': payload['timeout_activity_name'],
            'timeout_activity_sid': payload['timeout_activity_sid'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = WorkspaceContext(
                self._version,
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def default_activity_name(self):
        """ The default_activity_name """
        return self._properties['default_activity_name']

    @property
    def default_activity_sid(self):
        """ The default_activity_sid """
        return self._properties['default_activity_sid']

    @property
    def event_callback_url(self):
        """ The event_callback_url """
        return self._properties['event_callback_url']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def timeout_activity_name(self):
        """ The timeout_activity_name """
        return self._properties['timeout_activity_name']

    @property
    def timeout_activity_sid(self):
        """ The timeout_activity_sid """
        return self._properties['timeout_activity_sid']

    def fetch(self):
        self._context.fetch()

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, friendly_name=values.unset,
               timeout_activity_sid=values.unset):
        self._context.update(
            default_activity_sid=default_activity_sid,
            event_callback_url=event_callback_url,
            friendly_name=friendly_name,
            timeout_activity_sid=timeout_activity_sid,
        )

    def delete(self):
        self._context.delete()

    @property
    def activities(self):
        return self._context.activities

    @property
    def events(self):
        return self._context.events

    @property
    def tasks(self):
        return self._context.tasks

    @property
    def task_queues(self):
        return self._context.task_queues

    @property
    def workers(self):
        return self._context.workers

    @property
    def workflows(self):
        return self._context.workflows

    @property
    def statistics(self):
        return self._context.statistics
