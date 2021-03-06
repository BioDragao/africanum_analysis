import json
import os
import shutil
from itertools import islice

# with open("./_all_lab_genome_files.json", 'r') as f:
#     genome_pairs = json.loads(f.read())

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

all_fastq_files.sort()


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


genome_pairs = list(chunk(all_fastq_files, 2))



def run_spotyping(a_pair):

    genome_1 = a_pair[0]

    genome_2 = a_pair[1]

    # output = (a_pair[0].split(".")[0]).split("_")[0] + "_spo.out"

    output = "_".join(a_pair[0].split("_")[:-1]) + "_spo.out"

    # print(output)

    # NOTE the usage of spotyping command
    # python2.7 SpoTyping.py ./118_cat_R1.fastq ./118_cat_R2.fastq

    cmd = "vagrant ssh -c \"cd /vagrant/africanum_analysis/lab/ && " + \
           "python2.7 SpoTyping.py " + \
            genome_1 + \
            " " + \
            genome_2 + \
            " -o " + \
            output + \
            "\""

    print(cmd)

    #os.system(cmd)

    print("\n $$$$$$$$$$ \n")


for a_pair in genome_pairs:
    run_spotyping(a_pair)

print("DONE")
