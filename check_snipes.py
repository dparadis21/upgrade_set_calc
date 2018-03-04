from lxml import html
import requests
import os
import sys
import re

pset = sys.argv[1];

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

first = 1;

card_urls = [line.rstrip('\n') for line in open(pset)]; # get list of all muthead urls for player

for url in card_urls:
	player = url;
	live_auct = ['none'];
	completed = ['none'];
	live_auct_list = ['none'];
	completed_list = ['none'];
	page = requests.get(url); # get page
	tree = html.fromstring(page.content); # load source code
	live_auct = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[3]/td[4]/text()'); # get all current auctions
	completed = tree.xpath('//div[@class="player-prices-completed-sales"]/table/tr[2]/td[2]/text()');
	live_auct_list = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[*]/td[4]/text()');
	completed_list = tree.xpath('//div[@class="player-prices-completed-sales"]/table/tr[*]/td[2]/text()');
	nodata = 0;

	if not live_auct:
		nodata = 1;
		live_auct = -1;
	else:
		live_auct = re.sub('[^0-9]', '', live_auct[0]);

	if live_auct == '':
		live_auct = 0;
	else:
		live_auct = int(live_auct);

	if not completed:
		nodata = 1;
		completed = -1;
	else:
		completed = re.sub('[^0-9]', '', completed[0]);

	if completed == '':
		completed = 0;
	else:
		completed = int(completed);

	if (live_auct < (float(completed) * 0.9)) and (live_auct != -1) and (completed != -1):
		post_tax_price = int(float(completed) * 0.9);
		profit = int(post_tax_price) - int(live_auct);
		print bcolors.OKBLUE + bcolors.BOLD + '\n' + str(player) + bcolors.ENDC;
		print "Live Auctions: " + str(live_auct_list);
		print "Last Completed Auctions: " + str(completed_list) + "\n";
		print bcolors.OKGREEN + "Potential Profit: " + str(profit) + bcolors.ENDC;
