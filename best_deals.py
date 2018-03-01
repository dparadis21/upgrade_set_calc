from lxml import html
import requests

page = requests.get ('https://www.muthead.com/18/players/prices/31010-nick-foles/xbox-one')
tree = html.fromstring(page.content)

buyitnow = tree.xpath('//div[@class="player-prices-live-auctions"]/table/tr[*]/td[4]/text()')

print 'Buy it now Price:  ', buyitnow
