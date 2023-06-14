def mobile_bill():
	f = open('data.csv')
	incoming_minutes = 0
	outcoming_minutes = 0
	sms = 0
	for line in f.readlines():
		if line.split(',')[1] == '968247916':
			outcoming_minutes += float(line.split(',')[3])
			sms += int(line.split(',')[4])
		if line.split(',')[2] == '968247916':
			incoming_minutes += float(line.split(',')[3])
	return outcoming_minutes * 3 + incoming_minutes + sms

def traffic_bill():
	traffic = 0.0
	f = open('Damp.txt')
	for line in f.readlines():
		if len(line.split("217.15.20.194")) == 1:
			continue
		try:
			traffic += float(line.split()[-2])
		except ValueError:
			traffic += float(line.split()[-3]) * 1024.0 * 1024
	traffic /= 1024
	traffic -= 1000
	return round(traffic, 2)
