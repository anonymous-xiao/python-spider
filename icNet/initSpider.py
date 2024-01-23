
from icNet.common.utils.Download import Download
import lxml.html
class InitSpider:

    def __init__(self):
        self.url = 'https://www.ic.net.cn/search/MC74HC1G14DFT2G.html?page=1'

    def initSpider(url):
        html = Download(url).downloadHtml()
        print(html)
        tree = lxml.html.fromstring(html)
        div = tree.xpath('//*[@id="resultList"]/li[5]/div[2]/a')
        company_name = div.text_content()
        print(company_name)


if __name__ == "__main__":
    init = InitSpider.initSpider('https://www.ic.net.cn/search/MC74HC1G14DFT2G.html?page=1')