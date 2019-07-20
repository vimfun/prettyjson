r"""Command-line tool to validate and pretty-print JSON

Usage::

    $ echo '{"json":"obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

"""
import argparse
import json
import sys


def main():
    prog = 'python -m json.tool'
    description = ('A simple command line interface for json module '
                   'to validate and pretty-print JSON objects.')
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('infile', nargs='?', type=argparse.FileType(),
                        help='a JSON file to be validated or pretty-printed',
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        help='write the output of infile to outfile',
                        default=sys.stdout)
    parser.add_argument('--sort-keys', action='store_true', default=False,
                        help='sort the output of dictionaries alphabetically by key')
    parser.add_argument('--json-lines', action='store_true', default=False,
                        help='parse input using the jsonlines format')
    parser.add_argument('--indent', type=int, default=4,
                        help='generate pretty-printed JSON with the custom indent level, default value is 4')
    parser.add_argument('--no-ensure-ascii', action='store_true', default=False, help='not ensure_ascii')

    options = parser.parse_args()

    infile       = options.infile
    outfile      = options.outfile
    sort_keys    = options.sort_keys
    json_lines   = options.json_lines
    indent       = options.indent
    ensure_ascii = not options.no_ensure_ascii
    with infile, outfile:
        try:
            if json_lines:
                objs = (json.loads(line) for line in infile)
            else:
                objs = (json.load(infile), )

            for obj in objs:
                json.dump(obj, outfile, sort_keys=sort_keys, indent=indent, ensure_ascii=ensure_ascii)
                outfile.write('\n')
        except ValueError as e:
            raise SystemExit(e)


if __name__ == '__main__':
    main()
