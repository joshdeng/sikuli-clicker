from sikuli import *
import time

# target object (region and image)
class target():
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
    def getState():
        return this.state
    def setState(state):
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
    def clickTarget( this, target, nextTarget, nextState, delay = 0):
        
        location = None
        # find target
        location = this.findTarget(target);

        while this.state != nextState :
            
    
            # click target
            if location != None:
                target.getRegion().doubleClick(location)

            # delay
            wait(delay)
            
            # check next state
            nextLocation = this.findTarget(nextTarget)

            # update state
            if nextLocation != None:
                this.state = nextState
            
       
        



        
        
       