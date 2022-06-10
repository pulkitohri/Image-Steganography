from PIL import Image
m = input("Enter a text :\n ")
if m=="": 
  print("Message cant be blank enter again ")
  m = input("Enter a text :\n ")

#m = ' '.join(m)+"$" #split the text add blank spaces between the characters
m= '#'.join(m)+'$' #adding a special character to denote the message end while decoding
print(m)
m = list(m) #list of message with spaces
j=[bin(ord(i)).replace('0b','') for i in m ] #list of all characters in binary
print('binary is ',j)
g=len(j) 
ss=[len(j[v]) for v in range(0,g,2)] #ss is list containing length of binary of each character
sm = sum(ss)+(len(ss)) #number of tuples required
print(g,sm)
name = input("Enter Image name with extention ") #getting the image name to open
try:im1 = Image.open(name) #creating a try block to open image
except : 
  print("\n image not found enter again ") #telling user if image is not found
  name = input("Enter correct Image name with extention ") #asking to enter the correct image name
  im1=Image.open(name) #opening the image

rgbd = list(im1.getdata()) #storing image rgb data in variable
if im1.mode=='RGBA': #calculating number of pixels required if image is rgba and storing in lis variable
  if (sm%4==0):lis = int(sm/4)
  else : lis = int(sm/4+1)
if im1.mode=='RGB': #calculating number of pixels required if image is rgb and storing in lis variable
  if (sm%3==0):lis = int(sm/3)
  else : lis = int(sm/3+1)
rgbdset = rgbd[:lis] #storing only the pixels to be edited
print(rgbdset)
binlis=[]
for tup in rgbdset: #conveting the image pixels which are to be modified in binary
   for datap in tup:
     binlis.append(bin(datap).replace('0b',''))
msbls = []
print(len(binlis))
for pj in range(0,len(j)): #creating a message binary so it can be embedded into image pixels
  if j[pj] not in ('100000','100100','100011'):
    for chr in j[pj]:
      msbls.append(chr)
  else : msbls.append(j[pj])
print("message bin ",msbls) #printing the message binary
print("\n " , len(msbls))
newl = []
for i in range(len(msbls)): #changing the pixel values of the image with that of the message values
  ml = binlis[i]
  ml = list(ml)
  ml.pop(-1)
  if msbls[i]=='100000' or msbls[i]=='100100' or msbls[i]=='100011' : ml=msbls[i]
  else:  ml = ''.join(ml)+msbls[i]
  newl.append(ml)
print("replaced binary mess ",newl) #printing the modified pixel binary
ll = len(newl) 
newl.extend(binlis[ll:]) #extending the modified pixels with the others
ffnew = [int(i,2) for i in newl]
if im1.mode=='RGBA':finalList=[tuple(ffnew[f:f+4]) for f in range(0,len(ffnew),4)]
if im1.mode=='RGB':finalList=[tuple(ffnew[f:f+3]) for f in range(0,len(ffnew),3)]
rgbd[:lis]=finalList #merging pixels with other
im2 = Image.new(im1.mode,im1.size) #creating a new image
im2.putdata(rgbd)
savedImage = input("enter name for new image save file ") #getting new image name from user
try:
  im2.save(savedImage)
except :
  savedImage=savedImage+'.png'
  im2.save(savedImage)
d4=list(im2.getdata())
#print(rgbd[:lis])
print("DONE", f"\n image with name {savedImage} is saved") 
