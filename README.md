# theoldreader API wrapper 

simple python wrapper for theoldreader api
https://github.com/theoldreader/api



## usage example


#### establishing connection, getting auth_code

```Python
conn = theoldreader.Connection('email', 'password', 'application_name')
conn.login()
print(conn.auth_code)
```

or
```Python
conn = theoldreader.Connection('email', 'password', 'application_name')
```
and just go ahead and use it. It will try to login when before making a request


#### searching among items

```Python
search = theoldreader.ItemsSearch(conn)
unread = search.get_unread_only()
liked = search.get_liked_only()
shared = search.get_shared_only()
starred = search.get_starred_only()

print(u"unread - {}".format(len(unread)))
print(u"liked - {}".format(len(liked)))
print(u"shared - {}".format(len(shared)))
print(u"starred - {}".format(len(starred)))
```


#### changing status

```Python

for item in unread:
	item.get_details()
	if "php" in item.title.lower():
		item.mark_as_read()
		print(u"{} - marked as read ({})".format(item.title, item.item_id))
```
