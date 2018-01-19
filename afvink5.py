class DNA:
    def __init__(self,seq):
        self.seq = seq
        self.lenght = len(self.seq)
        self.gctotal = 0
        self.gcpercentage = 0
    def getdna(self):
        return self.seq
    def gettranscript(self):
        seq = ""
        for letter in self.seq:
            if letter == "A":
                letter = letter.replace("A","U")
                seq += letter
            elif letter == "T":
                letter = letter.replace("T","A")
                seq += letter
            elif letter == "G":
                letter = letter.replace("G","C")
                seq += letter
            elif letter == "C":
                 letter = letter.replace("C","G")
                 seq += letter
        self.seq = seq
        return(self.seq)
    def getlenght(self):
        return(self.lenght)
    def getgcpercentage(self):
        for line in self.seq:
            print(line)
            self.gctotal = line.count("G")+line.count("C")
            self.gcpercentage = (self.gctotal/self.lenght)*100
            #print(self.gcpercentage)
        return(self.gcpercentage)

def main():
    IS, IH = file()
    dnaobjecten = objectmaking(IS)
    gcpercentage(dnaobjecten)
def file():
    file = open("/home/stef/Documents/Python/course2/afvink5/Felis_catus.Felis_catus_8.0.cdna.all.fa")
    IH = []
    IS = []
    dna = ""
    for line in file:
        if ">" in line:
            line = line.replace("\n", "")
            IH.append(line)
            dna += (" ")
        else:
            line = line.replace("\n", "")
            dna += (line)
    IS = dna.split(" ")
    return (IH, IS)

def objectmaking(IS):
    objects = []
    for sequentie in IS:
        seq = DNA(IS)
        objects.append(seq)
    return(objects)

def gcpercentage(dnaobjecten):
    gcpercentage = []
    for item in dnaobjecten:
        gcpercentage.append(item.getgcpercentage())
    #print(gcpercentage)


#sequentie = "AAAATTTTCCCCCGGGGACTCGA"
#s = DNA(sequentie)
#s1 = s.gettranscript()
#l = s.getlenght()
main()
