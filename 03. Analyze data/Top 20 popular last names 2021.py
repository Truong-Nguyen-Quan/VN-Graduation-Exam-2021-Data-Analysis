datas = []
with open('clean_data.txt', encoding='utf8', mode='r') as file:
	datas = file.readlines()
	# for i in range(0,21):
	# 	datas.append(file.readline())

datas.pop(0)
for i in range(len(datas)):
	datas[i] = datas[i].replace('\n','')
	datas[i] = datas[i].split(',')

names = []
average_scores = []
for i in range(len(datas)):
	names.append(datas[i][1])
	total_scores = 0
	subject_count = 0
	for j in range(3,len(datas[i])):
		if datas[i][0] == '02065875' and j == 3:
			continue
		if datas[i][j] != '-1':
			total_scores = total_scores + float(datas[i][j])
			subject_count = subject_count + 1
	average_scores.append(round(total_scores/subject_count,2))

ln_all = []
for name in names:
	ln_all.append(name.split(' ')[0])

ln_unique = []
for ln in ln_all:
	if ln not in ln_unique:
		ln_unique.append(ln)

ln_unique_count = []
for i in range(len(ln_unique)):
	count = 0
	for j in range(len(ln_all)):
		if ln_unique[i] == ln_all[j]:
			count = count + 1
	ln_unique_count.append(count)

max_count = 0
pass_index = []
sort_ln_unique_count = []
sort_ln_unique = []
for i in range(len(ln_unique)):
	for j in range(len(ln_unique_count)):
		if ln_unique_count[j] > max_count and j not in pass_index:
			max_count = ln_unique_count[j]
			index = j
		if j == len(ln_unique_count)-1:
			sort_ln_unique_count.append(max_count)
			sort_ln_unique.append(ln_unique[index])
			pass_index.append(index)
			max_count = 0

sort_ln_unique_average_scores = []
for i in range(len(sort_ln_unique)):
	average_score = 0
	count = 0
	for j in range(len(ln_all)):
		if sort_ln_unique[i] == ln_all[j]:
			average_score = average_score + average_scores[j]
			count = count + 1
	sort_ln_unique_average_scores.append(round(average_score/count,2))
# print(ln_all)
# print('-----')
# print(average_scores)
# print('-----')
# print(sort_ln_unique)
# print('-----')
# print(sort_ln_unique_average_scores)

ln_twenty = sort_ln_unique[:20]
ln_count_twenty = sort_ln_unique_count[:20]
ln_average_scores_twenty = sort_ln_unique_average_scores[:20]
ln_percentage = []
total = 0
for i in range(len(ln_twenty)):
	total = total + ln_count_twenty[i]
for i in range(len(ln_count_twenty)):
	ln_percentage.append(round(ln_count_twenty[i]/total*100,2))

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.bar(ln_twenty,ln_percentage)
ax1.set_title('Top 20 popular last names')
ax1.set_xlabel('Last name')
ax1.set_ylabel('Percentage')
ax1.set_ylim([0,100])
rects = ax1.patches

ax2 = ax1.twinx()
ax2.plot(ln_twenty,ln_average_scores_twenty,color='r',marker='o')
ax2.tick_params(axis='y',colors='r')
ax2.set_ylabel('Average Scores',color='r')
ax2.set_ylim(0,10)

# Make some labels.
for rect, label in zip(rects, ln_percentage):
    height = rect.get_height()
    ax1.text(rect.get_x()+rect.get_width()/2, height+3, label, ha='center',va='bottom')

for x,y in zip(ln_twenty,ln_average_scores_twenty):
    ax2.annotate(y,(x,y),textcoords='offset points',xytext=(0,10),ha='center')

plt.show()
