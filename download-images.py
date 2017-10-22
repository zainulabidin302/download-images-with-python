import urllib.request
import threading
def getter(url):

	urllib.request.urlretrieve(url, 'imgs/'+url.split('/')[-1])
with open('links') as l:
	lis = l.readlines()
	for url in lis:
		#threading.Thread(target=getter, args=(url,)).start()
		print(url)	
		try:
		
			getter(url)
		except Exception as e:
			print(e)
