import sqlite3

from model.explorer import Explorer
from data.init import conn, curs, IntegrityError

from errors import Missing, Duplicate

curs.execute(
    """
    create table if not exists explorer(
        name text primary key,
        country text,
        description text
    )
    """
)


def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()


def get_one(name: str) -> Explorer:
    query = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(msg=f"Explorer {name} not found")


def get_all() -> list[Explorer]:
    query = "select * from explorer"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    query = """insert into explorer values
            (:name, :country, :description)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f"Explorer {explorer.name} already exists")
    conn.commit()
    return get_one(explorer.name)


def modify(explorer: Explorer):
    query = """
            update explorer
            set country=: country,
                name=: name,
                description=: description,
            where name=:name_orig 
    """
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(query, params)
    if curs.rowcount == 1:
        conn.commit()
        return get_one(explorer.name)
    raise Missing(f"Explorer {explorer.name} not found")


def replace(explorer: Explorer):
    return explorer


def delete(explorer: Explorer):
    if not explorer.name:
        return False
    query = "delete from explorer where name = :name"
    params = {"name": explorer.name}
    res = curs.execute(query, params)
    if res.rowcount != 1:
        raise Missing(msg=f"Explorer {explorer.name} not foun")
    conn.commit()
    return bool(res)
