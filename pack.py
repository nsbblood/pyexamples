from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='This is what you need to know')
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')

args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text + '\n')

print(f'Wrote "{args.text}" to file "{args.output}"')