import pickle

with open('rent.pickle', 'rb') as file :
	rentList = pickle.load(file)
	print(rentList[0]['name'])
	for i in range(0, len(rentList[0]['time'])) :
		print('time:', rentList[0]['time'][i], '/ lent:', rentList[0]['lent'][i], '/ returned:', rentList[0]['returned'][i])
	print('total stations:', len(rentList))
	print('total time:', len(rentList[0]['time']), 'days')