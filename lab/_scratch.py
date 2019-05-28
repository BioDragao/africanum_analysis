import json
import os
import shutil

# TODO create pairs of genomes based on same first name - in PYTHON
# Have done this in clojure already

# all_files = [f for f in os.listdir() if os.path.isfile(f)]

# def has_fastq_in_name(string):
#     if (string.find("fastq") == -1):
#         #print("NO")
#         return 0
#     else:
#         #print("YES")
#         return 1

# all_fastq_files = list(filter(lambda x: has_fastq_in_name(x), all_files))

# all_genomes_pairs = edn_format.loads("./_genome_pairs.edn")

with open("./_genome_pairs.json", 'r') as f:
    genome_pairs = json.loads(f.read())

print(genome_pairs[0])
