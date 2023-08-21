import requests
class Client():
	def __init__(self):
		self.api="http://archive.org/wayback"
	def url_timestamp(self,url:str,time:str):
		return requests.get(f"{self.api}/available?url={url}&timestamp={time}").json()
	def available_url(self,url:str):
		return requests.get(f"{self.api}/available?url={url}").json()