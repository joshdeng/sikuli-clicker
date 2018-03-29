# Sikuli Clicker

# TODOs:
1. pressWait() # press certain key till pattern shows up.
2. clickType() # click pattern then type conent.
# Usage:
```
import sys
# Script path
myScriptPath = "./"

# Check path
if not myScriptPath in sys.path: sys.path.append(myScriptPath)

# Import module
import clickBot
reload(clickBot)

# Create clicker object 
clicker = clickBot.Clicker()

# Target obect contains screenshot and region
target = clickBot.Target(screenshot,region)

# clickWait(target1, target2, nextState, clickType=0, delay=0) 
# It keeps click target1 till target2 shows up. 
#    clickType: 
#       0-> double click 
#       1-> single click 
#       2-> right click, 
#    delay: 
#       delay time between clicking target1 and checking target2 (int, sec)
      
clicker.clickWait(target1,target2,1)
```
