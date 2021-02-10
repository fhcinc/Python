from GLDAlign import *
from GLDViewAligned import *

merfiles = ["01-Nov-2019-13-36-09HMS1.gld"]
eogfiles = ["01-Nov-2019-13-36-10HMS2LFS.gld"]

for k in range(0,len(merfiles)):
    print(merfiles[k])
    t1, t2 = gld_align(merfiles[k], eogfiles[k])
    gld_view_aligned(t1,t2)

