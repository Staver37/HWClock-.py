#clock module
import turtle as t
from datetime import datetime
# time data

c_radius = 300

    
#print the time
def printTime(hours, minutes, seconds):
    print (f"{hours:02}:{minutes:02}:{seconds:02}" )    # template strings
    


def drawClock(hours, minutes, seconds):
    t.clear()
    drawClockCircle()
    drawClockHours(hours)
    drawClockMinutes(minutes)
    drawClockSeconds(seconds)
    
# draw clock circle
def drawClockCircle():
    t.speed(0)
    t.penup()
    t.setheading(0)
    t.setposition(0, - c_radius)
    t.pendown()
    t.circle(c_radius)

def drawClockHours(hours):
    t.penup()
    t.setposition(0,0)
    t.pensize(5)
    t.pendown()
    t.setheading( 90 + hours * -30)
    t.forward( c_radius * 0.7)
    
def drawClockMinutes(minutes):
    t.penup()
    t.setposition(0,0)
    t.pensize(2)
    t.pendown()
    t.setheading( 90 + minutes * -6)
    t.forward( c_radius * 0.8)

def drawClockSeconds(seconds ):
    t.penup()
    t.setposition(0,0)
    t.pensize(2)
    t.pendown()
    t.setheading( 90 + seconds * -6)
    t.forward( c_radius * 0.9)

def CheckAlarm ():
    a = datetime.now()
    
    h = 15
    m = 29
    s = 50
    
    if a.hour == h:
       if  a.minute == m:
           if  a.second <= s:
             print("CUCU")
            # screen = t.Screen()
            # screen.setup(400, 400)
            # screen.bgpic("cucu.jpg")
             
             
             
                 