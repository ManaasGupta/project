import os
# parse file 
os.makedirs("media_files",exist_ok=True)
os.chdir("media_files")
file_name=[]
for files in os.listdir("."):
    if files.endswith(".txt"):
        file_name.append(files)
file_name.sort(key=os.path.getctime)
count=[]
with open(str(file_name[-1]), 'r', encoding='utf-8') as f:
    for line in f:
        count.append(line.split(' ')[0])
    print(len(count))      
os.chdir("..") 