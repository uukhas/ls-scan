from pathlib import Path
import shutil, sys
from lib.loadmodule import load_module

def load_scenario(args):
    """
    Load scenario from CWD.
    """
    asked_scenario = Path(args.scenario).resolve()
    local_scenario = Path.cwd().joinpath(asked_scenario.name).resolve()

    if not asked_scenario.exists():
        print("Error: "+str(asked_scenario)+" doesn't exist.")
        sys.exit(2)
    if not local_scenario == asked_scenario:
        print('Copying '+str(asked_scenario)+' to '+str(Path.cwd())+'.')
        local_scenario.unlink(True)
        shutil.copy(asked_scenario, local_scenario)

    Scenario = load_module('Scenario', local_scenario)

    return Scenario
