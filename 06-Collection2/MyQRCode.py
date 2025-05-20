import qrcode

print("Please Enter Your UserName = ",end="")
userName = input()
print("Please Enter Your PhoneNumber = ",end="")
phoneNumber = input()

result = userName + " : " + phoneNumber

userName_qrCode = qrcode.make(result)
userName_qrCode.save("My_QRCode.jpg")

print("QR Code Generated and save as My_QRCode.jpg")
