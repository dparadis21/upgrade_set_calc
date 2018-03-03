from lxml import html
import requests
import os
import re
import sys

path = sys.argv[1];
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
	profit = -1;
	first = 1;

	card_urls = [line.rstrip('\n') for line in open(path + '/' + player)]; # get list of all muthead urls for player

	for url in card_urls:
		string = ['none'];
		page = requests.get(url); # get page
		tree = html.fromstring(page.content); # load source code
		string = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[2]/td[4]/text()');
		nodata = 0;

		if not string:
			nodata = 1;
			price = -1;
		else:
			price = re.sub('[^0-9]', '', string[0]);
			if price == '':
				price = 0;
			else:
				price = int(price);

		if first == 1: # if it is the first url, it's the reward
			reward_price = price;
		else:
			sum_of_parts += price;

		first = 0;

	if price != -1:
		post_tax_price = int(float(reward_price) * 0.9);
		profit = int(post_tax_price) - int(sum_of_parts);

	if profit > 0 and nodata != 1:
		if len(str(player)) > 14:
			print bcolors.OKGREEN + str(player) + ':\t\t' + str(reward_price) + '\t\t' + str(post_tax_price)  +'\t\t\t' + str(sum_of_parts) + '\t\t' + str(profit) + bcolors.ENDC;
		else:
			print bcolors.OKGREEN + str(player) + ':\t\t\t' + str(reward_price) + '\t\t' + str(post_tax_price)  +'\t\t\t' + str(sum_of_parts) + '\t\t' + str(profit) + bcolors.ENDC;

	if profit <= 0 and nodata != 1:
		if len(str(player)) > 14:
			print bcolors.FAIL + str(player) + ':\t\tNOT PROFITABLE' + bcolors.ENDC;
		else:
			print bcolors.FAIL + str(player) + ':\t\t\tNOT PROFITABLE' + bcolors.ENDC;
