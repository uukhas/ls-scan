import argparse
from regex import search
from pathlib import Path

class Parser:

    def __init__(self):
        """
        Read and store input arguments.

        For MODEL:
            We assume that executable has a name run_MODEL.x.
            We assume a LesHouches.in.MODEL name for a default template.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-D', '--ndots', type=int, required=True,
                        help='number of points to create')
        parser.add_argument('-P', '--nprocesses', type=int, required=True,
                        help='number of processes to launch')
        parser.add_argument('-S', '--scenario', type=str, required=True,
                        help='name of scenario to use')
        parser.add_argument('-X', '--executable', type=str, required=True,
                        help='executable path')
        self.args = parser.parse_args()
        path = Path(self.args.executable)
        model = path.parent.name
        self.args.model = model
        self.args.slha = path.parent.joinpath('LesHouches.in.'+model)
