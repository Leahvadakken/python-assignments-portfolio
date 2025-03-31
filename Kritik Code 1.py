x=float(input("Enter a number: ")) #this allows for any test number to be inputted, and x is any real number
def tanfunction(x): #defining my function
    if x>=0 and x<=1:
        def error (a,b): #This ensures that x is within the interval of [0,1]
            y=(a ** ((2 * b) + 1)) / ((2 * b) + 1)
            return y

        n=0
        while error(x,n)> 0.0001: #while the error is greater than 0.0001
            n+=1

        running=0 #initialize running sum
        for i in range (n):
            current = (((-1) ** i) * (x ** (2 * i + 1))) / (2 * i + 1)
            running+=current

        return (running,n,error(x,n)) #this ensures the final run is a tuple

    else:
        print ("Error!") #this ensures any value that is not within the range runs "Error!"


result = (tanfunction(x))
print(result)

input("press enter to continue")




