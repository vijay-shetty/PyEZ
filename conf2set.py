#!/usr/local/bin/python

firstline = "version"

#read in filepath from commandline
import sys
if len(sys.argv) < 2:
  print "  >> Usage: sys.argv[0] <filepath>"
  exit()
filepath = sys.argv[1]

#open filepath for reading
f = open(filepath, "r")

#skip lines until we match "firstline" - skip this line too
line = ""
while not line.startswith(firstline):
  line = f.readline().rstrip()

from string import whitespace as ws
setline = []

def traverseJuniperConfig( filehandle, setline ):
  #print "setline = 'set " + " ".join(setline) + "'"
  lineorig = filehandle.readline()
  #EOF check
  if len(lineorig) == 0:
    return "-1"
  line = lineorig.strip()
  ###if line ends in ';', join/print 
  if line.endswith(";"):
    setlineprint = " ".join(setline)
    if len(setlineprint) > 0:
      setlineprint = setlineprint + " "
    printline = "set " + setlineprint + line.rstrip(";")
    print printline
    #setline = setline
  ###elif line ends in '}', remove last element of setline
  elif line.endswith("}"):
    setline = setline[0:-1]
  ###elif line ends in '{', update setline and recurse
  elif line.endswith("{"):
    linestrip = line.rstrip(ws + "{")
    setline.append(linestrip)
    setline = traverseJuniperConfig( filehandle, setline )
  return setline

#iterate through file until EOF
while setline != "-1":
  setline = traverseJuniperConfig( f, setline )
