from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://desktop.mt365.alpha.tmogroup.asia')
browser.maximize_window()
logoname=browser.find_element_by_class_name("site-logo").text
print (logoname)
if logoname=='Glyco365':
 print ('登陆成功！')
else :
 raise NameError ('登录失败啦啦啦!')
