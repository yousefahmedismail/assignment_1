k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def board():
    print(k[0],"/",k[1],"/",k[2],"/",k[3])
    print(k[4],"/",k[5],"/",k[6],"/",k[7])
    print(k[8],"/",k[9],"/",k[10],"/",k[11])
    print(k[12],"/",k[13],"/",k[14],"/",k[15])


while True:
    board()
    turn=1
    p11=int(input("Player1, please enter first number:"))
    p12=int(input("Player1, please enter second number:"))

    while(abs(p11-p12)!=1 and abs(p11-p12)!=4):
        print("error")
        p11 = int(input("Player1, please enter first number:"))
        p12 = int(input("Player1, please enter second number:"))

    k[p11] = "x"
    k[p12] = "x"


    board()
    turn=2
    p21 = int(input("Player2, please enter first number:"))
    p22 = int(input("Player2, please enter second number:"))
    while(abs(p21-p22)!=1 and abs(p21-p22)!=4):
        print("error")
        p21 = int(input("Player2, please enter first number:"))
        p22 = int(input("Player2, please enter second number:"))
    k[p21] = "x"
    k[p22] = "x"



