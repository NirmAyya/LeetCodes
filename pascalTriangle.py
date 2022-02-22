numRows=int(input("How many rows do you want to compute to: "))

 #if they ask for 1 or 2 rows we hardcode that
pascal =[[1]]
if numRows==1:
    print(pascal)
pascal.append([1,1])
if numRows==2:
    print(pascal)


#if they ask for more rows we make each new row we need and add to final list. 
for row in range(2,numRows):
    nthRow=[1]
    nRow=pascal[row-1]
    for x in range(1,row):
        if x!= row:
            nthRow.append(nRow[x]+nRow[x-1])
    nthRow.append(1)    
    pascal.append(nthRow)    
print(pascal)
    