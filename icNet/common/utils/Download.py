
"""
下载html文件
"""
import urllib.request as urllib2
import urllib.parse as urlparse
from fake_useragent import UserAgent


class Download():

    def __init__(self, url):
        self.url = url
        self.num_retries = 2
        ua = UserAgent()
        self.user_agent = ua.random
        self.cookie = '__snaker__id=PCePOSHsUQUnRNfi; PHPSESSID=epl8mlll13nrm38msp1786jf8v; ICNet[Host]=https%3A%2F%2Fwww.ic.net.cn; Hm_lvt_01dd801871f8a184f89f8e6863636c12=1705978108; ICNet[LoginModel]=HiSpa6Ht9VF8ppvNzvqLpg%3D%3D; ICNet[Guest]=EOQN1oiXOYDDvhNyAaDOGQ%3D%3D; ICNet[CompanyId]=ki3I6j1G7G3FgmSuMXtaalXVrxadzNNV8tC06UPawqs%3D; ICNet[MemberType]=MXvdVzoEbPYR5vKoPKkI_A%3D%3D; ICNet[ActiveFlag]=1_dkMVyzeKEo2Pzw_xlOjA%3D%3D; ICNet[MemLevel]=vr6FgP0HOFFlWZ7ITXdhIw%3D%3D; ICNet[AutoLogin]=xn3yTJtU4GPXXvvw0ZBtjg%3D%3D; ICNet[LoginType_og]=WOnX0mQLH9z8sarx6_Ye3A%3D%3D; ICNet[ValidDate]=yDUVRuhDHeGOOrWJBDWMv8mh5wNwfO894Z1qZVFndd0%3D; ICNet[Version]=0vGCusZTfN81WWMFuenh3Q%3D%3D; ICNet[ICNetVersion2]=3.1; ICNet[LoginType]=9djdei9qSou56XVLfue19Q%3D%3D; ICNet[ICNETUUID]=qHr4jg0XW9TtD7GBnKamNqrPfUGvwSaWXlCrrdTY6lY%3D; ICNet[jpk]=%5B%22Xk%22%2C%22RN%22%2C%22rg%22%2C%22NNk%22%2C%22NNk%22%2C%22NNk%22%5D; ICNet[SearchLog][0]=MC74HC1G14DFT2G; ICNet[SearchLog][1]=MC74HC1G14DF; ICNet[SearchLog][2]=MC74HC1G; ICNet[SearchLog][3]=MC; ICNet[SearchLog][4]=LM358DR; PHPSESSID=c5ki6fmn377e7kin3fip1lc8n0; gdxidpyhxdE=LhO4Lxj4oHDYmZkGOy2jRU9JJ%2B%5CZC2gO4mp09%5CW48rdluSujwwqm8V5BL2%2FP3R7JCszgM87z0gG728JMZ%5Ca1mAuuNZ%2Ff1yEdzIHhiqw0ZNdQ%5C%5CT2N%5CmB1A%2FJEWx21K8Q4GB5yTU21kQJE5YlBAv3yBrYYvR5%2BTtGd3yUUPDo568mnwgT%3A1705991023682; Hm_lpvt_01dd801871f8a184f89f8e6863636c12=1705990483; ICNet[sgj]=%5B%22JJcyaJbc%22%2C%22JJccaJbi%22%2C%22JJAkaJbW%22%2C%22JJAkaJDb%22%2C%22JJAiaJDA%22%2C%22JJAAaJDi%22%2C%22JJDWaJDy%22%2C%22JJDyaJAb%22%2C%22JJDiaJAA%22%2C%22JJDMaJAi%22%2C%22JJDcaJAy%22%2C%22JJDDaJcb%22%2C%22JJbWaJcM%22%2C%22JJbJaJck%22%2C%22JJbyaJcJ%22%2C%22JJbyaJMA%22%2C%22JJbyaJMc%22%2C%22JJbyaJMi%22%2C%22JJbyaJMy%22%2C%22JJbyaJMW%22%2C%22JJbyaJiD%22%2C%22JJbyaJiM%22%2C%22JJbyaJiy%22%2C%22JJbyaJiJ%22%2C%22JJbyaJkD%22%2C%22JJbyaJkc%22%2C%22JJbkaJki%22%2C%22JJbkaJky%22%2C%22JJbkaJkJ%22%2C%22JJbkaJkW%22%2C%22JJbiaJyb%22%2C%22JJbiaJyb%22%2C%22JJbiaJyb%22%2C%22JJbiaJyb%22%2C%22JJbiaJyb%22%2C%22JJbiaJyb%22%2C%22JJbMaJyb%22%2C%22JJbcaJyb%22%2C%22JJbcaJyb%22%2C%22JJbAaJyb%22%2C%22JJbDaJyb%22%2C%22JJbbaJyb%22%2C%22JyWWaJyb%22%2C%22JyWWaJyD%22%2C%22JyWJaJyD%22%2C%22JyWyaJyD%22%2C%22JyWyaJyD%22%2C%22JyWyaJyD%22%2C%22JyWkaJyD%22%2C%22JyWkaJyA%22%2C%22JyWiaJyA%22%2C%22JyWiaJyc%22%2C%22JyWiaJyc%22%2C%22JyWMaJyc%22%2C%22JyWMaJyM%22%2C%22JyWMaJyM%22%2C%22JyWMaJyi%22%2C%22JyWMaJyi%22%2C%22JyWMaJyi%22%2C%22JyWcaJyi%22%2C%22JyWcaJyk%22%2C%22JyWcaJyk%22%2C%22JyWcaJyk%22%2C%22JyWcaJyk%22%2C%22JyWcaJyk%22%2C%22JyWAaJyy%22%2C%22JyWAaJyy%22%2C%22JyWAaJyy%22%2C%22JyWAaJyy%22%2C%22JyWDaJyy%22%2C%22JyJWaJyJ%22%2C%22JyJJaJyW%22%2C%22JyJyaJyW%22%2C%22JyJkaJyW%22%2C%22JyJiaJJb%22%2C%22JyJiaJJb%22%2C%22JyJMaJJb%22%2C%22JyJMaJJb%22%2C%22JyJMaJJD%22%2C%22JyJcaJJD%22%2C%22JyJcaJJD%22%2C%22JyJcaJJD%22%2C%22JyJcaJJD%22%2C%22JyJAaJJD%22%2C%22JyJAaJJD%22%2C%22JyJAaJJD%22%2C%22JyJDaJJD%22%2C%22JyJDaJJD%22%2C%22JyJDaJJD%22%2C%22JyJbaJJD%22%2C%22JyJbaJJA%22%2C%22JyJbaJJA%22%2C%22JyyWaJJc%22%2C%22JyyJaJJc%22%2C%22JyyyaJJc%22%2C%22JyyyaJJM%22%2C%22JyykaJJM%22%2C%22JyyiaJJM%22%2C%22JyyMaJJi%22%2C%22JyyMaJJi%22%5D; ICNet[sct]=cd42c941faa2bf084bf337d266a08cc1f1ac9dc6'
        self.proxy = None

    def downloadHtml(self):
        print('Downloading ' + self.url)
        headers = {'User-Agent': self.user_agent,
                   'Cookie': self.cookie }

        request = urllib2.Request(url=self.url, headers=headers)
        opener = urllib2.build_opener()
        if self.proxy:
            proxy_params = {urlparse.urlparse(self.url).scheme: self.proxy}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            html = urllib2.urlopen(request).read()
        except urllib2.URLError as e:
            print('Error downloading ' + e.reason)
            html = None
            if self.num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code <= 600:
                    self.num_retries -=1
                    return self.downloadHtml(self)
        return html
