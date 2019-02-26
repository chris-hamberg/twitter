try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Numeric
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Numeric
    from application.subprocess.subroutines import filter
finally:    
    from requests import get

class id(Numeric): 
    '''Returns all the information about a known place. 

	- id
	A place in the world. These IDs can be retrieved from 
	geo/reverse_geocode.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> retrieved from geo/reverse_geocode'''

class reverse_geocode(AbstractBase): 
    '''Given a latitude and a longitude, searches for up to 20 places that can 
be used as a place_id when updating a status. 

This request is an informative call and will deliver generalized results about 
geography. 

	- lat
	The latitude to search around. This parameter will be ignored unless it is 
    inside the range -90.0 to +90.0 (North is positive) inclusive. It will also 
    be ignored if there isn’t a corresponding long parameter. 

	- long
	The longitude to search around. The valid ranges for longitude is -180.0 to 
    +180.0 (East is positive) inclusive. This parameter will be ignored if 
    outside that range, if it is not a number, if geo_enabled is disabled, or if 
    there not a corresponding lat parameter. 

	- accuracy
	A hint on the “region” in which to search. If a number, then this is a 
    radius in meters, but it can also take a string that is suffixed with ft to 
    specify feet. If this is not passed in, then it is assumed to be 0m. If 
    coming from a device, in practice, this value is whatever accuracy the 
    device has measuring its location (whether it be coming from a GPS, WiFi 
    triangulation, etc.). 

	- granularity
	This is the minimal granularity of place types to return and must be one of: 
    poi, neighborhood, city, admin or country. If no granularity is provided for 
    the request neighborhood is assumed. Setting this to city, for example, will 
    find places which have a type of city, admin or country. 

	- max_results
	A hint as to the number of results to return. This does not guarantee that 
    the number of results returned will equal max_results, but instead informs 
    how many “nearby” results to return. Ideally, only pass in the number of 
    places you intend to display to the user here. 

	- callback
	If supplied, the response will use the JSONP format with a callback of the 
    given name.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, lat=None, long=None, accuracy=None, granularity=None, 
            max_results=None, callback=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 lat         -> -90 <= float <= 90
 long        -> -180 <= float <= 180
 accuracy    -> int, or a numeric string postfixed with 'ft'
 granularity -> str in {'poi', 'neighborhood', 'city', 'admin', 'country'}
 max_results -> int
 callback    -> string'''

class search(AbstractBase): 
    '''Search for places that can be attached to a statuses/update. Given a 
latitude and a longitude pair, an IP address, or a name, this request will 
return a list of all the valid places that can be used as the place_id when 
updating a status. 

Conceptually, a query can be made from the user’s location, retrieve a list of 
places, have the user validate the location he or she is at, and then send the 
ID of this location with a call to POST statuses/update. 

This is the recommended method to use find places that can be attached to 
statuses/update. Unlike GET geo/reverse_geocode which provides raw data access, 
this endpoint can potentially re-order places with regards to the user who is 
authenticated. This approach is also preferred for interactive place matching 
with the user. 

Some parameters in this method are only required based on the existence of other 
parameters. For instance, “lat” is required if “long” is provided, and 
vice-versa. Authentication is recommended, but not required with this method. 

	- lat
	The latitude to search around. This parameter will be ignored unless it is 
    inside the range -90.0 to +90.0 (North is positive) inclusive. It will also 
    be ignored if there isn’t a corresponding long parameter. 

	- long
	The longitude to search around. The valid ranges for longitude is -180.0 to 
    +180.0 (East is positive) inclusive. This parameter will be ignored if 
    outside that range, if it is not a number, if geo_enabled is disabled, or if 
    there not a corresponding lat parameter. 

	- query
	Free-form text to match against while executing a geo-based query, best 
    suited for finding nearby locations by name. Remember to URL encode the 
    query. 

	- ip
	An IP address. Used when attempting to fix geolocation based off of the 
    user’s IP address. 

	- granularity
	This is the minimal granularity of place types to return and must be one of: 
    poi, neighborhood, city, admin or country. If no granularity is provided for 
    the request neighborhood is assumed. Setting this to city, for example, will 
    find places which have a type of city, admin or country. 

	- accuracy
	A hint on the “region” in which to search. If a number, then this is a 
    radius in meters, but it can also take a string that is suffixed with ft to 
    specify feet. If this is not passed in, then it is assumed to be 0m. If 
    coming from a device, in practice, this value is whatever accuracy the 
    device has measuring its location (whether it be coming from a GPS, WiFi 
    triangulation, etc.). 

	- max_results
	A hint as to the number of results to return. This does not guarantee that 
    the number of results returned will equal max_results, but instead informs 
    how many “nearby” results to return. Ideally, only pass in the number of 
    places you intend to display to the user here. 

	- contained_within
	This is the place_id which you would like to restrict the search results to. 
    Setting this value means only places within the given place_id will be 
    found. Specify a place_id. For example, to scope all results to places 
    within “San Francisco, CA USA”, you would specify a place_id of 
    “5a110d312052166f” 

    - attribute:street_address
	This parameter searches for places which have this given street address. 
    There are other well-known, and application specific attributes available. 
    Custom attributes are also permitted. Learn more about [node:208, 
    title=”Place Attributes”]. 

	- callback
	If supplied, the response will use the JSONP format with a callback of the 
    given name.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, lat=None, long=None, query=None, ip=None, 
            granularity=None, accuracy=None, max_results=None, 
            contained_within=None, street_address=None, callback=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 lat              -> -90 <= float <= 90
 long             -> -180 <= float <= 180
 query            -> string, name
 ip               -> ip address
 granularity      -> str in {'poi', 'neighborhood', 'city', 'admin', 'country'}
 accuracy         -> int, or a numeric string postfixed with 'ft'
 max_results      -> int
 contained_within -> place_id string
 street_address   -> string
 callback         -> string'''

# encapsulate namespace
geo = AbstractModule(globals())

# enforce singleton
del (id, reverse_geocode, search,
     AbstractBase, AbstractModule, Numeric, get)
