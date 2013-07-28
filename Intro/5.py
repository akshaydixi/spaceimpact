#Functions


#SI = P*R*T/100

def simpleinterest( principal, rate, time):  # A simple simple interest function
    si = ( principal * rate * time ) / 100
    return si    

def square(x):  # Return the square of the number
    return x*x
    

p = input("Principal : ")
r = input("Rate : ")
t = input("Time : ")

si = simpleinterest(p,r,t)  # Calling a function with the arguments 
                            # and storing the returned value in a variable
si2 = square(si)


print "Simple Interest = ",si
print "Simple Interest squared = ",si2 
