import re
import sys
print(len(re.sub("(dz=|c=|c-|d-|lj|nj|s=|z=)","?", sys.stdin.readline().rstrip())))
