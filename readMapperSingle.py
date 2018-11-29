import os,sys

def indexBuilder(fileLocations):

    executable='kallisto index -i'

    # build transcriptome index for M. smegmatis
    fastaFile=fileLocations.MSMtranscriptomeFile
    indexOutputDir=fileLocations.genomicIndexesDir+'kallisto/MSM.transcriptome.index'
    cmdList=[executable,indexOutputDir,fastaFile]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)
    
    # build transcriptome index for E. coli
    fastaFile=fileLocations.ECOtranscriptomeFile
    indexOutputDir=fileLocations.genomicIndexesDir+'kallisto/ECO.transcriptome.index'
    cmdList=[executable,indexOutputDir,fastaFile]
    cmd=' '.join(cmdList)
    print(cmd)
    os.system(cmd)

    return None

def main(fileLocations,sampleNames):

    # f.1. build index
    #indexBuilder(fileLocations)
    #sys.exit()

    #! to go
    cases=['case.1a','case.1b','case.2a','case.2b']
    
    # f.2. map reads
    executable='kallisto quant'
    flagIndex='-i {}'.format(fileLocations.genomicIndexesDir+'kallisto/MSM.transcriptome.index')
    flagOptions='-b 100 --single --plaintext -l 200 -s 20'

    for sampleName in sampleNames:
        for case in cases:
            for pair in ['R1','R2']:
                readFile=fileLocations.processedFASTQdir+sampleName+'_'+pair+'.{}.fastq'.format(case)
                flagOutput='-o {}'.format(fileLocations.resultsDir+'kallistoResults/MSM/{}.{}.{}'.format(sampleName,case,pair))

                cmdList=['time',executable,flagIndex,flagOutput,flagOptions,readFile]
                cmd=' '.join(cmdList)

                print('')
                print(cmd)
                print('')
                os.system(cmd)

            # need to check if --fr-stranded or reverse has an effect. Also the distance.
            # spit out the 20 most abundant transcripts with annotation


        

    return None
