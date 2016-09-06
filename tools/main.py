#!/usr/bin/env python3

#----------------------------------------------------------
# File objects.py
#----------------------------------------------------------
import bpy
import os
 
full_path_to_directory = os.path.join('C:\\', 'Users', 'name', 'Documents', 'OBJECTS')

def importFBX():
	print(full_path_to_directory)

 
if __name__ == "__main__":
	importFBX()