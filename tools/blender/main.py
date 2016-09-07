#!/usr/bin/env python3

#----------------------------------------------------------
# File objects.py
#----------------------------------------------------------
import bpy
import os
import argparse
import json
import sys

parser = argparse.ArgumentParser(description='Process Generate args.')
parser.add_argument('--gen', type=str, nargs='+',
                    help='Command begin generate')
parser.add_argument('--env', type=str, nargs='+',
                    help='Define the enviroment')

passed_argv = sys.argv[(sys.argv.index("--")+1):]

# Parse args
args, unknown = parser.parse_known_args(passed_argv)

# Get the working location
file_path = os.getcwd()

# Read package.json
with open(os.path.join(file_path,'package.json')) as data_file:    
	# parse package json
    config_data = json.load(data_file)

deps = config_data["deps"]

deps_list = list()
for dep in deps:
	dep_name = list(dep.keys())[0]
	dep_version = list(dep.values())[0]
	dep_path = os.path.join(file_path,'luban_modules', dep_name)
	dep_data = dict()
	dep_data["dep_name"] = dep_name
	dep_data["dep_version"] = dep_version
	dep_data["dep_path"] = dep_path
	deps_list.append(dep_data)

print(args)
print(file_path)
print(config_data)
print(deps_list)

# def importFBX():
 
# if __name__ == "__main__":
# 	importFBX()