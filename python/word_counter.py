import os
# parse file
os.chdir("media_files")
count=[]
with open('trail.txt', 'r', encoding='utf-8') as f:
    for line in f:
        count.append(line.split(' ')[0])
    print(len(count))        