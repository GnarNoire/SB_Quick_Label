#### SB_decreaseFont###### ON FLY 
import nuke
def SB_increaseFont():
	for n in nuke.selectedNodes():

		currentfont=n['note_font_size'].getValue()

		n['note_font_size'].setValue(currentfont+10)
		
# mapping to shift- >		