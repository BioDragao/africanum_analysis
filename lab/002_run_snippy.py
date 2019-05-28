import os
import shutil

genome_pairs = [["ERR234097_R1.fastq.gz", "ERR234097_R2.fastq.gz"],
                ["ERR234106_R1.fastq.gz", "ERR234106_R2.fastq.gz"],
                ["ERR234113_R1.fastq.gz", "ERR234113_R2.fastq.gz"],
                ["ERR234142_R1.fastq.gz", "ERR234142_R2.fastq.gz"],
                ["ERR234143_R1.fastq.gz", "ERR234143_R2.fastq.gz"],
                ["ERR234144_R1.fastq.gz", "ERR234144_R2.fastq.gz"],
                ["ERR234145_R1.fastq.gz", "ERR234145_R2.fastq.gz"],
                ["ERR234146_R1.fastq.gz", "ERR234146_R2.fastq.gz"],
                ["ERR234147_R1.fastq.gz", "ERR234147_R2.fastq.gz"],
                ["ERR234148_R1.fastq.gz", "ERR234148_R2.fastq.gz"],
                ["ERR234149_R1.fastq.gz", "ERR234149_R2.fastq.gz"],
                ["ERR234150_R1.fastq.gz", "ERR234150_R2.fastq.gz"],
                ["ERR234151_R1.fastq.gz", "ERR234151_R2.fastq.gz"],
                ["ERR234160_R1.fastq.gz", "ERR234160_R2.fastq.gz"],
                ["ERR234176_R1.fastq.gz", "ERR234176_R2.fastq.gz"],
                ["ERR234184_R1.fastq.gz", "ERR234184_R2.fastq.gz"],
                ["ERR234186_R1.fastq.gz", "ERR234186_R2.fastq.gz"],
                ["ERR234199_R1.fastq.gz", "ERR234199_R2.fastq.gz"],
                ["ERR234202_R1.fastq.gz", "ERR234202_R2.fastq.gz"],
                ["ERR234204_R1.fastq.gz", "ERR234204_R2.fastq.gz"],
                ["ERR234254_R1.fastq.gz", "ERR234254_R2.fastq.gz"],
                ["ERR234255_R1.fastq.gz", "ERR234255_R2.fastq.gz"],
                ["ERR234257_R1.fastq.gz", "ERR234257_R2.fastq.gz"],
                ["ERR234261_R1.fastq.gz", "ERR234261_R2.fastq.gz"],
                ["ERR502471_1.fastq.gz", "ERR502471_2.fastq.gz"],
                ["ERR502475_1.fastq.gz", "ERR502475_2.fastq.gz"],
                ["ERR502476_1.fastq.gz", "ERR502476_2.fastq.gz"],
                ["ERR502477_1.fastq.gz", "ERR502477_2.fastq.gz"],
                ["ERR502480_1.fastq.gz", "ERR502480_2.fastq.gz"],
                ["ERR502481_1.fastq.gz", "ERR502481_2.fastq.gz"],
                ["ERR502482_1.fastq.gz", "ERR502482_2.fastq.gz"],
                ["ERR502483_1.fastq.gz", "ERR502483_2.fastq.gz"],
                ["ERR502484_1.fastq.gz", "ERR502484_2.fastq.gz"],
                ["ERR502485_1.fastq.gz", "ERR502485_2.fastq.gz"],
                ["ERR502486_1.fastq.gz", "ERR502486_2.fastq.gz"],
                ["ERR502487_1.fastq.gz", "ERR502487_2.fastq.gz"],
                ["ERR502489_1.fastq.gz", "ERR502489_2.fastq.gz"],
                ["ERR502490_1.fastq.gz", "ERR502490_2.fastq.gz"],
                ["ERR502492_1.fastq.gz", "ERR502492_2.fastq.gz"],
                ["ERR502493_1.fastq.gz", "ERR502493_2.fastq.gz"],
                ["ERR502494_1.fastq.gz", "ERR502494_2.fastq.gz"],
                ["ERR502496_1.fastq.gz", "ERR502496_2.fastq.gz"],
                ["ERR502497_1.fastq.gz", "ERR502497_2.fastq.gz"],
                ["ERR502498_1.fastq.gz", "ERR502498_2.fastq.gz"],
                ["ERR502500_1.fastq.gz", "ERR502500_2.fastq.gz"],
                ["ERR502501_1.fastq.gz", "ERR502501_2.fastq.gz"],
                ["ERR502502_1.fastq.gz", "ERR502502_2.fastq.gz"],
                ["ERR502503_1.fastq.gz", "ERR502503_2.fastq.gz"],
                ["ERR502505_1.fastq.gz", "ERR502505_2.fastq.gz"],
                ["ERR502506_1.fastq.gz", "ERR502506_2.fastq.gz"],
                ["ERR502507_1.fastq.gz", "ERR502507_2.fastq.gz"],
                ["ERR502508_1.fastq.gz", "ERR502508_2.fastq.gz"],
                ["ERR502509_1.fastq.gz", "ERR502509_2.fastq.gz"],
                ["ERR502510_1.fastq.gz", "ERR502510_2.fastq.gz"],
                ["ERR502511_1.fastq.gz", "ERR502511_2.fastq.gz"],
                ["ERR502512_1.fastq.gz", "ERR502512_2.fastq.gz"],
                ["ERR502513_1.fastq.gz", "ERR502513_2.fastq.gz"],
                ["ERR502514_1.fastq.gz", "ERR502514_2.fastq.gz"],
                ["ERR502515_1.fastq.gz", "ERR502515_2.fastq.gz"],
                ["ERR502516_1.fastq.gz", "ERR502516_2.fastq.gz"],
                ["ERR502517_1.fastq.gz", "ERR502517_2.fastq.gz"],
                ["ERR502521_1.fastq.gz", "ERR502521_2.fastq.gz"],
                ["ERR502522_1.fastq.gz", "ERR502522_2.fastq.gz"],
                ["ERR502523_1.fastq.gz", "ERR502523_2.fastq.gz"],
                ["ERR502524_1.fastq.gz", "ERR502524_2.fastq.gz"],
                ["ERR502525_1.fastq.gz", "ERR502525_2.fastq.gz"],
                ["ERR502527_1.fastq.gz", "ERR502527_2.fastq.gz"],
                ["ERR502528_1.fastq.gz", "ERR502528_2.fastq.gz"],
                ["ERR502530_1.fastq.gz", "ERR502530_2.fastq.gz"],
                ["ERR502531_1.fastq.gz", "ERR502531_2.fastq.gz"],
                ["ERR502532_1.fastq.gz", "ERR502532_2.fastq.gz"],
                ["ERR502533_1.fastq.gz", "ERR502533_2.fastq.gz"],
                ["ERR502534_1.fastq.gz", "ERR502534_2.fastq.gz"],
                ["ERR502536_1.fastq.gz", "ERR502536_2.fastq.gz"],
                ["ERR502537_1.fastq.gz", "ERR502537_2.fastq.gz"],
                ["ERR517471_1.fastq.gz", "ERR517471_2.fastq.gz"],
                ["ERR551617_1.fastq.gz", "ERR551617_2.fastq.gz"],
                ["ERR552021_1.fastq.gz", "ERR552021_2.fastq.gz"],
                ["ERR552172_1.fastq.gz", "ERR552172_2.fastq.gz"],
                ["ERR552187_1.fastq.gz", "ERR552187_2.fastq.gz"],
                ["ERR552328_1.fastq.gz", "ERR552328_2.fastq.gz"],
                ["ERR552506_1.fastq.gz", "ERR552506_2.fastq.gz"],
                ["ERR552588_1.fastq.gz", "ERR552588_2.fastq.gz"],
                ["ERR552963_1.fastq.gz", "ERR552963_2.fastq.gz"],
                ["ERR702400_1.fastq.gz", "ERR702400_2.fastq.gz"],
                ["ERR702401_1.fastq.gz", "ERR702401_2.fastq.gz"],
                ["ERR702407_1.fastq.gz", "ERR702407_2.fastq.gz"],
                ["ERR702408_1.fastq.gz", "ERR702408_2.fastq.gz"],
                ["ERR702409_1.fastq.gz", "ERR702409_2.fastq.gz"],
                ["ERR702410_1.fastq.gz", "ERR702410_2.fastq.gz"],
                ["ERR702411_1.fastq.gz", "ERR702411_2.fastq.gz"],
                ["ERR702412_1.fastq.gz", "ERR702412_2.fastq.gz"],
                ["ERR702413_1.fastq.gz", "ERR702413_2.fastq.gz"],
                ["ERR702414_1.fastq.gz", "ERR702414_2.fastq.gz"],
                ["ERR702415_1.fastq.gz", "ERR702415_2.fastq.gz"],
                ["ERR702416_1.fastq.gz", "ERR702416_2.fastq.gz"],
                ["ERR702417_1.fastq.gz", "ERR702417_2.fastq.gz"],
                ["ERR702418_1.fastq.gz", "ERR702418_2.fastq.gz"],
                ["ERR702419_1.fastq.gz", "ERR702419_2.fastq.gz"],
                ["ERR702420_1.fastq.gz", "ERR702420_2.fastq.gz"],
                ["ERR702421_1.fastq.gz", "ERR702421_2.fastq.gz"],
                ["ERR702422_1.fastq.gz", "ERR702422_2.fastq.gz"],
                ["ERR702423_1.fastq.gz", "ERR702423_2.fastq.gz"],
                ["ERR702424_1.fastq.gz", "ERR702424_2.fastq.gz"],
                ["ERR702425_1.fastq.gz", "ERR702425_2.fastq.gz"],
                ["ERR702426_1.fastq.gz", "ERR702426_2.fastq.gz"],
                ["ERR702427_1.fastq.gz", "ERR702427_2.fastq.gz"],
                ["ERR702428_1.fastq.gz", "ERR702428_2.fastq.gz"],
                ["ERR702429_1.fastq.gz", "ERR702429_2.fastq.gz"],
                ["ERR702430_1.fastq.gz", "ERR702430_2.fastq.gz"],
                ["ERR702431_1.fastq.gz", "ERR702431_2.fastq.gz"],
                ["ERR702432_1.fastq.gz", "ERR702432_2.fastq.gz"],
                ["ERR702434_1.fastq.gz", "ERR702434_2.fastq.gz"],
                ["ERR702435_1.fastq.gz", "ERR702435_2.fastq.gz"],
                ["ERR702436_1.fastq.gz", "ERR702436_2.fastq.gz"],
                ["ERR751290_1.fastq.gz", "ERR751290_2.fastq.gz"],
                ["ERR751291_1.fastq.gz", "ERR751291_2.fastq.gz"],
                ["ERR751292_1.fastq.gz", "ERR751292_2.fastq.gz"],
                ["ERR751293_1.fastq.gz", "ERR751293_2.fastq.gz"],
                ["ERR751294_1.fastq.gz", "ERR751294_2.fastq.gz"],
                ["ERR751295_1.fastq.gz", "ERR751295_2.fastq.gz"],
                ["ERR751296_1.fastq.gz", "ERR751296_2.fastq.gz"],
                ["ERR751297_1.fastq.gz", "ERR751297_2.fastq.gz"],
                ["ERR751298_1.fastq.gz", "ERR751298_2.fastq.gz"],
                ["ERR751299_1.fastq.gz", "ERR751299_2.fastq.gz"],
                ["ERR751300_1.fastq.gz", "ERR751300_2.fastq.gz"],
                ["ERR751301_1.fastq.gz", "ERR751301_2.fastq.gz"],
                ["ERR751302_1.fastq.gz", "ERR751302_2.fastq.gz"],
                ["ERR751303_1.fastq.gz", "ERR751303_2.fastq.gz"],
                ["ERR751304_1.fastq.gz", "ERR751304_2.fastq.gz"],
                ["ERR751305_1.fastq.gz", "ERR751305_2.fastq.gz"],
                ["ERR751306_1.fastq.gz", "ERR751306_2.fastq.gz"],
                ["ERR751307_1.fastq.gz", "ERR751307_2.fastq.gz"],
                ["ERR751308_1.fastq.gz", "ERR751308_2.fastq.gz"],
                ["ERR751309_1.fastq.gz", "ERR751309_2.fastq.gz"],
                ["ERR751310_1.fastq.gz", "ERR751310_2.fastq.gz"],
                ["ERR751311_1.fastq.gz", "ERR751311_2.fastq.gz"],
                ["ERR751312_1.fastq.gz", "ERR751312_2.fastq.gz"],
                ["ERR751313_1.fastq.gz", "ERR751313_2.fastq.gz"],
                ["ERR751314_1.fastq.gz", "ERR751314_2.fastq.gz"],
                ["ERR751315_1.fastq.gz", "ERR751315_2.fastq.gz"],
                ["ERR751317_1.fastq.gz", "ERR751317_2.fastq.gz"],
                ["ERR751318_1.fastq.gz", "ERR751318_2.fastq.gz"],
                ["ERR751319_1.fastq.gz", "ERR751319_2.fastq.gz"],
                ["ERR751320_1.fastq.gz", "ERR751320_2.fastq.gz"],
                ["ERR751321_1.fastq.gz", "ERR751321_2.fastq.gz"],
                ["ERR751322_1.fastq.gz", "ERR751322_2.fastq.gz"],
                ["ERR751323_1.fastq.gz", "ERR751323_2.fastq.gz"],
                ["ERR751324_1.fastq.gz", "ERR751324_2.fastq.gz"],
                ["ERR751325_1.fastq.gz", "ERR751325_2.fastq.gz"],
                ["ERR751326_1.fastq.gz", "ERR751326_2.fastq.gz"],
                ["ERR751327_1.fastq.gz", "ERR751327_2.fastq.gz"],
                ["ERR751328_1.fastq.gz", "ERR751328_2.fastq.gz"],
                ["ERR751329_1.fastq.gz", "ERR751329_2.fastq.gz"],
                ["ERR751330_1.fastq.gz", "ERR751330_2.fastq.gz"],
                ["ERR751331_1.fastq.gz", "ERR751331_2.fastq.gz"],
                ["ERR751332_1.fastq.gz", "ERR751332_2.fastq.gz"],
                ["ERR751333_1.fastq.gz", "ERR751333_2.fastq.gz"],
                ["ERR751334_1.fastq.gz", "ERR751334_2.fastq.gz"],
                ["ERR751335_1.fastq.gz", "ERR751335_2.fastq.gz"],
                ["ERR751336_1.fastq.gz", "ERR751336_2.fastq.gz"],
                ["ERR751337_1.fastq.gz", "ERR751337_2.fastq.gz"],
                ["ERR751338_1.fastq.gz", "ERR751338_2.fastq.gz"],
                ["ERR751339_1.fastq.gz", "ERR751339_2.fastq.gz"],
                ["ERR751341_1.fastq.gz", "ERR751341_2.fastq.gz"],
                ["ERR751342_1.fastq.gz", "ERR751342_2.fastq.gz"],
                ["ERR751343_1.fastq.gz", "ERR751343_2.fastq.gz"],
                ["ERR751344_1.fastq.gz", "ERR751344_2.fastq.gz"],
                ["ERR751345_1.fastq.gz", "ERR751345_2.fastq.gz"],
                ["ERR751346_1.fastq.gz", "ERR751346_2.fastq.gz"],
                ["ERR751347_1.fastq.gz", "ERR751347_2.fastq.gz"],
                ["ERR751348_1.fastq.gz", "ERR751348_2.fastq.gz"],
                ["ERR751349_1.fastq.gz", "ERR751349_2.fastq.gz"],
                ["ERR756344_R1.fastq.gz", "ERR756344_R2.fastq.gz"],
                ["ERR756345_R1.fastq.gz", "ERR756345_R2.fastq.gz"],
                ["ERR756346_R1.fastq.gz", "ERR756346_R2.fastq.gz"],
                ["ERR756347_R1.fastq.gz", "ERR756347_R2.fastq.gz"],
                ["ERR756348_R1.fastq.gz", "ERR756348_R2.fastq.gz"],
                ["ERR845916_1.fastq.gz", "ERR845916_2.fastq.gz"],
                ["ERR868539_1.fastq.gz", "ERR868539_2.fastq.gz"],
                ["ERR909753_1.fastq.gz", "ERR909753_2.fastq.gz"],
                ["ERR909754_1.fastq.gz", "ERR909754_2.fastq.gz"],
                ["ERR1082113_1.fastq.gz", "ERR1082113_2.fastq.gz"],
                ["ERR1082114_1.fastq.gz", "ERR1082114_2.fastq.gz"],
                ["ERR1082115_1.fastq.gz", "ERR1082115_2.fastq.gz"],
                ["ERR1082116_1.fastq.gz", "ERR1082116_2.fastq.gz"],
                ["ERR1082117_1.fastq.gz", "ERR1082117_2.fastq.gz"],
                ["ERR1082118_1.fastq.gz", "ERR1082118_2.fastq.gz"],
                ["ERR1082119_1.fastq.gz", "ERR1082119_2.fastq.gz"],
                ["ERR1082120_1.fastq.gz", "ERR1082120_2.fastq.gz"],
                ["ERR1082121_1.fastq.gz", "ERR1082121_2.fastq.gz"],
                ["ERR1082122_1.fastq.gz", "ERR1082122_2.fastq.gz"],
                ["ERR1082123_1.fastq.gz", "ERR1082123_2.fastq.gz"],
                ["ERR1082124_1.fastq.gz", "ERR1082124_2.fastq.gz"],
                ["ERR1082125_1.fastq.gz", "ERR1082125_2.fastq.gz"],
                ["ERR1082126_1.fastq.gz", "ERR1082126_2.fastq.gz"],
                ["ERR1082127_1.fastq.gz", "ERR1082127_2.fastq.gz"],
                ["ERR1082128_1.fastq.gz", "ERR1082128_2.fastq.gz"],
                ["ERR1082129_1.fastq.gz", "ERR1082129_2.fastq.gz"],
                ["ERR1082130_1.fastq.gz", "ERR1082130_2.fastq.gz"],
                ["ERR1082131_1.fastq.gz", "ERR1082131_2.fastq.gz"],
                ["ERR1082132_1.fastq.gz", "ERR1082132_2.fastq.gz"],
                ["ERR1082133_1.fastq.gz", "ERR1082133_2.fastq.gz"],
                ["ERR1082134_1.fastq.gz", "ERR1082134_2.fastq.gz"],
                ["ERR1082135_1.fastq.gz", "ERR1082135_2.fastq.gz"],
                ["ERR1082136_1.fastq.gz", "ERR1082136_2.fastq.gz"],
                ["ERR1082137_1.fastq.gz", "ERR1082137_2.fastq.gz"],
                ["ERR1082138_1.fastq.gz", "ERR1082138_2.fastq.gz"],
                ["ERR1082139_1.fastq.gz", "ERR1082139_2.fastq.gz"],
                ["ERR1082140_1.fastq.gz", "ERR1082140_2.fastq.gz"],
                ["ERR1082141_1.fastq.gz", "ERR1082141_2.fastq.gz"],
                ["ERR1082142_1.fastq.gz", "ERR1082142_2.fastq.gz"],
                ["ERR1082143_1.fastq.gz", "ERR1082143_2.fastq.gz"],
                ["ERR1203053_1.fastq.gz", "ERR1203053_2.fastq.gz"],
                ["ERR1203054_1.fastq.gz", "ERR1203054_2.fastq.gz"],
                ["ERR1203055_1.fastq.gz", "ERR1203055_2.fastq.gz"],
                ["ERR1203056_1.fastq.gz", "ERR1203056_2.fastq.gz"],
                ["ERR1203057_1.fastq.gz", "ERR1203057_2.fastq.gz"],
                ["ERR1203058_1.fastq.gz", "ERR1203058_2.fastq.gz"],
                ["ERR1203059_1.fastq.gz", "ERR1203059_2.fastq.gz"],
                ["ERR1203061_1.fastq.gz", "ERR1203061_2.fastq.gz"],
                ["ERR1203062_1.fastq.gz", "ERR1203062_2.fastq.gz"],
                ["ERR1203065_1.fastq.gz", "ERR1203065_2.fastq.gz"],
                ["ERR1203066_1.fastq.gz", "ERR1203066_2.fastq.gz"],
                ["ERR1203068_1.fastq.gz", "ERR1203068_2.fastq.gz"],
                ["ERR1203069_1.fastq.gz", "ERR1203069_2.fastq.gz"],
                ["ERR1203070_1.fastq.gz", "ERR1203070_2.fastq.gz"],
                ["ERR1203072_1.fastq.gz", "ERR1203072_2.fastq.gz"],
                ["ERR1203074_1.fastq.gz", "ERR1203074_2.fastq.gz"],
                ["ERR1203076_1.fastq.gz", "ERR1203076_2.fastq.gz"],
                ["ERR1203077_1.fastq.gz", "ERR1203077_2.fastq.gz"],
                ["ERR1215460_1.fastq.gz", "ERR1215460_2.fastq.gz"],
                ["ERR1215461_1.fastq.gz", "ERR1215461_2.fastq.gz"],
                ["ERR1215462_1.fastq.gz", "ERR1215462_2.fastq.gz"],
                ["ERR1215463_1.fastq.gz", "ERR1215463_2.fastq.gz"],
                ["ERR1215464_1.fastq.gz", "ERR1215464_2.fastq.gz"],
                ["ERR1215465_1.fastq.gz", "ERR1215465_2.fastq.gz"],
                ["ERR1215466_1.fastq.gz", "ERR1215466_2.fastq.gz"],
                ["ERR1215467_1.fastq.gz", "ERR1215467_2.fastq.gz"],
                ["ERR1215468_1.fastq.gz", "ERR1215468_2.fastq.gz"],
                ["ERR1215469_1.fastq.gz", "ERR1215469_2.fastq.gz"],
                ["ERR1215470_1.fastq.gz", "ERR1215470_2.fastq.gz"],
                ["ERR1215471_1.fastq.gz", "ERR1215471_2.fastq.gz"],
                ["ERR1215472_1.fastq.gz", "ERR1215472_2.fastq.gz"],
                ["ERR1215473_1.fastq.gz", "ERR1215473_2.fastq.gz"],
                ["ERR1215474_1.fastq.gz", "ERR1215474_2.fastq.gz"],
                ["ERR1215475_1.fastq.gz", "ERR1215475_2.fastq.gz"],
                ["ERR1215476_1.fastq.gz", "ERR1215476_2.fastq.gz"],
                ["ERR1215477_1.fastq.gz", "ERR1215477_2.fastq.gz"],
                ["ERR1215478_1.fastq.gz", "ERR1215478_2.fastq.gz"],
                ["ERR1215479_1.fastq.gz", "ERR1215479_2.fastq.gz"],
                ["ERR1215480_1.fastq.gz", "ERR1215480_2.fastq.gz"],
                ["ERR1215481_1.fastq.gz", "ERR1215481_2.fastq.gz"],
                ["ERR1215482_1.fastq.gz", "ERR1215482_2.fastq.gz"],
                ["ERR1215483_1.fastq.gz", "ERR1215483_2.fastq.gz"],
                ["ERR1334049_1.fastq.gz", "ERR1334049_2.fastq.gz"],
                ["ERR1334050_1.fastq.gz", "ERR1334050_2.fastq.gz"],
                ["ERR1334051_1.fastq.gz", "ERR1334051_2.fastq.gz"],
                ["ERR1334052_1.fastq.gz", "ERR1334052_2.fastq.gz"],
                ["ERR1334053_1.fastq.gz", "ERR1334053_2.fastq.gz"],
                ["ERR2181458_1.fastq.gz", "ERR2181458_2.fastq.gz"],
                ["L1_R1.fastq.gz", "L1_R2.fastq.gz"],
                ["L2_R1.fastq.gz", "L2_R2.fastq.gz"],
                ["L3_R1.fastq.gz", "L3_R2.fastq.gz"],
                ["L4_R1.fastq.gz", "L4_R2.fastq.gz"],
                ["L5_R1.fastq.gz", "L5_R2.fastq.gz"],
                ["L6_R1.fastq.gz", "L6_R2.fastq.gz"],
                ["L7_R1.fastq.gz", "L7_R2.fastq.gz"],
                ["MAFBRA00707_R1.fastq.gz", "MAFBRA00707_R2.fastq.gz"],
                ["Mcanettii_R1.fastq.gz", "Mcanettii_R2.fastq.gz"],
                ["UT307_R1.fastq.gz", "UT307_R2.fastq.gz"]]


def run_snippy(a_pair):

    # snippy --cpus 4 --outdir Mcanettii --ref ./NC000962_3.gbk --R1 ./Mcanettii_R1.fastq.gz --R2 ./Mcanettii_R2.fastq.gz

    genome_name = a_pair[0].split("_")[0]

    genome_1 = a_pair[0]

    genome_2 = a_pair[1]

    location_on_host = "/biodragon/vagrantBox/mozambique_genomes/maf_endgame/lab"

    location_on_guest = "/vagrant/mozambique_genomes/maf_endgame/lab"

    snippy_initial_command = "  vagrant ssh -c \"cd  /vagrant/mozambique_genomes/maf_endgame/lab   && " + \
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

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")


for a_pair in genome_pairs:
    run_snippy(a_pair)
