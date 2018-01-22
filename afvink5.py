class DNA:
    def __init__(self,seq):
        self.seq = seq
        self.lenght = len(self.seq)
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
    def getlenght(self):
        self.length = len(self.seq)
        return(self.lenght)
    def getgcpercentage(self):
        self.gcper = 0
        CGG = 0
        CGC = 0
        """
        try:
            print(self.seq)
            for letter in self.seq:
                if letter == "G":
                    CGG += 1
                if letter == "C":
                    CGC += 1
            self.gcper = ((CGG+CGC)/(len(self.seq)))*100
        except ZeroDivisionError:
            self.gcper = 100
        """
        print(self.seq)
        for item in self.seq:
            self.gctotal = self.seq.count("G")+self.seq.count("C")
            self.gcpercentage = (self.gctotal/(self.getlenght())*100)
        #print(self.gcpercentage)
        return(self.gcper)

def main():
    IH, IS = file()
    dnaobjecten = objectmaking(IS)
    print(gcpercentage(dnaobjecten))
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
        seq = DNA(IS)
        objects.append(seq)
    return(objects)

def gcpercentage(dnaobjecten):
    gclijst = []
    for object in dnaobjecten:
        gclijst.append(object.getgcpercentage())
    return(gclijst)


#sequentie = "AAAATTTTCCCCCGGGGACTCGA"
#s = DNA(sequentie)
#s1 = s.gettranscript()
#l = s.getlenght()
main()
