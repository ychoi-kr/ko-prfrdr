import glob
import os
import argparse


def insert_fig_num(new_fig_num, dry_run):
    for name in glob.glob('*.*'):
        oldname = name

        name, ext = name.rsplit('.', 1)

        if name.startswith('그림 '):
            prefix = '그림 '
            name = name.split(' ', 1)[1]
        else:
            prefix = ''

        if ' ' in name:
            fig_num, title = name.split(' ', 1)
        else:
            fig_num = name
            title = ''

        ch_num, fig_num = map(int, fig_num.split('.', 1))

        if int(new_fig_num) <= fig_num:
            fig_num += 1
            newname = f'{prefix}{ch_num}.{fig_num} {title}.{ext}'
            print(f'Renaming {oldname} to {newname} ...')

            if dry_run:
                pass
            else:
                os.rename(oldname, newname)
        else:
            print(f'{oldname} is not be changed.')

    print('Done.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("new_fig_num")
    parser.add_argument('--dry_run', action="store_true")
    args = parser.parse_args()
    insert_fig_num(args.new_fig_num, args.dry_run)
