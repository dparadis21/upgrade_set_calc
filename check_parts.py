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
	print bcolors.OKBLUE + bcolors.BOLD + str(player) + bcolors.ENDC;
	live_auct = ['none'];
	completed = ['none'];
	page = requests.get(url); # get page
	tree = html.fromstring(page.content); # load source code
	live_auct = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[*]/td[4]/text()'); # get all current auctions
	completed = tree.xpath('//div[@class="player-prices-completed-sales"]/table/tr[*]/td[2]/text()');
	nodata = 0;

	print "Live Auctions: " + str(live_auct);
	print "Last Completed Auctions: " + str(completed) + "\n";

#	if (not live_auct)  or (not completed):
#		nodata = 1;
#		price = -1;
#	else:
#		for i in range(0, 10):
#			if (i < live_auct.length) and (i < completed.length):
#				print str(live_auct) + '\t' + str(completed_price);
#			elif (i < live_auct.length):
#				print str(live_auct);
#			elif (i < completed.length):
#				print '\t\t\t' + str(completed_price);
