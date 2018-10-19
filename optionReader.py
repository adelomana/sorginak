import os,sys

def main():

    dataDir='/Volumes/omics4tb/alomana/projects/mtb/data/01_VS_Splitseq-190834694/'

    detectedFiles=os.listdir(dataDir)
    pairedLabels=[element.split('_R1')[0] for element in detectedFiles if '_R1' in element]

    pairedLabels=list(set(pairedLabels))
    pairedLabels.sort()

    return dataDir,pairedLabels
