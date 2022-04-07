count = 3

while True:
	count = count - 1
	passwd = input('Please enter the password: ')

	if passwd == 'a123456':
		print('Login successful!')
		break
	else:
		if count >= 1:
			print('Login failed!')
			print('You still have', count, 'times')
		elif count < 1:
			print('You are locked!')
			break
