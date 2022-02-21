# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Union, cast
from uuid import UUID

from eventsourcing.application import Application, ProcessingEvent
from eventsourcing.domain import Aggregate, AggregateEvent, LogEvent
from eventsourcing.persistence import Recording

from albert_demo.domainmodel import Task


class Tasks(Application):
    def register_task(self, name: str) -> UUID:
        task = Task(name)
        self.save(task)
        return task.id

    def set_status(self, task_id: UUID, status: str) -> None:
        task = cast(Task, self.repository.get(task_id))
        task.set_status(status)
        self.save(task)

    def get_task(self, task_id: UUID) -> Dict[str, Any]:
        task = cast(Task, self.repository.get(task_id))
        return {"name": task.name, "status": task.status}

    def _record(self, processing_event: ProcessingEvent) -> List[Recording]:
        event_counter = 0
        while event_counter < len(processing_event.events):
            new_event = processing_event.events[event_counter]
            self.policy(new_event, processing_event)
            event_counter += 1
        return super()._record(processing_event)

    def policy(
        self,
        domain_event: Union[AggregateEvent[Any], LogEvent],
        processing_event: ProcessingEvent,
    ) -> None:
        if isinstance(domain_event, Task.StatusChanged):
            task = cast(
                Task,
                self._get_aggregate_within_policy(
                    processing_event, domain_event.originator_id
                ),
            )
            if task.status == "started":
                task.set_status("finished")
                processing_event.collect_events(task)

    def _get_aggregate_within_policy(
        self, processing_event: ProcessingEvent, aggregate_id: UUID
    ) -> Aggregate:
        return processing_event.aggregates.get(aggregate_id) or self.repository.get(
            aggregate_id
        )
