try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Collision
    from twitter.application.api.superclass.superclasses import Numeric
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Collision
    from application.api.superclass.superclasses import Numeric
    from application.subprocess.subroutines import filter
finally:    
    from requests import get, post

class mentions_timeline(AbstractBase):
    '''Returns the 20 most recent mentions (tweets containing a users’s 
@screen_name) for the authenticating user. 

The timeline returned is the equivalent of the one seen when you view your 
mentions on twitter.com. 

This method can only return up to 800 tweets. 

See Working with Timelines for instructions on traversing timelines. 

    - count
    Specifies the number of tweets to try and retrieve, up to a maximum of 200. 
    The value of count is best thought of as a limit to the number of tweets to 
    return because suspended or deleted content is removed after the count has 
    been applied. We include retweets in the count, even if include_rts is not 
    supplied. It is recommended you always send include_rts=1 when using this 
    API method. 

    - since_id
    Returns results with an ID greater than (that is, more recent than) the 
    specified ID. There are limits to the number of Tweets which can be accessed
    through the API. If the limit of Tweets has occured since the since_id, the 
    since_id will be forced to the oldest ID available. 

    - max_id
    Returns results with an ID less than (that is, older than) or equal to the 
    specified ID. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

    - contributor_details
    This parameter enhances the contributors element of the status response to 
    include the screen_name of the contributor. By default only the user_id of 
    the contributor is included. 

    - include_entities
    The entities node will be disincluded when set to false.'''
   
    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, count=20, since_id=None, max_id=None, trim_user=False, 
            contributor_details=False, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 count -> 0 <= int <= 200; amount of tweets to get
 since_id -> int; a twitter tweet id number
 max_id -> twitter tweet id number
 trim_user -> true, t or 1
 contributor_details -> bool
 include_entities -> bool'''

class user_timeline(AbstractBase):
    '''Returns a collection of the most recent Tweets posted by the user 
indicated by the screen_name or user_id parameters. 

User timelines belonging to protected users may only be requested when the 
authenticated user either “owns” the timeline or is an approved follower of the 
owner. 

The timeline returned is the equivalent of the one seen when you view a user’s 
profile on twitter.com. 

This method can only return up to 3,200 of a user’s most recent Tweets. Native 
retweets of other statuses by the user is included in this total, regardless of 
whether include_rts is set to false when requesting this resource. 

See Working with Timelines for instructions on traversing timelines. 

See Embeddable Timelines, Embeddable Tweets, and GET statuses/oembed for tools 
to render Tweets according to Display Requirements. 

    - user_id
    The ID of the user for whom to return results for. 

    - screen_name
    The screen name of the user for whom to return results for. 

    - since_id
    Returns results with an ID greater than (that is, more recent than) the 
    specified ID. There are limits to the number of Tweets which can be accessed 
    through the API. If the limit of Tweets has occured since the since_id, 
    the since_id will be forced to the oldest ID available. 

    - count
    Specifies the number of tweets to try and retrieve, up to a maximum of 200 
    per distinct request. The value of count is best thought of as a limit to 
    the number of tweets to return because suspended or deleted content is 
    removed after the count has been applied. We include retweets in the count, 
    even if include_rts is not supplied. It is recommended you always send 
    include_rts=1 when using this API method. 

    - max_id
    Returns results with an ID less than (that is, older than) or equal to the 
    specified ID. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

    - exclude_replies
    This parameter will prevent replies from appearing in the returned timeline. 
    Using exclude_replies with the count parameter will mean you will receive 
    up-to count tweets — this is because the count parameter retrieves that many 
    tweets before filtering out retweets and replies. This parameter is only 
    supported for JSON and XML responses. 

    - contributor_details
    This parameter enhances the contributors element of the status response to 
    include the screen_name of the contributor. By default only the user_id of 
    the contributor is included. 

    - include_rts
    When set to false, the timeline will strip any native retweets (though they 
    will still count toward both the maximal length of the timeline and the 
    slice selected by the count parameter). Note: If you’re using the trim_user 
    parameter in conjunction with include_rts, the retweets will still contain a 
    full user object.'''

    def __init__(self):
        super().__init__()
        self._method = get
    
    def __call__(self, user_id=None, screen_name=None, since_id=None, count=20, 
            max_id=None, trim_user=False, exclude_replies=False, 
            contributor_details=False, include_rts=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 user_id             -> int
 screen_name         -> str
 since_id            -> int; tweet id
 count               -> nonzero int <= 200; number of tweete
 max_id              -> int; tweet id
 trim_user           -> true, t or 1
 exclude_replies     -> bool (only supported for JSON and XML res
 contributor_details -> bool
 include_rts         -> bool'''

class home_timeline(AbstractBase):
    '''Returns a collection of the most recent Tweets and retweets posted by the 
authenticating user and the users they follow. The home timeline is central to 
how most users interact with the Twitter service. 

Up to 800 Tweets are obtainable on the home timeline. It is more volatile for 
users that follow many users or follow users who tweet frequently. 

See Working with Timelines for instructions on traversing timelines efficiently. 

    - count
    Specifies the number of records to retrieve. Must be less than or equal to 
    200. Defaults to 20. The value of count is best thought of as a limit to the 
    number of tweets to return because suspended or deleted content is removed 
    after the count has been applied. 

    - since_id
    Returns results with an ID greater than (that is, more recent than) the 
    specified ID. There are limits to the number of Tweets which can be accessed 
    through the API. If the limit of Tweets has occured since the since_id, the 
    since_id will be forced to the oldest ID available. 

    - max_id
    Returns results with an ID less than (that is, older than) or equal to the 
    specified ID. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

    - exclude_replies
    This parameter will prevent replies from appearing in the returned timeline. 
    Using exclude_replies with the count parameter will mean you will receive 
    up-to count tweets — this is because the count parameter retrieves that many 
    tweets before filtering out retweets and replies. 

    - contributor_details
    This parameter enhances the contributors element of the status response to 
    include the screen_name of the contributor. By default only the user_id of 
    the contributor is included. 

    - include_entities
    The entities node will be disincluded when set to false.'''

    def __init__(self):
        super().__init__()
        self._method = get
    
    def __call__(self, count=20, since_id=None, max_id=None, trim_user=False, 
            exclude_replies=False, contributor_details=False, 
            include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 count               -> 0 <= int <= 200
 since_id            -> int; tweet id
 max_id              -> int; tweet id
 trim_user           -> true, t or 1 
 exclude_replies     -> bool 
 contributor_details -> bool
 include_entities    -> bool'''

class retweets_of_me(AbstractBase):
    '''Returns the most recent tweets authored by the authenticating user that 
have been retweeted by others. This timeline is a subset of the user’s GET 
statuses / user_timeline. 

See Working with Timelines for instructions on traversing timelines. 

    - count
	Specifies the number of records to retrieve. Must be less than or equal to 
    100. If omitted, 20 will be assumed. 

	- since_id
	Returns results with an ID greater than (that is, more recent than) the 
    specified ID. There are limits to the number of Tweets which can be accessed 
    through the API. If the limit of Tweets has occured since the since_id, the 
    since_id will be forced to the oldest ID available. 

	- max_id
	Returns results with an ID less than (that is, older than) or equal to the 
    specified ID. 

    - trim_user
	When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

	- include_entities
	The tweet entities node will not be included when set to false. 

	- include_user_entities
	The user entities node will not be included when set to false.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, count=20, since_id=None, max_id=None, trim_user=False, 
            include_entities=False, include_user_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 count                 -> 0 <= int <= 100
 since_id              -> int; tweet id
 max_id                -> int; tweet id
 trim_user             -> true, t or 1 
 include_entities      -> bool
 include_user_entities -> bool'''
   
class retweets(Numeric): 
    '''Returns a collection of the 100 most recent retweets of the tweet 
specified by the id parameter. 

    - id
    The numerical ID of the desired status. 

	- count
	Specifies the number of records to retrieve. Must be less than or equal to 
    100. 

	- trim_user
	When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object.'''
   
    def __init__(self):
        suffix = 's/{id}.json'
        super().__init__(suffix)
        self._method = get
        self._endpoint += '/:id'
    
    def __call__(self, id=None, count=20, trim_user=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 id -> int; tweet id
 count -> 0 <= int <= 100
 trim_user -> true, t or 1'''

class show(AbstractBase): 
    '''Returns a single Tweet, specified by the id parameter. The Tweet’s author 
will also be embedded within the tweet. 

See GET statuses / lookup for getting Tweets in bulk (up to 100 per call). See 
also Embeddable Timelines, Embeddable Tweets, and GET statuses/oembed for tools 
to render Tweets according to Display Requirements. 

                                     About Geo 

        If there is no geotag for a status, then there will be an empty <geo/> 
        or "geo" : {}. This can only be populated if the user has used the 
        Geotagging API to send a statuses/update. 

        The JSON response mostly uses conventions laid out in GeoJSON. 
        Unfortunately, the coordinates that Twitter renders are reversed from 
        the GeoJSON specification (GeoJSON specifies a longitude then a 
        latitude, whereas we are currently representing it as a latitude then a 
        longitude). Our JSON renders as: 
		            
            "geo": { "type":"Point", "coordinates":[37.78029, -122.39697] } 

                                    Contributors 

        If there are no contributors for a Tweet, then there will be an empty or 
        "contributors" : {}. This field will only be populated if the user has 
        contributors enabled on his or her account — this is a beta feature that 
        is not yet generally available to all. 

        This object contains an array of user IDs for users who have contributed 
        to this status (an example of a status that has been contributed to is 
        this one). In practice, there is usually only one ID in this array. The 
        JSON renders as such "contributors":[8285392]. 

    - id
    The numerical ID of the desired Tweet. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

    - include_my_retweet
    When set to either true, t or 1, any Tweets returned that have been 
    retweeted by the authenticating user will include an additional 
    current_user_retweet node, containing the ID of the source status for the 
    retweet. 

    - include_entities
    The entities node will be disincluded when set to false.'''
   
    def __init__(self):
        super().__init__()
        self._method = get
        self._endpoint += '/:id'
    
    def __call__(self, id=None, trim_user=False, include_my_retweet=False, 
			include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 id                 -> int; tweet id
 trim_user          -> true, t or 1 
 include_my_retweet -> true, t or 1 
 include_entities   -> bool'''

class destroy(AbstractBase):
    '''Destroys the status specified by the required ID parameter. The 
authenticating user must be the author of the specified status. Returns the 
destroyed status if successful. 

    - id
    The numerical ID of the desired status. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object.'''

    def __init__(self):
        super().__init__()
        self._method = post
        self._endpoint = None
    
    def __call__(self, id=None, trim_user=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 id -> int; tweet id
 trim_user -> true, t or 1'''

class update(AbstractBase):
    '''Updates the authenticating user’s current status, also known as Tweeting. 

For each update attempt, the update text is compared with the authenticating 
user’s recent Tweets. Any attempt that would result in duplication will be 
blocked, resulting in a 403 error. Therefore, a user cannot submit the same 
status twice in a row. 

While not rate limited by the API a user is limited in the number of Tweets they 
can create at a time. If the number of updates posted by the user reaches the 
current allowed limit this method will return an HTTP 403 error. 

                                    About Geo 

        Any geo-tagging parameters in the update will be ignored if geo_enabled 
        for the user is false (this is the default setting for all users unless 
        the user has enabled geolocation in their settings) 

	    The number of digits passed the decimal separator passed to lat, up to 
        8, will be tracked so that the lat is returned in a status object it 
        will have the same number of digits after the decimal separator. 

	    Please make sure to use to use a decimal point as the separator (and not 
        the decimal comma) for the latitude and the longitude - usage of the 
        decimal comma will cause the geo-tagged portion of the status update to 
        be dropped. 

	    For JSON, the response mostly uses conventions described in GeoJSON. 
        Unfortunately, the geo object has coordinates that Twitter renderers are 
        reversed from the GeoJSON specification (GeoJSON specifies a longitude 
        then a latitude, whereas we are currently representing it as a latitude 
        then a longitude. Our JSON renders as: 
        
            "geo": { "type":"Point", "coordinates":[37.78217, -122.40062] } 

	    The coordinates object is replacing the geo object (no deprecation date 
        has been set for the geo object yet) — the difference is that the 
        coordinates object, in JSON, is now rendered correctly in GeoJSON. 

	    If a place_id is passed into the status update, then that place will be 
        attached to the status. If no place_id was explicitly provided, but 
        latitude and longitude are, we attempt to implicitly provide a place by 
        calling geo/reverse_geocode. 

	    Users will have the ability, from their settings page, to remove all the 
        geotags from all their tweets en masse. Currently we are not doing any 
        automatic scrubbing nor providing a method to remove geotags from 
        individual tweets. 

    - status
    The text of your status update, typically up to 140 characters. URL encode 
    as necessary. t.co link wrapping may affect character counts. There are some 
    special commands in this field to be aware of. For instance, preceding a 
    message with “D ” or “M ” and following it with a screen name can create a 
    direct message to that user if the relationship allows for it. 

    - in_reply_to_status_id
    The ID of an existing status that the update is in reply to. Note: this 
    parameter will be ignored unless the author of the tweet this parameter 
    references is mentioned within the status text. Therefore, you must include 
    @username, where username is the author of the referenced tweet, within the 
    update. 

    - possibly_sensitive
    If you upload Tweet media that might be considered sensitive content such as 
    nudity, violence, or medical procedures, you should set this value to true. 
    See Media setting and best practices for more context. Defaults to false. 

    - lat
    The latitude of the location this tweet refers to. This parameter will be 
    ignored unless it is inside the range -90.0 to +90.0 (North is positive) 
    inclusive. It will also be ignored if there isn’t a corresponding long 
    parameter. 

    - long
    The longitude of the location this tweet refers to. The valid ranges for 
    longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter 
    will be ignored if outside that range, if it is not a number, if geo_enabled 
    is disabled, or if there not a corresponding lat parameter. 

    - place_id
    A place in the world. 

    - display_coordinates
    Whether or not to put a pin on the exact coordinates a tweet has been sent 
    from. 

    - trim_user
	When set to either true, t or 1, each Tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

    - media_ids
    A list of media_ids to associate with the Tweet. You may include up to 4 
    photos or 1 animated GIF or 1 video in a Tweet. See Uploading Media for 
    further details on uploading media.'''

    def __init__(self):
        super().__init__()
        self._method = post
        self._endpoint = None
    
    def __call__(self, status=None, in_reply_to_status_id=None, 
            possibly_sensitive=False, lat=None, long=None, place_id=None,
            display_coordinates=False, trim_user=False, media_ids=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 status                    -> text of your status update, max 140 char
 in_reply_to_status_id     -> int, user ID; must include @username in the update
 possibly_sensitive        -> bool
 lat                       -> range -90.0 to +90.0 (North is +); must include 
                              long param
 long                      -> range -180.0 to +180.0 (East is +); geo_enabled 
                              must be enabled
 place_id                  -> str
 display_coordinates       -> bool
 trim_user                 -> true, t or 1 
 media_ids                 -> list of media_ids; see Uploading Media'''

class retweet(Numeric):
    '''Retweets a tweet. Returns the original tweet with retweet details 
embedded. 

                                   Usage Notes: 

        This method is subject to update limits. A HTTP 403 will be returned if 
        this limit as been hit. 

        Twitter will ignore attempts to perform duplicate retweets. 

        The retweet_count will be current as of when the payload is generated 
        and may not reflect the exact count. It is intended as an approximation. 

    - id
    The numerical ID of the desired status. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object.'''
   
    def __init__(self):
        super().__init__()
        self._endpoint = None
    
    def __call__(self, id=None, trim_user=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 id        -> int; tweet id
 trim_user -> true, t or 1'''

class unretweet(Numeric): 
    '''Untweets a retweeted status. Returns the original Tweet with retweet 
details embedded. 

                        		Usage Notes: 

        This method is subject to update limits. A HTTP 429 will be returned if 
        this limit has been hit. 

        The untweeted retweet status ID must be authored by the user backing the 
        authentication token. 

        An application must have write privileges to POST. A HTTP 401 will be 
        returned for read-only applications. 

        When passing a source status ID instead of the retweet status ID a HTTP 
        200 response will be returned with the same Tweet object but no action. 

    - id
    The numerical ID of the desired retweet status. 

    - trim_user
    When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object.'''
   
    def __init__(self):
        super().__init__()
        self._endpoint = None
    
    def __call__(self, id=None, trim_user=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 id        -> int; tweet id
 trim_user -> true, t or 1'''

class oembed(AbstractBase):
    '''Returns a single Tweet, specified by a Tweet web URL, in an 
oEmbed-compatible format. The returned HTML snippet will be automatically 
recognized as an embedded Tweet when Twitter’s widget JavaScript is included on 
the page. 

The oEmbed endpoint allows customization of the final appearance of an Embedded 
Tweet by setting the corresponding properties in HTML markup to be interpreted 
by Twitter’s JavaScript bundled with the HTML response by default. The format of 
the returned markup may change over time as Twitter adds new features or adjusts 
its Tweet representation. 

The Tweet fallback markup is meant to be cached on your servers for up to the 
suggested cache lifetime specified in the cache_age. 

    - url
    The URL of the Tweet to be embedded. Example: 
        https://twitter.com/Interior/status/507185938620219395

    - maxwidth
    The maximum width of a rendered Tweet in whole pixels. This value must be 
    between 220 and 550 inclusive. A supplied value under or over the allowed 
    range will be returned as the minimum or maximum supported width 
    respectively; the reset width value will be reflected in the returned width 
    property. Note that Twitter does not support the oEmbed maxheight parameter. 
    Tweets are fundamentally text, and are therefore of unpredictable height 
    that cannot be scaled like an image or video. Relatedly, the oEmbed response 
    will not provide a value for height. Implementations that need consistent 
    heights for Tweets should refer to the hide_thread and hide_media parameters 
    below. 

    - hide_media
    When set to true, t or 1 links in a Tweet are not expanded to photo, video, 
    or link previews. 

    - hide_thread
    When set to true, t or 1 a collapsed version of the previous Tweet in a 
    conversation thread will not be displayed when the requested Tweet is in 
    reply to another Tweet. 

    - omit_script
    When set to true, t or 1 the <script> responsible for loading widgets.js 
    will not be returned. Your webpages should include their own reference to 
    widgets.js for use across all Twitter widgets including Embedded Tweets. 

    - align
    Specifies whether the embedded Tweet should be floated left, right, or 
    center in the page relative to the parent element. Valid values are left, 
    right, center, and none. Defaults to none, meaning no alignment styles are 
    specified for the Tweet. 

    - related
    A comma-separated list of Twitter usernames related to your content. This 
    value will be forwarded to Tweet action intents if a viewer chooses to 
    reply, favorite, or retweet the embedded Tweet. 
			
    - lang
    Request returned HTML and a rendered Tweet in the specified Twitter language 
    supported by embedded Tweets. 

    - widget_type
    Set to video to return a Twitter Video embed for the given Tweet. 

    - hide_tweet
    Applies to video type only. Set to 1 or true to link directly to the Tweet 
    URL instead of displaying a Tweet overlay when a viewer clicks on the 
    Twitter bird logo.'''

    def __init__(self):
        super().__init__()
        self._method = get
        self._url = 'https://publish.twitter.com/oembed'
        self._endpoint = '/statuses/oembed'
    
    def __call__(self, url=None, maxwidth=None, hide_media=False,
            hide_thread=False, omit_script=False, align=None, related=None, 
            lang=None, widget_type=None, hide_tweet=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 url         -> The URL of the Tweet to be embedded
 maxwidth    -> int in range (220, 550) inclusive 
 hide_media  -> true, t or 1 
 hide_thread -> true, t or 1 
 omit_script -> true, t or 1
 align       -> 'left', 'right', 'center', or 'none'
 related     -> csv list of usernames related to the content
 lang        -> specified Twitter language supported by embedded Tweets.
 widget_type -> 'video' 
 hide_tweet  -> 1 or true; Applies to video type only'''

class retweeters(AbstractBase):
    '''Returns a collection of up to 100 user IDs belonging to users who have 
retweeted the tweet specified by the id parameter. 

This method offers similar data to GET statuses / retweets / :id. 

    - id
    The numerical ID of the desired status. 

    - cursor
    Causes the list of IDs to be broken into pages of no more than 100 IDs at a 
    time. The number of IDs returned is not guaranteed to be 100 as suspended 
    users are filtered out after connections are queried. If no cursor is 
    provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See our cursor docs for more information. While 
    this method supports the cursor parameter, the entire result set can be 
    returned in a single cursored collection. Using the count parameter with 
    this method will not provide segmented cursors for use with this parameter. 

    - stringify_ids
    Many programming environments will not consume our ids due to their size. 
    Provide this option to have ids returned as strings instead.'''

    def __init__(self):
        super().__init__()
        self._method = get
        self._url = self._url.rstrip('.json') + 's/ids.json'
        self._endpoint += '/ids'
    
    def __call__(self, id=None, cursor=-1, stringify_ids=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 id            -> int; tweet id
 cursor        -> int
 stringify_ids -> bool'''

class lookup(AbstractBase):
    '''Returns fully-hydrated tweet objects for up to 100 tweets per request, as 
specified by comma-separated values passed to the id parameter. 

This method is especially useful to get the details (hydrate) a collection of 
Tweet IDs. 

GET statuses / show / :id is used to retrieve a single tweet object. 

There are a few things to note when using this method. 

        You must be following a protected user to be able to see their most 
        recent tweets. If you don’t follow a protected user their status will be 
        removed. 

		The order of tweet IDs may not match the order of tweets in the returned 
        array. 

		If a requested tweet is unknown or deleted, then that tweet will not be 
        returned in the results list, unless the map parameter is set to true, 
        in which case it will be returned with a value of null. 

		If none of your lookup criteria matches valid tweet IDs an empty array 
        will be returned for map=false. 

		You are strongly encouraged to use a POST for larger requests. 

	- id
	A comma separated list of tweet IDs, up to 100 are allowed in a single 
    request. 

	- include_entities
	The entities node that may appear within embedded statuses will be 
    disincluded when set to false. 

	- trim_user
	When set to either true, t or 1, each tweet returned in a timeline will 
    include a user object including only the status authors numerical ID. Omit 
    this parameter to receive the complete user object. 

	- map
	When using the map parameter, tweets that do not exist or cannot be viewed 
    by the current user will still have their key represented but with an 
    explicitly null value paired with it'''

    def __init__(self):
        super().__init__()
        self._method = get
    
    def __call__(self, id=None, include_entities=False, trim_user=False, 
            map=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' 
	id -> csv list of tweet IDs; max 100 entries 
	include_entities -> bool
	trim_user -> true, t or 1  
	map -> bool'''

# encapsulate namespace
statuses = AbstractModule(globals())

# enforce singleton
del (mentions_timeline, user_timeline, home_timeline, retweets_of_me, retweets, 
     show, destroy, update, retweet, unretweet, oembed, retweeters, lookup,
     
     AbstractBase, AbstractModule, Numeric,
     get, post)
