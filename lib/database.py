import os
from pathlib import Path
from orator import DatabaseManager, Schema

class Database:
    def __init__(self, args, Scenario):
        scenario_name = Path(args.scenario).stem + '.db'
        if Path(scenario_name).exists():
            Path(scenario_name).unlink(True)
        self.__table = 'data'
        config = {'sqlite': {'driver': 'sqlite', 'database': scenario_name}}
        self.__db = DatabaseManager(config)
        with Schema(self.__db).create(self.__table) as table:
            for col in Scenario(1).output:
                table.double(str(col), 15).nullable()

    def insert(self, data):
        self.__db.table(self.__table).insert(data)
