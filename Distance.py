import urllib2
import string
import math

def do_maths(coords1, coords2):

    try:
        R = 6371e3
        lat1 = float(coords1[0])
        long1 = float(coords1[1])
        lat2 = float(coords2[0])
        long2 = float(coords2[1])

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        deltaPhi = math.radians(lat2 - lat1)
        deltaLambda = math.radians(long2 - long1)

        a = math.sin(deltaPhi / 2) * math.sin(deltaPhi / 2) + \
            math.cos(phi1) * math.cos(phi2) * \
            math.sin(deltaLambda / 2) * math.sin(deltaLambda / 2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = R * c

        return d

    except(ValueError):
        print "Not valid city names"
        exit()


def do_stuff(city):

    try:
        site = 'https://en.wikipedia.org/wiki/' + city
        response = urllib2.urlopen(site).read()
        location = response.find('<span class="geo">') + len('<span class="geo">')
        subString = response[location:]
        coords = subString.split('<', 1)[0].replace(' ', '').split(';')
        return coords
    except(urllib2.HTTPError):
        print "Not a valid wikipedia entry"
        exit()

city1 = string.capwords(raw_input('Enter first city: ')).replace(' ', '_')
coords1 = do_stuff(city1)

city2 = string.capwords(raw_input('Enter second city: ')).replace(' ', '_')
coords2 = do_stuff(city2)

print "The Distance between", city1.replace('_', ' '), "and", city2.replace('_', ' '), "is: "

distanceKM = do_maths(coords1, coords2)/1000
distanceMILES = distanceKM/1.621371

print distanceKM, "km"
print distanceMILES, "miles"