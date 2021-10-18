import glob
import os


def pad(digit):
    for name in glob.glob('*'):
        if name.startswith('그림 '):
            newname = '그림 ' + str(digit) + name.split(' ', 1)[1]
        elif name[0] in '123456789':
            newname = str(digit) + name
        else:
            newname = None

        if newname:
            print(f'Renaming {name} to {newname} ...')
            os.rename(name, newname)
        else:
            print('Cannot find expected pattern.')

    print('Done.')
