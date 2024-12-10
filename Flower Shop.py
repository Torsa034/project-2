item_dict={}
f=open("E:\\Flower Shop.txt","r")
while True:
    item=f.readline()
    if item=="\n":
        break
    qntt=f.readline()
    uprc=f.readline()
    item=item[:len(item)-1]
    qntt=int(qntt[:len(qntt)-1])
    uprc=float(uprc[:len(uprc)-1])

    item_dict[item]=[qntt,uprc]
f.close()

"""
item_dict={"napa":[500,1.25],
           "napa extra":[1250,2.50],
           "ace plus":[2500,3.50],
           "monas":[3000,8.50],
           "fenadin":[50,9.25]}
"""


def present_data():
    print(28*"=")
    print("FLOWERY PARADISE".center(25))
    print(30*"=")
    for x in item_dict:
        print(x,(20-len(x))*" ",
              (8-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(30*"-")
        


def dec_quant(item,amount):
    item_dict[item][0]-=amount
    
def inc_quant(item,amount):
    item_dict[item][0]+=amount



def receive_order():
    while True:
        item =  input("Item:(type'x' to stop:")
        if item=='x':
            break
        amnt=int(input("Amount:"))
        if item not in item_dict:
            print("New item found")
            uprice=float(input("Enter the unit price"))
            item_dict[item]=[amnt,uprice]
            continue
        inc_quant(item,amnt)

    
#present_data()
     
def process_demand():
    demand_list=[]
    while True:
        item =  input("Item:(type'x' to stop: ")
        if item=='x':
            break
        if item not in item_dict:
            print("sorry! Item is not avialable")
            continue
        amnt=int(input("Amount:"))
        if amnt>item_dict[item][0]:
            print(f"{Totalitem_dict[item][0]} pcs available!")
            continue
        dec_quant(item,amnt)
        demand_list+=[item,amnt,
                      item_dict[item][1],amnt*item_dict[item][1]],
    print(40*"=")
    print("**Payment Reciept**".center(40))
    print(40*"-")
    print("item name",3*" ","Quant.",
              "U.price","S.Total")
    print(40*"-")
    tprice=0
    for x in demand_list:
        tprice+=x[3]
        print(x[0].title(),(14-len(x[0]))*" ",
              (5-len(str(x[1])))*" ",x[1],
              (6-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
              (8-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print(40*"_")
    tprice="%.2f"%tprice
    print("Total Price:",(26-len(str(tprice)))*" ",tprice)
    print(40*" ")

while True:
      present_data()
      print("Choose an option")
      print("Type '1': To process demand")
      print("Type '2': To receive order")
      print("type '3': To exit the program")
      choice=input("Choice: ")
      if choice=='1':
           process_demand()
      elif choice=='2':
           receive_order()
      elif choice=='3':
            break
      else:
            continue
f=open("E:\\Flower Shop.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.write("\n")
f.close()
    #present_data()


