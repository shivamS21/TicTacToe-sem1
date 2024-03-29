import random		#using random to take input from the system
a=[" "," "," "]
b=[" "," "," "]
c=[" "," "," "]
e="_ . _ . _"
x=[]          		#empty list to fill with index of matrix
f=""          		#strings to print list in string format
g=""
h=""
#1.defining function for filling matrix
def check1(p,name,sign):
  if p not in x:
    x.append(p)
    if p[0]=="a":
      a[int(p[1])-1]=sign
    elif p[0]=="b":
      b[int(p[1])-1]=sign
    elif p[0]=="c":
      c[int(p[1])-1]=sign
    f=a[0]+" | "+a[1]+" | "+a[2]    		#obtaining string from the elements of the list
    g=b[0]+" | "+b[1]+" | "+b[2]
    h=c[0]+" | "+c[1]+" | "+c[2]
    print(f+"\n"+e+"\n"+g+"\n"+e+"\n"+h)
  else:               		    		#input again in case p already exists in x.
    print("WARNING:",p,"is already filled,so enter the index again")
    p=input("-"+name+"("+sign+")"+":>")
    check1(p,name,sign)            		#calling the function again

#2.defining function for giving instruction
def instruct():
  print("""
~INSTRUCTION::GIVE INPUT AS PER GIVEN INDEX OF UNIQUE ROWs and COLUMNs:-
    a1 | a2 | a3\n    ___.____.___\n    b1 | b2 | b3\n    ___.____.___\n    c1 | c2 | c3
  """)
y=["a1","a2","a3","b1","b2","b3","c1","c2","c3"]  		#list for the index of the matrix
player=int(input("~Enter the no of players(1 or 2):-"))		#input of no of players

#p1.WHEN NO OF PLAYERS ARE 2
if player==2:
  name1=input("~player1 enter your name:").upper()
  name2=input("~player2 enter your name:").upper()
  s=0       					#running loop to get correct sign i.e. 0 or #.
  while s<1:
    sign1=input("~"+name1+" choose the sign between 0 and #: ")
    if sign1=="0" or sign1=="#":		#only when correct sign is entered,sign2 is assigned to other player
      s=2
      if sign1=="0":
        sign2="#"
      else:
        sign2="0"
      print("~Hey "+name2+",you are assigned with :"+sign2)
    else:
      print("~Error"+"\t"+"Instruction:-Enter the correct sign")
      s=0
  instruct()           				#calling function for giving instruction
  for i in range(1,6):
    print("                 --:ROUND:",i,":--")
    s=0
    while s<1:
      p=input(name1+"("+sign1+")"+":>") 	#position in matrix of player one
      s=2       				#running loop to get right index i.e. which exists in list y.
      if p not in y:
        print("~Error"+"\n"+"Instruction:-Enter the correct index") 
        s=0
      else:
        check1(p,name1,sign1)
    if 5>=i>2:   	      			#comparing 8 cases of winning the game
      if (a[0]==a[1]==a[2]==sign1 or b[0]==b[1]==b[2]==sign1 or c[0]==c[1]==c[2]==sign1 or a[0]==b[0]==c[0]==sign1 or a[1]==b[1]==c[1]==sign1 or a[2]==b[2]==c[2]==sign1 or a[0]==b[1]==c[2]==sign1 or a[2]==b[1]==c[0]==sign1):
        print("                    "+name1+" WINS")
        break
    if i!=5:
      s=0     					#running loop to get correct sign i.e. 0 or #.
      while s<1:
        q=input("-"+name2+"("+sign2+")"+":>") 	#position in matrix of player one
        s=2
        if q not in y:
          print("~Error"+"\n"+"Instruction:-Enter the correct index")
          s=0
        else:
          check1(q,name2,sign2)
    else:             	     			#declaring draw
      print("   MATCH IS DRAWN!PLAY AGAIN")
    if 5>=i>2:               			#comparing 8 cases of winning the game
      if (a[0]==a[1]==a[2]==sign2 or b[0]==b[1]==b[2]==sign2 or c[0]==c[1]==c[2]==sign2 or a[0]==b[0]==c[0]==sign2 or a[1]==b[1]==c[1]==sign2 or a[2]==b[2]==c[2]==sign2 or a[0]==b[1]==c[2]==sign2 or a[2]==b[1]==c[0]==sign2):
        print("                     "+name2+" WINS")
        break

#p2. WHEN NO OF PLAYER IS 1
elif player==1:
  name=input("~Hey! Enter your name to compete with the system:").upper()
  s=0
  while s<1:
    sign3=input("~So,"+name+" which sign u wanna choose between 0 and # :")
    if sign3=="0" or sign3=="#":
      if sign3=="0":
        sign4="#"
      else:
        sign4="0"
      print("...System is assigned with "+sign4)
      s=2
    else:
      print("...Error "+"\n"+"Instruction:-Enter the correct sign")
      s=0
  instruct()                 			#calling function for giving instruction
  for i in range(1,6):
    print("                 --:ROUND:",i,":--")
    s=0
    while s<1:
      q=input("-"+name+"("+sign3+")"+":>") 	#position in matrix of player one
      s=2
      if q not in y:
        print("...Error"+"\n"+"Instruction:-Enter the correct sign")
        s=0
      else:
        check1(q,name,sign3)
    if 5>=i>2:               			#comparing 8 cases of winning the game
      if (a[0]==a[1]==a[2]==sign3 or b[0]==b[1]==b[2]==sign3 or c[0]==c[1]==c[2]==sign3 or a[0]==b[0]==c[0]==sign3 or a[1]==b[1]==c[1]==sign3 or a[2]==b[2]==c[2]==sign3 or a[0]==b[1]==c[2]==sign3 or a[2]==b[1]==c[0]==sign3):
        print("                   ~YOU WIN~")
        break
    #running function for the system input
    def check2(q):
      if q not in x:
        x.append(q)
        if q[0]=="a":
          a[int(q[1])-1]=sign4
        elif q[0]=="b":
          b[int(q[1])-1]=sign4
        elif q[0]=="c":
          c[int(q[1])-1]=sign4
        f=a[0]+" | "+a[1]+" | "+a[2]
        g=b[0]+" | "+b[1]+" | "+b[2]  
        h=c[0]+" | "+c[1]+" | "+c[2]
        print("-Android:"+"\n"+f+"\n"+e+"\n"+g+"\n"+e+"\n"+h)
      else:       	     			#input from the system if q already exists in x
        s=chr(random.randrange(97,100))
        t=str(random.randrange(1,4))
        q=s+t
        check2(q)   	     			#calling function to print output for the system
    if i!=5:        	     			#taking input from the system
      s=chr(random.randrange(97,100))
      t=str(random.randrange(1,4))
      q=s+t
      check2(q)     	     			#calling function to print output for the system
    else:
      print("MATCH IS DRAWN!PLAY AGAIN")
    if 5>=i>2:               			#comparing 8 cases of winning the game
      if (a[0]==a[1]==a[2]==sign4 or b[0]==b[1]==b[2]==sign4 or c[0]==c[1]==c[2]==sign4 or a[0]==b[0]==c[0]==sign4 or a[1]==b[1]==c[1]==sign4 or a[2]==b[2]==c[2]==sign4 or a[0]==b[1]==c[2]==sign4 or a[2]==b[1]==c[0]==sign4):
        print("                ANDROID WINS")
        break



