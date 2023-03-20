# Profiles REST API

Profiles REST API course code.

## Functionalities Profile API

1. Register new profile

    * Handle registration of new users
    * Validate Profile data

2. Listing existing profiles

    * Search for profiles
    * Email and name 

3. View specific profile

    * Profile ID

4. Update profile of existing user

    * Change name, email address and password

5. Delete profile


### URLs

1. /api/profile/


    * List all profiles when HTTP GET is called
    * Create a new profile when HTTP POST is called
   
 
2. /api/profile/ID


    * View specific profile details by using HTTP GET
    * Update object using HTTP PUT / HTTP PATCH
    * Remove object using HTTP DELETE


## Functionalities Profile Feed API

1. Create a new feed item
    
    * Logged in users only

2. Update feed items
    
    * Logged in users only

3. Delete item

    * Logged in users only

4. View existing items

    * All users

### URLs

1.  /api/feed/

    
    * Root url to list all items in the feed
    * Support HTTP GET (List all)
    * Support HTTP POST (Create a new item) - for authenticated profile (logged user only )


2. /api/feed/item_id


    * Manage specific item
    * Supports HTTP GET (get specific item, Detailed View)
    * Supports HTTP PUT (update feed item)
    * Supports HTTP PATCH (update feed item)
    * Supports HTTP DELETE (delete feed item)
