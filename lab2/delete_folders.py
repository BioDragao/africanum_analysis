import os 

all_dirs = [f for f in os.listdir() if os.path.isdir(f)]
all_dirs.remove('ref')


for a_dir in all_dirs:
    cmd = "rm -rf " + a_dir
    print(cmd)
    os.system(cmd)


