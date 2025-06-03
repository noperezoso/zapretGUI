import subprocess as sp
import os

class Service:
    def __init__(self, zapret_dir=None):
        if not zapret_dir:
            zapret_dir = os.getcwd() + '\\zapret-win-bundle-master\\zapret-winws'
        self.exec_dir = os.path.abspath(zapret_dir) + '\\'

    def create(self, args, name='winws', description='zapret DPI bypass software', start='auto'):
        args = ' '.join(args)
        binPath = f'"{self.exec_dir}winws.exe" {args}'
        displayName = f'zapret DPI bypass : {name}'
        self.delete(name)
        sp.run(['sc', 'create', name, 'start=', start, 'binPath=', binPath, 'DisplayName=', displayName])
        sp.run(['sc', 'description', name, description])


    def delete(self, name='winws'):
        self.stop(name)
        sp.run(['sc', 'delete', name])

    def start(self, name='winws'):
        sp.run(['sc', 'start', name])

    def stop(self, name='winws'):
        sp.run(['net', 'stop', name])


class Task:
    def __init__(self, zapret_dir=None):
        if not zapret_dir:
            zapret_dir = os.getcwd() + '\\zapret-win-bundle-master\\zapret-winws'
        self.exec_dir = os.path.abspath(zapret_dir) + '\\'

    def create(self, args, name='winws', schedule='onstart'):
        args = ' '.join(args)
        binPath = f'"{self.exec_dir}winws.exe" {args}'
        sp.run(['schtasks', '/Create', '/F', '/TN', name, '/NP', '/RU', '', '/SC', schedule, '/TR', binPath])

    def delete(self, name='winws'):
        self.stop(name)
        sp.run(['schtasks', '/Delete', '/TN', name, '/F'])

    def start(self, name='winws'):
        sp.run(['schtasks', '/Run', '/TN', name])

    def stop(self, name='winws'):
        sp.run(['schtasks', '/End', '/TN', name])


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
