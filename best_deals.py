from lxml import html
import requests
import os

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

print bcolors.BOLD + "Player\t\t\t\tSell Price\tAfter Tax Profit\tParts Cost\tProfit" + bcolors.ENDC;

for player in sets:
	reward_price = 0;
	sum_of_parts = 0;
	first = 1;

	card_urls = [line.rstrip('\n') for line in open('sets/' + player)]; # get list of all muthead urls for player

	for url in card_urls:
		string = ['none'];
		page = requests.get(url); # get page
		tree = html.fromstring(page.content); # load source code
		string = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[2]/td[4]/text()');
		nodata = 0;

		if not string:
			nodata = 1;
		else:
			price = int(string[0].translate(None, ',')); # remove comma from price and convert to an int

		if first == 1: # if it is the first url, it's the reward
			reward_price = price;
		else:
			sum_of_parts += price;

		first = 0;

	post_tax_price = int(float(reward_price) * 0.9);
	profit = int(post_tax_price) - int(sum_of_parts);

	if profit > 0 and nodata != 1:
		print bcolors.OKGREEN + str(player) + ':\t\t' + str(reward_price) + '\t\t' + str(post_tax_price)  +'\t\t\t' + str(sum_of_parts) + '\t\t' + str(profit) + bcolors.ENDC;
	if nodata == 1:
		print "Incomplete data";
#	else:
#		print bcolors.FAIL + str(player) + ':\t\t' + str(reward_price) + '\t\r' + str(post_tax_price)  +'\t\t\t' + str(sum_of_parts) + '\t\t' + str(profit) + bcolors.ENDC;
	
