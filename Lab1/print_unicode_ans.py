# -*- coding: utf-8 -*-
import sys
import unicodedata

def print_unicode_table(words):
    print(words)
    print("decimal hex chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if all(elem in name.lower() for elem in words):
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code += 1
# End print_unicode_table

# Start main script
words = None

if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
    else:
        words = sys.argv[1:]

if words:
    print_unicode_table(words)

#End main script
