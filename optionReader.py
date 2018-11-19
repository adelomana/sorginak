import os,sys

def main():

    dataDir='/Users/adriandelomana/Google Drive/projects/mtb/data/splitseq/01_VS_Splitseq-190834694/'
    indexDir='/Users/adriandelomana/Google Drive/projects/mtb/data/splitseq/referenceGenome/microbes.online/indexes'

    detectedFiles=os.listdir(dataDir)
    pairedLabels=[element.split('_R1')[0] for element in detectedFiles if '_R1' in element]

    pairedLabels=list(set(pairedLabels))
    pairedLabels.sort()

    return dataDir,indexDir,pairedLabels
