import os,sys

class PathClass:

    def __init__(self):
        self.FASTQdir=None
        self.indexDir=None

def main():

    fileLocations=PathClass()

    fileLocations.FASTQdir='/Volumes/omics4tb/alomana/projects/mtb/data/01_VS_Splitseq-190834694/'
    fileLocations.resultsDir='/Volumes/omics4tb/alomana/projects/mtb/results/'
    fileLocations.genomicIndexesDir='/Volumes/omics4tb/alomana/projects/mtb/data/indexes/'
    fileLocations.bamDir='/Volumes/omics4tb/alomana/projects/mtb/data/bam/'

    fileLocations.MSMgenomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/246196.genome.fasta'
    fileLocations.MSMtranscriptomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/246196.transcriptomes.fasta'
    fileLocations.ECOgenomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/511145.genome.fasta'
    fileLocations.ECOtranscriptomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/511145.transcriptomes.fasta'

    return fileLocations
