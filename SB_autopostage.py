
import nuke
import os


def SB_autopostage():
	s = nuke.selectedNode()
	# print s
	input_label = '[value this.input0.label]'
	print(input_label)
	sname = s.name()
	# print sname
	p = nuke.nodes.PostageStamp
	# print p
	# s['note_font_color'].setValue(00fffa

	p(name='PosStmp_' + s.name(), label=input_label, selected=True, note_font_color=(0, 1, 1), hide_input=True,
	  postage_stamp=True, tile_color=(0, 1, 1)).setInput(0, s)

	# n['label'].setValue(txt)

	#### IF READ NODE

	def postNamer():
		for i in nuke.selectedNodes('PostageStamp'):
			firstInput = i.input(0)
			if firstInput.Class() == 'Read':
				Fname = nuke.filename(firstInput)
				Fname = os.path.basename(Fname)
				Fname = Fname.split('.')[0]
				i['label'].setValue(Fname)
			elif firstInput.Class() != 'Read':
				pass

	postNamer()

	###copy label
	def copy_label():
		p = nuke.selectedNode()
		firstInput = p.input(0)
		if firstInput.Class() != 'Read':
			d = nuke.selectedNode().name()
			l = p['label'].getValue()
			txt = nuke.getInput('Change label', 'SB_POS_STMP_')
			print
			if l == "":
				for n in nuke.selectedNodes():
					n['label'].setValue(txt)
				else:
					n['label'].setValue(l + txt)
			if firstInput.Class() == 'Blur':
				p['label'].setValue('Blur size= [value this.input0.size]' + "__" + txt)
			if firstInput.Class() == 'Merge2':
				p['label'].setValue('Merge Mix= [value this.input0.mix]' + "__" + txt)
			if firstInput.Class() == 'Switch':
				p['label'].setValue('Switch input= [value this.input0.which]' + "__" + txt)
			if firstInput.Class() == 'TimeOffset':
				p['label'].setValue('TimeOffset= [value this.input0.time_offset]' + "__" + txt)
			if firstInput.Class() == 'Defocus':
				p['label'].setValue('defocus amount= [value this.input0.defocus]' + "__" + txt)
			if firstInput.Class() == 'AdjBBox':
				p['label'].setValue('amount= [value this.input0.numpixels]' + "__" + txt)
			if firstInput.Class() == 'Tracker4':
				p['label'].setValue('amount= [value this.input0.transform]' + "__" + txt)
			if firstInput.Class() == 'Reformat':
				p['label'].setValue('reformat= [value this.input0.format]' + "__" + txt)

	copy_label()

	###### SET COLOR######
	col = nuke.getColor()
	# h = inverse col
	if col:
		for n in nuke.selectedNodes():
			n['tile_color'].setValue(col)
			n['gl_color'].setValue(col)

	# def code():
	#  for i in nuke.selectedNodes:
	#      firstInput = i.input(0)
	#      xC = firstInput.xpos() + firstInput.screenWidth()/2
	#     yC = firstInput.ypos() + firstInput.screenHeight()/2
	#      nuke.zoom( 3, [ xC, yC ])'''

	def findPapa():
		for n in nuke.selectedNodes('PostageStamp'):
			m = nuke.PyScript_Knob("Papa", "Papa", "SB_button.code()")
			n.addKnob(m)
	findPapa()

