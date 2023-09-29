import sqlite3

from model.creature import Creature
from data.init import conn, curs, IntegrityError
from errors import Missing, Duplicate

curs.execute(
    """
    create table if not exists creature(
        name text primary key,
        description text,
        country text,
        area text,
        aka text
    )
    """
)


def row_to_model(row: tuple) -> Creature:
    return Creature(
        name=row[0], country=row[1], area=row[2], description=row[3], aka=row[4]
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def get_one(name: str) -> Creature:
    query = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(msg=f"Creature {name} not found")


def get_all() -> list[Creature]:
    query = "select * from creature"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    query = """insert into creature values
            (:name, :country, :area, :description, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f"Creature {creature.name} already exists")
    conn.commit()
    return get_one(creature.name)


def modify(creature: Creature):
    query = """
            update creature
            set name=: name,
                country=: country,
                area=: area,
                description=: description,
                aka=: aka,
            where name=:name_orig 
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute(query, params)
    if curs.rowcount == 1:
        conn.commit()
        return get_one(creature.name)
    raise Missing(f"Explorer {creature.name} not found")


def replace(creature: Creature):
    return creature


def delete(creature: Creature):
    query = "delete from creature where name = :name"
    params = {"name": creature.name}
    res = curs.execute(query, params)
    if res.rowcount != 1:
        raise Missing(msg=f"Creature {creature.name} not found")
    conn.commit()
    return bool(res)
