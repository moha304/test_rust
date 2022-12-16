import sys
from prova.cli import randomData
import pytest

@pytest.fixture(autouse=True)
def sum():
    assert randomData(7,7) == 14
    assert randomData(8,7) == 15
    assert randomData(2,2) == 4


