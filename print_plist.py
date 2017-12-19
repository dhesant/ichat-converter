import plistlib
import sys
import os
import pprint

if (len(sys.argv) < 2):
    print("No argument. Usage: \"print_plist [FILE]\"")
    sys.exit(1)

fn = sys.argv[1]

if os.path.isfile(fn):
    f = plistlib.readPlist(fn)
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(f)

else:
    print("Invalid file")


