from ccl_bplist import ccl_bplist
import sys
import os
#import pprint

if (len(sys.argv) < 2):
    print("No argument. Usage: \"print_plist [FILE]\"")
    sys.exit(1)

fn = sys.argv[1]

if not os.path.isfile(fn):
    print("Invalid file")
    sys.exit(1)

f = open(fn, "rb")
plist = ccl_bplist.load(f)
obj = ccl_bplist.deserialise_NsKeyedArchiver(plist)
ccl_bplist.set_object_converter(ccl_bplist.NSKeyedArchiver_common_objects_convertor)

lst = obj['NS.objects'][2]

print("Time,Sender,Message,BColor, Font, FColor, FSize")

for msg in lst:
    if msg['Sender'] is None:
        print(msg['Time'], ",\"", msg['MessageText']['NSString'], "\" , System")
    else:
        print(msg['Time'], ",\"", msg['MessageText']['NSString'], "\",\"", msg['Sender']['ID'], "\",\"", msg['Color']['NSRGB'], "\",\"", msg['MessageText']['NSAttributes']['NSFont']['NSName'], "\",\"", msg['MessageText']['NSAttributes']['NSColor']['NSRGB'], "\",", msg['MessageText']['NSAttributes']['NSFont']['NSSize'])



