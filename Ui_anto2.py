import time
from selenium import webdriver
driver=webdriver.Chrome()#初始化浏览器
driver.get("http://erp.lemfix.com/index.html")
driver.implicitly_wait(2)
if driver.title=="柠檬ERP":
    print("网址正确，可以测试")
else:
    print("网址错误，请检查后重新进入")
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
reg_name=driver.find_element_by_xpath("//p").text
print(reg_name)
if reg_name=="测试用户":
    print("用户名正确，继续测试")
else:
    print("用户名错误，请重新测试")













driver.quit()