password = 'a123456'
number = 3
while number > 0:
	number = number - 1
	answer = input('請輸入密碼:')
	if answer == password:
		print('登出成功!')
		break
	else:
		print('密碼錯誤!')
		if number > 0:
			print('還有', number, '次機會')
		else:
			print('沒機會嘗試了! 要鎖帳號了啦!')	
		

	


	