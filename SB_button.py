def code():
    for i in nuke.selectedNodes():
        firstInput = i.input(0)
        xC = firstInput.xpos() + firstInput.screenWidth()/2
        yC = firstInput.ypos() + firstInput.screenHeight()/2    
        nuke.zoom( 3, [ xC, yC ])

        
