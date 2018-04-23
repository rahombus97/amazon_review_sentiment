from amazon_review_scrape import ParseReviews
from time import sleep
import json

def ReadAsin(catagory):
	#Add your own ASINs here 
	if catagory == "speakers":
		AsinList = ['B071JN4FW6','B06XNMXXCP','B00EZ9XKCM','B010OYASRG','B00BXF5HQ8','B0071I0O2I']
	elif catagory == "phones":
		AsinList = ['B079H6L4V2','B078NCL7GK','B01IB9QEJW','B0791VS3N9','B01N6IW6UN','B074BWGRKH']
	extracted_data = []
	for asin in AsinList:
		print("Downloading and processing page http://www.amazon.com/product-reviews/"+asin)
		extracted_data.append(ParseReviews(asin))
		sleep(5)
	f = open(catagory + '_data.json','w')
	json.dump(extracted_data,f,indent=4)

if __name__ == '__main__':
	ReadAsin("phones")