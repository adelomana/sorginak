import os,sys

class PathClass:

    def __init__(self):
        self.FASTQdir=None
        self.indexDir=None

def genomeAnnotationReader(fileLocations):

    genomeAnnotation={}
    with open(fileLocations.MSMtranscriptomeFile,'r') as f:
        for line in f:
            if line[0] == '>':
                v=line.split()
                geneName=v[0][1:]
                geneInfo=' '.join(v[1:])
                genomeAnnotation[geneName]=geneInfo

    return genomeAnnotation
        
def main():

    fileLocations=PathClass()

    fileLocations.FASTQdir='/Volumes/omics4tb/alomana/projects/mtb/data/01_VS_Splitseq-190834694/'
    #fileLocations.FASTQdir='/Volumes/omics4tb/alomana/projects/mtb/data/02_VS_Splitseq_noblockers-190854678/'
    #fileLocations.FASTQdir='/Volumes/omics4tb/alomana/projects/mtb/data/03_VS_Splitseq_23s-190846701/'
    #fileLocations.FASTQdir='/Volumes/omics4tb/alomana/projects/mtb/data/04_VS_Splitseq_gDNA-190855677/'
    
    fileLocations.MSMgenomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/246196.genome.fasta'
    fileLocations.MSMtranscriptomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/246196.transcriptomes.fasta'
    fileLocations.ECOgenomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/511145.genome.fasta'
    fileLocations.ECOtranscriptomeFile='/Volumes/omics4tb/alomana/projects/mtb/data/references/511145.transcriptomes.fasta'

    fileLocations.resultsDir='/Volumes/omics4tb/alomana/projects/mtb/results/'
    fileLocations.processedFASTQdir=fileLocations.resultsDir+'processedFASTQdir/'
    fileLocations.bamDir=fileLocations.resultsDir+'bam/'
    fileLocations.genomicIndexesDir=fileLocations.resultsDir+'indexes/'

    # f.2. retrieve genome annotation
    genomeAnnotation=genomeAnnotationReader(fileLocations)

    return fileLocations,genomeAnnotation
