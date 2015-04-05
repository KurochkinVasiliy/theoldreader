# theoldreader API wrapper 

simple python wrapper for theoldreader api
https://github.com/theoldreader/api

## usage example

#### establishing connection, getting auth_code
conn = TheOldReaderConnection('application_name', 'email', 'password')
print(conn.auth_code)

#### searching among items

search = theoldreader.TheOldReaderItemsSearch(conn.header)
unread = search.get_unread_only()
liked = search.get_liked_only()
shared = search.get_shared_only()
starred = search.get_starred_only()

print("unread - ", unread.__len__())
print("liked - ", liked.__len__())
print("shared - ", shared.__len__())
print("starred - ", starred.__len__())


#### changing status
clean_up_list = liked + starred + shared


for item in unread:
	item.get_details()
	if "php" in item.title.lower():
		item.mark_as_read()
		print(item.title, " - marked as read (", item.item_id, ")")
