from selenium import webdriver
browser=webdriver.Chrome()
browserA.ge('https://desktop.mt365.alpha.tmogroup.asia')
browser.maximize_window()
logoname=browser.find_element_by_class_name("site-logo").text
print (logoname)
if logoname=='Glyco366':
 print ('登陆成功.GET是错误的！')
else :
 raise NameError ('登录失败啦啦啦!')
