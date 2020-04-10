from bs4 import BeautifulSoup as bs
import requests

#url = requests.get('https://www.sgu.ru/schedule/knt/do/141')
#soup = bs(url.content, 'lxml')

#table = soup(id='schedule')
#rows = table('tr')
#for row in rows:
#	cells = row.find_all('td')
#
#	for cell in cells:
#		if cell.text != '':
#			print(cell)
class Parser:
	base_url = 'https://www.sgu.ru/schedule/'

	def __init__(self):
		pass

#	def parse(self):
#		ans = ''
#		table_top = soup.find('table')
#		rows = table_top.find_all('tr')
#		for row in rows:
#			cells = row.find_all('td')
#			for cell in cells:
#				divs = cell.find_all('div')
#				time = cell.find_previous_siblings('th')
#				if cell.text != '':
#					ans += str(time)
#				ans += '\n'
#				for i, div in enumerate(divs, start=0):
#					if i == 0:
#						continue
#					ans += div.text
#					ans +='\n'
#		return(ans)

	def get_info(self, cell, les):
		objs = cell.find_all(class_='l')
		cur_les = '{0} пара'.format(les)
		info_lst = [cur_les]
		for obj in objs:
			divs = obj.find_all('div')
			for i, div in enumerate(divs, start = 0):
				if i <= 1:
					continue
				if div.text != '':
					info_lst.append(div.text)
		ans = ''
		for info in info_lst:
			ans += info
			ans += '\n'
		return(ans)

	def get_column(self, group, sub, faculty):
		ans = ''
		base_url = self.base_url + f'{faculty}/do/{group}'
		url = requests.get(base_url)
		soup = bs(url.content, 'lxml')
		table_top = soup.find('table')
		day = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
		for j in range(1, 6):
			cur_day = day[j - 1]
			ans += cur_day
			ans += '\n'
			for i in range(1, 8):
				cur = table_top.find(id='{0}_{1}'.format(i,j))
				if cur.text != '':
					ans += self.get_info(cur, i)
		return(ans)

