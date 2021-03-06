####################Extract fasta sequence for each chromosome from the total fasta file###################

def chrFasta(fastaFile,writeDir):
    import os
    from itertools import chain
    # 1:22+"X"+"Y"
    chrom_list=[[str(i) for i in xrange(1,23,1)],'X','Y','M']
    chrom = list(chain(*chrom_list))
    with open(fastaFile,'r') as f:
        for line in f:
            for num in chrom:
                chrom_num=str(num)
                if line.startswith(">chr{chrom_num} {chrom_num}".format(chrom_num=chrom_num)):
                    w=open('{writeDir}/chr{chrom_num}.fa'.format(writeDir=writeDir,chrom_num=chrom_num),'w')
            w.write('{line}'.format(line=line))
            w.flush()
    w.close()


# parametes setting and script running
fastaFile="/mnt/xdlab/ref/GRCh37/GRCh37.p13.genome.fa"
writeDir="/home/luokai/CRC/prepData/chrFiles"
chrFasta(fastaFile,writeDir)
