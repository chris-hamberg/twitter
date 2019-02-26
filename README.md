Welcome to the Twitter API Python Client. Before proceeding, note that Twitter 
requires OAuthorization credentials for client applications. OAuth credentials 
are provided by Twitter.com, when you register an application with your Twitter 
user account.
                 
This library is organized as a Tree; the root being twitter = Twitter(). This 
makes usage extremely easy; more on this in a bit. 

The application provides two access points. One access point, as an interactive
session, accessible from immediately outside the twitter directory as:

    ~$ python twitter

Alternatively the application provides import access from along the import path 
as:

    >>> from twitter import Twitter
    >>> twitter = Twitter()

Multi-account support is built-in using an sqlite3 database account registry. To 
switch accounts use the twitter.login() method. If accounts are registered with 
the application and no argument is provided to login, the method defaults to the 
first entry in the database. To switch between registered accounts during a 
session, the login method expects a Twitter screen name as an argument. To view 
registered screen names use the twitter.accounts property. You can manage the 
accounts registry from the cli by running:
                 
    >>> twitter.manage_accounts()

Running this command initiates a text-based user interface which will prompt for
oauth credientials, and the addition or removal of accounts from the application 
registry. (developers may want to port this feature into a more elegant 
UI experience retaining the underlying data model and controller. The prompt UI 
is located in the twitter/application/registry/prompt.py directory.)

NOTE that in this alpha early release the twitter application registration 
details are stored as plaintext in the database. That is, the secret key, etc, 
provided by Twitter.com. This could be a security issue. Future updates intend 
to rectify this potential security flaw.

It is worth noting that dependency on the application account registry can be 
bypassed altogether. That is, the Twitter class twitter.login() method has 
provides support for OAuth authorization as a Python script. This can be done by 
providing a token keyword argument to the twitter.login() method. For example:

    >>> twitter.login(token=token_obj)

The token argument is defined as an OAuth1 authorization object provided by the 
3rd party requests_oauthlib OAuth1 class. requests_oauthlib can be downloaded 
and installed from PyPI using pip.

Finally, note that either the registry must contain entries, or the login method
must be supplied with an OAuth1 authorization object. Otherwise the Twitter
server will return a 401 unauthorized error for any Twitter api requests made.

This library automatically halts rate limited requests. Rate limits are stored 
in a cache that is updated every 15 minutes. Note that the cache will refresh
only if a server request is being made after the cache expiry time. If no
outgoing requests are being made, and the cache expires, the expired cache will 
idlely wait. There is little, if any, reason to disable the rate limiting 
feature. If you must disable rate limiting, use the following command:
                 
    >>> twitter.RATE_LIMITING = False

Setting RATE_LIMITING to False notifies the application that all requests have
a rate limit of infinity, the library ignores the cache, and the cache becomes 
idle. Setting RATE_LIMITING to True completely restores default state.

As mentioned before, this library UI is organized as a Tree structure, with 
twitter = Twitter() as the root. Observe the following primary usage notes:

    >>> twitter
    displays the complete list of resource families

    >>> twitter.statuses
    displays the complete list, for the statuses resource family, of its
    endpoints

    >>> twitter.statuses.update
    displays the complete list of parameters and their expected data types, 
    for the /statuses/update endpoint

    >>> twitter.statuses.update(<parameters>)
    <Response [200]>

Positional endpoint arguments must be provided in exaclty the same order as they 
occur in the list displayed by the endpoint __repr__. 

    >>> twitter.statuses.home_timeline
     PARAMETERS
     count     -> 0 <= int <= 200
     since_id  -> int; tweet id
     max_id    -> int; tweet id
     trim_user -> true, t or 1
    .
    .
    .

    >>> twitter.statuses.home_timeline(5, 12938824, 23234999, 'true')
    <Response [200]>

endpoint methods can also take keyword arguments.

    >>> twitter.statuses.update(status='Hello Twitter!')
    <Response [200]>

As a convenience feature, the most recent response (for an endpoint) is stored 
in that endpoint. Thus,

    >>> twitter.account.settings()
    <Response [200]>
    >>> twitter.account.settings.response
    <Response [200]>

Note: recommended usage

    >>> res = twitter.statuses.update(<parameters>)
    >>> res.json()
    {'the json sent back from Twitter': 'as a Python dict'}

The authoritative Twitter api documentation for every endpoint is included with 
that endpoint in its docstring. These docs explain the behaviors associated with
the endpoint parameters, and details with respect to their data types. The 
docstrings are accessible in the standard Python convential way, by, 
for example: 

    >>> help(twitter.account.settings)

*DEPRICATED* Note (for human client application devs):
Accounts are stored in an instance of the Database class, found in the 
twitter/application/registry/model.py module. This class is a wrapper for the 
shelve module, and is an extension of which enforces the singleton design 
pattern (this is to allow simultaneous access from multiple access points 
(because there exists the case in which both the Twitter controller class, and 
the application.registry.prompt UI require simultaneous access to the unreleased 
database resource.)) The Database class consists predominately of a subset of
the standard Python dict interface, directly on the shelve file object; minor 
extensions are added to support the add() and remove() routines in the 
prompt.py module, and a polymorphic key method which is expected by the 
Twitter class. 

Database entries consists of <username>: <User class instance> 
key-value pairs. The definition of User is easily understood by reviewing the 
User class ORM data model located at the twitter/application/registry/model.py 
module. 

Ultimately, the Twitter controller class always expects a requests_oauthlib 
OAuth1 authorization object in its login method. When the database is populated,
or if a registered username is provided as an argument to login, the aquisition 
of the oauth resource and subsequent instantiation of the OAuth1 authorization 
object is typically handled directly by the login method. Calling the Twitter 
class login method stores that authorization token as a Twitter class instance 
data attribute; using that attribute value (that is, the OAuth1 authorization 
object) to authorize server resource requests, such that:
    
    import requests
    requests.get(url, headers, auth=controller.auth).

Where controller.auth is the read-only class property returning the value stored 
in the twitter._auth data attribute, which is set by the Twitter class login 
method.

You can suppress logging with the command:

    >>> twitter.log.set_level(LEVEL)
    where level is defined by the Python logging module.

To view this help document in interactive mode:
                 
    ~$ python twitter
    >>> twitter.help()
