password = 'a123456'
number = 3
while number > 0:
	answer = input('請輸入密碼:')
	if answer == password:
		print('登出成功!')
		break
	else:
		number = number - 1
		print('密碼錯誤! 還有', number, '次機會')
		

	


	