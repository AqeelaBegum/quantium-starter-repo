import csv

#method to filter through each file
def fileSquisher(path, squishPath):
    with open(path) as file:
        fileReader = csv.reader(file, delimiter=',') #seperates contents at ,
        
        #squish file (one with only pink morsel)
        with open(squishPath, "a") as squishFile:
            next(fileReader) #skips first line because it contains the header
            
            #extracting data from a file
            for row in fileReader:
                if row[0] == "pink morsel":
                    price = row[1]
                    quantity= row[2]

                    #sales = price * quantity, needed to also slice price to get rid of $
                    sales = str(float(price[1:]) * int(quantity))

                    date = row[3].strip()
                    region = row[4].strip()

                    #putting the data together in a row
                    squishFile.write(sales+"," + date + "," + region+"\n")
        squishFile.close()
    file.close()

#method calling the squisher method on each file
def task2():
    path = "data\daily_sales_data_pink_morsels.csv"

    #writes the header
    with open(path, "w") as file: #I did w to start the file from scratch again to prevent repeats
        file.write("Sales, Date, Region"+"\n")    
    file.close()

    #calls squish method on each file
    for i in range(3):
        fileSquisher("data\daily_sales_data_"+str(i)+".csv",path)

task2()
