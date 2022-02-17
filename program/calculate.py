data = None
import os
nowDir = os.path.dirname(__file__)
with open(os.path.join(nowDir,input())) as f:
    f.readline()
    data = eval(f.readline())
print(type(data))
print(len(data[0][3]))


data.sort(key = lambda x:x[0])
low_rank = data[0][0]

i = 0
get_result = list()
while low_rank == data[i][0]:
    get_result.append([data[i][1], data[i][2]])
    i += 1
print("low_rank:",low_rank)
print(get_result)