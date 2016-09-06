#!/usr/bin/env python3

#----------------------------------------------------------
# File objects.py
#----------------------------------------------------------
import bpy
import os
import argparse

parser = argparse.ArgumentParser(description='Process Generate args.')
parser.add_argument('--gen', type=str, nargs='+',
                    help='command begin generate')
parser.add_argument('--env', type=str, nargs='+',
                    help='define the enviroment')

# Parse args
args, unknown = parser.parse_known_args()
print(args)

# def importFBX():
 
# if __name__ == "__main__":
# 	importFBX()