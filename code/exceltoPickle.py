import xlrd
import pickle

def statPos(stat, rentList) :
	for i in range(0, len(rentList)) :
		if stat == rentList[i]['name'] :
			return i
	return -1

def addInfo(row, rentList, pos) :
	date = xlrd.xldate.xldate_as_tuple(sh.cell_value(rowx=i, colx=1), datemode=0)
	hour = int(sh.cell_value(rowx=i, colx=2))

	rentList[pos]['time'].append([date[0], date[1], date[2], hour])
	rentList[pos]['lent'].append(int(sh.cell_value(rowx=row, colx=3)))
	rentList[pos]['returned'].append(int(sh.cell_value(rowx=row, colx=4)))


rentList = []
for i in range(3,8) :
	print('<deal with month', i, '...>')
	bookname = 'rent_' + str(i) + '.xlsx'
	book = xlrd.open_workbook(bookname)
	sh = book.sheet_by_index(0)	

	for i in range(1, sh.nrows) :
		print(sh.cell_value(rowx=i, colx=0))
		position = statPos(sh.cell_value(rowx=i, colx=0), rentList)
		if position < 0 :
			position = len(rentList)
			statInfo = {}
			statInfo['name'] = sh.cell_value(rowx=i, colx=0)
			statInfo['time'] = []
			statInfo['lent'] = []
			statInfo['returned'] = []
			rentList.append(statInfo)
		addInfo(i, rentList, position)

with open('rent.pickle', 'wb') as file :
	pickle.dump(rentList, file, protocol=pickle.HIGHEST_PROTOCOL)

print('<complete>')