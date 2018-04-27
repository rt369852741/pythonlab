print("Hello World")
print("Hello","World")
print("Hello","world",sep="-")
print("Hello","world",sep="-",end="*") # end使程式不換行
print("abc")

print(9//2) #整數除法
print(9%5)  #得餘數
print(3**4) #3的四次方

a=1
b=2
print(a+b) #python不用定義變數(var...)

str1="I am learning Programming." #str:字串
print(str1) 
print(len(str1)) #len用來測試字串長度

print(str1[3]) #印出第二個字母a(字母從0開始)
print(str1[5:13]) #印出第五個字母到第十三個字母(13為要的字母後一個//g為12//)可以印出learning這個字
print(str1[5:]) #第五個字母之後
print(str1[:13]) #第十三個字母之前
print(str1[:]) 
print(str1[::-1]) #倒著印

print("{0} {1}".format(100,200))   #設定位置
print("num1: {0}""num2: {1}".format(a,b))
print("{0:10}{1:10}".format(200,300))

s="Stone Campus"
#請定義一個字串 str = "Stone Campus", 請印出以下內容:
#這個字串的長度
print(len(s))
#位置 6 的字母 (使用 [])
print(s[6])
#從位置 3 到 9 的子字串 "ne Camp" (使用util.slice())
print(s[3:10])
#從位置 3 到 最後的子字串 "ne Campus" (使用util.slice())
print(s[3:])
#從位置 0 到 9 的子字串 "Stone Camp"  (使用util.slice())
print(s[:10])
#請寫一個 test() 函數來測試你的程式

