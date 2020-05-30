#Working with conditional statements

def main():
    x, y = 10, 10
    
    if(x < y):
        st = "x is less than y"  
    elif(x>y):
        st = "x is greater than y"
    else:
        st = "x is equal to y"    
      
    print(st)   

#conditional statements let you use "a if c else b"
    st = "x is less than y" if (x<y) else "x is greater than or same as y"
    print(st)   

#if __name__ == "__main__":
main()    