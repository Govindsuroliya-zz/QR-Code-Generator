import qrcode
print("Welcame to QR Code Generator")
data = input("Enter your data just likes - link,text,numbers,password. - ")
path = input("Enter your Path where you want save your qrcode. - ")
save = input("Enter your file name - ")

imgw =  qrcode.make(data)

imgw.save(path+"/"+save+".png")