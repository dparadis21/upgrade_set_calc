from lxml import html
import requests
import os
import io

path = 'sets'
sets = os.listdir(path)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for player in sets:
	reward_price = 0;
	sum_of_parts = 0;
	first = 1;

	card_urls = [line.rstrip('\n') for line in open('sets/' + player)]; # get list of all muthead urls for player

	for url in card_urls:
		page = requests.get(url); # get page
		tree = html.fromstring(page.content); # load source code
		string = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[2]/td[4]/text()');

		price = int(string[0].translate(None, ',')); # remove comma from price and convert to an int

		if first == 1: # if it is the first url, it's the reward
			reward_price = price;
		else:
			sum_of_parts += price;

		first = 0;

	post_tax_price = int(float(reward_price) * 0.9);

	if int(reward_price) > int(post_tax_price):
		print bcolors.OKGREEN + str(player) + ': ' + str(reward_price) + '\t' + str(post_tax_price)  +'\t' + str(sum_of_parts) + bcolors.ENDC;
	else:
		print bcolors.WARNING + str(player) + ': ' + str(reward_price) + '\t' + str(post_tax_price)  +'\t' + str(sum_of_parts) + bcolors.ENDC;
	
