x=1
img=0
e=1
mode="RIGHT"
o=0
t=900
w="LEFT"
def setup():
    size(1000,800)
    global img,o
    img=loadImage("1.jpg")
    o=loadImage("2.jpg")
def draw():
    global x,img,mode,e,o,t,w
    background(x)
    fill(50)
    rect(100,220,180,500)
    stroke(50,0,0)
    strokeWeight(4)
    line(100,720,280,220)
    line(280,720,100,220)
    fill(50,0,0)
    triangle(100,220,280,220,190,100)
    fill(20)
    rect(280,220,400,500)
    fill(50)
    rect(680,220,180,500)
    fill(50,0,0)
    line(680,220,860,720)
    line(860,220,680,720)
    triangle(680,220,860,220,770,100)
    fill(153,204,255)
    noStroke()
    rect(320,400,100,100)
    rect(520,400,100,100)
    fill(50)
    rect(300,180,30,40)
    push()
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    pop()
    fill(153,102,51)
    ellipse(480,720,210,290)
    fill(0,153,51)
    rect(0,720,1000,300)
    image(img, e, 650, 100, 100)
    image(o,t,650,100,100)
    x=x+1
    if x >= 255:
        x=0
    if e <=10:
        mode= "RIGHT"
    if mode=="RIGHT":
        e=e+1
    if e >= 900:
        mode="LEFT"
    if mode=="LEFT":
        e=e-1
        
    if t <=10:
        w= "RIGHT"
    if w=="RIGHT":
        t=t+1
    if t >= 900:
        w="LEFT"
    if w=="LEFT":
        t=t-1
    if keyPressed:
        fill(100,100,0)
        rect(560,455,15,45)
        ellipse(568,445,25,25)
        fill(100,100,0)
        rect(380,455,15,45)
        line(380,460,400,440)
        ellipse(388,445,25,25)
        for step in 1,2,3,4,5,6,7:
            fill(0,0,150)
            rect(random(10,900),random(10,700),10,15)

    
