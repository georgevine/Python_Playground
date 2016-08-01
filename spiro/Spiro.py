import turtle
import math

#class for drawing spirograph
class Spiro:
    #construct
    #xc-x coord of large circle; yc-y coord of large circle; col-color
    #R-radius of large circle; r-radius of small circle;
    #l-the ratio of the distance from the tip of the pen to the center of the small circle over the radius of the small circle
    def _init_(self, xc, yc, col, R, r, l):

        #create turtle
        self.t = turtle.Turtle()
        #choose turtle cursor shape
        self.t.shape('turtle')
        #set degrees to increment turtle each tick during drawing
        self.step = 5
        #set drawing complete flag
        drawingComplete = False
        #set params
        self.setParams(xc, yc, col, R, r, l)
        #init drawing
        self.restart()


    #set up parameters
    def setparams(self, xc, yc, col, R, r, l):
        #spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        #find the greatest common divisor of the radi of the large and small circles
        #radius of the small circle divided by the gcd of the two radi will be the number of times the large circle
        #must be rotated to draw the whole spirograph
        gcdval = gcd(self.r, self.R)
        #the number of rotations of the big circle required
        self.nRot = self.r/gdcval
        #find the ratio of the two radi
        self.k = r/float(R)
        #set color
        self.t.color(*col)
        #save current angle
        self.a = 0


    #restart the animation
    def restart(self):
        #set the drawing complete flag
        self.drawingComplete = False
        #show the turtle
        self.t.showturtle()
        #go to the start point of the drawing
        #this lifts the pen up so nothing is drawn as it moves
        self.t.up()
        R, k, l = self.R, self.k, self.l
        #compute position of cursor at angle 0 to prepare to begin drawing
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        #move cursor to starting position
        self.t.setpos(self.xc + x, self.yc + y)
        #put the pen down so it is ready to draw
        self.t.down()


    #draw the curve in a single continuous line
    def draw(self):
        #draw the points
        R, k, l = self.R, self.k, self.l
        #move the cursor to the positions defined by the parametric equations
        #at each angle, incremented by the defined step value, until the drawing is complete
        for i in range(0, 360*self.nRot + 1, self.step):
            #compute cursor postion at current angle
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        #done drawing, so hide the cursor
        self.t.hideturtle()


    #draw single point on curve
    def update(self):
        #return if the drawing is done
        if self.drawingComplete:
            return
        #increment the angle
        self.a += self.step
        #draw this step
        R, k, l = self.R, self.k, self.l
        a = math.radians(i)
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        #if drawing complete, set flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            #hide cursur
            self.t.hideturtle()




#class for animating spirograph
#N-number of spiros to animate
class SpiroAnimator:
    #construct
    def _init_(self, N):
        #set value of timer in millis
        self.deltaT = 10
        #get window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        #create spiros
        self.spiros = []
        for i in range(N):
            #generate random parameters
            rparams = self.genRandomParams()
            #set spiro parameters
            spiro = Spiro(*rparams)
            #add new spiro to array
            self.spiros.append(spiro)
        #set the ontimer method to call update() every deltaT millis
        turtle.ontimer(self.update, self.deltaT)


    #generate random parameters for a spiro
    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)/2)
        r = random.randint(10, 9*R/10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width/2, width/2)
        yc = random.randint(-height/2, height/2)
        col = (random.random(), random.random(), random.random())
        return(xc, yc, col, R, r, l)
    
