import json
import os
import shutil

# TODO create pairs of genomes based on same first name

all_files = [f for f in os.listdir() if os.path.isfile(f)]


def has_fastq_in_name(string):
    if (string.find("fastq") == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1


all_fastq_files = list(filter(lambda x: has_fastq_in_name(x), all_files))

all_genomes_pairs = json.loads("./")
