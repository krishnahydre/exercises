from bs4 import BeautifulSoup
from selenium.webdriver import Chrome


# BASE ON JIMDO
# image url
url = 'https://image.jimcdn.com/app/cms/image/transf/dimension=750x1280:format=jpg/path/s47d0e438db4abd25/image/i7cb6c3bb8a61744c/version/1590264580/image.jpg'

url = 'https://www.gravidu.com//app/module/webproduct/goto/m/m9ea9cd58d3dcc471'

# driver.manage().window().maximize();
# driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
# driver.findElement(By.id("identifierId")).sendKeys("your email", Keys.ENTER);

browser = Chrome()
browser.get(url)
content = browser.page_source
b_content = BeautifulSoup(content)
get_image_tag = b_content.findAll('img')
get_description_tag = b_content.findAll('div', {'class':'description'}, limit=1)
get_product_gallery_image = b_content.findAll('div', {'class' : 'cc-shop-product-img'}, limit=1)
get_product_detail = b_content.findAll('ul', {'class' : 'cc-shop-product-availability j-product-details'}, limit=1)
# cookies = browser.get_cookies()
browser.close()
