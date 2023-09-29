import os
import pytest
from model.creature import Creature
from errors import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import init, creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        resp = creature.create(sample)


def test_get_exists(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        resp = creature.get_one("blackbox")

def test_delete(sample):
    resp = creature.delete(sample)
    assert resp is True

def test_delete_missing(sample):
    with pytest.raises(Missing):
        resp = creature.delete(sample)