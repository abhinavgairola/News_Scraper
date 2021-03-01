import re
import requests
from bs4 import BeautifulSoup
import os
import datetime
import json

class NewsExtractor:
	""" 
	A class with associated functions to scrape the abc news website. 
	It will generate folders for each day and parse the news and their urls in a json file.
	"""
	def __init__(self):#, *args):
		#n1, n2 = args
		self.url_1 = None
		self.url_2 = None
	
	def print_(self):
		print(self.url_1)

	def requests_1(self,url):
		content = requests.get(url)
		soup = BeautifulSoup(content.text,'html.parser')
		if content.status_code == 200:
			links=(soup.findAll('a'))
			extracted_links = [li.get('href') for li in links]
		return extracted_links,soup

	def print_url(self,url_):
		extracts, Soup= self.requests_1(url_)

		Links = []
		for links in extracts:
			if 'https:'in links:

				Links.append(links)
		Links = self.link_separator(Links)
		return Links

	def link_separator(self, Links_):
		pattern = re.compile('International|US|Business')
		Dict = {}

		US_International = [ txt for txt in Links_ if re.search(pattern,txt)]
	
		return US_International

	def article_extractor(self,url):
		Article = []
		content = requests.get(url)
		soup = BeautifulSoup(content.text,'html.parser')
		if content.status_code == 200:
			paragraph=(soup.findAll('p'))
			if len(paragraph)!=0:
				for txt in paragraph:
					Article.append(txt.getText())
		if len(Article)!=0:
		
			return Article
	
	def json_writer(self,file_, dictionary):
		print('=='*100)
		print("Writing news json for the today's date {}".format(datetime.date.today()))
		with open(file_,'w') as f:
			json.dump(dictionary, f)
					
		


		



if __name__ =='__main__':
	url_3 = r'https://abcnews.go.com/'
	obj=NewsExtractor()#url_1, url_2)
	Links = obj.print_url(url_3)
	All_Links = {"Links":sorted(Links)}
	Article_main = {}
	for i,links in enumerate(Links):
		
		Article_main[i] = obj.article_extractor(links)

	today_date = datetime.date.today()
	folder_name = str(today_date.day)+str(today_date.month)+str(today_date.year)
	full_path = os.getcwd()+'/'+folder_name
	os.makedirs(full_path)
	obj.json_writer(full_path+'/'+'ABC_news.json',Article_main)
	obj.json_writer(full_path+'/'+'Links.json',All_Links)


	

