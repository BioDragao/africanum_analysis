import os
import shutil

# # TODO create pairs of genomes based on same first name

# all_files = [f for f in os.listdir() if  os.path.isfile(f)]

# def has_fastq_in_name(string):
#     if (string.find("fastq") == -1):
#         #print("NO")
#         return 0
#     else:
#         #print("YES")
#         return 1

# all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))
with open("./_genome_pairs.json", 'r') as f:
    genome_pairs = json.loads(f.read())

# java -jar /opt/Trimmomatic-0.36.jar PE -phred33

# 118_cat_R1.fastq.gz
# 118_cat_R2.fastq.gz
# 118_cat_R1.p.fastq.gz
# 118_cat_R1.s.fastq.gz
# 118_cat_R2.p.fastq.gz
# 118_cat_R2.s.fastq.gz

# ILLUMINACLIP:NexteraPE-PE.fa:2:30:10 LEADING:15 TRAILING:15 HEADCROP:7 SLIDINGWINDOW:4:15 MINLEN:36

file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"


def run_trimmomatic(a_pair):

    genome_1 = a_pair[0]
    #    print(genome_1)
    genome_1_s = "".join(a_pair[0].split(".")[:-2]) + ".s.fastq.gz"
    #    print(genome_1_s)
    genome_1_p = "".join(a_pair[0].split(".")[:-2]) + ".p.fastq.gz"
    #    print(genome_1_p)
    genome_2 = a_pair[1]
    #    print(genome_2)
    genome_2_s = "".join(a_pair[1].split(".")[:-2]) + ".s.fastq.gz"
    #    print(genome_2_s)
    genome_2_p = "".join(a_pair[1].split(".")[:-2]) + ".p.fastq.gz"
    #    print(genome_2_p)

    # java -jar /opt/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33
    # 118_cat_R1.fastq.gz
    # 118_cat_R2.fastq.gz
    # 118_cat_R1.p.fastq.gz
    # 118_cat_R1.s.fastq.gz
    # 118_cat_R2.p.fastq.gz
    # 118_cat_R2.s.fastq.gz
    # LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36

    trimmomatic_location_and_params = "java -jar /opt/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33"

    illumina_string = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36\""

    cmd = "vagrant ssh -c \"cd /vagrant/africanum_analysis/lab/ && " + \
          trimmomatic_location_and_params + " " + \
          genome_1 + " " + \
          genome_2 + " " + \
          genome_1_p + " " + \
          genome_1_s + " " + \
          genome_2_p + " " + \
          genome_2_s + " " + \
          illumina_string

    print(cmd)

    #os.system(cmd)

    print("\n $$$$$$$$$$ \n")


for a_pair in genome_pairs:
    run_trimmomatic(a_pair)
