import sys
import optionReader,dataReader
import barcodeWorkerSingle,readMapperSingle

def main():

    # f.1. read user defined variables
    fileLocations,genomeAnnotation=optionReader.main()

    # f.2. read sequence data
    sampleNames=dataReader.main(fileLocations)

    # f.3. generate barcode-specific FASTQ files
    #/ consider this step for parallelization
    #for sampleName in sampleNames:
    #    print(sampleName)
    #    barcodeWorkerSingle.main(fileLocations,sampleName)


    # f.4. run quantification pipelines for each barcode-specific FASTQ file

    # f.5. map reads
    #readMapper.main(fileLocations,sampleNames) 
    readMapperSingle.main(fileLocations,genomeAnnotation,sampleNames) 

    # f.6. generate histograms of read maping for highesta buundace transcripts.

    return None

###
### MAIN
###
main()
