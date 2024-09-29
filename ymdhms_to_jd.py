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
year = float('nan')  
month = float('nan') 
day = float('nan') 
hour = float('nan') 
minute = float('nan') 
sec = float('nan')

# parse script arguments
if len(sys.argv)==7:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  sec = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

jd1 = (day - 32075.0) + 1461.0*((year+4800.0 + (month-14.0)/12.0)/4.0)
jd2 = 367.0*((month-2.0-((month-14.0)/12.0) * 12.0)/12.0)
jd3 = -3.0*(((year+4900.0+ ((month-14.0)/12.0))/100.0)/4.0)
jd = trunc(jd1+jd2+jd3)
jd_mn = jd - 0.5
d_frac = (sec + (60.0*(month + 60.0*hour)))/86400.0
jd_frac = jd_mn + d_frac

# Print Statments
print(jd_frac)

