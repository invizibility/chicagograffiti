import os
import csv
import codecs
from geopy.geocoders import GoogleV3
from pygeocoder import Geocoder

geocoder1 = GoogleV3()


with open('test.csv','w') as fp:
	with open('newdat2.csv','rb') as locations:
		header = locations.next()
		#print "yo"

		a = csv.writer(fp, delimiter=',')
		#for row in locations:
		for row in csv.reader(locations, delimiter=","):
			geostring = row[0]+' '+"Chicago,IL"
			results = Geocoder.geocode(geostring)
			print results[0].coordinates 
			#print row
			#print "yo"
			#print locations
			#print row[0]
			#print geocoder1.geocode(row[0]+' '+"Chicago,IL", exactly_one=False)[0]




	 	



# csvfile = open('newdat.csv','rb')

# dialect = csv.Sniffer().sniff(csvfile.read(10*1024))
# csvfile.seek(0)

# reader = csv.reader(csvfile, dialect)

# data = [row for row in reader]
# print data