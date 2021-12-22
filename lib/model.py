from pathlib import Path
from itertools import takewhile
import sys, shutil, csv, copy, random
from subprocess import call, DEVNULL

def data_and_names(file_name):
    data = []
    input_lines = {}
    line_num = -1
    with open(file_name) as f:
        f_reader = csv.reader(f, delimiter = ' ', skipinitialspace = True)
        for row in f_reader:
            line = list(takewhile(lambda s: s!='#', row))
            if len(line) != 0:
                line_num += 1
                if line[0] == 'Block':
                    block = line[1]
                else:
                    parameter_name = block+'_'+'_'.join(line[:-1])
                    input_lines[parameter_name] = line_num
                data.append(line)
    return data, input_lines

def constructor(self, executable, scenario):
    Class = self.__class__
    self.scenario = scenario
    self.exe = executable
    self.data = copy.deepcopy(Class.data)
    for parameter, value in scenario.input.items():
        self.data[Class.input_lines[parameter]][-1] = str(value)

def run(self):
    self.temporary_dir = Path.cwd().joinpath('wd_'+str(random.random()))
    self.temporary_dir.mkdir()
    self.in_slha  = self.temporary_dir.joinpath('in.slha')
    self.out_slha = self.temporary_dir.joinpath('out.slha')

    with open(self.in_slha, 'w', newline='') as f:
        out = csv.writer(f, delimiter=' ')
        for row in self.data:
            out.writerow(row)

    command = [self.exe,
        '--slha-input-file=' + str(self.in_slha),
        '--slha-output-file=' + str(self.out_slha)]

    return call(command, stdout=DEVNULL, stderr=DEVNULL)

def clear(self):
    self.in_slha.unlink(True)
    self.out_slha.unlink(True)
    self.temporary_dir.rmdir()

def make_output_lines(self):
    self.run()
    new_data = data_and_names(self.out_slha)

    lines = {}
    for parameter in self.scenario.output:
        lines[parameter] = new_data[1][parameter]
    lines = dict(sorted(lines.items(), key=lambda item: item[1]))

    self.__class__.output_lines = lines
    self.clear()

def run_and_save(self):
    flag = self.run()
    if flag == 0:
        with open(self.out_slha) as f:
            f_reader = csv.reader(f, delimiter = ' ', skipinitialspace = True)
            numbers = self.__class__.output_lines.values()
            rows = [row for idx, row in enumerate(f_reader) if idx in numbers]

            keys = self.__class__.output_lines.keys()
            vals = []
            for row in rows:
                vals.append(float(list(takewhile(lambda s: s!='#', row))[-1]))
            result = dict(zip(keys, vals))
    else:
        result = {}

    self.clear()
    return flag, result

# TODO(uukhas): add synonims for input_lines keys.
def load_model(args, Scenario):
    """
    Create a class for a given model.
    """
    default_slha = Path(args.slha).resolve()
    local_slha = Path.cwd().joinpath(default_slha.name).resolve()

    if not local_slha.exists():
        print('File '+str(local_slha)+' does not exist.')
        print('Copying '+str(default_slha)+' to '+str(Path.cwd())+'.')
        if not default_slha.exists():
            print('Error: '+str(default_slha)+' does not exist.')
            sys.exit(2)
        shutil.copy(str(default_slha), str(local_slha))

    class_attributes = data_and_names(local_slha)
    test_scenario = Scenario(1)

    required_lines = {}
    for parameter, value in test_scenario.input.items():
        required_lines[parameter] = class_attributes[1][parameter]

    # Creating class dynamically.
    Model = type('Model', (object, ), {
        '__init__': constructor,
        'data': class_attributes[0],
        'input_lines': required_lines,
        'run': run,
        'clear': clear,
        'run_and_save': run_and_save,
        'make_output_lines': make_output_lines
    })

    # Running model once to get lines to parse.
    Model(args.executable, test_scenario).make_output_lines()

    return Model
