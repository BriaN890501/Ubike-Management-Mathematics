import pickle

with open('bestSellers.pickle', 'rb') as file :
	top = pickle.load(file)

# for record in top :
# 	for i in range(0, len(record['books'])) :
# 		record['books'][i] = record['books'][i].strip()
# 		record['books'][i] = record['books'][i].strip('\n')
# 		record['books'][i] = record['books'][i].strip()
# 		print(record['books'][i])

# with open('bestSellers.pickle', 'wb') as file :
# 	pickle.dump(top, file)




for record in top :
	cnt = 0
	for book in record['books'] :
		cnt += 1
		print(cnt, '# :', book)

print('years:', len(top))
for bs in top :
	print(bs['year'], ':', len(bs['books']))