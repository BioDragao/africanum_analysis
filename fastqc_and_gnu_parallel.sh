parallel --gnu gunzip  ::: *gz

 fastqc -t 10 *fastq
 
