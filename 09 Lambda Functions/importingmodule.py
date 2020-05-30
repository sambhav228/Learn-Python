'''Different ways of importing a module'''

import myMath

print(myMath.sum(10,5))
print(myMath.diff(10,5))


'''or'''

import myMath as ma             # giving a alias name to our module

print(ma.sum(10,5))
print(ma.diff(10,5))


'''or'''

from myMath import *            # This is the best one

print(sum(10,5))
print(diff(10,5))