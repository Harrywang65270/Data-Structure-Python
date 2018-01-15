'''

def listsum(numList):
    
    if len(numList) == 1:
        
        return numList[0]
    
    else:
        
        return numList[0] + listsum(numList[1:len(numList)])



numList = [1,2,3,4]

print numList[1:len(numList)]


print listsum(numList)

def toStr(n,base):
    convString = "0123456789ABCDEF"
    if n < base:
        return convString[n]
    else:
        return toStr(n//base,base) + convString[n%base]

print toStr(1453,16)



import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle,lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

'''

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin =turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
