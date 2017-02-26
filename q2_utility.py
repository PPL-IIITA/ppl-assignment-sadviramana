import csv
from random import randint
#create a csv file from data provided
def create_csv(data,filename):
    csv_file = open(filename,'wb')
    pointer = csv.writer(csv_file,delimiter=',')
    for i in data :
        pointer.writerow(i)



def utility():
    #Boy types
    btype = ["Miser","Generous","Geek"]
    #Girl types
    gtype = ["Choosy","Normal","Desparate"]
    #gifttypes
    giftype = ["Essential" , "Luxury" , "Utility"]
    BOY = [('BID'+str(i+1),randint(1,10),randint(1,100),randint(1,50),randint(1,9),btype[randint(0,2)]) for i in range(0,15)]
    GIRL = [('GID'+str(i+1),randint(1,10),randint(1,100),randint(1,50),gtype[randint(0,2)]) for i in range(0,5)]
    GIFT = [('GIFID'+str(i+1),randint(1,20),randint(1,10),giftype[randint(0,2)]) for i in range(1,10)]
    #create two files boys.csv and girls.csv and gifts.csv
    create_csv(BOY,'boys.csv')
    create_csv(GIRL,'girls.csv')
    create_csv(GIFT,'gifts.csv')

#utility()
