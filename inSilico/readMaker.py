import random,pickle

# 0. defined variables

# 0.1. user defined variables
fragmentsCount=100
transcriptHits=[0,1,2]
readLength=75
pairDistance=50 is this good for bowtie??? check it
leftRange=[0.1,0.2]
rightRange=[0.8,0.9]

# 0.2. read organism
f=open(similarityJar,'rb')
transcriptome,genome=pickle.load(f)
f.close()

# 1. create reads
reads=[[],[]]
for fragmentIndex in range(fragmentCount):

    # choose transcript membership
    transcriptIndex=random.choice(transcriptHits)

    # choose read1 position and sequence

    # choose read2 position and sequence

    

# 2. write reads
