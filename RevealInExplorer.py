import nuke
def RevealInExplorer():
    import os
    import subprocess
    a=nuke.selectedNode()
    b=a['file'].value()
    u=os.path.split(b) [0]
    u = os.path.normpath (u)
    print (u)
    subprocess.Popen(r"explorer /select, %s" %(u))


