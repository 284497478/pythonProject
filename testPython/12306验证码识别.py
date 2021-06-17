import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from testPython.chaojiying.chaojiying import Chaojiying_Client
import base64

url = 'https://kyfw.12306.cn/otn/resources/login.html'

driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver')
driver.get(url)
time.sleep(1)
pwd_login_ele = driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
# driver.execute_script('javascript:;', pwd_login_ele)
pwd_login_ele.click()
time.sleep(1)
# driver.save_screenshot('./chromedriver/screen.png')
driver.get_screenshot_as_file('/Users/mac/PycharmProjects/pythonProject/testPython/chromedriver/screen.png')
code_ele = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
img_bs64 = code_ele.get_attribute('src')
print('src :', img_bs64)
code_ele_location = code_ele.location
print('location', code_ele_location)
code_img_size = code_ele.size
print('code_size:', code_img_size)
rangle = (int(code_ele_location['x'] * 2), int(code_ele_location['y'] * 2),
          int(code_ele_location['x'] * 2 + code_img_size['width'] * 2),
          int(code_ele_location['y'] * 2 + code_img_size['height'] * 2))
# x = 1691
# y = 582
# rangle = (x, y, int(x + code_img_size['width']),
#           int(y + code_img_size['height']))
i = Image.open('./chromedriver/screen.png')
code_img_name = './chromedriver/code.png'
# 裁剪
frame = i.crop(rangle)
frame.save(code_img_name)
img_data = base64.b64decode(img_bs64.split(',')[1])
print('img_data:', img_data)
with open(code_img_name, 'wb') as fp:
    fp.write(img_data)

chaojiying = Chaojiying_Client('17396446825', 'Cjy584allen', '918508')  # 用户中心>>软件ID 生成一个替换 96001
im = open(code_img_name, 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']  # 返回结果为22,22|33,22
print('超级鹰返回的坐标是：', result)
point_list = []  # 结果为[[22,11],[333,111]]
if result != '':
    if '|' in result:
        result_list = result.split('|')
        count_1 = len(result_list)
        for i in range(count_1):
            xy_list = []
            x = int(result_list[i].split(',')[0])
            y = int(result_list[i].split(',')[1])
            xy_list.append(x)
            xy_list.append(y)
            point_list.append(xy_list)
    else:
        xy_list = []
        x = int(result.split(',')[0])
        y = int(result.split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        point_list.append(xy_list)
    print('组装后的坐标数组为：', point_list)
    # 遍历列表，并使用动作链
    for l in point_list:
        x = l[0]
        y = l[1]
        ActionChains(driver).move_to_element_with_offset(code_ele, x, y).click().perform()
        time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys('15108971715')
    driver.find_element_by_xpath('//*[@id="J-password"]').send_keys('12306584allen')
    driver.find_element_by_xpath('//*[@id="J-login"]').click()
else:
    print('返回坐标为空！')
time.sleep(3)
driver.quit()
