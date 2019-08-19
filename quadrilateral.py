class Quadrilateral:
    def _init_(self,a,b,c,d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side=d

    def perimeter(self):
        p=self.side1+self.side2+self.side3+self.side4
        print("perimeter=",p)
