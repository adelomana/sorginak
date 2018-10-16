###
### 
###

import sys

def readPairEvaluator(readPair):

    flag=[0,0]

    r1=readPair[0]; r2=readPair[1]

    if barcode in r1:
        flag[0]=1
        
    if reverseComplementBarcode in r2:
        flag[1]=1
    
    return flag

###
### MAIN
###

barcode='ATTCACTTCAGTCATGAT'
reverseComplementBarcode='ATCATGACTGAAGTGAAT'


# select reads with the barcode in R1 or the reverse complement in R2
read1file='/Volumes/omics4tb/alomana/projects/mtb/data/test/VS-Splitseq_S1_L001_R1_001.fastq'
read2file='/Volumes/omics4tb/alomana/projects/mtb/data/test/VS-Splitseq_S1_L001_R2_001.fastq'

#read1file='/Volumes/omics4tb/alomana/projects/mtb/data/test/test.1.fastq'
#read2file='/Volumes/omics4tb/alomana/projects/mtb/data/test/test.2.fastq'

relativeIndex=0

forwardFound=0; reverseFound=0; bothFound=0; acceptableFound=0

totalNumberOfFragments=0

acceptableFragments=[]
fragmentThresholdLength=25

with open(read1file,'r') as r1, open(read2file,'r') as r2:
    for lineR1, lineR2 in zip(r1,r2):

        # counting a new line
        relativeIndex=relativeIndex+1

        # 
        if relativeIndex == 1:
            readNameR1=lineR1.split('\n')[0]
            readNameR2=lineR2.split('\n')[0]

        #
        if relativeIndex == 2:
            readSequenceR1=lineR1.split('\n')[0]
            readSequenceR2=lineR2.split('\n')[0]

        # 
        if relativeIndex == 4:
            qualityR1=lineR1.split('\n')[0]
            qualityR2=lineR2.split('\n')[0]

            print(readNameR1)

            flag=[0,0]
            if barcode in readSequenceR1:
                forwardFound=forwardFound+1
                flag[0]=1
                trimmedR1=readSequenceR1.split(barcode)[-1]
                trimmedR1quality=qualityR1[-len(trimmedR1):]
                trimmedR2=readSequenceR2
                trimmedR2quality=qualityR2
                
                print(readSequenceR1,len(readSequenceR1))
                print(qualityR1,len(qualityR1))
                print(barcode)
                print(trimmedR1,len(trimmedR1))
                print(trimmedR1quality,len(trimmedR1quality))
                
            if reverseComplementBarcode in readSequenceR2:
                reverseFound=reverseFound+1
                flag[1]=1
                trimmedR2=readSequenceR2.split(reverseComplementBarcode)[0]
                trimmedR2quality=qualityR2[:len(trimmedR2)]
                trimmedR1=readSequenceR1
                trimmedR1quality=qualityR1

                print('\t',readSequenceR2,len(readSequenceR2))
                print('\t',qualityR2,len(qualityR2))
                print('\t',reverseComplementBarcode)
                print('\t',trimmedR2,len(trimmedR2))
                print('\t',trimmedR2quality,len(trimmedR2quality))
                
            if flag == [1,1]:
                bothFound=bothFound+1
            if sum(flag) == 1:
                acceptableFound=acceptableFound+1                
                
                # check for minimum length
                if min([len(trimmedR1),len(trimmedR2)]) >= fragmentThresholdLength:
                    a=[readNameR1,trimmedR1,trimmedR1quality]
                    b=[readNameR2,trimmedR2,trimmedR2quality]
                    acceptableFragments.append([a,b])
                else:
                    print('oops')
                    print(readNameR1)
                    print(min([len(trimmedR1),len(trimmedR2)]))
                
            relativeIndex=0
            totalNumberOfFragments=totalNumberOfFragments+1

r1.close()
r2.close()

print('')
for element in acceptableFragments:
    print(element[0][1],len(element[0][1]))
    print(element[1][1],len(element[1][1]))
    print('')
print('')

ratio=100*(forwardFound/totalNumberOfFragments)
print('{}/{} forward reads contain the barcode ({:.3f}%).'.format(forwardFound,totalNumberOfFragments,ratio))
ratio=100*(reverseFound/totalNumberOfFragments)
print('{}/{} reverse reads contain the reverse complement to barcode ({:.3f}%).'.format(reverseFound,totalNumberOfFragments,ratio))
ratio=100*(bothFound/totalNumberOfFragments)
print('{}/{} fragments contain both the barcode and the reverse complement to barcode ({:.3f}%).'.format(bothFound,totalNumberOfFragments,ratio))

ratio=100*(acceptableFound/totalNumberOfFragments)
print('{}/{} fragments survived ({:.3f}%).'.format(acceptableFound,totalNumberOfFragments,ratio))


ratio=100*(len(acceptableFragments)/totalNumberOfFragments)
print('{}/{} fragments passed minimum length of {} bp ({:.3f}%).'.format(len(acceptableFragments),totalNumberOfFragments,fragmentThresholdLength,ratio))


# 2. write trimmed reads
read1fileo=read1file.replace('.fastq','.barcode.fastq')
read2fileo=read2file.replace('.fastq','.barcode.fastq')

with open(read1fileo,'w') as r1, open(read2fileo,'w') as r2:
    for element in acceptableFragments:
        r1.write('{}\n'.format(element[0][0]))
        r1.write('{}\n'.format(element[0][1]))
        r1.write('+\n')
        r1.write('{}\n'.format(element[0][2]))

        r2.write('{}\n'.format(element[1][0]))
        r2.write('{}\n'.format(element[1][1]))
        r2.write('+\n')
        r2.write('{}\n'.format(element[1][2]))


# generate histograms of read maping for highesta buundace transcripts.
