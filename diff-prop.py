#!/usr/bin/env python    

# Compare japanese translation files with spanish files 
import configparser
import pprint
import sys
import os

def main():
   if len (sys.argv) < 2:
       print ("provide one argument. Japan file to compare")
       sys.exit (1)
   file1 = sys.argv[1]
   file2 = file1.replace("_ja.properties", "_es.properties")
   if not os.path.isfile(file1):
      print ("%s doesn't exists" % file1)
      sys.exit(1)

   """
   if not os.path.isfile(file2):
      print ("%s doesn't exists" % file2)
      sys.exit(1)
   """


   config1 = configparser.RawConfigParser()
   try:
      config1.read (file1)
   except configparser.MissingSectionHeaderError:
      with open(file1) as stream:
         config1.read_string("[top]\n" + stream.read())

   config2 = configparser.RawConfigParser()
   try:
      config2.read (file2)
   except configparser.MissingSectionHeaderError:
      with open(file2) as stream:
         config2.read_string("[top]\n" + stream.read())

   try:
      setA = set(config1.options('top'))
   except configparser.NoSectionError:
      setA = set()

   try:
      setB = set(config2.options('top'))
   except configparser.NoSectionError:
      setB = set()

   onlySetA = setA.difference (setB)
   onlySetA_count = 0
   if onlySetA:
      onlySetA_count = len(onlySetA)
      print ("%d properties only in %s" % (onlySetA_count, file1));
      #pprint.pprint(onlySetA)

   onlySetB = setB.difference (setA)
   onlySetB_count = 0
   if onlySetB:
      onlySetB_count = len(onlySetB)
      print ("%d properties only in %s" % (onlySetB_count, file2));
      #pprint.pprint (onlySetB)

   commonProperties = setA.intersection (setB)
   commonProperties = 0
   if commonProperties:
      commonProperties_count = len(commonProperties)
      print ("%d properties common" % (commonProperties_count));
      """
      for key in commonProperties:
         pprint.pprint("-----%s" % key)
         pprint.pprint (config1.get('top', key))
         pprint.pprint (config2.get('top', key))
      """

   print ("\n%d/%d = %d%% translated" % (len(setB), len(setA), len(setB)*100/len(setA)))

if __name__== "__main__":
   main ()
