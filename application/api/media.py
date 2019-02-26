try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.subprocess.base64encode import base64encode
    from twitter.application.api.superclass.superclasses import Media
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.subprocess.base64encode import base64encode
    from application.api.superclass.superclasses import Media
    from application.subprocess.subroutines import filter
finally:    
    from requests import post, get

# TODO
###### from application.api._media.media import multipart

class upload(Media):
    '''Use this endpoint to upload images to Twitter. It returns a media_id 
which can be used in most Twitter endpoints that accept images. For example, a 
media_id value can be used to create a Tweet with an attached photo using the 
POST statuses/update endpoint.

This is a simple image upload endpoint, with a limited set of features. The 
preferred alternative is the chunked upload endpoint which supports both images 
and videos, provides better reliability, allows resumption of file uploads, and 
other important features. In the future, new features will only be supported for 
the chunked upload endpoint.

See the Uploading media guide for constraints and requirements on media files.

Use the media metadata endpoint to provide image alt text information.

The response provides a media identifier in the media_id (64-bit integer) and 
media_id_string (string) fields. Use the media_id_string provided in the API 
response from JavaScript and other languages that cannot accurately represent a 
long integer.

The returned media_id is only valid for expires_after_secs seconds. Any attempt 
to use media_id after this time period in other endpoints will result in an HTTP 
4xx Bad Request.

The additional_owners field enables media to be uploaded media as user A and 
then used to create Tweets as user B.

Please note that for certain types of data (tweet_gif, tweet_video and 
amplify_video), you need to use the chunked upload end-point.

    - image
    The base64-encoded file content being uploaded. 

    - additional_owners
    A comma-separated list of user IDs to set as additional owners allowed to 
    use the returned media_id in Tweets or Cards. Up to 100 additional owners 
    may be specified.'''

    def __init__(self):
        super().__init__()

    def __call__(self, image=None, additional_owners=None):
        self._data = {'media_data': base64encode(
                     {'image': image}
                     )['image']}
        del image
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 image             -> abspath to jpg, gif, or png
 additional_owners -> comma separated list of user ids'''

# encapsulate namespace
media = AbstractModule(globals())

# TODO
###### setattr(media, 'multipart', multipart)

# enforce singleton
del (upload,
     Media, AbstractBase, AbstractModule, get, post)
