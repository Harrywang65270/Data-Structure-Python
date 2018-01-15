
class yrange:
    def __init__(self,n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()



class zrange:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return zrange_iter(self.n)
class zrange_iter:
    def __init__(self,n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
        


y = yrange(5)
for n in y:
    print n
for n in y:
    print n
    
#z = zrange(5)
#print iter(z)
#for n in iter(z):
#    print n
#for n in iter(z):
#    print n

'''
      
y = yrange(5)
print list(y)
print list(y)

z = zrange(5)
print list(z)
print list(z)

'''



class FibIterable:

    def __init__(self,iLast=1,iSecondLast=0,iMax=50):
        self.iLast = iLast
        self.iSecondLast = iSecondLast
        self.iMax = iMax

    def __iter__(self):
        return self
 
    def next(self):
        iNext = self.iLast + self.iSecondLast
        if iNext > self.iMax:
            raise StopIteration()
        self.iSecondLast = self.iLast
        self.iLast = iNext
        return iNext


    
'''
o = FibIterable()
print o

print o.next()
print o.next()
print o.next()
for i in o:
    print i  # This remains a question!!! Need to check the code of FOR and LIST()!!! I think they use .next() 

'''    
    




List_1 = [1,2,3]
x = iter(List_1)
print list(x)
print list(x)

for i in List_1:
    print i

'''
print x
print x.next()
print x.next()
print x.next()


y = List_1.__iter__()
print y
print y.next()
print y.next()
print y.next()

'''

