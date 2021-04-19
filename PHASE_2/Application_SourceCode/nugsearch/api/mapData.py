
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
    return toReturn