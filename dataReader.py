import os

def main(fileLocations):

    detectedFiles=os.listdir(fileLocations.FASTQdir)
    sampleNames=[element.split('_R1')[0] for element in detectedFiles if '_R1' in element]

    sampleNames=list(set(sampleNames))
    sampleNames.sort()
    
    return sampleNames
