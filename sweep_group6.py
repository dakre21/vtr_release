#!/usr/bin/env pythong
import glob, os

os.chdir("vtr_flow/tasks/group6")

# Sweep VPR parameters
print "****************VPR******************" 
for file in glob.glob("*/*/run1/*/*/vpr.out"):
  print file
  f = open(file)

  for line in f.readlines():
    if "average net length" in str(line) or \
      "critical path delay" in str(line):
      print line

  print "***************************************" 

print "****************POWER******************" 
# Sweep Power parameters
for file in glob.glob("*/*/run1/*/*/*.power"):
  print file
  f = open(file)

  for line in f.readlines():
    if "Routing" in str(line) or \
      "PB Types" in str(line):
      print line

  print "*************************************" 


