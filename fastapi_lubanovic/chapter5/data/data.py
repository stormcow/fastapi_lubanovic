from ..models.creature import Creature

_creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CH",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    ),
    Creature(
        name="sasquatch",
        country="US",
        area="*",
        description="Yetis Cousin",
        aka="bigfood",
    ),
]


def get_creatures() -> list[Creature]:
    return _creatures
