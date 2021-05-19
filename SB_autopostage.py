
import nuke
import os
def SB_autopostage():
	s=nuke.selectedNode()
	#print s
	sname=s.name() 
	#print sname
	p=nuke.nodes.PostageStamp
	#print p

	#s['note_font_color'].setValue(00fffa)
	p(name='PosStmp_' + s.name(), selected=True, note_font_color=(0,1,1), hide_input= True, postage_stamp= True, tile_color = 1).setInput(0, s)


	#### IF READ NODE 

	def postNamer():
		for i in nuke.selectedNodes('PostageStamp'):
			firstInput = i.input(0)
			if firstInput.Class() == 'Read':
				Fname = nuke.filename(firstInput)
				Fname = os.path.basename(Fname)
				Fname = Fname.split('.')[0]
			elif firstInput.Class() != 'Read':
				pass


	postNamer()


	###copy label

	p=nuke.selectedNode()
	d=nuke.selectedNode().name()
	l=p['label'].getValue()
	txt = nuke.getInput('Change label','SB_POS_STMP_')
	txt = nuke.getInput('Change label','SB_POS_STMP_')
	print 
	if l=="":
		for n in nuke.selectedNodes():
			n['label'].setValue(txt)
		else:
			n['label'].setValue(l + txt)

		

		


	###### SET COLOR######
	col = nuke.getColor()
	#h = inverse col
	if col:
		for n in nuke.selectedNodes():
			n['tile_color'].setValue(col)
			n['gl_color'].setValue(col)
			
			
#SB_autopostage()