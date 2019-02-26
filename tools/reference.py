#NOTE commented means either completed or precluded
##### preclusion is either mentioned in the todo.txt
##### or not intended to be implemented for reasons
##### ex. it might be a paid for endpoint

#GET account/settings 
#GET account/verify_credentials 
#POST account/remove_profile_banner 
#POST account/settings 
#POST account/update_profile 
#POST account/update_profile_banner 
#POST account/update_profile_image 

#GET blocks/ids 
#GET blocks/list 
#POST blocks/create 
#POST blocks/destroy 

#GET collections/entries 
#GET collections/list 
#GET collections/show 
#POST collections/create 
#POST collections/destroy 
#POST collections/entries/add 
#POST collections/entries/curate 
#POST collections/entries/move 
#POST collections/entries/remove 
#POST collections/update 

#GET compliance/firehose 

#DELETE custom_profiles/destroy.json 
#GET custom_profiles/:id 
#GET custom_profiles/list 
#POST custom_profiles/new.json 

#DELETE direct_messages/events/destroy 
#GET direct_messages/events/list 
#GET direct_messages/events/show 
#POST direct_messages/events/new (message_create) 
#POST direct_messages/indicate_typing 
#POST direct_messages/mark_read 

#TODO super confusing, need to work on these
#DELETE direct_messages/welcome_messages/destroy 
#GET direct_messages/welcome_messages/show 
#POST direct_messages/welcome_messages/new 
#PUT direct_messages/welcome_messages/update 
#GET direct_messages/welcome_messages/list 

DELETE direct_messages/welcome_messages/rules/destroy 
GET direct_messages/welcome_messages/rules/list 
GET direct_messages/welcome_messages/rules/show 
POST direct_messages/welcome_messages/rules/new 

#GET favorites/list 
#POST favorites/destroy 
#POST favorites/create 

#GET feedback/events.json 
#GET feedback/show/:id.json 
#POST feedback/create.json 

#GET followers/ids 
#GET followers/list 

#GET friends/ids 
#GET friends/list 

#GET friendships/incoming 
#GET friendships/lookup 
#GET friendships/no_retweets/ids 
#GET friendships/outgoing 
#GET friendships/show 
#POST friendships/create 
#POST friendships/destroy 
#POST friendships/update 

#GET geo/id/:place_id 
#GET geo/reverse_geocode 
#GET geo/search

#GET lists/list 
#GET lists/members 
#GET lists/memberships 
#GET lists/ownerships 
#GET lists/show 
#GET lists/statuses 
#GET lists/subscribers 
#GET lists/subscriptions 
#POST lists/create 
#POST lists/destroy 
#POST lists/update 

#GET lists/members/show 
#POST lists/members/create 
#POST lists/members/create_all 
#POST lists/members/destroy 
#POST lists/members/destroy_all 

#POST lists/subscribers/create 
#POST lists/subscribers/destroy 
#GET lists/subscribers/show 

GET media/upload (STATUS) 
POST media/metadata/create 
POST media/upload 
POST media/upload (APPEND) 
POST media/upload (FINALIZE) 
POST media/upload (INIT) 

#POST mutes/users/create 
#POST mutes/users/destroy 
#GET mutes/users/ids 
#GET mutes/users/list 

#GET oauth/authenticate 
#GET oauth/authorize 
#POST oauth/access_token 
#POST oauth/request_token 
#POST oauth2/invalidate_token 
#POST oauth2/token 

#POST saved_searches/create 
#POST saved_searches/destroy/:id 
#GET saved_searches/list 
#GET saved_searches/show/:id 

#POST statuses/filter 
#GET statuses/home_timeline 
#GET statuses/mentions_timeline 
#GET statuses/user_timeline 
#GET statuses/lookup 
#GET statuses/oembed 
#GET statuses/retweeters/ids 
#GET statuses/retweets/:id 
#GET statuses/retweets_of_me 
#GET statuses/show/:id 
#POST statuses/destroy/:id 
#POST statuses/retweet/:id 
#POST statuses/unretweet/:id 
#POST statuses/update 
#GET statuses/sample 

#GET trends/available 
#GET trends/closest 
#GET trends/place 

#GET users/lookup 
#GET users/search 
#GET users/show 
#GET users/suggestions 
#GET users/suggestions/:slug 
#GET users/suggestions/:slug/members 
#GET users/profile_banner 
#POST users/report_spam 
