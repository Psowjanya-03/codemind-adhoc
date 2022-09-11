num_rows = int(input());
for i in range (0,num_rows):  
    for j in range (num_rows,i,-1):  
        print("*", end="")
    print()