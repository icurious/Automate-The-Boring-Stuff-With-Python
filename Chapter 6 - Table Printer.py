tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

#function that adjusts strings
def adjust_list(row,l):
    new_row = []
    for i,x in enumerate(row):
        if len(x)!=l:
            x = x.rjust(l)
            new_row.append(x)
        else:
            new_row.append(x)
    return new_row

#list with lengths of max string in every row
max_len = []
for row in tableData:
    lst= []
    for x in row:
        lst.append(len(x))
    max_len.append(max(lst))

# new table with adjusted strings
new_table = []
for i,row in enumerate(tableData):
    new_table.append(adjust_list(row,max_len[i]))


# printing table in the desired format
for i in range(len(new_table[0])):
    str1 = ''
    for row in new_table:
        str1 = str1 +" "+row[i]
    print(str1)







