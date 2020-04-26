import time
import sys
import subprocess as sp

print("Program starting here...")

name = open("name.txt").read()
gitsha = None

try:
    sp.call("git --no-pager log HEAD".split())
except:
    pass

print("\nIn a forever loop")
count = 0
while True:
    count +=1
    sys.stdout.write(f"[stdout] #{count} | Hello {name}\n")
    sys.stdout.flush()
    sys.stderr.write(f"[stderr] #{count} | Hello {name}\n")
    sys.stderr.flush()
    time.sleep(2)

