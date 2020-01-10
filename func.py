# funtion 函式/功能

#function是用來"收納"程式碼的
#他只是個功能! 並不會執行

def wash(dry=False, water=80): #wash是function name 不能數字開頭 盡量全小寫
# 括弧內要填參數(parameter) 像是投幣孔
	print('add', water, '% water') 
	print('add laundry soap')
	print('spin')
	if dry:
		print('dry')

wash() # 這邊才真正執行了funcion
wash(water=100)
wash(dry=True, water=50)

def add(x, y): #投幣孔可以複數但是數量要跟錢幣數量一致
	print(x + y)

add(3,4)
add(123,321)

#參數可以是預設值，那這樣不一定要投參數進去
def adding(x=1, y=1):
	print(x + y)

adding() #這會變2
adding(5) # 這樣就是x=5, y=1 也就是6
adding(y=5) #這樣就是x=1, y=5 也是6


def good(x, y):
	return x + y #就是把function 的執行結果"存下來" return就是他給出的結果
#要有return 後面才能存成result
result = good(3,4)
print(result)
print(good(3,5))
result = good(5,100)
print(result)

def average(numbers):
	return sum(numbers)/len(numbers) # 數字總和/多少個數字

a = average([1, 2, 3])
print(a)
print(average([1, 2, 3])) #同樣都會印出平均值2
print(average([65, 5645, 1000]))