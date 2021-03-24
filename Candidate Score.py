class Candidate:
    def __init__(self,id):
        self.id = id
        
    def round1(self,a,b,c):
        self.r1a = a
        self.r1b = b
        self.r1c = c
        self.total = a + b + c
        r1_avg = (self.total)/3
        if a < 75 or b < 75 or c < 75:
            return False
        if r1_avg < 85:
            return False

        return True
        
    def round2(self,a,b,c):
        self.r2a = a
        self.r2b = b
        self.r2c = c
        self.total += a + b + c
        r12_avg = (self.total)/6
        
        if a < 75 or b < 75 or c < 75:
            return False
        if r12_avg < 85:
            return False

        return True
        

    def round3(self,a,b,c):
        self.r3a = a
        self.r3b = b
        self.r3c = c
        self.total += a + b + c


def candidate_score(candidates):
    round1_shortlist = []
    round2_shortlist = []
    round3_shortlist = []
    final_shortlist = []

    
    for c in candidates:
        x,y,z = [int(x) for x in input("Enter Round 1 Scores for candidate " + str(c.id)).split()]
        if c.round1(x,y,z):
            round1_shortlist.append(c)

    round1_shortlist.sort(key = lambda x: x.total, reverse = True)
    
    for i in range(100):
        c = round1_shortlist[i]
        x,y,z = [int(x) for x in input("Enter Round 2 Scores for candidate " + str(c.id)).split()]
        if c.round2(x,y,z):
            round2_shortlist.append(c)

    round2_shortlist.sort(key = lambda x: x.total, reverse = True)
    
    for i in range(10):
        c = round2_shortlist[i]
        x,y,z = [int(x) for x in input("Enter Round 3 Score for candidate " + str(c.id)).split()]
        round3_shortlist.append(c)
    round3_shortlist.sort(key = lambda x: x.total, reverse = True)  

    for i in range(5):
        final_shortlist.append(round3_shortlist[i])


    return final_shortlist #return final three condidates

