try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Empty
    from twitter.application.api.superclass.superclasses import Base64
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Empty
    from application.api.superclass.superclasses import Base64
    from application.subprocess.subroutines import filter
finally:
    from requests import get, post

class settings(Empty): 
    '''Returns settings (including current trend, geo and sleep time 
information) for the authenticating user.'''

    def __init__(self):
        super().__init__()
        self._method = get

class verify_credentials(AbstractBase):
    '''Returns an HTTP 200 OK response code and a representation of the 
requesting user if authentication was successful; returns a 401 status code and 
an error message if not. Use this method to test if supplied user credentials 
are valid. 

Requesting a user’s email address requires your application to be whitelisted by 
Twitter. To request access, please use this form. Once whitelisted, the “Request 
email addresses from users” checkbox will be available under your app 
permissions on apps.twitter.com. Privacy Policy URL and Terms of Service URL 
fields will also be available under settings which are required for email 
access. If enabled, users will be informed via the oauth/authorize dialog that 
your app can access their email address.  

    - include_entities
    The entities node will not be included when set to false. 

    - skip_status
    When set to either true, t or 1 statuses will not be included in the 
    returned user object. 

    - include_email
    Use of this parameter requires whitelisting. When set to true email will be 
    returned in the user objects as a string. If the user does not have an email 
    address on their account, or if the email address is un-verified, null will 
    be returned.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, include_email=False, include_entities=False, 
            skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 include_entities -> bool
 skip_status      -> bool
 include_email    -> bool'''

class update_settings(AbstractBase): 
    '''Updates the authenticating user’s settings. 

    - sleep_time_enabled
	When set to true, t or 1, will enable sleep time for the user. Sleep time is 
    the time when push or SMS notifications should not be sent to the user. 

    - start_sleep_time
    The hour that sleep time should begin if it is enabled. The value for this 
    parameter should be provided in ISO8601 format (i.e. 00-23). The time is 
    considered to be in the same timezone as the user’s time_zone setting. 

    - end_sleep_time
    The hour that sleep time should end if it is enabled. The value for this 
    parameter should be provided in ISO8601 format (i.e. 00-23). The time is 
    considered to be in the same timezone as the user’s time_zone setting. 

    - time_zone
    The timezone dates and times should be displayed in for the user. The 
    timezone must be one of the Rails TimeZone names. 

    - trend_location_woeid
    The Yahoo! Where On Earth ID to use as the user’s default trend location. 
    Global information is available by using 1 as the WOEID. The woeid must be 
    one of the locations returned by [node:59]. 

    - allow_contributor_request
    Whether to allow others to include user as contributor. Possible values 
    include “all” (anyone can include user), “following” (only followers can 
    include user) or “none”. Also note that changes to this field require the 
    request also include a “current_password” value with the user’s password to 
    successfully modify this field. 

    - lang
    The language which Twitter should render in for this user. The language must 
    be specified by the appropriate two letter ISO 639-1 representation. 
    Currently supported languages are provided by this endpoint.'''

    def __init__(self):
        super().__init__()
        self._url = 'https://api.twitter.com/1.1/account/settings.json'
        self._method = post
        self._endpoint = None
   
    def __call__(self, sleep_time_enabled=False, start_sleep_time=None,
            end_sleep_time=None, time_zone=None, trend_location_woeid=None, 
            allow_contributor_request=None, lang=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 sleep_time_enabled        -> bool
 start_sleep_time          -> 00 <= int <= 23; *see time_zone
 end_sleep_time            -> 00 <= int <= 23; *see time_zone
 time_zone                 -> Rails TimeZone name
 trend_location_woeid      -> positive int
 allow_contributor_request -> str: ['all', 'following', 'none']; requires passwd
 lang                      -> 2-chr ISO 639-1 representation'''

class update_profile(AbstractBase):
    '''Sets some values that users are able to set under the “Account” tab of 
their settings page. Only the parameters specified will be updated. 

    - name
    Full name associated with the profile. Maximum of 20 characters. 

    - url
    URL associated with the profile. Will be prepended with “http://” if not 
    present. Maximum of 100 characters. 

    - location
    The city or country describing where the user of the account is located. The 
    contents are not normalized or geocoded in any way. Maximum of 30 
    characters. 

    - description
    A description of the user owning the account. Maximum of 160 characters. 

    - profile_link_color
    Sets a hex value that controls the color scheme of links used on the 
    authenticating user’s profile page on twitter.com. This must be a valid 
    hexadecimal value, and may be either three or six characters (ex: F00 or 
    FF0000). This parameter replaces the deprecated (and separate) 
    update_profile_colors API method. 

    - include_entities
    The entities node will not be included when set to false. 

    - skip_status
    When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, name=None, url=None, location=None, description=None, 
            profile_link_color=None, include_entities=False, skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 name               -> max 20 chars
 url                -> prepends http:// if not present. max 100 chars 
 location           -> city or country; content not normalized nor geocoded
                       max 30 chars 
 description        -> of user; max 160 chars
 profile_link_color -> hex; three or six chars 
 include_entities   -> bool
 skip_status        -> true, t or 1'''

class update_profile_image(Base64):
    '''Updates the authenticating user’s profile image. Note that this method 
expects raw multipart data, not a URL to an image. 

This method asynchronously processes the uploaded file before updating the 
user’s profile image URL. You can either update your local cache the next time 
you request the user’s information, or, at least 5 seconds after uploading the 
image, ask for the updated URL using GET users / show. 

    - image
    The avatar image for the profile, base64-encoded. Must be a valid GIF, JPG, 
    or PNG image of less than 700 kilobytes in size. Images with width larger 
    than 400 pixels will be scaled down. Animated GIFs will be converted to a 
    static GIF of the first frame, removing the animation. 

    - include_entities
    The entities node will not be included when set to false. 

    - skip_status
    When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._key = 'image'

    def __call__(self, image=None, include_entities=False, skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 image            -> abspath to img; GIF, JPG, or PNG < 700 kb
 include_entities -> bool
 skip_status      -> true, t or 1'''

class remove_profile_banner(AbstractBase):
    '''Removes the uploaded profile banner for the authenticating user. Returns 
HTTP 200 upon success.'''

    def __init__(self):
        super().__init__()
        self._method = post
        self._endpoint = None

class update_profile_banner(Base64):
    '''Uploads a profile banner on behalf of the authenticating user. More 
information about sizing variations can be found in User Profile Images and 
Banners and GET users / profile_banner.

Profile banner images are processed asynchronously. The profile_banner_url and 
its variant sizes will not necessary be available directly after upload.
        
    - banner
    The Base64-encoded or raw image data being uploaded as the user’s new 
    profile banner.
            
    - width
    The width of the preferred section of the image being uploaded in pixels. 
    Use with height, offset_left, and offset_top to select the desired region of 
    the image to use.
            
    - height
    The height of the preferred section of the image being uploaded in pixels. 
    Use with width, offset_left, and offset_top to select the desired region of 
    the image to use.
            
    - offset_left
    The number of pixels by which to offset the uploaded image from the left. 
    Use with height, width, and offset_top to select the desired region of the 
    image to use.
            
    - offset_top
    The number of pixels by which to offset the uploaded image from the top. Use 
    with height, width, and offset_left to select the desired region of the 
    image to use.'''

    def __init__(self):
        super().__init__()
        self._key = 'banner'

    def __call__(self, banner=None, width=None, height=None, offset_left=None,
            offset_top=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return ''' PARAMETERS
 banner      -> image file abspath/location
 width       -> pos int; width of preferred section of the img, in pixels
 height      -> height of the preferred section.
 offset_left -> num of px by which to offset the image from the left
 offset_top  -> num px to offset the uploaded image from the top.'''

# encapsulate namespace
account = AbstractModule(globals())

# enforce singleton
del (settings, verify_credentials, update_settings,
     update_profile, update_profile_image, remove_profile_banner,
     update_profile_banner,
     
     AbstractBase, AbstractModule, Empty, 
     Base64, get, post)
