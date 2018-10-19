import sys
import optionReader,barcodeWorker

def main():

    # f.1. generate barcode-specific FASTQ files
    #/ this step needs to be parallel
    for pairedLabel in pairedLabels:
        barcodeWorker.main(dataDir,pairedLabel)

    # run quantification pipelines for each barcode-specific FASTQ file
    

    return None

# 0. define variables


# 0.1. hard-coded variable

# 0.2. read user defined variables
dataDir,pairedLabels=optionReader.main()

# 1. run algoritm
main()
