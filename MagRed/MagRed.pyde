add_libraly("sound")
f=0
g=0
img=0
img2=0
img3=0
klok=0

def setup():
    size(600,600)
    global f,g,img,img2,img3
    img = loadImage("red.png")
    img2 = loadImage("fire.jpg")
    img3 = loadImage("RED.jpg")
    klok=SoundFile("Jo.mp3")
    
def draw():
    global f,g,img,img2,img3
    clear()
    image(img,f,g,100,100)
    if f==-1:
        f=f+1
    if f==501:
        f=f-1
    if g==-1:
        g=g+1
    if g==501:
        g=g-1
    if key=='y':
        image(img3,0,0,600,600)
        klok.play()
    
def keyPressed():
    global f,g,img,img2,img3
    if key=='w':
        g=g-1
    if key=='s':
        g=g+1
    if key=='a':
        f=f-1
    if key=='d':
        f=f+1
    if key=='e':
        f=f+1
        g=g-1
    if key=='q':
        f=f-1
        g=g-1
    if key=='z':
        f=f-1
        g=g+1
    if key=='x':
        f=f+1
        g=g+1
