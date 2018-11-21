import os,sys

def indexBuilder(fileLocations):

    executable='bowtie2-build'

    # build genome index for M. smegmatis
    fastaFile=fileLocations.MSMgenomeFile
    indexOutputDir=fileLocations.genomicIndexesDir+'MSM.genome.index'
    cmdList=[executable,fastaFile,indexOutputDir]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    # build transcriptome index for M. smegmatis
    fastaFile=fileLocations.MSMtranscriptomeFile
    indexOutputDir=fileLocations.genomicIndexesDir+'MSM.transcriptome.index'
    cmdList=[executable,fastaFile,indexOutputDir]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    # build genome index for E. coli
    fastaFile=fileLocations.ECOgenomeFile
    indexOutputDir=fileLocations.genomicIndexesDir+'ECO.genome.index'
    cmdList=[executable,fastaFile,indexOutputDir]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    # build transcriptome index for E. coli
    fastaFile=fileLocations.ECOtranscriptomeFile
    indexOutputDir=fileLocations.genomicIndexesDir+'ECO.transcriptome.index'
    cmdList=[executable,fastaFile,indexOutputDir]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    return None

def main(fileLocations,sampleNames):

    # f.1. build index
    indexBuilder(fileLocations)

    #! to go
    cases=['case.1a','case.1b','case.2a','case.2b']
    
    # f.2. map reads
    executable='bowtie2'
    flag0='-x'
    index=fileLocations.genomicIndexesDir+'ECO.genome.index'
    flag1='-1'
    flag2='-2'
    flag3='-S'

    for sampleName in sampleNames:
        for case in cases:

            pair1=fileLocations.FASTQdir+sampleName+'_R1_001.'+case+'.fastq'
            pair2=fileLocations.FASTQdir+sampleName+'_R2_001.'+case+'.fastq'
            outputBAM=fileLocations.bamDir+sampleName+'.'+case+'.sam'

            cmdList=['time',executable,flag0,index,flag1,pair1,flag2,pair2,flag3,outputBAM]
            cmd=' '.join(cmdList)

            print('')
            print(cmd)
            print('')
            os.system(cmd)

        # mapping the original using local
        pair1=fileLocations.FASTQdir+sampleName+'_R1_001.fastq'
        pair2=fileLocations.FASTQdir+sampleName+'_R2_001.fastq'
        outputBAM=fileLocations.bamDir+sampleName+'.original.sam'

        cmdList=['time',executable,flag0,index,flag1,pair1,flag2,pair2,flag3,outputBAM,'-p 4 --local']
        cmd=' '.join(cmdList)

        print('')
        print(cmd)
        print('')
        os.system(cmd)

        sys.exit()

    return None
