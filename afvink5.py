class DNA:
    def __init__(self,seq):
        self.seq = seq
        self.length = len(self.seq)
        self.gctotal = ""
        self.gcper = 0
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
    def getlength(self):
        self.length = len(self.seq)
        return(self.length)
    def getgcpercentage(self):
        self.gcper = 0
        self.gctotal = self.seq.count("G")+self.seq.count("C")
        self.gcper = (self.gctotal/(self.getlength())*100)
        return(self.gcper)

def main():
    IH, IS = file()
    dnaobjecten = objectmaking(IS)
    gcpercentage(dnaobjecten,IH)
def file():
    file = open("test")
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
    del(IS[0])
    return (IH, IS)

def objectmaking(IS):
    objects = []
    for sequentie in IS:
        seq = DNA(sequentie)
        objects.append(seq)
    return(objects)

def gcpercentage(dnaobjecten,IH):
    gclijst = []
    for item in dnaobjecten:
        gclijst.append(item.getgcpercentage())

    max1 = 0
    max1 = gclijst.index(max(gclijst))
    print(max(gclijst))
    print(dnaobjecten[max1].gettranscript())
    print(dnaobjecten[max1].getlength())
    return(gclijst)

main()
