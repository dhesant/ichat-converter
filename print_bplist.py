from ccl_bplist import ccl_bplist
import sys
import os
import pprint

if (len(sys.argv) < 2):
    print("No argument. Usage: \"print_plist [FILE]\"")
    sys.exit(1)

fn = sys.argv[1]

if os.path.isfile(fn):
    f = open(fn, "rb")
    plist = ccl_bplist.load(f)
    obj = ccl_bplist.deserialise_NsKeyedArchiver(plist)
    pp=pprint.PrettyPrinter(indent=1)
    pp.pprint(obj)

else:
    print("Invalid file")


