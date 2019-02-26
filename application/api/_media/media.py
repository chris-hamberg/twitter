#from application.api.superclass.abstract_base_class import AbstractBase
#from application.api.superclass.abstract_module import AbstractModule
from application.subprocess.base64encode import base64encode
from application.api.superclass.superclasses import Media
from application.subprocess.subroutines import filter
from requests import post, get
from math import ceil
import mimetypes, os

class INIT(Media):
    '''The INIT command request is used to initiate a file upload session. It 
returns a media_id which should be used to execute all subsequent requests. The 
next step after a successful return from INIT command is the APPEND command.

See the Uploading media guide for constraints and requirements on media files.

Requests should be either multipart/form-data or 
application/x-www-form-urlencoded POST formats.

    - total_bytes
    The size of the media being uploaded in bytes.

    - media_type
    The MIME type of the media being uploaded.

    - media_category
    A string enum value which identifies a media usecase. This identifier is 
    used to enforce usecase specific constraints (e.g. file size, video 
    duration) and enable advanced features.

    - additional_owners
    A comma-separated list of user IDs to set as additional owners allowed to 
    use the returned media_id in Tweets or Cards. Up to 100 additional owners 
    may be specified.'''

    def __init__(self):
        super().__init__()

    def __call__(self, total_bytes=None, media_type=None, media_category=None, 
            additional_owners=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 total_bytes       -> int
 media_type        -> string; MIME type
 media_category    -> str in {'dm_image', 'dm_gif', 'dm_video', None}
 additional_owners -> comma-separated list of user IDs'''

class APPEND(Media):
    '''The APPEND command is used to upload a chunk (consecutive byte range) of 
the media file. For example, a 3 MB file could be split into 3 chunks of size 1 
MB, and uploaded using 3 APPEND command requests. After the entire file is 
uploaded, the next step is to call the FINALIZE command.

    - media_id
    The media_id returned from the INIT command.

    - media	
    The raw binary file content being uploaded. It must be <= 5 MB, and cannot 
    be used with media_data.	 	 

    - media_data
    The base64-encoded chunk of media file. It must be <= 5 MB and cannot be 
    used with media. Use raw binary (media parameter) when possible.	 	 

    - segment_index
    An ordered index of file chunk. It must be between 0-999 inclusive. The 
    first segment has index 0, second segment has index 1, and so on.'''

    def __init__(self):
        super().__init__()

    def __call__(self, media_id=None, media=None, media_data=None, 
            segment_index=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 media_id -> returned by INIT
 media -> raw binary <= 5MB
 media_data -> base64 <= 5MB
 segment_index -> zero-basaed index for file chunk'''

class STATUS(Media):
    '''The STATUS command is used to periodically poll for updates of media 
processing operation. After the STATUS command response returns succeeded, you 
can move on to the next step which is usually create Tweet with media_id.

The response body contains processing_info field which provides information 
about current state of media processing operation. It contains a state field 
which has transition flow: “pending” -> “in_progress” -> [“failed” | 
“succeeded”]. You can not use the media_id to create Tweet or other entities 
before the state field is set to “succeeded”.

    - media_id
    The media_id returned from the INIT command.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, media_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 media_id -> returned by INIT'''

class FINALIZE(Media):
    '''The FINALIZE command should be called after the entire media file is 
uploaded using APPEND commands. If and (only if) the response of the FINALIZE 
command contains a processing_info field, it may also be necessary to use a 
STATUS command and wait for it to return success before proceeding to Tweet 
creation.
    
The response provides a media identifier in the media_id (64-bit integer) and 
media_id_string (string) fields. Use the media_id_string provided in the API 
response from JavaScript and other languages that cannot accurately represent a 
long integer.

The returned mediaId is only valid for expires_after_secs seconds. Any attempt 
to use mediaId after this time period in other API calls will result in a Bad 
Request (HTTP 4xx) response.

If the response contains a processing_info field, then use the STATUS command to 
poll for the status of the FINALIZE operation. The async finalize approach is 
used for cases where media processing requires more time. In future, all video 
and animated GIF processing will only be supported using async finalize. This 
behavior is enabled if an upload session was initialized with a media_category 
parameter, and when then media type is either video or animated GIF.

If a processing_info field is NOT returned in the response, then media_id is 
ready for use in other API endpoints.    

    - media_id
    The media_id returned from the INIT command.'''

    def __init__(self):
        super().__init__()

    def __call__(self, media_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 media_id -> returned by INIT'''

def multipart(fpath, media_category=None):

    init     = INIT()
    append   = APPEND()
    finalize = FINALIZE()

    b64 = base64encode({'image': fpath})['image']
    size = 100000

    mimetype         = mimetypes.guess_type(fpath)[0]
    byte_count       = len(open(fpath, 'rb').read())
    character_count  = len(b64)
    number_of_chunks = ceil(character_count/size)
    
    chunks = [
             b64[index*size: (index*size)+size] 
             for index in range(number_of_chunks
             )]

    init(total_bytes=byte_count, 
                    media_type=mimetype, 
                    media_category=media_category)
    
    media_id = init.response.json()['media_id']

    for e, chunk in enumerate(chunks):
        append._data = {'media_data': chunk}
        append(media_id, segment_index=e)
    
    finalize(media_id)

    return media_id
