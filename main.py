import math
def main_func(tw,cl,turn,shape):
    center=[float(input("Enter the x coordinate:")),float(input("Enter the y coordinate:"))]    #this line ask the coordinate for center of the PCB inductor 
    x=center[0]
    y=center[1]
    ly = "F.Cu" if int(input("Select the Layer using the number \n 1)Top Layer \n 2)Bottom Layer \nSelect Layer: ")) == 1 else "B.Cu" # this line asks you to select the layer of the PCB
    net=1
    c=0  
    the=float(input("Enter the starting angle in degree :"))
    rot=int(input("Enter +1 for anti clockwise, Enter -1 for clockwise: "))   
    input("Press Enter to get the coordinates........ ") 
    if(shape==1):
        x, y, c = square_plot(tw, cl, turn, x, y, ly, net, c, the, rot)
    elif(shape==2):
        x, y, c = hex_plot(tw, cl, turn, x, y, ly, net, c, the, rot)
    elif(shape==3):
        oct_plot(tw, cl, turn, x, y, ly, net, c, the, rot) 
def oct_plot(tw, cl, turn, x, y, ly, net, c, the, rot):
    for i in range (8*turn):
        travel=abs((tw+cl)/(2*math.sin(math.radians(315))))
        u=x
        v=y
        if(i%4==0):
            c=c+1
        if(rot==1):
            x=x + travel*c*math.cos(math.radians(the)+i*math.radians(315))
        else:
            x=x - travel*c*math.cos(math.radians(the)+i*math.radians(315))
        y=y + travel*c*math.sin(math.radians(the)+i*math.radians(315))        
        coordinates(u,v,x,y,tw,ly,net)
def hex_plot(tw, cl, turn, x, y, ly, net, c, the, rot):
    for i in range (6*turn):
        travel=abs(((tw+cl)/2)/math.sin(math.radians(300)))
        u=x
        v=y
        if(i%3==0):
            c=c+1
        if(rot==1):
            x=x + travel*c*math.cos(math.radians(the)+i*math.radians(300))
        else:
            x=x - travel*c*math.cos(math.radians(the)+i*math.radians(300))
        y=y + travel*c*math.sin(math.radians(the)+i*math.radians(300))        
        coordinates(u,v,x,y,tw,ly,net)
    return x,y,c
def square_plot(tw, cl, turn, x, y, ly, net, c, the, rot):
    for i in range (4*turn):
        travel=abs((tw+cl)/math.sin(math.radians(270)))
        u=x
        v=y
        if(i%2==0):
            c=c+1
        if(rot==1):
            x=x + travel*c*math.cos(math.radians(the)+i*math.radians(270))
        else:
            x=x - travel*c*math.cos(math.radians(the)+i*math.radians(270))
        y=y + travel*c*math.sin(math.radians(the)+i*math.radians(270))        
        coordinates(u,v,x,y,tw,ly,net)
    return x,y,c    
def coordinates(u,v,x,y,tw,ly,net):
    print("(segment(start",u,v,")(end",x,y,")(width",tw,")(layer",ly,")(net",net,"))") 
def calc_inductance(B, a1, a2, a3, a4, a5,shape): 


    """
    this function calculates the inductance which is given in the following link 
    https://coil32.net/pcb-coil.html 
    """

    tw=float(input("Enter the track width in mm :"))*1000
    cl=float(input("Enter the clearance in mm :"))*1000
    turn=int(input("Enter the number of turns :"))
    id=2*(tw+cl)
    od=turn*id
    Davg=(od+id)/2
    print("the avg diameter of the coil is ",Davg,"micro meter")
    l=B*pow(od,a1)*pow(tw,a2)*pow(Davg,a3)*pow(turn,a4)*pow(cl,a5)
    print("The inductance of the coil is ",l," nano henry")
    input("Press enter to continue.......")
    main_func(tw/1000,cl/1000,turn,shape)
def get_shape(): #the code starts here where you need to select the shape you need
    x=int(input("Select shape using the number \n 1.Square\n 2.Octagon\n 3.Hexagon\n Seclect shape:"))
    if x==1:
        B,a1,a2,a3,a4,a5=1.62*pow(10,-3),-1.21,-0.147,2.4,1.78,-0.03
        calc_inductance(B, a1, a2, a3, a4, a5,x)       
    elif x==2:
        B,a1,a2,a3,a4,a5 = 1.28*pow(10,-3),-1.24,-0.174,2.47,1.77,-0.049
        calc_inductance(B, a1, a2, a3, a4, a5,x)
    elif x==3:
        B,a1,a2,a3,a4,a5 = 1.33*pow(10,-3),-1.21,-0.163,2.43,1.75,-0.049
        calc_inductance(B, a1, a2, a3, a4, a5,x)


get_shape() 
