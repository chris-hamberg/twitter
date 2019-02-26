import base64, os
import pathlib

KILOBYTE = 1024
IMAGE_LIMIT = 700
BANNER_LIMIT = float('inf')

def base64encode(namespace):

    image = 'image' in namespace # Boolean flag.

    try: 
        if image: fname = namespace.pop('image')
        else: fname = namespace.pop('banner')
        validate(fname, image)
    except (KeyError, AssertionError, AttributeError) as error:
        twitter.log.error(str(error))
    else:
        with open(fname, 'rb') as fhand:
            encoded = base64.b64encode(fhand.read())
        fname = os.path.basename(fname)
        twitter.log.info('{fname} successfully encoded '
                 'to base64.'.format_map(vars()))
        return {'image': encoded} if image else {'banner': encoded}

def validate(fname, image):
    '''
    Validate the file extension, file size, and confirm that the file exists.
    '''
    valid_extensions = set({'.png', '.jpg', '.jpeg', '.gif'})
    limit = IMAGE_LIMIT if image else BANNER_LIMIT
    fname = pathlib.Path(fname)
  
    assert fname.suffix.lower() in valid_extensions, (
            'the file extension is not valid.')
    assert os.path.exists(fname), (
            '{fname} does not exist.'.format_map(vars()))
    assert (os.path.getsize(fname) / KILOBYTE) <= limit, (
            'files larger than 700 kb in size are prohibited.')

def unittest():

    ### construct the path to a test image
    fpath = os.path.dirname(__file__)
    fpath = os.sep.join(fpath.split(os.sep)[:-2])
    fpath = os.path.join(fpath, 'test', 'test_img.jpg')
    
    ### test the base64encode() process
    base64encode({'image': fpath}) # expect pass

    ### test failing cases (size test excluded due to practical limitations)
    invalid_ext = pathlib.Path(fpath).with_suffix('.pdf')
    does_not_exist = 'taco_bell.jpg'

    cases = [
        (invalid_ext, 'invalid extension'), 
        (does_not_exist, 'file does not exist')
        ]

    for case, error in cases: # expect fail
        twitter.log.info('expect an error: {error}'.format_map(vars()))
        base64encode({'image': case})

if __name__ == '__main__':
    from log import logger
    class Controller: pass
    twitter = Twitter()
    twitter.log = logger()
    unittest()
