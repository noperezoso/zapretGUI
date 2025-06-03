import subprocess as sp
import os


EXEC_DIR = os.path.abspath('zapret-win-bundle-master\\zapret-winws')

class Exec:
    def __init__(self, exec_dir=EXEC_DIR):
        self.exec_dir = os.path.abspath(exec_dir)
        self.name='winws'

    def start(self, args):
        sp.run([f'{self.exec_dir}\\winws.exe', *args])

    def stop(self):
        sp.run(['taskkill', '/F', '/IM', 'winws.exe'])


class Service(Exec):
    def create(self, args, description='zapret DPI bypass software', start='auto'):
        args = ' '.join(args)
        binPath = f'"{self.exec_dir}\\winws.exe" {args}'
        displayName = f'zapret DPI bypass : {self.name}'
        self.delete()
        sp.run(['sc', 'create', self.name, 'start=', start, 'binPath=', binPath, 'DisplayName=', displayName])
        sp.run(['sc', 'description', self.name, description])


    def delete(self):
        self.stop()
        sp.run(['sc', 'delete', self.name])

    def start(self):
        sp.run(['sc', 'start', self.name])

    def stop(self):
        sp.run(['net', 'stop', self.name])


class Task(Exec):
    def create(self, args, schedule='onstart'):
        args = ' '.join(args)
        binPath = f'"{self.exec_dir}\\winws.exe" {args}'
        sp.run(['schtasks', '/Create', '/F', '/TN', self.name, '/NP', '/RU', '', '/SC', schedule, '/TR', binPath])

    def delete(self):
        self.stop()
        sp.run(['schtasks', '/Delete', '/TN', self.name, '/F'])

    def start(self):
        sp.run(['schtasks', '/Run', '/TN', self.name])

    def stop(self):
        sp.run(['schtasks', '/End', '/TN', self.name])


class ArgParser:
    def __init__(self, strategies_dir=None):
        if strategies_dir:
            self.strat_dir = strategies_dir
        else:
            self.strat_dir = EXEC_DIR

        self.get_strat_files()

    def filter_args(self, args):
        '''Clean and adjust arguments.'''
        if type(args) is str:
            args = args.replace('^', '').replace(' \\', '')
            args = args.split()

        for i in range(len(args)):
            args[i] = args[i].strip().replace('"', '')
            args[i] = args[i].replace('%~dp0', EXEC_DIR + '\\')
        
        return args

    def get_strat_files(self):
        '''Get the list of strategy files.'''
        if not os.path.exists(self.strat_dir):
            self.strat_files = dict()
            return
        
        strat_files = dict()
        for obj in os.listdir(self.strat_dir):
            if obj.rsplit('.')[-1] in ('cmd', 'bat'):
                strat_files.update([[obj, f'{self.strat_dir}\\{obj}']])
        
        self.strat_files = strat_files

    def import_args(self, path):
        with open(path, 'r') as arg_source:
            arg_lines = list()
            for line in arg_source.readlines():
                if line[0]=='-':
                    arg_lines.append(line)
        return ''.join(arg_lines)
