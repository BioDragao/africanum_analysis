1. The genomes were downloaded from the three sources 

- ENA 

```
#aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502472/ERR502472_1.fastq.gz" -o "./lab/SAMEA2340877_1.fastq.gz"

#SAMEA2340877	ERS398548	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502472/ERR502472_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502472/ERR502472_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502472/ERR502472_1.fastq.gz" -o "./genomes_ena/SAMEA2340877_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502472/ERR502472_2.fastq.gz" -o "./genomes_ena/SAMEA2340877_2.fastq.gz"

#SAMEA2340878	ERS398549	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502473/ERR502473_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502473/ERR502473_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502473/ERR502473_1.fastq.gz" -o "./genomes_ena/SAMEA2340878_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502473/ERR502473_2.fastq.gz" -o "./genomes_ena/SAMEA2340878_2.fastq.gz"

#SAMEA2340879	ERS398550	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502474/ERR502474_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502474/ERR502474_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502474/ERR502474_1.fastq.gz" -o "./genomes_ena/SAMEA2340879_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502474/ERR502474_2.fastq.gz" -o "./genomes_ena/SAMEA2340879_2.fastq.gz"

#SAMEA2340883	ERS398554	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502478/ERR502478_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502478/ERR502478_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502478/ERR502478_1.fastq.gz" -o "./genomes_ena/SAMEA2340883_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502478/ERR502478_2.fastq.gz" -o "./genomes_ena/SAMEA2340883_2.fastq.gz"

#SAMEA2340884	ERS398555	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502479/ERR502479_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502479/ERR502479_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502479/ERR502479_1.fastq.gz" -o "./genomes_ena/SAMEA2340884_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502479/ERR502479_2.fastq.gz" -o "./genomes_ena/SAMEA2340884_2.fastq.gz"

#SAMEA2340885	ERS398556	ftp.sra.ebi.ac.uk/vol1/fastq/ERR517/ERR517472/ERR517472_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR517/ERR517472/ERR517472_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR517/ERR517472/ERR517472_1.fastq.gz" -o "./genomes_ena/SAMEA2340885_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR517/ERR517472/ERR517472_2.fastq.gz" -o "./genomes_ena/SAMEA2340885_2.fastq.gz"

#SAMEA2340887	ERS398558	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502480/ERR502480_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502480/ERR502480_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502480/ERR502480_1.fastq.gz" -o "./genomes_ena/SAMEA2340887_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502480/ERR502480_2.fastq.gz" -o "./genomes_ena/SAMEA2340887_2.fastq.gz"

#SAMEA2340895	ERS398566	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502488/ERR502488_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502488/ERR502488_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502488/ERR502488_1.fastq.gz" -o "./genomes_ena/SAMEA2340895_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502488/ERR502488_2.fastq.gz" -o "./genomes_ena/SAMEA2340895_2.fastq.gz"

#SAMEA2340898	ERS398569	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502491/ERR502491_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502491/ERR502491_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502491/ERR502491_1.fastq.gz" -o "./genomes_ena/SAMEA2340898_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502491/ERR502491_2.fastq.gz" -o "./genomes_ena/SAMEA2340898_2.fastq.gz"

#SAMEA2340902	ERS398573	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502495/ERR502495_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502495/ERR502495_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502495/ERR502495_1.fastq.gz" -o "./genomes_ena/SAMEA2340902_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502495/ERR502495_2.fastq.gz" -o "./genomes_ena/SAMEA2340902_2.fastq.gz"

#SAMEA2340906	ERS398577	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502499/ERR502499_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502499/ERR502499_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502499/ERR502499_1.fastq.gz" -o "./genomes_ena/SAMEA2340906_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502499/ERR502499_2.fastq.gz" -o "./genomes_ena/SAMEA2340906_2.fastq.gz"

#SAMEA2340911	ERS398582	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502504/ERR502504_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502504/ERR502504_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502504/ERR502504_1.fastq.gz" -o "./genomes_ena/SAMEA2340911_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502504/ERR502504_2.fastq.gz" -o "./genomes_ena/SAMEA2340911_2.fastq.gz"

#SAMEA2340926	ERS398597	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502518/ERR502518_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502518/ERR502518_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502518/ERR502518_1.fastq.gz" -o "./genomes_ena/SAMEA2340926_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502518/ERR502518_2.fastq.gz" -o "./genomes_ena/SAMEA2340926_2.fastq.gz"

#SAMEA2340927	ERS398598	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502519/ERR502519_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502519/ERR502519_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502519/ERR502519_1.fastq.gz" -o "./genomes_ena/SAMEA2340927_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502519/ERR502519_2.fastq.gz" -o "./genomes_ena/SAMEA2340927_2.fastq.gz"

#SAMEA2340928	ERS398599	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502520/ERR502520_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502520/ERR502520_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502520/ERR502520_1.fastq.gz" -o "./genomes_ena/SAMEA2340928_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502520/ERR502520_2.fastq.gz" -o "./genomes_ena/SAMEA2340928_2.fastq.gz"

#SAMEA2340934	ERS398605	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502526/ERR502526_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502526/ERR502526_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502526/ERR502526_1.fastq.gz" -o "./genomes_ena/SAMEA2340934_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502526/ERR502526_2.fastq.gz" -o "./genomes_ena/SAMEA2340934_2.fastq.gz"

#SAMEA2340937	ERS398608	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502529/ERR502529_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502529/ERR502529_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502529/ERR502529_1.fastq.gz" -o "./genomes_ena/SAMEA2340937_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502529/ERR502529_2.fastq.gz" -o "./genomes_ena/SAMEA2340937_2.fastq.gz"

#SAMEA2340945	ERS398616	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502535/ERR502535_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502535/ERR502535_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502535/ERR502535_1.fastq.gz" -o "./genomes_ena/SAMEA2340945_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502535/ERR502535_2.fastq.gz" -o "./genomes_ena/SAMEA2340945_2.fastq.gz"

#SAMEA2340948	ERS398619	ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502538/ERR502538_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502538/ERR502538_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502538/ERR502538_1.fastq.gz" -o "./genomes_ena/SAMEA2340948_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR502/ERR502538/ERR502538_2.fastq.gz" -o "./genomes_ena/SAMEA2340948_2.fastq.gz"

#SAMEA2627005	ERS496915	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702399/ERR702399_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702399/ERR702399_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702399/ERR702399_1.fastq.gz" -o "./genomes_ena/SAMEA2627005_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702399/ERR702399_2.fastq.gz" -o "./genomes_ena/SAMEA2627005_2.fastq.gz"

#SAMEA2627008	ERS496918	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702402/ERR702402_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702402/ERR702402_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702402/ERR702402_1.fastq.gz" -o "./genomes_ena/SAMEA2627008_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702402/ERR702402_2.fastq.gz" -o "./genomes_ena/SAMEA2627008_2.fastq.gz"

#SAMEA2627009	ERS496919	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702403/ERR702403_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702403/ERR702403_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702403/ERR702403_1.fastq.gz" -o "./genomes_ena/SAMEA2627009_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702403/ERR702403_2.fastq.gz" -o "./genomes_ena/SAMEA2627009_2.fastq.gz"

#SAMEA2627010	ERS496920	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702404/ERR702404_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702404/ERR702404_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702404/ERR702404_1.fastq.gz" -o "./genomes_ena/SAMEA2627010_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702404/ERR702404_2.fastq.gz" -o "./genomes_ena/SAMEA2627010_2.fastq.gz"

#SAMEA2627011	ERS496921	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702405/ERR702405_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702405/ERR702405_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702405/ERR702405_1.fastq.gz" -o "./genomes_ena/SAMEA2627011_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702405/ERR702405_2.fastq.gz" -o "./genomes_ena/SAMEA2627011_2.fastq.gz"

#SAMEA2627012	ERS496922	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702406/ERR702406_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702406/ERR702406_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702406/ERR702406_1.fastq.gz" -o "./genomes_ena/SAMEA2627012_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702406/ERR702406_2.fastq.gz" -o "./genomes_ena/SAMEA2627012_2.fastq.gz"

#SAMEA2627034	ERS496944	ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909753/ERR909753_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909753/ERR909753_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909753/ERR909753_1.fastq.gz" -o "./genomes_ena/SAMEA2627034_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909753/ERR909753_2.fastq.gz" -o "./genomes_ena/SAMEA2627034_2.fastq.gz"

#SAMEA2627040	ERS496950	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702433/ERR702433_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702433/ERR702433_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702433/ERR702433_1.fastq.gz" -o "./genomes_ena/SAMEA2627040_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702433/ERR702433_2.fastq.gz" -o "./genomes_ena/SAMEA2627040_2.fastq.gz"

#SAMEA2627044	ERS496954	ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702437/ERR702437_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702437/ERR702437_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702437/ERR702437_1.fastq.gz" -o "./genomes_ena/SAMEA2627044_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR702/ERR702437/ERR702437_2.fastq.gz" -o "./genomes_ena/SAMEA2627044_2.fastq.gz"

#SAMEA2627045	ERS496955	ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909754/ERR909754_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909754/ERR909754_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909754/ERR909754_1.fastq.gz" -o "./genomes_ena/SAMEA2627045_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR909/ERR909754/ERR909754_2.fastq.gz" -o "./genomes_ena/SAMEA2627045_2.fastq.gz"

#SAMEA2794338	ERS556317	ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751316/ERR751316_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751316/ERR751316_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751316/ERR751316_1.fastq.gz" -o "./genomes_ena/SAMEA2794338_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751316/ERR751316_2.fastq.gz" -o "./genomes_ena/SAMEA2794338_2.fastq.gz"

#SAMEA2794356	ERS556335	ftp.sra.ebi.ac.uk/vol1/fastq/ERR845/ERR845916/ERR845916_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR845/ERR845916/ERR845916_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR845/ERR845916/ERR845916_1.fastq.gz" -o "./genomes_ena/SAMEA2794356_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR845/ERR845916/ERR845916_2.fastq.gz" -o "./genomes_ena/SAMEA2794356_2.fastq.gz"

#SAMEA2794363	ERS556342	ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751340/ERR751340_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751340/ERR751340_2.fastq.gz
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751340/ERR751340_1.fastq.gz" -o "./genomes_ena/SAMEA2794363_1.fastq.gz"
aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR751/ERR751340/ERR751340_2.fastq.gz" -o "./genomes_ena/SAMEA2794363_2.fastq.gz"



```


- Emilyn's onedrive folder

```
rclone copy onedrive-em:maf_genomes ./genomes_em/ -vv
```

- Abhinav Onedrive


```
##DUPLICATES
#ERR1215473 SAMEA3359901
#rclone copy onedrive-abhi:maf-genomes/ERR1215473_1.fastq.gz ./genomes_abhi/SAMEA3359901_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR1215473_2.fastq.gz ./genomes_abhi/SAMEA3359901_2.fastq.gz -vv
#ERR502480 SAMEA2340887
#rclone copy onedrive-abhi:maf-genomes/ERR502480_1.fastq.gz ./genomes_abhi/SAMEA2340887_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR502480_2.fastq.gz ./genomes_abhi/SAMEA2340887_2.fastq.gz -vv
#ERR845916 SAMEA2794356
#rclone copy onedrive-abhi:maf-genomes/ERR845916_1.fastq.gz ./genomes_abhi/SAMEA2794356_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR845916_2.fastq.gz ./genomes_abhi/SAMEA2794356_2.fastq.gz -vv
#ERR909753 SAMEA2627034
#rclone copy onedrive-abhi:maf-genomes/ERR909753_1.fastq.gz ./genomes_abhi/SAMEA2627034_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR909753_2.fastq.gz ./genomes_abhi/SAMEA2627034_2.fastq.gz -vv
#ERR909754 SAMEA2627045
#rclone copy onedrive-abhi:maf-genomes/ERR909754_1.fastq.gz ./genomes_abhi/SAMEA2627045_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR909754_2.fastq.gz ./genomes_abhi/SAMEA2627045_2.fastq.gz -vv



# #ERR1215473 SAMEA3359901
# rm -rf SAMEA3359901_1.fastq.gz
# rm -rf SAMEA3359901_2.fastq.gz
# #ERR502480 SAMEA2340887
# rm -rf SAMEA2340887_1.fastq.gz
# rm -rf SAMEA2340887_2.fastq.gz
# #ERR845916 SAMEA2794356
# rm -rf SAMEA2794356_1.fastq.gz
# rm -rf SAMEA2794356_2.fastq.gz
# #ERR909753 SAMEA2627034
# rm -rf SAMEA2627034_1.fastq.gz
# rm -rf SAMEA2627034_2.fastq.gz
# #ERR909754 SAMEA2627045
# rm -rf SAMEA2627045_1.fastq.gz
# rm -rf SAMEA2627045_2.fastq.gz



######################

##MISSING_GENOMES
#ERR1203075 SAMEA3504622
#rclone copy onedrive-abhi:maf-genomes/ERR1203075_1.fastq.gz ./genomes_abhi/SAMEA3504622_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR1203075_2.fastq.gz ./genomes_abhi/SAMEA3504622_2.fastq.gz -vv
#ERR1203078 SAMEA3504625
#rclone copy onedrive-abhi:maf-genomes/ERR1203078_1.fastq.gz ./genomes_abhi/SAMEA3504625_1.fastq.gz -vv
#rclone copy onedrive-abhi:maf-genomes/ERR1203078_2.fastq.gz ./genomes_abhi/SAMEA3504625_2.fastq.gz -vv



# aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR120/005/ERR1203075/ERR1203075_1.fastq.gz" -o "./genomes_abhi/SAMEA3504622_1.fastq.gz"
# aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR120/005/ERR1203075/ERR1203075_2.fastq.gz" -o "./genomes_abhi/SAMEA3504622_2.fastq.gz"


# aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR120/008/ERR1203078/ERR1203078_1.fastq.gz" -o "./genomes_abhi/SAMEA3504625_1.fastq.gz"
# aria2c "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR120/008/ERR1203078/ERR1203078_2.fastq.gz" -o "./genomes_abhi/SAMEA3504625_2.fastq.gz"

######################


# rclone copy onedrive-abhi:maf-genomes/NC000962_3.fasta ./genomes_abhi/ -vv
# rclone copy onedrive-abhi:maf-genomes/NC000962_3.gbk ./genomes_abhi/ -vv
# rclone copy onedrive-abhi:maf-genomes/NexteraPE-PE.fa ./genomes_abhi/ -vv


######################

#ERR1082136 SAMEA3359902
rclone copy onedrive-abhi:maf-genomes/ERR1082136_1.fastq.gz ./genomes_abhi/SAMEA3359902_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082136_2.fastq.gz ./genomes_abhi/SAMEA3359902_2.fastq.gz -vv

#ERR1082137 SAMEA3359903
rclone copy onedrive-abhi:maf-genomes/ERR1082137_1.fastq.gz ./genomes_abhi/SAMEA3359903_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082137_2.fastq.gz ./genomes_abhi/SAMEA3359903_2.fastq.gz -vv

#ERR1082138 SAMEA3359904
rclone copy onedrive-abhi:maf-genomes/ERR1082138_1.fastq.gz ./genomes_abhi/SAMEA3359904_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082138_2.fastq.gz ./genomes_abhi/SAMEA3359904_2.fastq.gz -vv

#ERR1082139 SAMEA3359906
rclone copy onedrive-abhi:maf-genomes/ERR1082139_1.fastq.gz ./genomes_abhi/SAMEA3359906_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082139_2.fastq.gz ./genomes_abhi/SAMEA3359906_2.fastq.gz -vv

#ERR1082140 SAMEA3359910
rclone copy onedrive-abhi:maf-genomes/ERR1082140_1.fastq.gz ./genomes_abhi/SAMEA3359910_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082140_2.fastq.gz ./genomes_abhi/SAMEA3359910_2.fastq.gz -vv

#ERR1082141 SAMEA3359913
rclone copy onedrive-abhi:maf-genomes/ERR1082141_1.fastq.gz ./genomes_abhi/SAMEA3359913_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082141_2.fastq.gz ./genomes_abhi/SAMEA3359913_2.fastq.gz -vv

#ERR1082142 SAMEA3359914
rclone copy onedrive-abhi:maf-genomes/ERR1082142_1.fastq.gz ./genomes_abhi/SAMEA3359914_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082142_2.fastq.gz ./genomes_abhi/SAMEA3359914_2.fastq.gz -vv

#ERR1082143 SAMEA3359915
rclone copy onedrive-abhi:maf-genomes/ERR1082143_1.fastq.gz ./genomes_abhi/SAMEA3359915_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1082143_2.fastq.gz ./genomes_abhi/SAMEA3359915_2.fastq.gz -vv

#ERR1203053 SAMEA3504596
rclone copy onedrive-abhi:maf-genomes/ERR1203053_1.fastq.gz ./genomes_abhi/SAMEA3504596_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203053_2.fastq.gz ./genomes_abhi/SAMEA3504596_2.fastq.gz -vv

#ERR1203054 SAMEA3504597
rclone copy onedrive-abhi:maf-genomes/ERR1203054_1.fastq.gz ./genomes_abhi/SAMEA3504597_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203054_2.fastq.gz ./genomes_abhi/SAMEA3504597_2.fastq.gz -vv

#ERR1203055 SAMEA3504598
rclone copy onedrive-abhi:maf-genomes/ERR1203055_1.fastq.gz ./genomes_abhi/SAMEA3504598_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203055_2.fastq.gz ./genomes_abhi/SAMEA3504598_2.fastq.gz -vv

#ERR1203056 SAMEA3504599
rclone copy onedrive-abhi:maf-genomes/ERR1203056_1.fastq.gz ./genomes_abhi/SAMEA3504599_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203056_2.fastq.gz ./genomes_abhi/SAMEA3504599_2.fastq.gz -vv

#ERR1203057 SAMEA3504600
rclone copy onedrive-abhi:maf-genomes/ERR1203057_1.fastq.gz ./genomes_abhi/SAMEA3504600_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203057_2.fastq.gz ./genomes_abhi/SAMEA3504600_2.fastq.gz -vv

#ERR1203058 SAMEA3504601
rclone copy onedrive-abhi:maf-genomes/ERR1203058_1.fastq.gz ./genomes_abhi/SAMEA3504601_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203058_2.fastq.gz ./genomes_abhi/SAMEA3504601_2.fastq.gz -vv

#ERR1203059 SAMEA3504602
rclone copy onedrive-abhi:maf-genomes/ERR1203059_1.fastq.gz ./genomes_abhi/SAMEA3504602_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203059_2.fastq.gz ./genomes_abhi/SAMEA3504602_2.fastq.gz -vv

#ERR1203061 SAMEA3504606
rclone copy onedrive-abhi:maf-genomes/ERR1203061_1.fastq.gz ./genomes_abhi/SAMEA3504606_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203061_2.fastq.gz ./genomes_abhi/SAMEA3504606_2.fastq.gz -vv

#ERR1203062 SAMEA3504607
rclone copy onedrive-abhi:maf-genomes/ERR1203062_1.fastq.gz ./genomes_abhi/SAMEA3504607_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203062_2.fastq.gz ./genomes_abhi/SAMEA3504607_2.fastq.gz -vv

#ERR1203065 SAMEA3504610
rclone copy onedrive-abhi:maf-genomes/ERR1203065_1.fastq.gz ./genomes_abhi/SAMEA3504610_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203065_2.fastq.gz ./genomes_abhi/SAMEA3504610_2.fastq.gz -vv

#ERR1203066 SAMEA3504611
rclone copy onedrive-abhi:maf-genomes/ERR1203066_1.fastq.gz ./genomes_abhi/SAMEA3504611_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203066_2.fastq.gz ./genomes_abhi/SAMEA3504611_2.fastq.gz -vv

#ERR1203068 SAMEA3504612
rclone copy onedrive-abhi:maf-genomes/ERR1203068_1.fastq.gz ./genomes_abhi/SAMEA3504612_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203068_2.fastq.gz ./genomes_abhi/SAMEA3504612_2.fastq.gz -vv

#ERR1203069 SAMEA3504613
rclone copy onedrive-abhi:maf-genomes/ERR1203069_1.fastq.gz ./genomes_abhi/SAMEA3504613_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203069_2.fastq.gz ./genomes_abhi/SAMEA3504613_2.fastq.gz -vv

#ERR1203070 SAMEA3504614
rclone copy onedrive-abhi:maf-genomes/ERR1203070_1.fastq.gz ./genomes_abhi/SAMEA3504614_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203070_2.fastq.gz ./genomes_abhi/SAMEA3504614_2.fastq.gz -vv

#ERR1203072 SAMEA3504615
rclone copy onedrive-abhi:maf-genomes/ERR1203072_1.fastq.gz ./genomes_abhi/SAMEA3504615_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203072_2.fastq.gz ./genomes_abhi/SAMEA3504615_2.fastq.gz -vv

#ERR1203074 SAMEA3504621
rclone copy onedrive-abhi:maf-genomes/ERR1203074_1.fastq.gz ./genomes_abhi/SAMEA3504621_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203074_2.fastq.gz ./genomes_abhi/SAMEA3504621_2.fastq.gz -vv

#ERR1203075 SAMEA3504622
rclone copy onedrive-abhi:maf-genomes/ERR1203075_1.fastq.gz ./genomes_abhi/SAMEA3504622_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203075_2.fastq.gz ./genomes_abhi/SAMEA3504622_2.fastq.gz -vv

#ERR1203076 SAMEA3504623
rclone copy onedrive-abhi:maf-genomes/ERR1203076_1.fastq.gz ./genomes_abhi/SAMEA3504623_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203076_2.fastq.gz ./genomes_abhi/SAMEA3504623_2.fastq.gz -vv

#ERR1203077 SAMEA3504624
rclone copy onedrive-abhi:maf-genomes/ERR1203077_1.fastq.gz ./genomes_abhi/SAMEA3504624_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1203077_2.fastq.gz ./genomes_abhi/SAMEA3504624_2.fastq.gz -vv

#ERR1215460 SAMEA3359878
rclone copy onedrive-abhi:maf-genomes/ERR1215460_1.fastq.gz ./genomes_abhi/SAMEA3359878_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215460_2.fastq.gz ./genomes_abhi/SAMEA3359878_2.fastq.gz -vv

#ERR1215461 SAMEA3359879
rclone copy onedrive-abhi:maf-genomes/ERR1215461_1.fastq.gz ./genomes_abhi/SAMEA3359879_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215461_2.fastq.gz ./genomes_abhi/SAMEA3359879_2.fastq.gz -vv

#ERR1215462 SAMEA3359881
rclone copy onedrive-abhi:maf-genomes/ERR1215462_1.fastq.gz ./genomes_abhi/SAMEA3359881_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215462_2.fastq.gz ./genomes_abhi/SAMEA3359881_2.fastq.gz -vv

#ERR1215463 SAMEA3359882
rclone copy onedrive-abhi:maf-genomes/ERR1215463_1.fastq.gz ./genomes_abhi/SAMEA3359882_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215463_2.fastq.gz ./genomes_abhi/SAMEA3359882_2.fastq.gz -vv

#ERR1215464 SAMEA3359883
rclone copy onedrive-abhi:maf-genomes/ERR1215464_1.fastq.gz ./genomes_abhi/SAMEA3359883_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215464_2.fastq.gz ./genomes_abhi/SAMEA3359883_2.fastq.gz -vv

#ERR1215465 SAMEA3359884
rclone copy onedrive-abhi:maf-genomes/ERR1215465_1.fastq.gz ./genomes_abhi/SAMEA3359884_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215465_2.fastq.gz ./genomes_abhi/SAMEA3359884_2.fastq.gz -vv

#ERR1215466 SAMEA3359889
rclone copy onedrive-abhi:maf-genomes/ERR1215466_1.fastq.gz ./genomes_abhi/SAMEA3359889_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215466_2.fastq.gz ./genomes_abhi/SAMEA3359889_2.fastq.gz -vv

#ERR1215467 SAMEA3359890
rclone copy onedrive-abhi:maf-genomes/ERR1215467_1.fastq.gz ./genomes_abhi/SAMEA3359890_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215467_2.fastq.gz ./genomes_abhi/SAMEA3359890_2.fastq.gz -vv

#ERR1215468 SAMEA3359891
rclone copy onedrive-abhi:maf-genomes/ERR1215468_1.fastq.gz ./genomes_abhi/SAMEA3359891_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215468_2.fastq.gz ./genomes_abhi/SAMEA3359891_2.fastq.gz -vv

#ERR1215469 SAMEA3359892
rclone copy onedrive-abhi:maf-genomes/ERR1215469_1.fastq.gz ./genomes_abhi/SAMEA3359892_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215469_2.fastq.gz ./genomes_abhi/SAMEA3359892_2.fastq.gz -vv

#ERR1215470 SAMEA3359893
rclone copy onedrive-abhi:maf-genomes/ERR1215470_1.fastq.gz ./genomes_abhi/SAMEA3359893_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215470_2.fastq.gz ./genomes_abhi/SAMEA3359893_2.fastq.gz -vv

#ERR1215471 SAMEA3359894
rclone copy onedrive-abhi:maf-genomes/ERR1215471_1.fastq.gz ./genomes_abhi/SAMEA3359894_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215471_2.fastq.gz ./genomes_abhi/SAMEA3359894_2.fastq.gz -vv

#ERR1215472 SAMEA3359895
rclone copy onedrive-abhi:maf-genomes/ERR1215472_1.fastq.gz ./genomes_abhi/SAMEA3359895_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215472_2.fastq.gz ./genomes_abhi/SAMEA3359895_2.fastq.gz -vv

#ERR1215474 SAMEA3359905
rclone copy onedrive-abhi:maf-genomes/ERR1215474_1.fastq.gz ./genomes_abhi/SAMEA3359905_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215474_2.fastq.gz ./genomes_abhi/SAMEA3359905_2.fastq.gz -vv

#ERR1215475 SAMEA3359907
rclone copy onedrive-abhi:maf-genomes/ERR1215475_1.fastq.gz ./genomes_abhi/SAMEA3359907_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215475_2.fastq.gz ./genomes_abhi/SAMEA3359907_2.fastq.gz -vv

#ERR1215476 SAMEA3359908
rclone copy onedrive-abhi:maf-genomes/ERR1215476_1.fastq.gz ./genomes_abhi/SAMEA3359908_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215476_2.fastq.gz ./genomes_abhi/SAMEA3359908_2.fastq.gz -vv

#ERR1215477 SAMEA3359909
rclone copy onedrive-abhi:maf-genomes/ERR1215477_1.fastq.gz ./genomes_abhi/SAMEA3359909_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215477_2.fastq.gz ./genomes_abhi/SAMEA3359909_2.fastq.gz -vv

#ERR1215478 SAMEA3359912
rclone copy onedrive-abhi:maf-genomes/ERR1215478_1.fastq.gz ./genomes_abhi/SAMEA3359912_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215478_2.fastq.gz ./genomes_abhi/SAMEA3359912_2.fastq.gz -vv

#ERR1215479 SAMEA3359913
rclone copy onedrive-abhi:maf-genomes/ERR1215479_1.fastq.gz ./genomes_abhi/SAMEA3359913_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215479_2.fastq.gz ./genomes_abhi/SAMEA3359913_2.fastq.gz -vv

#ERR1215480 SAMEA3359916
rclone copy onedrive-abhi:maf-genomes/ERR1215480_1.fastq.gz ./genomes_abhi/SAMEA3359916_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215480_2.fastq.gz ./genomes_abhi/SAMEA3359916_2.fastq.gz -vv

#ERR1215481 SAMEA3359917
rclone copy onedrive-abhi:maf-genomes/ERR1215481_1.fastq.gz ./genomes_abhi/SAMEA3359917_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215481_2.fastq.gz ./genomes_abhi/SAMEA3359917_2.fastq.gz -vv

#ERR1215482 SAMEA3359918
rclone copy onedrive-abhi:maf-genomes/ERR1215482_1.fastq.gz ./genomes_abhi/SAMEA3359918_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215482_2.fastq.gz ./genomes_abhi/SAMEA3359918_2.fastq.gz -vv

#ERR1215483 SAMEA3359919
rclone copy onedrive-abhi:maf-genomes/ERR1215483_1.fastq.gz ./genomes_abhi/SAMEA3359919_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1215483_2.fastq.gz ./genomes_abhi/SAMEA3359919_2.fastq.gz -vv

#ERR1334049 SAMEA3504595
rclone copy onedrive-abhi:maf-genomes/ERR1334049_1.fastq.gz ./genomes_abhi/SAMEA3504595_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1334049_2.fastq.gz ./genomes_abhi/SAMEA3504595_2.fastq.gz -vv

#ERR1334050 SAMEA3504603
rclone copy onedrive-abhi:maf-genomes/ERR1334050_1.fastq.gz ./genomes_abhi/SAMEA3504603_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1334050_2.fastq.gz ./genomes_abhi/SAMEA3504603_2.fastq.gz -vv

#ERR1334051 SAMEA3504605
rclone copy onedrive-abhi:maf-genomes/ERR1334051_1.fastq.gz ./genomes_abhi/SAMEA3504605_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1334051_2.fastq.gz ./genomes_abhi/SAMEA3504605_2.fastq.gz -vv

#ERR1334052 SAMEA3504608
rclone copy onedrive-abhi:maf-genomes/ERR1334052_1.fastq.gz ./genomes_abhi/SAMEA3504608_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1334052_2.fastq.gz ./genomes_abhi/SAMEA3504608_2.fastq.gz -vv

#ERR1334053 SAMEA3504609
rclone copy onedrive-abhi:maf-genomes/ERR1334053_1.fastq.gz ./genomes_abhi/SAMEA3504609_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR1334053_2.fastq.gz ./genomes_abhi/SAMEA3504609_2.fastq.gz -vv

#ERR502471 SAMEA2340876
rclone copy onedrive-abhi:maf-genomes/ERR502471_1.fastq.gz ./genomes_abhi/SAMEA2340876_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502471_2.fastq.gz ./genomes_abhi/SAMEA2340876_2.fastq.gz -vv

#ERR502475 SAMEA2340880
rclone copy onedrive-abhi:maf-genomes/ERR502475_1.fastq.gz ./genomes_abhi/SAMEA2340880_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502475_2.fastq.gz ./genomes_abhi/SAMEA2340880_2.fastq.gz -vv

#ERR502476 SAMEA2340881
rclone copy onedrive-abhi:maf-genomes/ERR502476_1.fastq.gz ./genomes_abhi/SAMEA2340881_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502476_2.fastq.gz ./genomes_abhi/SAMEA2340881_2.fastq.gz -vv

#ERR502477 SAMEA2340882
rclone copy onedrive-abhi:maf-genomes/ERR502477_1.fastq.gz ./genomes_abhi/SAMEA2340882_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502477_2.fastq.gz ./genomes_abhi/SAMEA2340882_2.fastq.gz -vv

#ERR502481 SAMEA2340888
rclone copy onedrive-abhi:maf-genomes/ERR502481_1.fastq.gz ./genomes_abhi/SAMEA2340888_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502481_2.fastq.gz ./genomes_abhi/SAMEA2340888_2.fastq.gz -vv

#ERR502482 SAMEA2340889
rclone copy onedrive-abhi:maf-genomes/ERR502482_1.fastq.gz ./genomes_abhi/SAMEA2340889_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502482_2.fastq.gz ./genomes_abhi/SAMEA2340889_2.fastq.gz -vv

#ERR502483 SAMEA2340890
rclone copy onedrive-abhi:maf-genomes/ERR502483_1.fastq.gz ./genomes_abhi/SAMEA2340890_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502483_2.fastq.gz ./genomes_abhi/SAMEA2340890_2.fastq.gz -vv

#ERR502484 SAMEA2340891
rclone copy onedrive-abhi:maf-genomes/ERR502484_1.fastq.gz ./genomes_abhi/SAMEA2340891_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502484_2.fastq.gz ./genomes_abhi/SAMEA2340891_2.fastq.gz -vv

#ERR502485 SAMEA2340892
rclone copy onedrive-abhi:maf-genomes/ERR502485_1.fastq.gz ./genomes_abhi/SAMEA2340892_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502485_2.fastq.gz ./genomes_abhi/SAMEA2340892_2.fastq.gz -vv

#ERR502486 SAMEA2340893
rclone copy onedrive-abhi:maf-genomes/ERR502486_1.fastq.gz ./genomes_abhi/SAMEA2340893_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502486_2.fastq.gz ./genomes_abhi/SAMEA2340893_2.fastq.gz -vv

#ERR502487 SAMEA2340894
rclone copy onedrive-abhi:maf-genomes/ERR502487_1.fastq.gz ./genomes_abhi/SAMEA2340894_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502487_2.fastq.gz ./genomes_abhi/SAMEA2340894_2.fastq.gz -vv

#ERR502489 SAMEA2340896
rclone copy onedrive-abhi:maf-genomes/ERR502489_1.fastq.gz ./genomes_abhi/SAMEA2340896_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502489_2.fastq.gz ./genomes_abhi/SAMEA2340896_2.fastq.gz -vv

#ERR502490 SAMEA2340897
rclone copy onedrive-abhi:maf-genomes/ERR502490_1.fastq.gz ./genomes_abhi/SAMEA2340897_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502490_2.fastq.gz ./genomes_abhi/SAMEA2340897_2.fastq.gz -vv

#ERR502492 SAMEA2340899
rclone copy onedrive-abhi:maf-genomes/ERR502492_1.fastq.gz ./genomes_abhi/SAMEA2340899_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502492_2.fastq.gz ./genomes_abhi/SAMEA2340899_2.fastq.gz -vv

#ERR502493 SAMEA2340900
rclone copy onedrive-abhi:maf-genomes/ERR502493_1.fastq.gz ./genomes_abhi/SAMEA2340900_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502493_2.fastq.gz ./genomes_abhi/SAMEA2340900_2.fastq.gz -vv

#ERR502494 SAMEA2340901
rclone copy onedrive-abhi:maf-genomes/ERR502494_1.fastq.gz ./genomes_abhi/SAMEA2340901_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502494_2.fastq.gz ./genomes_abhi/SAMEA2340901_2.fastq.gz -vv

#ERR502496 SAMEA2340903
rclone copy onedrive-abhi:maf-genomes/ERR502496_1.fastq.gz ./genomes_abhi/SAMEA2340903_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502496_2.fastq.gz ./genomes_abhi/SAMEA2340903_2.fastq.gz -vv

#ERR502497 SAMEA2340904
rclone copy onedrive-abhi:maf-genomes/ERR502497_1.fastq.gz ./genomes_abhi/SAMEA2340904_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502497_2.fastq.gz ./genomes_abhi/SAMEA2340904_2.fastq.gz -vv

#ERR502498 SAMEA2340905
rclone copy onedrive-abhi:maf-genomes/ERR502498_1.fastq.gz ./genomes_abhi/SAMEA2340905_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502498_2.fastq.gz ./genomes_abhi/SAMEA2340905_2.fastq.gz -vv

#ERR502500 SAMEA2340907
rclone copy onedrive-abhi:maf-genomes/ERR502500_1.fastq.gz ./genomes_abhi/SAMEA2340907_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502500_2.fastq.gz ./genomes_abhi/SAMEA2340907_2.fastq.gz -vv

#ERR502501 SAMEA2340908
rclone copy onedrive-abhi:maf-genomes/ERR502501_1.fastq.gz ./genomes_abhi/SAMEA2340908_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502501_2.fastq.gz ./genomes_abhi/SAMEA2340908_2.fastq.gz -vv

#ERR502502 SAMEA2340909
rclone copy onedrive-abhi:maf-genomes/ERR502502_1.fastq.gz ./genomes_abhi/SAMEA2340909_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502502_2.fastq.gz ./genomes_abhi/SAMEA2340909_2.fastq.gz -vv

#ERR502503 SAMEA2340910
rclone copy onedrive-abhi:maf-genomes/ERR502503_1.fastq.gz ./genomes_abhi/SAMEA2340910_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502503_2.fastq.gz ./genomes_abhi/SAMEA2340910_2.fastq.gz -vv

#ERR502505 SAMEA2340912
rclone copy onedrive-abhi:maf-genomes/ERR502505_1.fastq.gz ./genomes_abhi/SAMEA2340912_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502505_2.fastq.gz ./genomes_abhi/SAMEA2340912_2.fastq.gz -vv

#ERR502506 SAMEA2340913
rclone copy onedrive-abhi:maf-genomes/ERR502506_1.fastq.gz ./genomes_abhi/SAMEA2340913_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502506_2.fastq.gz ./genomes_abhi/SAMEA2340913_2.fastq.gz -vv

#ERR502507 SAMEA2340914
rclone copy onedrive-abhi:maf-genomes/ERR502507_1.fastq.gz ./genomes_abhi/SAMEA2340914_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502507_2.fastq.gz ./genomes_abhi/SAMEA2340914_2.fastq.gz -vv

#ERR502508 SAMEA2340915
rclone copy onedrive-abhi:maf-genomes/ERR502508_1.fastq.gz ./genomes_abhi/SAMEA2340915_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502508_2.fastq.gz ./genomes_abhi/SAMEA2340915_2.fastq.gz -vv

#ERR502509 SAMEA2340916
rclone copy onedrive-abhi:maf-genomes/ERR502509_1.fastq.gz ./genomes_abhi/SAMEA2340916_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502509_2.fastq.gz ./genomes_abhi/SAMEA2340916_2.fastq.gz -vv

#ERR502510 SAMEA2340917
rclone copy onedrive-abhi:maf-genomes/ERR502510_1.fastq.gz ./genomes_abhi/SAMEA2340917_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502510_2.fastq.gz ./genomes_abhi/SAMEA2340917_2.fastq.gz -vv

#ERR502511 SAMEA2340918
rclone copy onedrive-abhi:maf-genomes/ERR502511_1.fastq.gz ./genomes_abhi/SAMEA2340918_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502511_2.fastq.gz ./genomes_abhi/SAMEA2340918_2.fastq.gz -vv

#ERR502512 SAMEA2340919
rclone copy onedrive-abhi:maf-genomes/ERR502512_1.fastq.gz ./genomes_abhi/SAMEA2340919_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502512_2.fastq.gz ./genomes_abhi/SAMEA2340919_2.fastq.gz -vv

#ERR502513 SAMEA2340920
rclone copy onedrive-abhi:maf-genomes/ERR502513_1.fastq.gz ./genomes_abhi/SAMEA2340920_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502513_2.fastq.gz ./genomes_abhi/SAMEA2340920_2.fastq.gz -vv

#ERR502514 SAMEA2340921
rclone copy onedrive-abhi:maf-genomes/ERR502514_1.fastq.gz ./genomes_abhi/SAMEA2340921_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502514_2.fastq.gz ./genomes_abhi/SAMEA2340921_2.fastq.gz -vv

#ERR502515 SAMEA2340922
rclone copy onedrive-abhi:maf-genomes/ERR502515_1.fastq.gz ./genomes_abhi/SAMEA2340922_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502515_2.fastq.gz ./genomes_abhi/SAMEA2340922_2.fastq.gz -vv

#ERR502516 SAMEA2340923
rclone copy onedrive-abhi:maf-genomes/ERR502516_1.fastq.gz ./genomes_abhi/SAMEA2340923_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502516_2.fastq.gz ./genomes_abhi/SAMEA2340923_2.fastq.gz -vv

#ERR502517 SAMEA2340924
rclone copy onedrive-abhi:maf-genomes/ERR502517_1.fastq.gz ./genomes_abhi/SAMEA2340924_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502517_2.fastq.gz ./genomes_abhi/SAMEA2340924_2.fastq.gz -vv

#ERR502521 SAMEA2340929
rclone copy onedrive-abhi:maf-genomes/ERR502521_1.fastq.gz ./genomes_abhi/SAMEA2340929_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502521_2.fastq.gz ./genomes_abhi/SAMEA2340929_2.fastq.gz -vv

#ERR502522 SAMEA2340930
rclone copy onedrive-abhi:maf-genomes/ERR502522_1.fastq.gz ./genomes_abhi/SAMEA2340930_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502522_2.fastq.gz ./genomes_abhi/SAMEA2340930_2.fastq.gz -vv

#ERR502523 SAMEA2340931
rclone copy onedrive-abhi:maf-genomes/ERR502523_1.fastq.gz ./genomes_abhi/SAMEA2340931_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502523_2.fastq.gz ./genomes_abhi/SAMEA2340931_2.fastq.gz -vv

#ERR502524 SAMEA2340932
rclone copy onedrive-abhi:maf-genomes/ERR502524_1.fastq.gz ./genomes_abhi/SAMEA2340932_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502524_2.fastq.gz ./genomes_abhi/SAMEA2340932_2.fastq.gz -vv

#ERR502525 SAMEA2340933
rclone copy onedrive-abhi:maf-genomes/ERR502525_1.fastq.gz ./genomes_abhi/SAMEA2340933_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502525_2.fastq.gz ./genomes_abhi/SAMEA2340933_2.fastq.gz -vv

#ERR502527 SAMEA2340935
rclone copy onedrive-abhi:maf-genomes/ERR502527_1.fastq.gz ./genomes_abhi/SAMEA2340935_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502527_2.fastq.gz ./genomes_abhi/SAMEA2340935_2.fastq.gz -vv

#ERR502528 SAMEA2340936
rclone copy onedrive-abhi:maf-genomes/ERR502528_1.fastq.gz ./genomes_abhi/SAMEA2340936_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502528_2.fastq.gz ./genomes_abhi/SAMEA2340936_2.fastq.gz -vv

#ERR502530 SAMEA2340938
rclone copy onedrive-abhi:maf-genomes/ERR502530_1.fastq.gz ./genomes_abhi/SAMEA2340938_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502530_2.fastq.gz ./genomes_abhi/SAMEA2340938_2.fastq.gz -vv

#ERR502531 SAMEA2340939
rclone copy onedrive-abhi:maf-genomes/ERR502531_1.fastq.gz ./genomes_abhi/SAMEA2340939_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502531_2.fastq.gz ./genomes_abhi/SAMEA2340939_2.fastq.gz -vv

#ERR502532 SAMEA2340940
rclone copy onedrive-abhi:maf-genomes/ERR502532_1.fastq.gz ./genomes_abhi/SAMEA2340940_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502532_2.fastq.gz ./genomes_abhi/SAMEA2340940_2.fastq.gz -vv

#ERR502533 SAMEA2340941
rclone copy onedrive-abhi:maf-genomes/ERR502533_1.fastq.gz ./genomes_abhi/SAMEA2340941_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502533_2.fastq.gz ./genomes_abhi/SAMEA2340941_2.fastq.gz -vv

#ERR502534 SAMEA2340942
rclone copy onedrive-abhi:maf-genomes/ERR502534_1.fastq.gz ./genomes_abhi/SAMEA2340942_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502534_2.fastq.gz ./genomes_abhi/SAMEA2340942_2.fastq.gz -vv

#ERR502536 SAMEA2340946
rclone copy onedrive-abhi:maf-genomes/ERR502536_1.fastq.gz ./genomes_abhi/SAMEA2340946_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502536_2.fastq.gz ./genomes_abhi/SAMEA2340946_2.fastq.gz -vv

#ERR502537 SAMEA2340947
rclone copy onedrive-abhi:maf-genomes/ERR502537_1.fastq.gz ./genomes_abhi/SAMEA2340947_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR502537_2.fastq.gz ./genomes_abhi/SAMEA2340947_2.fastq.gz -vv

#ERR517471 SAMEA2340874
rclone copy onedrive-abhi:maf-genomes/ERR517471_1.fastq.gz ./genomes_abhi/SAMEA2340874_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR517471_2.fastq.gz ./genomes_abhi/SAMEA2340874_2.fastq.gz -vv

#ERR551617 SAMEA2534073
rclone copy onedrive-abhi:maf-genomes/ERR551617_1.fastq.gz ./genomes_abhi/SAMEA2534073_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR551617_2.fastq.gz ./genomes_abhi/SAMEA2534073_2.fastq.gz -vv

#ERR552021 SAMEA2534357
rclone copy onedrive-abhi:maf-genomes/ERR552021_1.fastq.gz ./genomes_abhi/SAMEA2534357_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552021_2.fastq.gz ./genomes_abhi/SAMEA2534357_2.fastq.gz -vv

#ERR552172 SAMEA2534462
rclone copy onedrive-abhi:maf-genomes/ERR552172_1.fastq.gz ./genomes_abhi/SAMEA2534462_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552172_2.fastq.gz ./genomes_abhi/SAMEA2534462_2.fastq.gz -vv

#ERR552187 SAMEA2534473
rclone copy onedrive-abhi:maf-genomes/ERR552187_1.fastq.gz ./genomes_abhi/SAMEA2534473_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552187_2.fastq.gz ./genomes_abhi/SAMEA2534473_2.fastq.gz -vv

#ERR552328 SAMEA2534569
rclone copy onedrive-abhi:maf-genomes/ERR552328_1.fastq.gz ./genomes_abhi/SAMEA2534569_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552328_2.fastq.gz ./genomes_abhi/SAMEA2534569_2.fastq.gz -vv

#ERR552506 SAMEA2534695
rclone copy onedrive-abhi:maf-genomes/ERR552506_1.fastq.gz ./genomes_abhi/SAMEA2534695_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552506_2.fastq.gz ./genomes_abhi/SAMEA2534695_2.fastq.gz -vv

#ERR552588 SAMEA2534751
rclone copy onedrive-abhi:maf-genomes/ERR552588_1.fastq.gz ./genomes_abhi/SAMEA2534751_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552588_2.fastq.gz ./genomes_abhi/SAMEA2534751_2.fastq.gz -vv

#ERR552963 SAMEA2535035
rclone copy onedrive-abhi:maf-genomes/ERR552963_1.fastq.gz ./genomes_abhi/SAMEA2535035_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR552963_2.fastq.gz ./genomes_abhi/SAMEA2535035_2.fastq.gz -vv

#ERR702400 SAMEA2627006
rclone copy onedrive-abhi:maf-genomes/ERR702400_1.fastq.gz ./genomes_abhi/SAMEA2627006_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702400_2.fastq.gz ./genomes_abhi/SAMEA2627006_2.fastq.gz -vv

#ERR702401 SAMEA2627007
rclone copy onedrive-abhi:maf-genomes/ERR702401_1.fastq.gz ./genomes_abhi/SAMEA2627007_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702401_2.fastq.gz ./genomes_abhi/SAMEA2627007_2.fastq.gz -vv

#ERR702407 SAMEA2627013
rclone copy onedrive-abhi:maf-genomes/ERR702407_1.fastq.gz ./genomes_abhi/SAMEA2627013_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702407_2.fastq.gz ./genomes_abhi/SAMEA2627013_2.fastq.gz -vv

#ERR702408 SAMEA2627014
rclone copy onedrive-abhi:maf-genomes/ERR702408_1.fastq.gz ./genomes_abhi/SAMEA2627014_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702408_2.fastq.gz ./genomes_abhi/SAMEA2627014_2.fastq.gz -vv

#ERR702409 SAMEA2627015
rclone copy onedrive-abhi:maf-genomes/ERR702409_1.fastq.gz ./genomes_abhi/SAMEA2627015_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702409_2.fastq.gz ./genomes_abhi/SAMEA2627015_2.fastq.gz -vv

#ERR702410 SAMEA2627016
rclone copy onedrive-abhi:maf-genomes/ERR702410_1.fastq.gz ./genomes_abhi/SAMEA2627016_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702410_2.fastq.gz ./genomes_abhi/SAMEA2627016_2.fastq.gz -vv

#ERR702411 SAMEA2627017
rclone copy onedrive-abhi:maf-genomes/ERR702411_1.fastq.gz ./genomes_abhi/SAMEA2627017_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702411_2.fastq.gz ./genomes_abhi/SAMEA2627017_2.fastq.gz -vv

#ERR702412 SAMEA2627018
rclone copy onedrive-abhi:maf-genomes/ERR702412_1.fastq.gz ./genomes_abhi/SAMEA2627018_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702412_2.fastq.gz ./genomes_abhi/SAMEA2627018_2.fastq.gz -vv

#ERR702413 SAMEA2627019
rclone copy onedrive-abhi:maf-genomes/ERR702413_1.fastq.gz ./genomes_abhi/SAMEA2627019_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702413_2.fastq.gz ./genomes_abhi/SAMEA2627019_2.fastq.gz -vv

#ERR702414 SAMEA2627020
rclone copy onedrive-abhi:maf-genomes/ERR702414_1.fastq.gz ./genomes_abhi/SAMEA2627020_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702414_2.fastq.gz ./genomes_abhi/SAMEA2627020_2.fastq.gz -vv

#ERR702415 SAMEA2627021
rclone copy onedrive-abhi:maf-genomes/ERR702415_1.fastq.gz ./genomes_abhi/SAMEA2627021_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702415_2.fastq.gz ./genomes_abhi/SAMEA2627021_2.fastq.gz -vv

#ERR702416 SAMEA2627022
rclone copy onedrive-abhi:maf-genomes/ERR702416_1.fastq.gz ./genomes_abhi/SAMEA2627022_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702416_2.fastq.gz ./genomes_abhi/SAMEA2627022_2.fastq.gz -vv

#ERR702417 SAMEA2627023
rclone copy onedrive-abhi:maf-genomes/ERR702417_1.fastq.gz ./genomes_abhi/SAMEA2627023_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702417_2.fastq.gz ./genomes_abhi/SAMEA2627023_2.fastq.gz -vv

#ERR702418 SAMEA2627024
rclone copy onedrive-abhi:maf-genomes/ERR702418_1.fastq.gz ./genomes_abhi/SAMEA2627024_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702418_2.fastq.gz ./genomes_abhi/SAMEA2627024_2.fastq.gz -vv

#ERR702419 SAMEA2627025
rclone copy onedrive-abhi:maf-genomes/ERR702419_1.fastq.gz ./genomes_abhi/SAMEA2627025_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702419_2.fastq.gz ./genomes_abhi/SAMEA2627025_2.fastq.gz -vv

#ERR702420 SAMEA2627026
rclone copy onedrive-abhi:maf-genomes/ERR702420_1.fastq.gz ./genomes_abhi/SAMEA2627026_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702420_2.fastq.gz ./genomes_abhi/SAMEA2627026_2.fastq.gz -vv

#ERR702421 SAMEA2627027
rclone copy onedrive-abhi:maf-genomes/ERR702421_1.fastq.gz ./genomes_abhi/SAMEA2627027_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702421_2.fastq.gz ./genomes_abhi/SAMEA2627027_2.fastq.gz -vv

#ERR702422 SAMEA2627028
rclone copy onedrive-abhi:maf-genomes/ERR702422_1.fastq.gz ./genomes_abhi/SAMEA2627028_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702422_2.fastq.gz ./genomes_abhi/SAMEA2627028_2.fastq.gz -vv

#ERR702423 SAMEA2627029
rclone copy onedrive-abhi:maf-genomes/ERR702423_1.fastq.gz ./genomes_abhi/SAMEA2627029_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702423_2.fastq.gz ./genomes_abhi/SAMEA2627029_2.fastq.gz -vv

#ERR702424 SAMEA2627030
rclone copy onedrive-abhi:maf-genomes/ERR702424_1.fastq.gz ./genomes_abhi/SAMEA2627030_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702424_2.fastq.gz ./genomes_abhi/SAMEA2627030_2.fastq.gz -vv

#ERR702425 SAMEA2627031
rclone copy onedrive-abhi:maf-genomes/ERR702425_1.fastq.gz ./genomes_abhi/SAMEA2627031_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702425_2.fastq.gz ./genomes_abhi/SAMEA2627031_2.fastq.gz -vv

#ERR702426 SAMEA2627032
rclone copy onedrive-abhi:maf-genomes/ERR702426_1.fastq.gz ./genomes_abhi/SAMEA2627032_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702426_2.fastq.gz ./genomes_abhi/SAMEA2627032_2.fastq.gz -vv

#ERR702427 SAMEA2627033
rclone copy onedrive-abhi:maf-genomes/ERR702427_1.fastq.gz ./genomes_abhi/SAMEA2627033_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702427_2.fastq.gz ./genomes_abhi/SAMEA2627033_2.fastq.gz -vv

#ERR702428 SAMEA2627035
rclone copy onedrive-abhi:maf-genomes/ERR702428_1.fastq.gz ./genomes_abhi/SAMEA2627035_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702428_2.fastq.gz ./genomes_abhi/SAMEA2627035_2.fastq.gz -vv

#ERR702429 SAMEA2627036
rclone copy onedrive-abhi:maf-genomes/ERR702429_1.fastq.gz ./genomes_abhi/SAMEA2627036_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702429_2.fastq.gz ./genomes_abhi/SAMEA2627036_2.fastq.gz -vv

#ERR702430 SAMEA2627037
rclone copy onedrive-abhi:maf-genomes/ERR702430_1.fastq.gz ./genomes_abhi/SAMEA2627037_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702430_2.fastq.gz ./genomes_abhi/SAMEA2627037_2.fastq.gz -vv

#ERR702431 SAMEA2627038
rclone copy onedrive-abhi:maf-genomes/ERR702431_1.fastq.gz ./genomes_abhi/SAMEA2627038_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702431_2.fastq.gz ./genomes_abhi/SAMEA2627038_2.fastq.gz -vv

#ERR702432 SAMEA2627039
rclone copy onedrive-abhi:maf-genomes/ERR702432_1.fastq.gz ./genomes_abhi/SAMEA2627039_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702432_2.fastq.gz ./genomes_abhi/SAMEA2627039_2.fastq.gz -vv

#ERR702434 SAMEA2627041
rclone copy onedrive-abhi:maf-genomes/ERR702434_1.fastq.gz ./genomes_abhi/SAMEA2627041_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702434_2.fastq.gz ./genomes_abhi/SAMEA2627041_2.fastq.gz -vv

#ERR702435 SAMEA2627042
rclone copy onedrive-abhi:maf-genomes/ERR702435_1.fastq.gz ./genomes_abhi/SAMEA2627042_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702435_2.fastq.gz ./genomes_abhi/SAMEA2627042_2.fastq.gz -vv

#ERR702436 SAMEA2627043
rclone copy onedrive-abhi:maf-genomes/ERR702436_1.fastq.gz ./genomes_abhi/SAMEA2627043_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR702436_2.fastq.gz ./genomes_abhi/SAMEA2627043_2.fastq.gz -vv

#ERR751290 SAMEA2794312
rclone copy onedrive-abhi:maf-genomes/ERR751290_1.fastq.gz ./genomes_abhi/SAMEA2794312_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751290_2.fastq.gz ./genomes_abhi/SAMEA2794312_2.fastq.gz -vv

#ERR751291 SAMEA2794313
rclone copy onedrive-abhi:maf-genomes/ERR751291_1.fastq.gz ./genomes_abhi/SAMEA2794313_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751291_2.fastq.gz ./genomes_abhi/SAMEA2794313_2.fastq.gz -vv

#ERR751292 SAMEA2794314
rclone copy onedrive-abhi:maf-genomes/ERR751292_1.fastq.gz ./genomes_abhi/SAMEA2794314_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751292_2.fastq.gz ./genomes_abhi/SAMEA2794314_2.fastq.gz -vv

#ERR751293 SAMEA2794315
rclone copy onedrive-abhi:maf-genomes/ERR751293_1.fastq.gz ./genomes_abhi/SAMEA2794315_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751293_2.fastq.gz ./genomes_abhi/SAMEA2794315_2.fastq.gz -vv

#ERR751294 SAMEA2794316
rclone copy onedrive-abhi:maf-genomes/ERR751294_1.fastq.gz ./genomes_abhi/SAMEA2794316_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751294_2.fastq.gz ./genomes_abhi/SAMEA2794316_2.fastq.gz -vv

#ERR751295 SAMEA2794317
rclone copy onedrive-abhi:maf-genomes/ERR751295_1.fastq.gz ./genomes_abhi/SAMEA2794317_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751295_2.fastq.gz ./genomes_abhi/SAMEA2794317_2.fastq.gz -vv

#ERR751296 SAMEA2794318
rclone copy onedrive-abhi:maf-genomes/ERR751296_1.fastq.gz ./genomes_abhi/SAMEA2794318_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751296_2.fastq.gz ./genomes_abhi/SAMEA2794318_2.fastq.gz -vv

#ERR751297 SAMEA2794319
rclone copy onedrive-abhi:maf-genomes/ERR751297_1.fastq.gz ./genomes_abhi/SAMEA2794319_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751297_2.fastq.gz ./genomes_abhi/SAMEA2794319_2.fastq.gz -vv

#ERR751298 SAMEA2794320
rclone copy onedrive-abhi:maf-genomes/ERR751298_1.fastq.gz ./genomes_abhi/SAMEA2794320_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751298_2.fastq.gz ./genomes_abhi/SAMEA2794320_2.fastq.gz -vv

#ERR751299 SAMEA2794321
rclone copy onedrive-abhi:maf-genomes/ERR751299_1.fastq.gz ./genomes_abhi/SAMEA2794321_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751299_2.fastq.gz ./genomes_abhi/SAMEA2794321_2.fastq.gz -vv

#ERR751300 SAMEA2794322
rclone copy onedrive-abhi:maf-genomes/ERR751300_1.fastq.gz ./genomes_abhi/SAMEA2794322_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751300_2.fastq.gz ./genomes_abhi/SAMEA2794322_2.fastq.gz -vv

#ERR751301 SAMEA2794323
rclone copy onedrive-abhi:maf-genomes/ERR751301_1.fastq.gz ./genomes_abhi/SAMEA2794323_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751301_2.fastq.gz ./genomes_abhi/SAMEA2794323_2.fastq.gz -vv

#ERR751302 SAMEA2794324
rclone copy onedrive-abhi:maf-genomes/ERR751302_1.fastq.gz ./genomes_abhi/SAMEA2794324_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751302_2.fastq.gz ./genomes_abhi/SAMEA2794324_2.fastq.gz -vv

#ERR751303 SAMEA2794325
rclone copy onedrive-abhi:maf-genomes/ERR751303_1.fastq.gz ./genomes_abhi/SAMEA2794325_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751303_2.fastq.gz ./genomes_abhi/SAMEA2794325_2.fastq.gz -vv

#ERR751304 SAMEA2794326
rclone copy onedrive-abhi:maf-genomes/ERR751304_1.fastq.gz ./genomes_abhi/SAMEA2794326_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751304_2.fastq.gz ./genomes_abhi/SAMEA2794326_2.fastq.gz -vv

#ERR751305 SAMEA2794327
rclone copy onedrive-abhi:maf-genomes/ERR751305_1.fastq.gz ./genomes_abhi/SAMEA2794327_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751305_2.fastq.gz ./genomes_abhi/SAMEA2794327_2.fastq.gz -vv

#ERR751306 SAMEA2794328
rclone copy onedrive-abhi:maf-genomes/ERR751306_1.fastq.gz ./genomes_abhi/SAMEA2794328_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751306_2.fastq.gz ./genomes_abhi/SAMEA2794328_2.fastq.gz -vv

#ERR751307 SAMEA2794329
rclone copy onedrive-abhi:maf-genomes/ERR751307_1.fastq.gz ./genomes_abhi/SAMEA2794329_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751307_2.fastq.gz ./genomes_abhi/SAMEA2794329_2.fastq.gz -vv

#ERR751308 SAMEA2794330
rclone copy onedrive-abhi:maf-genomes/ERR751308_1.fastq.gz ./genomes_abhi/SAMEA2794330_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751308_2.fastq.gz ./genomes_abhi/SAMEA2794330_2.fastq.gz -vv

#ERR751309 SAMEA2794331
rclone copy onedrive-abhi:maf-genomes/ERR751309_1.fastq.gz ./genomes_abhi/SAMEA2794331_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751309_2.fastq.gz ./genomes_abhi/SAMEA2794331_2.fastq.gz -vv

#ERR751310 SAMEA2794332
rclone copy onedrive-abhi:maf-genomes/ERR751310_1.fastq.gz ./genomes_abhi/SAMEA2794332_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751310_2.fastq.gz ./genomes_abhi/SAMEA2794332_2.fastq.gz -vv

#ERR751311 SAMEA2794333
rclone copy onedrive-abhi:maf-genomes/ERR751311_1.fastq.gz ./genomes_abhi/SAMEA2794333_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751311_2.fastq.gz ./genomes_abhi/SAMEA2794333_2.fastq.gz -vv

#ERR751312 SAMEA2794334
rclone copy onedrive-abhi:maf-genomes/ERR751312_1.fastq.gz ./genomes_abhi/SAMEA2794334_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751312_2.fastq.gz ./genomes_abhi/SAMEA2794334_2.fastq.gz -vv

#ERR751313 SAMEA2794335
rclone copy onedrive-abhi:maf-genomes/ERR751313_1.fastq.gz ./genomes_abhi/SAMEA2794335_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751313_2.fastq.gz ./genomes_abhi/SAMEA2794335_2.fastq.gz -vv

#ERR751314 SAMEA2794336
rclone copy onedrive-abhi:maf-genomes/ERR751314_1.fastq.gz ./genomes_abhi/SAMEA2794336_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751314_2.fastq.gz ./genomes_abhi/SAMEA2794336_2.fastq.gz -vv

#ERR751315 SAMEA2794337
rclone copy onedrive-abhi:maf-genomes/ERR751315_1.fastq.gz ./genomes_abhi/SAMEA2794337_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751315_2.fastq.gz ./genomes_abhi/SAMEA2794337_2.fastq.gz -vv

#ERR751317 SAMEA2794339
rclone copy onedrive-abhi:maf-genomes/ERR751317_1.fastq.gz ./genomes_abhi/SAMEA2794339_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751317_2.fastq.gz ./genomes_abhi/SAMEA2794339_2.fastq.gz -vv

#ERR751318 SAMEA2794340
rclone copy onedrive-abhi:maf-genomes/ERR751318_1.fastq.gz ./genomes_abhi/SAMEA2794340_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751318_2.fastq.gz ./genomes_abhi/SAMEA2794340_2.fastq.gz -vv

#ERR751319 SAMEA2794341
rclone copy onedrive-abhi:maf-genomes/ERR751319_1.fastq.gz ./genomes_abhi/SAMEA2794341_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751319_2.fastq.gz ./genomes_abhi/SAMEA2794341_2.fastq.gz -vv

#ERR751320 SAMEA2794342
rclone copy onedrive-abhi:maf-genomes/ERR751320_1.fastq.gz ./genomes_abhi/SAMEA2794342_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751320_2.fastq.gz ./genomes_abhi/SAMEA2794342_2.fastq.gz -vv

#ERR751321 SAMEA2794343
rclone copy onedrive-abhi:maf-genomes/ERR751321_1.fastq.gz ./genomes_abhi/SAMEA2794343_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751321_2.fastq.gz ./genomes_abhi/SAMEA2794343_2.fastq.gz -vv

#ERR751322 SAMEA2794344
rclone copy onedrive-abhi:maf-genomes/ERR751322_1.fastq.gz ./genomes_abhi/SAMEA2794344_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751322_2.fastq.gz ./genomes_abhi/SAMEA2794344_2.fastq.gz -vv

#ERR751323 SAMEA2794345
rclone copy onedrive-abhi:maf-genomes/ERR751323_1.fastq.gz ./genomes_abhi/SAMEA2794345_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751323_2.fastq.gz ./genomes_abhi/SAMEA2794345_2.fastq.gz -vv

#ERR751324 SAMEA2794346
rclone copy onedrive-abhi:maf-genomes/ERR751324_1.fastq.gz ./genomes_abhi/SAMEA2794346_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751324_2.fastq.gz ./genomes_abhi/SAMEA2794346_2.fastq.gz -vv

#ERR751325 SAMEA2794347
rclone copy onedrive-abhi:maf-genomes/ERR751325_1.fastq.gz ./genomes_abhi/SAMEA2794347_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751325_2.fastq.gz ./genomes_abhi/SAMEA2794347_2.fastq.gz -vv

#ERR751326 SAMEA2794348
rclone copy onedrive-abhi:maf-genomes/ERR751326_1.fastq.gz ./genomes_abhi/SAMEA2794348_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751326_2.fastq.gz ./genomes_abhi/SAMEA2794348_2.fastq.gz -vv

#ERR751327 SAMEA2794349
rclone copy onedrive-abhi:maf-genomes/ERR751327_1.fastq.gz ./genomes_abhi/SAMEA2794349_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751327_2.fastq.gz ./genomes_abhi/SAMEA2794349_2.fastq.gz -vv

#ERR751328 SAMEA2794350
rclone copy onedrive-abhi:maf-genomes/ERR751328_1.fastq.gz ./genomes_abhi/SAMEA2794350_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751328_2.fastq.gz ./genomes_abhi/SAMEA2794350_2.fastq.gz -vv

#ERR751329 SAMEA2794351
rclone copy onedrive-abhi:maf-genomes/ERR751329_1.fastq.gz ./genomes_abhi/SAMEA2794351_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751329_2.fastq.gz ./genomes_abhi/SAMEA2794351_2.fastq.gz -vv

#ERR751330 SAMEA2794352
rclone copy onedrive-abhi:maf-genomes/ERR751330_1.fastq.gz ./genomes_abhi/SAMEA2794352_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751330_2.fastq.gz ./genomes_abhi/SAMEA2794352_2.fastq.gz -vv

#ERR751331 SAMEA2794353
rclone copy onedrive-abhi:maf-genomes/ERR751331_1.fastq.gz ./genomes_abhi/SAMEA2794353_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751331_2.fastq.gz ./genomes_abhi/SAMEA2794353_2.fastq.gz -vv

#ERR751332 SAMEA2794354
rclone copy onedrive-abhi:maf-genomes/ERR751332_1.fastq.gz ./genomes_abhi/SAMEA2794354_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751332_2.fastq.gz ./genomes_abhi/SAMEA2794354_2.fastq.gz -vv

#ERR751333 SAMEA2794355
rclone copy onedrive-abhi:maf-genomes/ERR751333_1.fastq.gz ./genomes_abhi/SAMEA2794355_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751333_2.fastq.gz ./genomes_abhi/SAMEA2794355_2.fastq.gz -vv

#ERR751334 SAMEA2794357
rclone copy onedrive-abhi:maf-genomes/ERR751334_1.fastq.gz ./genomes_abhi/SAMEA2794357_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751334_2.fastq.gz ./genomes_abhi/SAMEA2794357_2.fastq.gz -vv

#ERR751335 SAMEA2794358
rclone copy onedrive-abhi:maf-genomes/ERR751335_1.fastq.gz ./genomes_abhi/SAMEA2794358_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751335_2.fastq.gz ./genomes_abhi/SAMEA2794358_2.fastq.gz -vv

#ERR751336 SAMEA2794359
rclone copy onedrive-abhi:maf-genomes/ERR751336_1.fastq.gz ./genomes_abhi/SAMEA2794359_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751336_2.fastq.gz ./genomes_abhi/SAMEA2794359_2.fastq.gz -vv

#ERR751337 SAMEA2794360
rclone copy onedrive-abhi:maf-genomes/ERR751337_1.fastq.gz ./genomes_abhi/SAMEA2794360_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751337_2.fastq.gz ./genomes_abhi/SAMEA2794360_2.fastq.gz -vv

#ERR751338 SAMEA2794361
rclone copy onedrive-abhi:maf-genomes/ERR751338_1.fastq.gz ./genomes_abhi/SAMEA2794361_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751338_2.fastq.gz ./genomes_abhi/SAMEA2794361_2.fastq.gz -vv

#ERR751339 SAMEA2794362
rclone copy onedrive-abhi:maf-genomes/ERR751339_1.fastq.gz ./genomes_abhi/SAMEA2794362_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751339_2.fastq.gz ./genomes_abhi/SAMEA2794362_2.fastq.gz -vv

#ERR751341 SAMEA2794364
rclone copy onedrive-abhi:maf-genomes/ERR751341_1.fastq.gz ./genomes_abhi/SAMEA2794364_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751341_2.fastq.gz ./genomes_abhi/SAMEA2794364_2.fastq.gz -vv

#ERR751342 SAMEA2794365
rclone copy onedrive-abhi:maf-genomes/ERR751342_1.fastq.gz ./genomes_abhi/SAMEA2794365_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751342_2.fastq.gz ./genomes_abhi/SAMEA2794365_2.fastq.gz -vv

#ERR751343 SAMEA2794366
rclone copy onedrive-abhi:maf-genomes/ERR751343_1.fastq.gz ./genomes_abhi/SAMEA2794366_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751343_2.fastq.gz ./genomes_abhi/SAMEA2794366_2.fastq.gz -vv

#ERR751344 SAMEA2794367
rclone copy onedrive-abhi:maf-genomes/ERR751344_1.fastq.gz ./genomes_abhi/SAMEA2794367_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751344_2.fastq.gz ./genomes_abhi/SAMEA2794367_2.fastq.gz -vv

#ERR751345 SAMEA2794368
rclone copy onedrive-abhi:maf-genomes/ERR751345_1.fastq.gz ./genomes_abhi/SAMEA2794368_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751345_2.fastq.gz ./genomes_abhi/SAMEA2794368_2.fastq.gz -vv

#ERR751346 SAMEA2794369
rclone copy onedrive-abhi:maf-genomes/ERR751346_1.fastq.gz ./genomes_abhi/SAMEA2794369_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751346_2.fastq.gz ./genomes_abhi/SAMEA2794369_2.fastq.gz -vv

#ERR751347 SAMEA2794370
rclone copy onedrive-abhi:maf-genomes/ERR751347_1.fastq.gz ./genomes_abhi/SAMEA2794370_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751347_2.fastq.gz ./genomes_abhi/SAMEA2794370_2.fastq.gz -vv

#ERR751348 SAMEA2794371
rclone copy onedrive-abhi:maf-genomes/ERR751348_1.fastq.gz ./genomes_abhi/SAMEA2794371_1.fastq.gz -vv
rclone copy onedrive-abhi:maf-genomes/ERR751348_2.fastq.gz ./genomes_abhi/SAMEA2794371_2.fastq.gz -vv


```

2. Then all of the genomes were renamed either during the download process or were already named like we wanted.


3. Some genomes were of bad quality.


```
rm -rf SAMEA2340875_1.fastq.gz
rm -rf SAMEA2340875_2.fastq.gz	
rm -rf SAMEA2340877_1.fastq.gz
rm -rf SAMEA2340877_2.fastq.gz	
rm -rf SAMEA2340878_1.fastq.gz
rm -rf SAMEA2340878_2.fastq.gz	
rm -rf SAMEA2340879_1.fastq.gz
rm -rf SAMEA2340879_2.fastq.gz	
rm -rf SAMEA2340883_1.fastq.gz
rm -rf SAMEA2340883_2.fastq.gz	
rm -rf SAMEA2340884_1.fastq.gz
rm -rf SAMEA2340884_2.fastq.gz	
rm -rf SAMEA2340885_1.fastq.gz
rm -rf SAMEA2340885_2.fastq.gz	
rm -rf SAMEA2340888_1.fastq.gz
rm -rf SAMEA2340888_2.fastq.gz	
rm -rf SAMEA2340889_1.fastq.gz
rm -rf SAMEA2340889_2.fastq.gz	
rm -rf SAMEA2340890_1.fastq.gz
rm -rf SAMEA2340890_2.fastq.gz	
rm -rf SAMEA2340891_1.fastq.gz
rm -rf SAMEA2340891_2.fastq.gz	
rm -rf SAMEA2340892_1.fastq.gz
rm -rf SAMEA2340892_2.fastq.gz	
rm -rf SAMEA2340893_1.fastq.gz
rm -rf SAMEA2340893_2.fastq.gz	
rm -rf SAMEA2340896_1.fastq.gz
rm -rf SAMEA2340896_2.fastq.gz	
rm -rf SAMEA2340897_1.fastq.gz
rm -rf SAMEA2340897_2.fastq.gz	
rm -rf SAMEA2340899_1.fastq.gz
rm -rf SAMEA2340899_2.fastq.gz	
rm -rf SAMEA2340900_1.fastq.gz
rm -rf SAMEA2340900_2.fastq.gz	
rm -rf SAMEA2340903_1.fastq.gz
rm -rf SAMEA2340903_2.fastq.gz	
rm -rf SAMEA2340904_1.fastq.gz
rm -rf SAMEA2340904_2.fastq.gz	
rm -rf SAMEA2340905_1.fastq.gz
rm -rf SAMEA2340905_2.fastq.gz	
rm -rf SAMEA2340917_1.fastq.gz
rm -rf SAMEA2340917_2.fastq.gz	
rm -rf SAMEA2340918_1.fastq.gz
rm -rf SAMEA2340918_2.fastq.gz	
rm -rf SAMEA2340924_1.fastq.gz
rm -rf SAMEA2340924_2.fastq.gz	
rm -rf SAMEA2340932_1.fastq.gz
rm -rf SAMEA2340932_2.fastq.gz	
rm -rf SAMEA2340939_1.fastq.gz
rm -rf SAMEA2340939_2.fastq.gz	
rm -rf SAMEA2340940_1.fastq.gz
rm -rf SAMEA2340940_2.fastq.gz	
rm -rf SAMEA2534073_1.fastq.gz
rm -rf SAMEA2534073_2.fastq.gz	
rm -rf SAMEA2534321_1.fastq.gz
rm -rf SAMEA2534321_2.fastq.gz	
rm -rf SAMEA2534357_1.fastq.gz
rm -rf SAMEA2534357_2.fastq.gz	
rm -rf SAMEA2534462_1.fastq.gz
rm -rf SAMEA2534462_2.fastq.gz	
rm -rf SAMEA2534473_1.fastq.gz
rm -rf SAMEA2534473_2.fastq.gz	
rm -rf SAMEA2534569_1.fastq.gz
rm -rf SAMEA2534569_2.fastq.gz	
rm -rf SAMEA2627006_1.fastq.gz
rm -rf SAMEA2627006_2.fastq.gz	
rm -rf SAMEA2627010_1.fastq.gz
rm -rf SAMEA2627010_2.fastq.gz	
rm -rf SAMEA2627011_1.fastq.gz
rm -rf SAMEA2627011_2.fastq.gz	
rm -rf SAMEA2627012_1.fastq.gz
rm -rf SAMEA2627012_2.fastq.gz	
rm -rf SAMEA2627034_1.fastq.gz
rm -rf SAMEA2627034_2.fastq.gz	
rm -rf SAMEA2627036_1.fastq.gz
rm -rf SAMEA2627036_2.fastq.gz	
rm -rf SAMEA2627045_1.fastq.gz
rm -rf SAMEA2627045_2.fastq.gz	
rm -rf SAMEA2794339_1.fastq.gz
rm -rf SAMEA2794339_2.fastq.gz	
rm -rf SAMEA2794340_1.fastq.gz
rm -rf SAMEA2794340_2.fastq.gz	
rm -rf SAMEA2794347_1.fastq.gz
rm -rf SAMEA2794347_2.fastq.gz	
rm -rf SAMEA2794348_1.fastq.gz
rm -rf SAMEA2794348_2.fastq.gz	
rm -rf SAMEA2794356_1.fastq.gz
rm -rf SAMEA2794356_2.fastq.gz	
rm -rf SAMEA2794370_1.fastq.gz
rm -rf SAMEA2794370_2.fastq.gz	
rm -rf SAMEA3359870_1.fastq.gz
rm -rf SAMEA3359870_2.fastq.gz	
rm -rf SAMEA3359873_1.fastq.gz
rm -rf SAMEA3359873_2.fastq.gz	
rm -rf SAMEA3359883_1.fastq.gz
rm -rf SAMEA3359883_2.fastq.gz	
rm -rf SAMEA3359889_1.fastq.gz
rm -rf SAMEA3359889_2.fastq.gz	
rm -rf SAMEA3359892_1.fastq.gz
rm -rf SAMEA3359892_2.fastq.gz	
rm -rf SAMEA3359893_1.fastq.gz
rm -rf SAMEA3359893_2.fastq.gz	
rm -rf SAMEA3359907_1.fastq.gz
rm -rf SAMEA3359907_2.fastq.gz	
rm -rf SAMEA3359913_1.fastq.gz
rm -rf SAMEA3359913_2.fastq.gz	
rm -rf SAMEA3359917_1.fastq.gz
rm -rf SAMEA3359917_2.fastq.gz	
rm -rf SAMEA3359918_1.fastq.gz
rm -rf SAMEA3359918_2.fastq.gz	
rm -rf SAMEA3359919_1.fastq.gz
rm -rf SAMEA3359919_2.fastq.gz	
rm -rf SAMEA3504608_1.fastq.gz
rm -rf SAMEA3504608_2.fastq.gz	
rm -rf SAMEA2340933_1.fastq.gz
rm -rf SAMEA2340933_2.fastq.gz


```



