########################
theoldreader API wrapper
########################

simple python wrapper for theoldreader api
https://github.com/theoldreader/api

usage example
=============

establishing connection, getting auth_code
------------------------------------------
.. code-block:: python

    conn = theoldreader.Connection('application_name', 'email', 'password')
    print(conn.auth_code)


searching among items
---------------------
.. code-block:: python

    search = theoldreader.ItemsSearch(conn)
    unread = search.get_unread_only()
    liked = search.get_liked_only()
    shared = search.get_shared_only()
    starred = search.get_starred_only()
    
    print("unread - ",  len(unread))
    print("liked - ", len(liked))
    print("shared - ", len(shared))
    print("starred - ", len(starred))


changing status
---------------
.. code-block:: python

    for item in unread:
        item.get_details()
        if "php" in item.title.lower():
            item.mark_as_read()
            print(item.title, " - marked as read (", item.item_id, ")")
