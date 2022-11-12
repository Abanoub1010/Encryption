# coding: iso-8859-1 -*-

'''This is a simple Encryption method to secure the given code 
I have also applied a simple decryption method to decrypt that code to reuse it '''

#***********************************************************************************************#
#**************************                 Given Code                **************************#
#***********************************************************************************************#
code ='''.code
demomain:
  REPEAT 20
switch rv(nrandom, 9) ; generate a number between 0 and 8
mov ecx, 7
case 0
print "case 0"
case ecx ; in contrast to most other programming languages,
print "case 7" ; the Masm32 switch allows "variable cases"
case 1 .. 3
.if eax==1
print "case 1"
.elseif eax==2
print "case 2"
.else
print "cases 1 to 3: other"
.endif
case 4, 6, 8
print "cases 4, 6 or 8"
default
mov ebx, 19     ; print 20 stars
.Repeat
print "*"
dec ebx
.Until Sign? ; loop until the sign flag is set
endsw
print chr$(13, 10)
  ENDM
  exit
end demomain'''

#***********************************************************************************************#
#**************************                 Encryption                **************************#
#***********************************************************************************************#
enc1=code.replace("case","&")
enc2=enc1.replace("print","^->%")
enc3=enc2.replace("switch","0xFF")
enc4=enc3.replace("generate","<-#U")
enc5=enc4.replace("number","N09")
enc6=enc5.replace("between","B@T")

enc_list = list(enc6)

for n in range (0,(len(enc_list)+200),3):
	enc_list.insert(n,"0x05/n7")

eenc = ''.join([str(elem) for elem in enc_list])

print("*************************************************************************************************")
print("*******************************       Code after encryption       *******************************")
print("*************************************************************************************************")
print(eenc) #code after incryption


#***********************************************************************************************#
#**************************                 Decryption                **************************#
#***********************************************************************************************#

for i in range (0,482):
	if enc_list[i] == "0x05/n7":
		del enc_list[i]
		
eenc = ''.join([str(elem) for elem in enc_list])

enc7=eenc.replace("&","case")
enc8=enc7.replace("^->%","print")
enc9=enc8.replace("0xFF","switch")
enc10=enc9.replace("<-#U","generate")
enc11=enc10.replace("N09","number")
enc12=enc11.replace("B@T","between")

print("*************************************************************************************************")
print("*******************************       Code after decryption       *******************************")
print("*************************************************************************************************")
print(enc12) #code after decryption














