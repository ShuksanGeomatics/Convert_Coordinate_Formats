#!/usr/bin/env python3
'''Tools to convert longitude and latitudes as decimal degrees to different formats'''
__author__ = 'Gerry Gabrisch/Shuksan Geomatics'
__date__ = 'October 2020'
__copyright__ = '(C) 2020, Gerry Gabrisch'

import math

class DecimalDegree:
    '''Take a longitude and latitude as a tuple of decimal degrees, for example (-122.9754, 48.9864), and 
    extracts out the degrees, minutes, and seconds, and converts those coodinates to; degrees with decimal minutes;
    degrees, minutes, and seconds; or 'pretty prints' them with degree/minutes/second symbols.'''
    
    def __init__(self, long, lat):
        #define the attributes...
        self.long = long
        self.lat = lat
        
        if self.long <0:
            self.easting = 'W'
        else:
            self.easting = 'E'
        
        if self.lat <0:
            self.northing = 'S'
        else:
            self.northing = 'N'        
        
            def convert(dd):
                '''Takes the decimal degrees and returns degrees minutes, seconds as a tuple.
                This tuple is used for later conversions.'''
                negative = dd < 0
                dd = abs(dd)
                minutes,seconds = divmod(dd*3600.0,60.0)
                degrees,minutes = divmod(minutes,60.0)
                if negative:
                    if degrees > 0:
                        degrees = -degrees
                    elif minutes > 0:
                        minutes = -minutes
                    else:
                        seconds = -seconds
                return (degrees,minutes,seconds)        
        # get degree minute seconds
        self.long_deg = int(convert(long)[0])
        self.long_min = int(convert(long)[1])
        self.long_sec = round(convert(long)[2], 6)
        
        # get degree minute seconds
        self.lat_deg = int(convert(lat)[0])
        self.lat_min = int(convert(lat)[1])
        self.lat_sec = round(convert(lat)[2],6)
        
        #get decimal minutes
        self.long_dec_min = self.long_min + self.long_sec/60
        self.lat_dec_min = self.lat_min + self.lat_sec/60
        
    def dm(self):
        '''converts to decimal minutes.  Returns them as two tuples in a tuple...'''
        return ((self.long_deg, self.long_dec_min), (self.lat_deg, self.lat_dec_min))
    
    def dms(self):
        '''return the degrees, minutes, seconds, as a tuples of tuples...'''
        return((self.long_deg, self.long_min, self.long_sec),(self.lat_deg, self.lat_min, self.lat_sec))

    def pretty_dms(self):
        '''returns a string with dd mm ss formated with the correct degree symbols...'''
        return str(abs(self.long_deg)) + '\u00b0'+ str(self.long_min) + "'" + str(round(self.long_sec, 5)) + '"'+ self.easting + ', ' + str(self.lat_deg) + '\u00b0'+ str(self.lat_min) + "'" + str(round(self.lat_sec, 5)) + '"' +self.northing


class DecimalMinutes(DecimalDegree):
    '''Take a longitude and latitude as a tuple of decimal degrees with decimal minutes, for example (-122, 25.9754), (48, 38.9864), and 
    extracts out the degrees, minutes, and seconds, and converts those coodinates to; 
    degrees, minutes, and seconds; or 'pretty prints' them with degree/minutes/second symbols.'''
    
    def __init__(self , long, lat):
        #Get the degrees and decimal minutes as seporate values...
        self.long_deg2 = long[0]
        self.lat_deg2 = lat[0]
        self.long_decmin2 = long[1]
        self.lat_decmin2 = lat[1]
        
        #Set the scalers...
        if self.long_deg2 < 0:
            long_scaler = -1.0
        else:
            long_scaler = 1
        
        if self.lat_deg2 < 0:
            lat_scaler = -1.0
        else:
            lat_scaler = 1.0
            

        
        long = (abs(self.long_deg2 )+ self.long_decmin2/60) * long_scaler
        lat = (abs(self.lat_deg2)  + self.lat_decmin2/60) * lat_scaler
        #print(in_coords2)
       
        DecimalDegree.__init__(self, long, lat)  
        
class DegreesMinutesSeconds:
    '''takes degrees, minutes, and seconds as and converts them to other formats'''
    def __init__(self , long, lat):
        self.longdeg = long[0]
        self.longmin = long[1]
        self.longsec = long[2]
        
        self.latdeg = lat[0]
        self.latmin = lat[1]
        self.latsec = lat[2] 
        
    def dd(self):
        if self.longdeg < 0:
            long_scaler = -1
        else:
            long_scaler = 1
        if self.latdeg < 0:
            lat_scaler = -1
        else:
            lat_scaler = 1
        
        return (long_scaler * round(abs(self.longdeg) + self.longmin/60 + self.longsec/3600,6)),(lat_scaler * round(abs(self.latdeg) + self.longmin/60 + self.longsec/3600,6))
    
    def dm(self):
        return (self.longdeg, round(self.longmin + self.longsec/3600,8)), (self.latdeg, round(self.latmin + self.latsec/3600, 8))
    
