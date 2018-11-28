
def main(fileLocations,sampleName):


    # f.1. find the barcode
    print('detecting barcodes for {}...'.format(sampleName))
    
    #! must go
    barcode='ATTCACTTCAGTCATGAT'
    reverseBarcode,complementBarcode,reverseComplementBarcode=perspectiveViewer(barcode)
    read1file=fileLocations.FASTQdir+sampleName+'_R1_001.fastq'
    read2file=fileLocations.FASTQdir+sampleName+'_R2_001.fastq'
    fragmentThresholdLength=25



# f.1. find the barcode


# f.2. if found export the r1 and r2 into separate files
# f.3    do mapping. if not mapping, then consider reverse of R2.
