rclone copy onedrive-em:africanum_analysis/lab/SAMEA2794356_1.fastq.gz . -vv
rclone copy onedrive-em:africanum_analysis/lab/SAMEA2794356_2.fastq.gz . -vv


vagrant ssh -c "cd /vagrant/africanum_analysis/lab/ && snippy --cpus 4 --outdir SAMEA2794356 --ref NC000962_3.gbk  --R1 SAMEA2794356_1.fastq.gz --R2 SAMEA2794356_2.fastq.gz"
