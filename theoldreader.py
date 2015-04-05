__author__ = 'Qra'

import urllib.request
import urllib.request
import urllib.parse
import json


class TheOldReaderConnection(object):
	def __init__(self, client, email, password):
		url = 'https://theoldreader.com/accounts/ClientLogin'
		var = {
			'client': client,
			'accountType': 'HOSTED_OR_GOOGLE',
			'service': 'reader',
			'Email': email,
			'Passwd': password,
			'output': 'json'
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		resp1 = json.loads(the_page.decode("utf-8"))
		self.auth_code = resp1['Auth']
		self.header = {'Authorization': "GoogleLogin auth=" + self.auth_code}


class TheOldReaderItem(object):
	def __init__(self, header, item_id):
		self.item_id = item_id
		self.header = header
		self.title = None
		self.content = None
		self.href = None

	# Mark as read
	def mark_as_read(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'a': 'user/-/state/com.google/read',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# Mark as unread
	def mark_as_unread(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'r': 'user/-/state/com.google/read',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# Mark as starred
	def mark_as_starred(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'a': 'user/-/state/com.google/starred',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# remove_starred_mark
	def remove_starred_mark(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'r': 'user/-/state/com.google/starred',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# Mark as liked
	def mark_as_liked(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'a': 'user/-/state/com.google/like',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# remove_liked_mark
	def remove_liked_mark(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'r': 'user/-/state/com.google/like',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# Mark as shared
	def mark_as_shared(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'a': 'user/-/state/com.google/broadcast',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# Mark as shared (with_note)
	def mark_as_shared_with_note(self, note):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'a': 'user/-/state/com.google/broadcast',
			'annotation': note,
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# remove_shared_mark
	def remove_shared_mark(self):
		url = 'https://theoldreader.com/reader/api/0/edit-tag'
		var = {
			'r': 'user/-/state/com.google/broadcast',
			'i': self.item_id
		}
		data = urllib.parse.urlencode(var)
		data = data.encode('utf-8')  # data should be bytes
		req = urllib.request.Request(url, data=data, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		print(the_page)

	# get more information(title, description, link)
	def get_details(self):
		url = 'https://theoldreader.com/reader/api/0/stream/items/contents?output=json&i='
		req = urllib.request.Request(url + self.item_id, data=None, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		resp3 = json.loads(the_page.decode("utf-8"))
		item_det = resp3['items'][0]
		self.title = item_det['title']
		self.content = item_det['summary']['content']
		self.href = item_det['alternate'][0]['href']


class TheOldReaderItemsSearch(object):
	def __init__(self, header):
		self.header = header

	def get_unread_only(self):
		url = 'https://theoldreader.com/reader/api/0/stream/items/ids'
		var = {
			'output': 'json',
			's': 'user/-/state/com.google/reading-list',
			'xt': 'user/-/state/com.google/read',
			'n': 100
		}
		data = urllib.parse.urlencode(var)
		req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		resp = json.loads(the_page.decode("utf-8"))
		continuation = resp.get('continuation')
		items_list = []
		items_list = items_list + resp['itemRefs']
		while continuation is not None:
			var = {
				'output': 'json',
				's': 'user/-/state/com.google/reading-list',
				'xt': 'user/-/state/com.google/read',
				'n': 100,
				'c': continuation
			}
			data = urllib.parse.urlencode(var)
			req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
			response = urllib.request.urlopen(req)
			the_page = response.read()
			resp = json.loads(the_page.decode("utf-8"))
			continuation = resp.get('continuation')
			items_list = items_list + resp['itemRefs']
		obj_item_list = []
		for item in items_list:
			obj_item_list.append(TheOldReaderItem(self.header, item.get('id')))
		return obj_item_list

	def get_starred_only(self):
		url = 'https://theoldreader.com/reader/api/0/stream/items/ids'
		var = {
			'output': 'json',
			's': 'user/-/state/com.google/starred',
			'n': 100
		}
		data = urllib.parse.urlencode(var)
		req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		resp = json.loads(the_page.decode("utf-8"))
		continuation = resp.get('continuation')
		items_list = []
		items_list = items_list + resp['itemRefs']
		while continuation is not None:
			var = {
				'output': 'json',
				's': 'user/-/state/com.google/reading-list',
				'xt': 'user/-/state/com.google/read',
				'n': 100,
				'c': continuation
			}
			data = urllib.parse.urlencode(var)
			req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
			response = urllib.request.urlopen(req)
			the_page = response.read()
			resp = json.loads(the_page.decode("utf-8"))
			continuation = resp.get('continuation')
			items_list = items_list + resp['itemRefs']
		obj_item_list = []
		for item in items_list:
			obj_item_list.append(TheOldReaderItem(self.header, item.get('id')))
		return obj_item_list

	def get_liked_only(self):
		url = 'https://theoldreader.com/reader/api/0/stream/items/ids'
		var = {
			'output': 'json',
			's': 'user/-/state/com.google/like',
			'n': 100
		}
		data = urllib.parse.urlencode(var)
		req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		resp = json.loads(the_page.decode("utf-8"))
		continuation = resp.get('continuation')
		items_list = []
		items_list = items_list + resp['itemRefs']
		while continuation is not None:
			var = {
				'output': 'json',
				's': 'user/-/state/com.google/reading-list',
				'xt': 'user/-/state/com.google/read',
				'n': 100,
				'c': continuation
			}
			data = urllib.parse.urlencode(var)
			req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
			response = urllib.request.urlopen(req)
			the_page = response.read()
			resp = json.loads(the_page.decode("utf-8"))
			continuation = resp.get('continuation')
			items_list = items_list + resp['itemRefs']
		obj_item_list = []
		for item in items_list:
			obj_item_list.append(TheOldReaderItem(self.header, item.get('id')))
		return obj_item_list

	def get_shared_only(self):
		url = 'https://theoldreader.com/reader/api/0/stream/items/ids'
		var = {
			'output': 'json',
			's': 'user/-/state/com.google/broadcast',
			'n': 100
		}
		data = urllib.parse.urlencode(var)
		req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		resp = json.loads(the_page.decode("utf-8"))
		continuation = resp.get('continuation')
		items_list = []
		items_list = items_list + resp['itemRefs']
		while continuation is not None:
			var = {
				'output': 'json',
				's': 'user/-/state/com.google/reading-list',
				'xt': 'user/-/state/com.google/read',
				'n': 100,
				'c': continuation
			}
			data = urllib.parse.urlencode(var)
			req = urllib.request.Request(url + '?' + data, data=None, headers=self.header)
			response = urllib.request.urlopen(req)
			the_page = response.read()
			resp = json.loads(the_page.decode("utf-8"))
			continuation = resp.get('continuation')
			items_list = items_list + resp['itemRefs']
		obj_item_list = []
		for item in items_list:
			obj_item_list.append(TheOldReaderItem(self.header, item.get('id')))
		return obj_item_list