# Sikuli Clicker

# Usage:
```
import sys
# script path
myScriptPath = "./"

# check path
if not myScriptPath in sys.path: sys.path.append(myScriptPath)

# import module
import clickBot
reload(clickBot)

# create clicker object 
clicker = clickBot.Clicker()

# target obect contains screenshot and region
target = clickBot.Target(screenshot,region)

# clickWait(target1, target2, nextState, clickType=0, Delay=0) click then wait next target 
# it keeps click target1 till target2 shows up, clickType: 0->double click 1-> single click 2-> right click, Delay: delay time between each iteration 
clicker.clickWait(click)
```
