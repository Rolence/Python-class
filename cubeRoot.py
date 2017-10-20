#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:10:14 2017

@author: root
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:57:58 2017

@author: root
"""

x = 27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print ('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ('numGuesses =', numGuesses)
print (ans, 'is close to square root of', x)