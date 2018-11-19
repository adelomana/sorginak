import sys
import optionReader,barcodeWorker,readMapper

def main():

    # f.1. generate barcode-specific FASTQ files
    #/ consider this step for parallelization
    #for pairedLabel in pairedLabels:
    #    barcodeWorker.main(dataDir,pairedLabel)

    # f.2. run quantification pipelines for each barcode-specific FASTQ file

    # map reads
    readMapper.main(dataDir,indexDir)
    

    # generate histograms of read maping for highesta buundace transcripts.
    

    return None

# 0. define variables


# 0.1. hard-coded variable

# 0.2. read user defined variables
dataDir,indexDir,pairedLabels=optionReader.main()

# 1. run algoritm
main()
