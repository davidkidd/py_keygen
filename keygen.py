#/usr/bin/env python

'''
Batch key generator

Key format: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

Usage: keygen [number of keys] [output filename]

If output file exists, new keys will be appended to the existing file.
'''

import random, sys

CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == '__main__':
  try:
    with open(sys.argv[2], "a") as f:
      f.writelines(
        "\n".join(["-".join(["".join([random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") 
          for char  in range(5)])
          for chunk in range(5)])
          for key   in range(int(sys.argv[1]))]))
  except (IndexError, ValueError) as e:
    print "Usage: {0} [number of keys] [output filename]".format(sys.argv[0])
  except:
    raise