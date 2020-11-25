convert_degree_formats
Converts degrees, minutes, seconds, or degrees with decimal minutes to different formats and data types.

This scripts contains two classes to convert between common ways to represent degrees, minutes, and seconds.
Inputs must be longitude followed by latitude. Inputs can be a pair of decimal degrees or two tuples for degrees with decimal minutes.

---To convert from decimal degrees use....

#import module...
import convert_degree_formats
#Create a DecimalDegree object...
coords = DecimalDegree(-122.953, 48.955)

---To convert from degrees with decimal minutes use...
coords = DecimalMinutes((-122, 5.5), (48, 5.5))

Below are the returns and examples for both classes...
		
#Return degrees and decimal minutes as a tuple of tuples.  For example, ((-122, 57.18), (48, 57.3))
coords.dm()
		
#Returns a  well formated string.  For example 122°57'10.8"W, 48°57'18.0"N
coords.pretty_dms()
		
#Returns degrees, minutes, seconds as a tuple of tuples.  For example ((-122, 57, 10.8), (48, 57, 18.0))
coords.dms()
		
#Returns longitude degrees only as a double...
coords.long_deg
		
#Returns longitude minutes only as a double...
coords.long_min
		
#Return lonitude seconds only as a double...
coords.long_sec
		
#Return latitude degrees only as a double...
coords.lat_deg
		
#Return latitude minutes only as a double...
coords.lat_min
		
#Return latitude seconds only as a double...
coords.lat_sec

