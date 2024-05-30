#In this project, we'll use a button to toggle btwn snake lights, binary counter and traffic lights
from machine import Pin
from time import sleep

button_state=0
btn_Pn=Pin(10, Pin.IN, Pin.PULL_DOWN)

red=0
yellow=2
green=3
Led1=Pin(red,Pin.OUT)
Led2=Pin(yellow,Pin.OUT)
Led3=Pin(green,Pin.OUT)


def Snake_lights():
    print("-------------------")
    arr=[red,yellow,green]
    i=0
    T=0
    while True:
        led=Pin(arr[i],Pin.OUT)
        led.value(1)
        sleep(0.5)
        led.value(0)
        i=i+1
        if i==3:
            i=0
            T=T+1
            if T==3:
                Led1.value(0)
                Led2.value(0)
                Led3.value(0)
                print("Snake Lights done")
                print("-------------------")
                break
def Binary_Counter():
    print("-------------------")
    Binry=[0,0,0]
    T=0
    while True:
        for x in range(8):
            Binry[2]= x%2    
            x=x//2
            Binry[1]= x%2    
            x=x//2
            Binry[0]= x%2    
            x=x//2
            print(Binry)
            Led1.value(Binry[0])
            Led2.value(Binry[1])
            Led3.value(Binry[2])
            sleep(0.5)
            Led1.value(0)
            Led2.value(0)
            Led3.value(0)
            sleep(0.5)
        print("-------------------")
        T=T+1
        if T==1:
            Led1.value(0)
            Led2.value(0)
            Led3.value(0)
            print("Binary Counter done")
            print("-------------------")
            break;
def Traffic_Lights():
    print("-------------------")
    T=0
    while True:
        Led1.value(1)
        Led2.value(0)
        Led3.value(0)
        print("STOP")
        sleep(5)
        Led1.value(1)
        Led2.value(1)
        Led3.value(0)
        print("HOLD ON")
        sleep(1)
        Led1.value(0)
        Led2.value(1)
        Led3.value(0)
        print("WAIT")
        sleep(3)
        Led1.value(0)
        Led2.value(1)
        Led3.value(1)
        print("ALMOST")
        sleep(1)
        Led1.value(0)
        Led2.value(0)
        Led3.value(1)
        print("GO!")
        sleep(3)
        Led1.value(1)
        Led2.value(0)
        Led3.value(1)
        print("START BRAKING")
        sleep(1)
        
        T=T+1
        if T==1:
            Led1.value(0)
            Led2.value(0)
            Led3.value(0)
            print("Traffic Lights done")
            print("-------------------")
            break;
    
def disp_project():
    n=0
    while True:
        if btn_Pn.value():
            if n==0:
                print("-------------------")
                print("BUTTON PRESSED")
                print("Snake Lights")
                Snake_lights()
                
                
            if n==1:
                print("-------------------")
                print("BUTTON PRESSED")
                print("Binary Counter")
                Binary_Counter()
                
            
            if n==2:
                print("-------------------")
                print("BUTTON PRESSED")
                print("Traffic Lights")
                Traffic_Lights()
            n=n+1
            if n==3:
                n=0
        sleep(0.3)
    

disp_project()
    
    
    