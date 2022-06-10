class Student:

    def __init__(self,name,CH,QP):
        self.name=name
        self.CH=float(CH)
        self.QP=float(QP)
        
    def getName(self):
        return self.name
    
    def getCH(self):
        return self.CH

    def getQP(self):
        return self.QP
    
    def GPA(self):
        return self.QP/self.CH

def stuInfo(fx):
    name,CH,QP=fx.split(',')
    return Student(name,CH,QP)

def main():
    infile=open("test1.txt", 'r')
    fx=infile.readline()
    best=stuInfo(fx)

    for line in infile:
       s=stuInfo(line)
       if s.GPA()>best.GPA():
        best=s

    infile.close()

    print(best.name)
    print(best.GPA())
    print(s.name)
    print(s.GPA())

main()