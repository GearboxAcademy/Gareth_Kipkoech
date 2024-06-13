from machine import Pin, SoftSPI,ADC
import ssd1306
from time import sleep


#CS --- 15
#DC --- 6
#RES --- 5
#SDA --- 13
#SCL --- 14
#VDD --- 3.3 V
#GND --- GND
spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))

dc = Pin(6)   # data/command
rst = Pin(5)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this

display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

#Initializing the joyStick as analog input.
joy_Stick=ADC(Pin(27))

#x and y coordinates of the ball.
x_ball=0
y_ball=0
#initializing the x and y coordinates of the slider
x=0
y=55
#initializing the x and y speeds of the ball
y_speed=2
x_speed=1
#initialize the variable to store the player's score
score=0

while True:
    #Read the joystick analog value, map it between the screen limits you wish for your slider
    stick_Val=joy_Stick.read_u16()
    pos=((stick_Val)/65535)*80
    x=int(pos)
    print(stick_Val)
    print(int(pos))

    #Clear the screen for new data to be displayed to prevent overlapping of content
    display.fill(0)
    display.text('______',int(x),y,1)
    display.text(str(score), x_ball, y_ball, 1)

    #Update the position of the ball
    y_ball=y_ball+y_speed
    x_ball=x_ball+x_speed
    #if the ball has reached the y level of the slider, 
    if (y_ball>=y ):
        #Check if the ball has hit the slider
        if (x_ball>=x and x_ball<=(x+53)):
            print("Score!")
            score+=2
            #Make the ball bounce back
            y_speed=y_speed*-1
            if score>=10:
                x=0
                x_ball=0
                y_ball=0
                score=0
                display.fill(0)
                display.text('YOU WIN !!', 30, 30, 1)
                display.show()
                sleep(2) 
        else:
            score-=2
            #Restart the position of the ball if it misses the slider
            x=0
            x_speed=x_speed*-1
            y_ball=0
            if score<=0:
                score=0
                display.fill(0)
                display.text('GAME OVER', 30, 30, 1)
                display.show()
                sleep(2) 
    #Block of conditions to ensure the ball bounces off the top, left and right walls.        
    if (y_ball>=65):
        y_ball=0    
    if y_ball<0:
        y_speed=y_speed*-1
    if x_ball>=120 or x_ball<0:
        x_speed=x_speed*-1
    display.show()
    sleep(0.1)

