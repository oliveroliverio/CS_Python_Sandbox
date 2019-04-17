import os

dir = 'C:\\Users\\olivero\\Desktop\\Python test'
os.chdir(dir)
[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]

# next, make this a windows executable that can be ported to IXM4 computer and ran there.  
