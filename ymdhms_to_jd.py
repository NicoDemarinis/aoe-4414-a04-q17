# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Text explaining script usage
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
#  ...
# Output:
#  Makes the fractional Julian date form regular time
#
# Written by Nicola DeMarinis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv
from math import trunc

# initialize script arguments
year = int(0)  
month = int(0) 
day = int(0) 
hour = int(0) 
minute = int(0) 

# parse script arguments
if len(sys.argv)==7:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = int(sys.argv[4])
  minute = int(sys.argv[5])
  sec = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

jd = day - 32075 \
   + trunc(1461 * (year + 4800 +  trunc((month-14)/12))/4) \
   + trunc(367 * (month - 2 - (trunc((month-14)/12) *12 ))/12) \
   - trunc(3 * trunc((year + 4900 + trunc((month-14)/12))/100)/4)

jdmn = (jd) - 0.5
dfrac = (sec + 60*(minute + 60*hour))/86400
jd_frac = jdmn + dfrac

# Print Statments
print(jd_frac)

