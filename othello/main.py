from sys import path
path.append('src')
from othello import CuiRunner
from othello_gui import GuiRunner

from optparse import OptionParser
from sys import exit


def get_parser():
    parser = OptionParser('othello [option]')
    parser.add_option('--gui', action='store_true', default=False, dest='gui')
    parser.add_option('--cui', action='store_true', default=False, dest='cui')
    return parser


def main():
    parser = get_parser()
    (options, _) = parser.parse_args()

    if options.cui and options.gui:
        print("Can't set both cui and gui option.")
        exit()
    elif not options.cui:
        runner = GuiRunner()
    else:
        runner = CuiRunner()
    runner.main()

if __name__ == '__main__':
    main()
