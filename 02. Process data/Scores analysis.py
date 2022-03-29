import csv

sbd_number = 2000000
sbd_not_exist = []
with open('sbd_not_exist.txt','r') as file:
	sbd_not_exist = file.readlines()
for i in range(len(sbd_not_exist)):
	sbd_not_exist[i] = sbd_not_exist[i].replace('\n','')
header = ['sbd','tên','cmnd','toán','ngữ văn','vật lí','hóa học','sinh học','lịch sử','địa lí','gdcd','khtn','khxh','tiếng anh']
with open('clean_data.txt', encoding='utf8', mode='w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(header)
with open('raw data.txt', 'r') as file:
	datas = file.readlines()

for data in datas:
	sbd_number = sbd_number + 1
	sbd = '0' + str(sbd_number)
	if sbd in sbd_not_exist:
		continue
	data = data.replace('\\r','')
	data = data.split('\\n')
	for i in range(len(data)):
		data[i] = data[i].strip()

	#get Unicode codes and chars
	chars = []
	codes = []
	with open('Unicode.txt', encoding='utf8', mode='r') as file:
		unicode_list = file.readlines()
	for i in range(len(unicode_list)):
		unicode_list[i] = unicode_list[i].replace('\n','')
	for i in range(len(unicode_list)):
		x = unicode_list[i].split(' ')
		chars.append(x[0])
		codes.append(x[1])

	#decode Unicode
	for i in range(len(data)):
		for j in range(len(codes)):
			data[i] = data[i].replace(codes[j],chars[j])

	#decode web code
	for i in range(len(data)):
		if '&#' in data[i]:
			while ('&#' in data[i]):
				index = data[i].index('&#')
				data[i] = data[i][:index] + chr(int(data[i][index+2:index+5])) + data[i][index+6:]

	#get sbd, name, idendification no. & scores
	name = data[61]
	name = name.lower().title()
	iden_number = data[64]
	subjects_scores = data[67]

	#extract scores
	all_subjects = ['Toán','Ngữ văn','Vật lí','Hóa học','Sinh học','Lịch sử','Địa lí','GDCD','KHTN','KHXH','Tiếng Anh']
	scores = []
	if 'KHTN' or 'KHXH' in subjects_scores:
		try:
			index = subjects_scores.index('KHTN')
		except:
			index = subjects_scores.index('KHXH')
		subjects_scores = subjects_scores[:index+5] + '   ' + subjects_scores[index+6:]
	subjects_scores = subjects_scores.split('   ')
	for i in range(len(subjects_scores)):
		if subjects_scores[i].find(':') != -1:
			subjects_scores[i] = subjects_scores[i].replace(':','')
	for i in range(len(all_subjects)):
		if all_subjects[i] in subjects_scores:
			scores.append(subjects_scores[subjects_scores.index(all_subjects[i])+1])
		else:
			scores.append('-1')
	student_data = [sbd,name,iden_number]
	for score in scores:
		student_data.append(score)
	with open('clean_data.txt', encoding='utf8', mode='a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(student_data)