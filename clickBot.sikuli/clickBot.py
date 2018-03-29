from sikuli import *
import time

# target object (region and image)
class Target():
    def __init__(this, target, region = Region(0,24,1280,777)):
        this.region = region
        this.target = target

    # Getters and setters
    def getRegion(this):
        return this.region
    
    def setRegion(region):
        this.region = region

    def getTar(this):
        return this.target
    def setTar(target):
        this.target = target

    def getLocation(this):
        return this.getRegion().exists(this.getTar())



# Click bot
class Clicker():
    def __init__(this):
        this.state = 0        
        this.timeout = 1
        timer = 0 

    # getters and setters
    def getState(this):
        return this.state
    def setState(this,state):
        this.state = state
    

    # helper functions
    def findTarget (this, target):
        location = None
        for i in range (this.timeout):
            if target.getLocation()!= None:
                location = target.getLocation()
                break
            #wait(1)
        if location:
            return location
        else:
            return None

    # timer
    def timerReset (this):
        this.timer = time.time()
    def getTime (this):
        return time.time() - this.timer
                
    # public methods
    def clickWait( this, target, nextTarget, nextState,clickType=0, delay=0):
        
        location = None
        # find target
        location = this.findTarget(target);   
        if location != None:

            while this.state != nextState :
    
                # click target
                if clickType == 0:
                    target.getRegion().doubleClick(location)
                elif clickType == 1:
                    target.getRegion().click(location)
                elif clickType == 2:
                    target.getRegion().rightClick(location)
    
                # delay
                wait(delay)
                
                # check next state
                nextLocation = this.findTarget(nextTarget)
    
                # update state
                if nextLocation != None:
                    this.state = nextState
            
       
        



        
        
       