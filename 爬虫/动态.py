# from selenium import webdriver
# from bs4 import BeautifulSoup
# driver = webdriver.Chrome()
# #访问网站
# driver.get('http://huaban.com')
# #获得网页信息
# soup = BeautifulSoup(driver.page_source, "lxml")
# #利用开发者工具找到我们需要的图片地址
# results = soup.select('img[data-baiduimageplus-ignore="1"]')
# #for r in results时发现有最后两个列表元素不是我们需要的网址，用[0:-2]去除
# for r in results[0:-2]:
#     print('http:'+r['src'])
# #关闭浏览器
# driver.quit()
from selenium import webdriver
import time
br=webdriver.Chrome()
br.get('http://www.jd.com/')
input=br.find_element_by_id('key')
input.send_keys('零食')
time.sleep(3)
input.clear()
input.send_keys("方便面")
button=br.find_element_by_class_name('button')
button.click()
print()
