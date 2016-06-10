#!/usr/bin/env python
# Command-line program to use the parser to reflow
# a Python 2.6 program
import os, sys
from py2_scan import ENDMARKER
from py2_format import format_python2_stmts

if len(sys.argv) < 2:
    print("I need a filename to reformat")
    sys.exit(1)

for path in sys.argv[1:]:
    if not os.path.exists(path):
        print("Can't find file %s; skipping", path)
        continue

    with open(path, 'r') as fp:
        python2_stmts = fp.read()

        print(python2_stmts)
        formatted = format_python2_stmts(python2_stmts + ENDMARKER,
                                         show_tokens=True, showast=True,
                                         showgrammar=True)
        print('=' * 30)
        print(formatted)
        pass
    pass