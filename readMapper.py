import os

def indexBuilder():

    # build genome index
    executable='bowtie2-build'
    fastaFile='/Users/adriandelomana/Google\ Drive/projects/mtb/data/splitseq/referenceGenome/microbes.online/246196.genome.fasta'
    indexOutputDir='/Users/adriandelomana/Google\ Drive/projects/mtb/data/splitseq/referenceGenome/microbes.online/indexes/246196.genome.index'
    cmdList=[executable,fastaFile,indexOutputDir]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    # build transcriptome index
    executable='bowtie2-build'
    fastaFile='/Users/adriandelomana/Google\ Drive/projects/mtb/data/splitseq/referenceGenome/microbes.online/246196.transcriptomes.fasta'
    indexOutputDir='/Users/adriandelomana/Google\ Drive/projects/mtb/data/splitseq/referenceGenome/microbes.online/indexes/246196.transcriptome.index'
    cmdList=[executable,fastaFile,indexOutputDir]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    return None

def main(dataDir,indexDir):

    cmd='bowtie2-build'

    # f.1. build index
    #indexBuilder()
    
    # f.2. map reads
    executable='bowtie2'
    flag1='-x'
    index='/Users/adriandelomana/scratch/'+'246196.transcriptome.index'
    flag2='-1'
    flag3='-2'
    pair1='/Users/adriandelomana/scratch/'+'VS-Splitseq_S1_L002_R1_001.case.1a.fastq'
    pair2='/Users/adriandelomana/scratch/'+'VS-Splitseq_S1_L002_R2_001.case.1a.fastq'
    flag4='-S'
    outputBAM='test.sam'

    cmdList=['time',executable,flag1,index,flag2,pair1,flag3,pair2,flag4,outputBAM,'--dovetail','--ff']
    cmd=' '.join(cmdList)
    print('')
    print(cmd)
    print('')
    os.system(cmd)

    return None
