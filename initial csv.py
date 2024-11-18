import csv
def read():
    with open('xyz.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        data=list(csvFile)
    return(data)
def encrp(data,private_index):
    for i in range(length(data)):
        for j in (private_index):
            data_to_encrp[i][j]=data[i][j]
    return(data_to_encrp)
def superimpose(data,encrp_data,private_index):
    for i in range(length(data)):
        for j in (private_index):
            final_data[i][j]=encrp_data[i][j]
    return(final_data)
def write():
    with open('xyz.csv', 'a') as f:
        n=input("do u want to enter more data? y/n")
        writer=csv.writer(f)
        while(n!="n"):
            row=eval(input("enter row"))
write()
data=read()
private_index=eval(input("enter list of indexes to be encrypted"))
data_to_encrp=encrp(data,private_index)