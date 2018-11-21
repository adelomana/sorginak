import random,pickle

# 0. defined variables

# 0.1. user defined variables
transcriptCount=5
transcriptLength=1000

# 0.2. intrinsic variables
bases=['A','T','G','C']

# 2. make the organism

# 2.1. transcriptome
transcriptome=[]
for transcriptIndex in range(transcriptCount):
    transcript=''
    for baseIndex in range(transcriptLength):
        base=random.choice(bases)
        transcript=transcript+base
    transcriptome.append(transcript)

# 2.2. genome
genome="".join(transcriptome)

# 3. write the organism

# 3.0. pickle genome and transcriptome 
jar='ISI.pickle'
f=open(jar,'wb')
pickle.dump(transcriptome,genome,f)
f.close()

# 3.1. write the genome
with open('000000.genome.fasta','w') as f:
    f.write('> genome sequence of in silico organism 000000\n')
    for i in range(len(genome)):
        f.write(genome[i])

        count=i+1
        if count%60 == 0:
            f.write('\n')

# 3.2. write the transcriptome
with open('000000.transcriptome.fasta','w') as f:
    f.write('> transcriptome sequence for in silico organism 000000\n')
    for i in range(len(transcriptome)):
        f.write('>ISI000000 T{}\n'.format(i)) 

        for j in range(len(transcriptome[i])):
            f.write(transcriptome[i][j])
            count=j+1
            if count%60 == 0:
                f.write('\n')
        f.write('\n')
