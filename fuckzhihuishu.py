from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
#username =input('请输入账号:')
#password=input('请输入密码')
chrome = webdriver.Chrome()
chrome.maximize_window()
def login(username,password):
	chrome.find_element_by_name('username').send_keys(username)
	chrome.find_element_by_id('lPassword').send_keys(password)
	chrome.find_element_by_class_name('wall-sub-btn').click()


def isElementExist(element):
	flag = True
	try:
		a=chrome.find_element_by_css_selector(element)
		return flag
	except:
		flag = False
		return flag
if __name__ == '__main__':
	username ='13181750216'
	password='1114596502'
	chrome.get('http://online.zhihuishu.com/onlineSchool/student/index')
	login(username,password)
	while True:
		if isElementExist('.speedPromote_btn'):
			break
	chrome.find_elements_by_class_name('speedPromote_btn')[0].click()
	time.sleep(2)
	chrome.switch_to.window(chrome.window_handles[1])
	deleteflag=False #指导卡flag
	yesflag=False #warning dialog
	jsflag=False
	cate = chrome.find_element_by_css_selector('ul.catalogue_ul1').find_elements_by_tag_name('li')
	catelist = []
	for i in cate:
		if i.get_attribute('_videoid') != '0' and i.get_attribute('watchstate') != '1' and i.get_attribute('id').__contains__('video'):
			catelist.append((i.get_attribute('id')))
	print('课程数量:'+str(len(catelist)))
	for j in catelist:
		while True:
			if isElementExist('.popbtn_cancel'):
				for i in chrome.find_elements_by_css_selector('.popbtn_cancel'):
					try:
						i.click()
						jsflag=False
					except:
						print('popbtn_cancel click error')
			if  not yesflag and isElementExist('.popbtn_yes'):
				try:
					chrome.find_element_by_css_selector('.popbtn_yes').click()
					yesflag=True
					jsflag = False
				except:
					print('popbtn_yes click error')
			if not deleteflag and isElementExist('.popup_delete'):
				try:
					chrome.find_element_by_css_selector('.popup_delete').click()
					deleteflag=True
					jsflag = False
				except:
					print('print popup_delete error')
			# if not jsflag and isElementExist('.progressbar_box_tip'):
			# 	prosess = chrome.find_element_by_css_selector('.progressbar_box_tip')
			# 	jss = chrome.execute_script('arguments[0].style.display="block";', prosess)
			# 	print(prosess.text[12:-2])
			# 	jsflag=True
			if yesflag and deleteflag and isElementExist('.progressbar_box_tip'):
				prosess = chrome.find_element_by_css_selector('.progressbar_box_tip')
				jss = chrome.execute_script('arguments[0].style.display="block";', prosess)
				prosess = chrome.find_element_by_css_selector('.progressbar_box_tip').text[12:-2]
				print(prosess,end='\r')
				if prosess=='' or prosess=='0':
					pass
				elif prosess=='100' or float(prosess)>80:
					print('finish')
					break
			time.sleep(2)
		if yesflag and deleteflag and isElementExist('li[id="'+str(j)+'"]'):
			next=chrome.find_element_by_css_selector('li[id="'+str(j)+'"]')
			prosess = chrome.find_element_by_css_selector('.progressbar_box_tip')
			chrome.execute_script('arguments[0].style.display="none";', prosess)
			while True:
				try:
					next.click()
					time.sleep(3)
					break
				except:
					print('next error')
					Drag = chrome.find_element_by_class_name("catalogue_ul1")
					ActionChains(chrome).drag_and_drop_by_offset(Drag, 0, 5).perform()
		# try:
		#
		# except:
		# 	print('next error')


