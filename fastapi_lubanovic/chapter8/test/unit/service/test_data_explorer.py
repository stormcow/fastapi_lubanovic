import os
import pytest
from model.explorer import Explorer
from errors import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import init, explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Bobby Brown",
        country="USA",
        description="He goes down",
    )


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        resp = explorer.create(sample)


def test_get_exists(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        resp = explorer.get_one("blackbox")

def test_delete(sample):
    resp = explorer.delete(sample)
    assert resp is True

def test_delete_missing(sample):
    with pytest.raises(Missing):
        resp = explorer.delete(sample)