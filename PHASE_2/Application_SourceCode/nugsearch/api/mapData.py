
hardCodedResponseLocations = [
    {'location': {'lat': -37.74334184756751, 'lng': 144.96647844883083}, 'caseCount':1, 'date': "06 Feb 2021"},
    {'location': {'lat': -37.87768135480646, 'lng': 144.7133967111934}, 'caseCount':1, 'date': "08 Feb 2021"},
    {'location': {'lat': -37.895213114740876, 'lng': 144.75338769637898}, 'caseCount':1, 'date': "08 Feb 2021"},
    {'location': {'lat': -37.66907172693383, 'lng': 144.8409307387027}, 'caseCount':1, 'date': "09 Feb 2021"},
    {'location': {'lat': -37.84077052458711, 'lng': 144.953778227059}, 'caseCount':1, 'date': "09 Feb 2021"},
    {'location': {'lat': -37.70447615395613, 'lng': 144.91732626938497}, 'caseCount':1, 'date': "09 Feb 2021"},
    {'location': {'lat': -37.895213114740876, 'lng': 144.75338769637898}, 'caseCount':1, 'date': "10 Feb 2021"},
    {'location': {'lat': -37.70447615395613, 'lng': 144.91732626938497}, 'caseCount':1, 'date': "11 Feb 2021"}
]

hardCodedResponseRegions = [
    {'regionName': "Melbourne", "regionBounds" : {"northeast" : {"lat" : -37.5112737,"lng" : 145.5125288},"southwest" : {"lat" : -38.4338593,"lng" : 144.5937418}}, 'probabilityOfLockdown': 100},
    {'regionName': "Mitchell",  "regionBounds" : {"northeast" : {"lat" : -36.8353188,"lng" : 145.4296065},"southwest" : {"lat" : -37.5153787,"lng" : 144.5303438}}, 'probabilityOfLockdown': 50},
    {'regionName': "Yarra Ranges", "regionBounds" : {"northeast" : {"lat" : -37.5250901,"lng" : 146.1925247},"southwest" : {"lat" : -37.9751113,"lng" : 145.2816656}}, 'probabilityOfLockdown': 15},
]

def getCaseLocations(date, location):
    """
        Gets all cases in fortnight before given date, in an area around given location (to minimize response time)
        Returns array of dicts
        Dict format:{
            location: {
                lat:,
                lng:
            }, caseCount:
        }
    """
    toReturn = []
    toReturn = hardCodedResponseLocations
    return toReturn

def getRegions(date, location):
    """
        Gets regions around given location.
        Returns array of dicts.
        Dict format:{
            regionName:,
            regionBounds:{
                northEast:{
                    lat:,
                    lng:
                }, southWest:{
                    lat:,
                    lng:
                }
            }, probabilityOfLockdown: (Num 1-100)
        }
    """
    toReturn = []
    toReturn = hardCodedResponseRegions
    return toReturn