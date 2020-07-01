def setup():
    size(1000, 500)
    background('#F0EFDA')
    fill('#000000')
    stroke('#000000')
    strokeWeight(3)
    frameRate(50) # control how fast animation moves

x= 0 

def draw():
    global x
    background('#F0EFDA')
    fill('#000000')
    stroke('#000000')
    strokeWeight(3)
    
    e = 0 # x/5 # relativity!
    b = 0 # random(0,1) # road can be bumpy too!
    
    # create a road and a lane!
    line(0,280,width,280) 
    
    for l in range(0,width+e,50):
        line(l -e,380,l+30 -e,380)

    # trees
    tree_h = 180
    
    for tree in range(0, width+e, 30): # tree
        line(tree -e, tree_h, tree -e , 280)
        
        for branch in range(tree_h,250,10): # branch
            line(tree -10 -e, branch +10, tree -e, branch)
            line(tree +10 -e, branch +10, tree -e, branch)
        
    # other things
    fill('#FFFF00'); noStroke(); circle(80,80,50)
    
     # cars with loops
    fill('#000000');noStroke()
    rect(x*1.5, 420 +b, 80, 25) 
    rect(x*1.5 +10, 405 +b, 50, 20)
    stroke('#F0EFDA')
    circle(x*1.5 +15, 448 +b, 20); 
    circle(x*1.5 +65, 448 +b, 20)
        
    fill('#000000');noStroke()
    rect(x*2 -width, 320 +b, 80, 25) 
    rect(x*2 -width +10, 305 +b, 50, 20)
    stroke('#F0EFDA')
    circle(x*2 -width +15, 348 +b, 20); 
    circle(x*2 -width +65, 348 +b, 20)
    
    fill('#000000');noStroke()
    rect(x -width/2, 420, 80, 25) 
    rect(x -width/2 +10, 405, 50, 20)
    stroke('#F0EFDA')
    circle(x -width/2 +15, 448, 20); 
    circle(x -width/2 +65, 448, 20)
    
    fill('#000000');noStroke()
    rect(x*1.5 -width*1.5, 320, 100, 25) 
    rect(x*1.5 -width*1.5 +50, 305, 40, 25)
    stroke('#F0EFDA')
    circle(x*1.5 -width*1.5 +15, 348, 20); 
    circle(x*1.5 -width*1.5 +62, 348, 20)
    circle(x*1.5 -width*1.5 +85, 348, 20)
    

    x +=1
    noLoop()
    loop()
    
    
