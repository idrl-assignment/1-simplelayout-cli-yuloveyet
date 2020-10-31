import argparse
import os


def main():
    # define the input parse from cmd
    parser = argparse.ArgumentParser(prog='test')
    parser.add_argument('--board_grid', type=int, help='square size')
    parser.add_argument('--unit_grid', type=int, help='component size')
    parser.add_argument('--unit_n', type=int, help='component num')
    parser.add_argument('--positions', type=int,
                        nargs='*', help='location index')
    parser.add_argument('-o', '--outdir', type=str,
                        help='save path', default='example_dir')
    parser.add_argument('--file_name', type=str, default='example')
    args = parser.parse_args()  # reture the input args

    if args.board_grid % args.unit_grid != 0:
        print('modify unit_grid')
        exit()

    if len(args.positions) != args.unit_n:
        print('modify positions list')
        exit()
    for i in args.positions:
        if i > (args.board_grid/args.unit_grid)**2 or i < 1:
            print('modify positions num')
            exit()
            
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    file1 = args.outdir + '/' + args.file_name + '.mat'
    file2 = args.outdir + '/' + args.file_name + '.jpg'
    fo1 = open(file1, 'w')
    fo2 = open(file2, 'w')
    # fo1.write('test/n')
    # fo2.write('test')
    fo1.close()
    fo2.close()
    print('succeed')


if __name__ == "__main__":
    main()
