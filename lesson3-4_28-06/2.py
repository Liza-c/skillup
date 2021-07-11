#Реализовать декоратор подключения драйвера к принтеру

def conncetion(ip, port):
    def printer(func):
        def d(doc):
            print(f"Connected to IP: {ip}:{port}")
            func(doc)
            print("Close connection")
        return d
    return printer
        
@conncetion(ip="10.10.10.10", port=5555)
def hp(document):
     print("I am HP printer")
     print(f"Printing: {document}")
     
@conncetion(ip="10.10.10.10", port=5666)
def canon(document):
    print("I am Canon printer")
    print(f"Printing: {document}")
    
    
print(hp("some text"))
print(canon("another text "))

#Вывод:
#Connected to IP: 10.10.10.10:5555
#I am HP printer
#Printing: some text
#Close connection
#Connected to IP: 10.10.10.10:5666
#I am Canon printer
#Printing: another text
#Close connection