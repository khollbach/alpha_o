import sys
import os

def main(argv):
    if len(argv) == 2 and argv[1] == '-v':
        args = ' -v'
    else:
        args = ''
    os.system('python3 ../main/color.py' + args)
    os.system('python3 ../main/file_io.py' + args)
    os.system('python3 ../main/preprocess.py' + args)
    os.system('python3 ../main/puzzle.py' + args)

if __name__ == '__main__':
    main(sys.argv)
