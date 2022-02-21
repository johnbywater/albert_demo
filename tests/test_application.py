# -*- coding: utf-8 -*-
from albert_demo.application import Tasks


def test_tasks() -> None:
    # Construct application object.
    app = Tasks()

    # Call application command methods.
    task_id = app.register_task("My Task")
    app.set_status(task_id, "started")

    # Call application query method.
    assert app.get_task(task_id) == {
        "name": "My Task",
        "status": "finished",
    }
