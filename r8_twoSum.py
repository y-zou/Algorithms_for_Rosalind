A=[6,-7,2,3,-2,1,-1,0,11,-11]
import math
import collections

sum_dict=collections.defaultdict(list) #the value should be a list of adjacent vertex

for i in range(0,len(A)):
#math.abs(key) doesn't work on my machine somehow
    key = A[i]
    if key>0: sign=1
    else: sign =-1
    key_abs=key*sign
    # how to initialize the dict value as default[0]???
    if not(key_abs in sum_dict):
        sum_dict[key_abs].append(0)
    sum_dict[key_abs].append(i)
    sum_dict[key_abs][0] = sum_dict[key_abs][0]+1*sign

print(sum_dict)
for k in sum_dict:
    sum_list=sum_dict[k]
    if sum_list[0] < len(sum_list)-1 and sum_list[0]>(-1)*(len(sum_list)-1):
        print(sum_list[1:])
