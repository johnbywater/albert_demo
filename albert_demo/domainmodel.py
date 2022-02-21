# -*- coding: utf-8 -*-
from typing import Type

from eventsourcing.domain import Aggregate, event


class Task(Aggregate):
    @event("Registered")
    def __init__(self, name: str) -> None:
        self.name = name
        self.status: str = "not started"

    StatusChanged: Type[Aggregate.Event["Task"]]

    @event("StatusChanged")
    def set_status(self, status: str) -> None:
        self.status = status
