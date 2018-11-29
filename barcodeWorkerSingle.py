import sys
import Bio,Bio.Seq

def main(fileLocations,sampleName):


    #/ need to write clean reads into another folder

    print('detecting barcodes for {}...'.format(sampleName))
    
    #! must go
    barcode='ATTCACTTCAGTCATGAT'
    reverseBarcode,complementBarcode,reverseComplementBarcode=perspectiveViewer(barcode)
    read1file=fileLocations.FASTQdir+sampleName+'_R1_001.fastq'
    read2file=fileLocations.FASTQdir+sampleName+'_R2_001.fastq'
    fragmentThresholdLength=25

    # f.1. inspect reads
    totalNumberOfFragments=0
    acceptableFragments={}
    acceptableFragments['case.1a']=[]
    acceptableFragments['case.1b']=[]
    acceptableFragments['case.2a']=[]
    acceptableFragments['case.2b']=[]
    doubleCounts=[]
    
    relativeIndex=0
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

                pairedRead=[[readNameR1,readSequenceR1,qualityR1],[readNameR2,readSequenceR2,qualityR2]]
                acceptableFragments,doubleCounts=pairSelector(acceptableFragments,pairedRead,barcode,reverseBarcode,complementBarcode,reverseComplementBarcode,doubleCounts,fragmentThresholdLength)

                relativeIndex=0
                totalNumberOfFragments=totalNumberOfFragments+1
                
    r1.close()
    r2.close()

    # compute unique doublets
    uniqueDoubleCounts=list(set(doubleCounts))

    # print information
    print('\t Detected number of fragments: {}.'.format(totalNumberOfFragments))
    
    ratio=100*(len(uniqueDoubleCounts)/totalNumberOfFragments)
    print('\t Detected number of double barcodes: {}; {:.3f}%.'.format(len(uniqueDoubleCounts),ratio))

    allAccepted=0
    for case in acceptableFragments:
        ratio=100*(len(acceptableFragments[case])/totalNumberOfFragments)
        print('\t\t Detected fragments for {}: {}; {:.3f}%.'.format(case,len(acceptableFragments[case]),ratio))
        allAccepted=allAccepted+len(acceptableFragments[case])

    ratio=100*(allAccepted/totalNumberOfFragments)
    print('\t Total valid fragments: {}; {:.3f}%.'.format(allAccepted,ratio))

    # f.2. write trimmed reads
    for case in acceptableFragments:
        read1fileo=fileLocations.processedFASTQdir+sampleName+'_R1'+'.{}.fastq'.format(case)
        read2fileo=fileLocations.processedFASTQdir+sampleName+'_R2'+'.{}.fastq'.format(case)

        with open(read1fileo,'w') as r1, open(read2fileo,'w') as r2:
            for element in acceptableFragments[case]:

                if len(element[0]) > 0:
                    r1.write('{}\n'.format(element[0][0]))
                    r1.write('{}\n'.format(element[0][1]))
                    r1.write('+\n')
                    r1.write('{}\n'.format(element[0][2]))

                if len(element[1]) > 0:
                    r2.write('{}\n'.format(element[1][0]))
                    r2.write('{}\n'.format(element[1][1]))
                    r2.write('+\n')
                    r2.write('{}\n'.format(element[1][2]))

    return None

def pairSelector(acceptableFragments,pairedRead,barcode,reverseBarcode,complementBarcode,reverseComplementBarcode,doubleCounts,fragmentThresholdLength):

    '''
    This function defines valid read pairs, specifying which validity case.
    '''

    readNameR1=pairedRead[0][0]
    readSequenceR1=pairedRead[0][1]
    qualityR1=pairedRead[0][2]

    readNameR2=pairedRead[1][0]
    readSequenceR2=pairedRead[1][1]
    qualityR2=pairedRead[1][2]


    # f.1. inwards

    # case.1a: inwards, forward
    if barcode in readSequenceR1:
        x=[readSequenceR2.find(code) for code in [barcode,reverseBarcode,complementBarcode,reverseComplementBarcode]]
        if max(x) == -1:
            # trimming
            trimmedR1=readSequenceR1.split(barcode)[-1]
            trimmedR1quality=qualityR1[-len(trimmedR1):]
            if len(trimmedR1) >= fragmentThresholdLength:
                #acceptableFragments['case.1a'].append([[readNameR1,trimmedR1,trimmedR1quality],pairedRead[1]])
                acceptableFragments['case.1a'].append([[],pairedRead[1]])
        else:
            doubleCounts.append(readNameR1)

    # case.1b: inwards, reverse
    if barcode in readSequenceR2:
        x=[readSequenceR1.find(code) for code in [barcode,reverseBarcode,complementBarcode,reverseComplementBarcode]]
        if max(x) == -1:
            # trimming
            trimmedR2=readSequenceR2.split(barcode)[-1]
            trimmedR2quality=qualityR2[-len(trimmedR2):]
            if len(trimmedR2) >= fragmentThresholdLength:
                #acceptableFragments['case.1b'].append([pairedRead[0],[readNameR2,trimmedR2,trimmedR2quality]])
                acceptableFragments['case.1b'].append([pairedRead[0],[]])
        else:
            doubleCounts.append(readNameR1)

    # f.2. outwards

    # case.2a: outwards, reverse
    if reverseComplementBarcode in readSequenceR1:
        x=[readSequenceR2.find(code) for code in [barcode,reverseBarcode,complementBarcode,reverseComplementBarcode]]
        if max(x) == -1:
            # trimming
            trimmedR1=readSequenceR1.split(reverseComplementBarcode)[0]
            trimmedR1quality=qualityR1[:len(trimmedR1)]
            if len(trimmedR1) >= fragmentThresholdLength:
                #acceptableFragments['case.2a'].append([[readNameR1,trimmedR1,trimmedR1quality],pairedRead[1]])
                acceptableFragments['case.2a'].append([[],pairedRead[1]])
        else:
            doubleCounts.append(readNameR1)

    # case.2b: outwards, forward
    if reverseComplementBarcode in readSequenceR2:
        x=[readSequenceR1.find(code) for code in [barcode,reverseBarcode,complementBarcode,reverseComplementBarcode]]
        if max(x) == -1:
            # trimming
            trimmedR2=readSequenceR2.split(reverseComplementBarcode)[0]
            trimmedR2quality=qualityR2[:len(trimmedR2)]
            if len(trimmedR2) >= fragmentThresholdLength:
                #acceptableFragments['case.2b'].append([pairedRead[0],[readNameR2,trimmedR2,trimmedR2quality]])
                acceptableFragments['case.2b'].append([pairedRead[0],[]])
        else:
            doubleCounts.append(readNameR1)

    return acceptableFragments,doubleCounts

def perspectiveViewer(sequence):

    '''
    Given a sequence, this function returns the reverse sequence, the complement sequence and reverse complement sequence.
    '''
    
    s=Bio.Seq.Seq(sequence)

    reverseSequence=sequence[::-1]
    complementSequence=str(s.complement())
    reverseComplementSequence=str(s.reverse_complement())

    return reverseSequence,complementSequence,reverseComplementSequence
