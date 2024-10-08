#!/usr/bin/python3

# Generar combianciones de PIN

import itertools
import time

def main():
  for i in range(0, 7):
    for p in itertools.product(range(10), repeat=i):
      print(''.join(map(str, p)))

if __name__ == '__main__':
  start_time = time.time()
  main()
  print("--- %s seconds ---" % (time.time() - start_time))
