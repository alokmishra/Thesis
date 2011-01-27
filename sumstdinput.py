import sys
sum=0
for line in sys.stdin:
  sum += int(line.strip())

print "Final sum:" + str(sum)
