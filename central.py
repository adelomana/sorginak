import sys
import multiprocessing,multiprocessing.pool
import optionReader,dataReader

#import barcodeWorkerSingle,readMapperSingle
import barcodeWorkerSingleWithBarcode,readMapperSingleWithBarcode

def main():

    # f.1. read user defined variables
    fileLocations,genomeAnnotation=optionReader.main()

    # f.2. read sequence data
    sampleNames=dataReader.main(fileLocations)

    # f.3. generate barcode-specific FASTQ files

    # working in a parallel environment
    numberOfThreads=len(sampleNames)
    print('Initialized parallel analysis using {} threads...'.format(numberOfThreads))
    hydra=multiprocessing.pool.Pool(numberOfThreads)
    instances=[[fileLocations,sampleName] for sampleName in sampleNames]
    tempo=hydra.map(barcodeWorkerSingleWithBarcode.main,instances)
    print('... completed.')

    # working in serial
    #for sampleName in sampleNames:
    #    print(sampleName)
    #    barcodeWorkerSingleWithBarcode.main(fileLocations,sampleName)
   

    # f.4. run quantification pipelines for each barcode-specific FASTQ file

    # f.5. map reads
    #readMapper.main(fileLocations,sampleNames) 
    #readMapperSingle.main(fileLocations,genomeAnnotation,sampleNames)
    readMapperSingleWithBarcode.main(fileLocations,genomeAnnotation,sampleNames)

    # f.6. generate histograms of read maping for highesta buundace transcripts.

    return None

###
### MAIN
###
main()
