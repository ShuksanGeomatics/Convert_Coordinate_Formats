#!/usr/bin/env python3
'''Tester for geographic coordinate format converter'''

import traceback
import sys
import convert_degree_formats
try:
	def main():
		#Decimal Degree Converter Test...
		coords = convert_degree_formats.DecimalDegree(-122.953, 48.655)
		
		#Convert to a tuple of tuples with degrees and decimal minutes.  For example, ((dd, dm), (dd, dm))...
		print (coords.dm())
		
		#prints well formated coordinates.  For example 122°5'30.0"W, 48°5'30.0"N
		print(coords.pretty_dms())
		
		#Returns a tuple of tuples.  For example ((dd, mm, ss), (dd, mm, ss))
		print(coords.dms())
		
		#Easily get a portion of the coordinate with these method calls...
		#Returns longitude degrees only...
		print(coords.long_deg)
		
		#Returns longitude minutes only...
		print(coords.long_min)
		
		#Return lonitude seconds only...
		print(coords.long_sec)
		
		#Return latitude degrees only...
		print(coords.lat_deg)
		
		#Return latitude minutes only...
		print(coords.lat_min)
		
		#Return latitude seconds only...
		print(coords.lat_sec)
		
		#Returns longitude decimal minutes only
		print(coords.long_dec_min)
		
		#Returns latitude decimal minutes only
		print(coords.lat_dec_min)
		
		print()
		
		#For degrees with decimal minutes as input test...
		coords = convert_degree_formats.DecimalMinutes((-122, 57.18), (48, 57.3))
		print (coords.dm())
		print(coords.pretty_dms())
		print(coords.dms())
		print(coords.long_deg)
		print(coords.long_min)
		print(coords.long_sec)
		print(coords.lat_deg)
		print(coords.lat_min)
		print(coords.lat_sec)
		print(coords.long_dec_min)
		print(coords.lat_dec_min)	
		
		#Test with degrees, minutes, and seconds as a tuple of tuples...
		coords =convert_degree_formats.DegreesMinutesSeconds((-122, 40, 23.5),(48, 55,25))
		print(coords.dd())
		print(coords.dm())
		print(coords.pretty_dms())
		
except:
	tb = sys.exc_info()[2]
	tbinfo = traceback.format_tb(tb)[0]
	print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
	
if __name__ == "__main__":
	main()  

