#密碼重試程式

#現在程式碼中 設定好密碼 password = 'a123456'
#讓使用者"最多輸入3次密碼"
#不對的話, 就印出"密碼錯誤! 還有__次機會"
#對的話, 就印出"登入成功"

password = 'a123456'
i = 3 #剩餘機會
while i >= 1:
	keyin = input('請輸入密碼: ')
	if keyin == password:
		print('登入成功!')
		break
	else:
		i = i - 1
		print('密碼錯誤! 還有 ', i, ' 次機會')
		