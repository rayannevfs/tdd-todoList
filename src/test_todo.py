import os
import io
import sys
import builtins
import pytest

def test_add_task_success_and_list(tmp_path):
    tasks = []
    tasks.append("Comprar leite", "integral")
    assert len(tasks) == 2

