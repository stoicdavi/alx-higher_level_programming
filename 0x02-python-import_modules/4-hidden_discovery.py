#!/usr/bin/python3
if __name__ == '__main__':
    import importlib
    modules = importlib.import_module('hidden_4')

    func_names = [name for name in dir(modules) if not name.startswith('__')]
    func_names.sort()

    for func_name in func_names:
        if func_name.startswith('print'):
            continue
        print(func_name)
        func = getattr(modules, func_name)
        print(func)
