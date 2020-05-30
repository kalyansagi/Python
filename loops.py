#working with loops


def main():

    #define a while loop
    #x = 0
    #while (x<5):
    #    print(x)
    #    x=x+1
    
    #define a for loop
    #for x in range(5,10):
    #    print(x)
    
    #use a for loop over collection
    #days = ["mon", "tue", "wed"]
    #for d in days:
    #    print(d)

    #use the break and continue statements
    #for x in range(5,10):
        #if(x==7): break
    #    if(x%2==0): continue
    #    print(x)

    #using enumerate() function to get index
    days = ["mon", "tue", "wed"]
    for i,d in enumerate(days):
        print(i, d)

main()

