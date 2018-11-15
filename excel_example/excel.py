import xlrd

# input the excel(this file should be located at the same place with excel files)
book = xlrd.open_workbook("rent_3.xlsx")
sh = book.sheet_by_index(0)

# create a list to store the informations
items = []
# deal with informations of each station separately
currentSat = sh.cell_value(rowx=1, colx=0)
cnt = -1
for i in range(1, sh.nrows) :
	if (sh.cell_value(rowx=i, colx=0) != currentSat) or (i == 1):
		# create a dictionary to store informations of one station
		item = {}
		item['name'] = sh.cell_value(rowx=i, colx=0)
		# create a null list to store the daily record
		item['record'] = []
		# add the dictionary into the list
		items.append(item)
		cnt += 1
	# transfer the date as tuple(like constant list)
	date = xlrd.xldate.xldate_as_tuple(sh.cell_value(rowx=i, colx=1), datemode=0)
	hour = int(sh.cell_value(rowx=i, colx=2))
	# create a  dictionary to store daily information
	inf = {}
	inf['time'] = [date[0], date[1], date[2], hour]
	inf['lent'] = int(sh.cell_value(rowx=i, colx=3))
	inf['returned'] = int(sh.cell_value(rowx=i, colx=4))
	# add the daily information into "record" list
	items[cnt]['record'].append(inf)
# print out the first entry in the list
print(items[0])


# count how many station in the excel
# sample = items[0]['name']
# cnt = 1

# print(sample)

# for i in items:
# 	if i['name'] != sample:
# 		sample = i['name']
# 		cnt += 1
# 		print(sample)
# print(cnt)