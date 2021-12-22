#!/usr/bin/env python3
from lib.parser import Parser
from lib.scenario import load_scenario
from lib.model import load_model
from lib.points import Points
from lib.database import Database
from tqdm import tqdm
from multiprocessing import Pool

def run_model(i):
    model = Model(args.executable, Scenario(i))
    return model.run_and_save()

def operate_result(result):
    if result[0] == 0:
        points.update()
        db.insert(result[1])
    pbar.update()

if __name__ == '__main__':
    args = Parser().args
    Scenario = load_scenario(args)
    Model = load_model(args, Scenario)

    Model(args.executable, Scenario(1)).run_and_save()

    db = Database(args, Scenario)
    points = Points(args, Scenario)
    with tqdm(total = points.all) as pbar:
        pool = Pool(processes = args.nprocesses)
        for i in range(points.all):
            pool.apply_async(run_model, args = (i,), callback = operate_result)
        pool.close()
        pool.join()
