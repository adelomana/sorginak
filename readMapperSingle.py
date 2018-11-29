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

def main(fileLocations,genomeAnnotation,sampleNames):

    # f.1. build index
    #indexBuilder(fileLocations)
    #sys.exit()

    #! to go
    cases=['case.1a','case.1b','case.2a','case.2b']
    
    # f.2. map reads
    executable='kallisto quant'
    flagIndex='-i {}'.format(fileLocations.genomicIndexesDir+'kallisto/MSM.transcriptome.index')
    flagOutput='-o {}'.format(fileLocations.resultsDir+'kallistoResults/MSM/{}'.format('.'.join(sampleNames)))
    flagOptions='-b 10 --single --plaintext -l 100 -s 100 --pseudobam'

    inputFiles=[]
    for sampleName in sampleNames:
        for case in cases:
            for pair in ['R1','R2']:
                readFile=fileLocations.processedFASTQdir+sampleName+'_'+pair+'.{}.fastq'.format(case)
                fileInfo=os.stat(readFile)
                if fileInfo.st_size > 1:
                    inputFiles.append(readFile)
    inputFilesString=' '.join(inputFiles)
    cmdList=['time',executable,flagIndex,flagOutput,flagOptions,inputFilesString]
    cmd=' '.join(cmdList)

    print('')
    print(cmd)
    print('')
    os.system(cmd)

    # f.3. print out the 20 most expressed genes
    expression={}
    quantificationFile=flagOutput.split()[-1]+'/abundance.tsv'
    with open(quantificationFile,'r') as f:
        next(f)
        for line in f:
            v=line.split('\t')
            transcriptName=v[0]
            estimatedCounts=float(v[-2])
            expression[transcriptName]=estimatedCounts
    # sort
    sortedExpression=sorted(expression, key=expression.get,reverse=True)
    print('counts\tgeneID\tgeneDescription')
    for i in range(20):
        print('{}\t{}\t{}'.format(expression[sortedExpression[i]],sortedExpression[i],genomeAnnotation[sortedExpression[i]]))

    sys.exit()

# need to check if  has an effect. Also the distance.
# 50,10  54,2
# 100,10 53,5
# 150,15 52,2
# 200,20 50,8


    
# spit out the 20 most abundant transcripts with annotation


        

    return None
