import subprocess

start = 2000001
end = 2089276

with open('raw_data.txt', 'w') as file:
	for i in range(start,end):
		command = 'curl -F "sobaodanh=0' + str(i) + '" diemthi.hcm.edu.vn/Home/Show'
		result = subprocess.check_output(command)
		file.write(str(result) + '\n')