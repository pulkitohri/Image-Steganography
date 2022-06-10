#!/usr/bin/env python3
from PIL import Image
def dec():
  imname=input("Enter The Image name to decode : \n") #asking the user to enter image name
  im2 = im2=Image.open(imname) #opening the image 
  x,y = im2.size #storing the length of axis in respective variable
  bf=False
  jj=[]
  for i in range(0,x): #going through the x axis to get the changed pixels
    t1 = im2.getpixel((i,0))
    for j in t1:
      jj.append(j)
      if jj[-1]==36 : bf=True #stop iterating if the character is $
      if bf : return jj #returning the list with modified pixels

f = dec()
print("Set Of Modified Pixels ",f) 
g = [bin(n).replace('0b','') for n in f] #converting the modified pixels into binary
msg=[]
for i in g: 
  if i =='100000' or i=='100100' or i=='100011': msg.append(i)
  else :
    i = list(i)
    l = i[-1]
    msg.append(l) #extracting the message from last bit of pixel binary and append in msg variable 
#msgD = [int(n,2) for n in msg]
msgD = [str(int(n,2)) for n in msg] 
if msgD[-1]=='36' : msgD.pop(-1)  #removing the $ from message 
print("Message in Binary Bits is \n",msgD)
tex=(''.join(msgD).split('35')) #removing the spaces from message
print(tex)
decclist = [chr(int(f,2)) if f!='32' else chr(int(f)) for f in tex ] #converting the message to its original form
print("\n message hidden is :")
for msg in decclist:
    print(msg,end='') #printing the message
