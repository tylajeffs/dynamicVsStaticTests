class c1(object):

    def m1(self):
        return self.m2()

    def m2(self):
        return 13



class c2(c1):
    def m1(self):
        return 22
    
    def m2(self):
        return 23
    
    def m3(self):
        return super().m1()



class c3(c2):
    def m1(self):
        return 32
    
    def m2(self):
        return 33



def main():

    o3 = c3() 

    print(o3.m3())

main()
