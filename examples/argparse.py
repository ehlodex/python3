import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--all', action='store_true')
parser.add_argument('-b', '--bot', action='store_true')
parser.add_argument('-c', '--car', action='store_true')
parser.add_argument('-d', '--dog', action='store_true')
parser.add_argument('-e', '--egg', action='store_true')
args = parser.parse_args()

# Default action if no arguments are supplied.
# This only works for a small number or arguments.
if args.all or (args.bot == args.car == args.dog == args.egg):
    args.bot = args.car = args.dog = args.egg = True

print(f'b: {args.bot}')
print(f'c: {args.car}')
print(f'd: {args.dog}')
print(f'e: {args.egg}')