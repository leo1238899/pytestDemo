'''
webdriver元素定位方式
id              find_element_by_id()
name            find_element_by_name()
class name      find_element_by_class_name()
tag name        find_element_by_tag_name 标签
link text       find_element_by_link_text 链接显示的文本
partial link text   find_element_by_partial_text 部分链接的显示文本
xpath           find_element_by_xpath
css selector    find_element_by_css_selector

ID：使用元素的唯一标识ID来定位元素。
Name：使用元素的名称属性来定位元素。
Class Name：使用元素的class属性来定位元素。
Tag Name：使用元素的标签名来定位元素。
Link Text：使用超链接文本来定位链接元素。
Partial Link Text：使用超链接部分文本来定位链接元素。
CSS Selector：使用CSS选择器来定位元素。
XPath：使用XPath表达式来定位元素。

ID和Xpath是最常用的
'''
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()  # 打开浏览器
driver.get('http://www.baidu.com')  # 打开网址
time.sleep(3)
search = driver.find_element('id', 'kw')  # 定位搜索框元素
search.send_keys('selenium')  # 在搜索框中输入"selenium"
time.sleep(3)
print(search.get_attribute('outerHTML'))  # 查看搜索框元素的源码 value、href、src、class outerHTML
driver.quit()  # 关闭浏览器
'''
value属性：value属性代表一个元素的当前值。对于<input>、<textarea>等表单元素，value属性表示用户输入或通过脚本动态设置的值。

href属性：href属性用于指定链接元素(<a>)的目标URL。它定义了当用户点击链接时要访问的URL地址。

src属性：src属性用于指定嵌入内容的URL。常见的元素包括<img>、<script>和<iframe>等。src属性指定了要加载的图片、脚本或嵌入的网页的URL。

class属性：class属性是一个用于标识元素的CSS类名。它可以用来定义元素的外观和样式，或者用于JavaScript操作和样式设置。

outerHTML属性：outerHTML属性是一个元素对象的只读属性，返回表示整个元素及其内容的HTML字符串。它包括元素的开始标签、内容和结束标签，可以用于获取元素的完整HTML表示形式。
'''

