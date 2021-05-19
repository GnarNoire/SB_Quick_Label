
##################SB_ Quick LABELER
import nuke
import os

def SB_quickLabel():
  
    txt = nuke.getInput('Change label','unique label')
     
    for n in nuke.selectedNodes():
        existingLblTxt = n['label'].getValue()

        newLblTxt = existingLblTxt + '_-_' + txt
        n['label'].setValue(newLblTxt)
        
        curClass=n.Class()
        print (curClass)
         
        if curClass=='Dot':
            n['note_font_size'].setValue(40)
        else:
            print ("Im not a dot")


			
			
			
			
			
			
			
			
			
			
			
		
		
		
