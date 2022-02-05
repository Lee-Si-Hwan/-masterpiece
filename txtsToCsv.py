import os
nowDir = os.path.dirname(__file__)
to_write=''
for x in range(1,38):
    filename = os.path.join(nowDir,f'program/Dataset\\info\\{x}.txt')
    with open(filename, encoding='utf-8') as desc:
        name = desc.readline()
        description = desc.readline()
        year = desc.readline()
        to_write+=f'{x}, {name}, {description}, {year}\n'
    
# write to_write to file
print(to_write)
with open(os.path.join(nowDir,f'program/Dataset\\info\\info.csv'), 'w', encoding='utf-8') as f:
    f.write(to_write)