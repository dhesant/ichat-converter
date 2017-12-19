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

lst = obj['NS.objects'][2]['NS.objects']

print("Time,Sender,Message(,BColor, Font, FColor, FSize")

for msg in lst:
    if msg['Sender'] == '$null':
        print(msg['Time']['NS.time'], ",", msg['OriginalMessage'], " , System")
    else:
        print(msg['Time']['NS.time'], ",", msg['OriginalMessage'], ",", msg['Sender']['ID'], ",", msg['Color']['NSRGB'], ",", msg['MessageText']['NSAttributes']['NS.objects'][2]['NSName'], ",", msg['MessageText']['NSAttributes']['NS.objects'][0]['NSRGB'], ",", msg['MessageText']['NSAttributes']['NS.objects'][2]['NSSize'])



