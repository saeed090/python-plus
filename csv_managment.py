import csv

with open("data.csv" , "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Poduct_Name" , "Price" , "Size"])
    writer.writerow(["monitor" , 50 , 670])
    writer.writerow(["keyboard" , 150 , 140])