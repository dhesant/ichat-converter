from ccl_bplist import ccl_bplist
import sys
import os
import json
#import pprint

if (len(sys.argv) < 2):
    print("No argument. Usage: \"print_plist [FILE]\"")
    sys.exit(1)

fn = sys.argv[1]

if not os.path.isfile(fn):
    print("Invalid file")
    sys.exit(1)

with open(fn, "rb") as f:
    plist = ccl_bplist.load(f)
    
obj = ccl_bplist.deserialise_NsKeyedArchiver(plist)
ccl_bplist.set_object_converter(ccl_bplist.NSKeyedArchiver_common_objects_convertor)

with open(fn + ".json", "w") as f:
    f.write(json.dumps(obj, indent=4, sort_keys=True, default=str))

