######## add to your menu.py 
 
import SB_autopostage
#################   my menu add ######## 
import SB_quickLabel
import setnodecolor
toolbar = nuke.menu("Nodes")
SBscripts = toolbar.addMenu("SB", icon= 'SB_icn_pyra.png')
SBscripts.addCommand('SB_autopostage', 'SB_autopostage.SB_autopostage()', 'shift+p', icon= 'FrameRange.png',)
SBscripts.addCommand('Change Dat Color B', 'setnodecolor.setNodeColor()', 'alt+shift+c', icon= 'SB_icon.png')
SBscripts.addCommand('SB_QuickLabel', 'SB_quickLabel.SB_quickLabel()', 'shift+l', icon= 'Text.png',)
###########  font scale
import SB_increaseFont
import SB_decreaseFont
SBscripts.addCommand('SB_increaseFont', 'SB_increaseFont.SB_increaseFont()', 'shift+.', icon= 'SB_icon.png',)
SBscripts.addCommand('SB_decreaseFont', 'SB_decreaseFont.SB_decreaseFont()', 'shift+,', icon= 'SB_icon.png',) 
####### ADD RevealInExplorer #############
import RevealInExplorer
SBscripts.addCommand('SB_Reveal_In_Explorer', 'RevealInExplorer.RevealInExplorer()', 'shift+r', icon= 'CopyRectangle.png',)
