import json
import os
import shutil

# all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))
with open("./_genome_pairs.json", 'r') as f:
    genome_pairs = json.loads(f.read())


def run_snippy(a_pair):

    # snippy --cpus 4 --outdir Mcanettii --ref ./NC000962_3.gbk --R1 ./Mcanettii_R1.fastq.gz --R2 ./Mcanettii_R2.fastq.gz

    genome_name = a_pair[0].split("_")[0]

    genome_1 = a_pair[0]

    genome_2 = a_pair[1]

    snippy_initial_command = "vagrant ssh -c \"cd /vagrant/africanum_analysis/lab/ && " + \
                "snippy --cpus 4 --outdir " + \
                genome_name + \
                " --ref " + \
                "NC000962_3.gbk "

    cmd = snippy_initial_command + \
            " --R1 " + \
            genome_1 + \
            " --R2 " + \
            genome_2 + \
            "\""

    print(cmd)

    #os.system(cmd)

    print("\n $$$$$$$$$$ \n")


for a_pair in genome_pairs:
    run_snippy(a_pair)
