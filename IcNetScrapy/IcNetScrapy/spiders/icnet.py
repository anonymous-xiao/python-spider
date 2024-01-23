import scrapy
from fake_useragent import UserAgent



class IcnetSpider(scrapy.Spider):
    name = "icnet"
    allowed_domains = ["www.ic.net.cn"]
    start_urls = ["https://www.ic.net.cn/search/MC74HC1G14DFT2G.html?page=1"]
    # custom_settings = {
    #     "COOKIES_ENABLED": True
    # }

    def start_requests(self):

        cookies = '__snaker__id=ml9WyUeij0nScMHU; PHPSESSID=lveeihdfqpammrj9fbee28iufr; ICNet[Host]=https%3A%2F%2Fwww.ic.net.cn; ICNet[LoginModel]=HiSpa6Ht9VF8ppvNzvqLpg%3D%3D; ICNet[Guest]=EOQN1oiXOYDDvhNyAaDOGQ%3D%3D; ICNet[CompanyId]=ki3I6j1G7G3FgmSuMXtaauPA3CFGS7MeBMOfrDXKHts%3D; ICNet[MemberType]=MXvdVzoEbPYR5vKoPKkI_A%3D%3D; ICNet[ActiveFlag]=1_dkMVyzeKEo2Pzw_xlOjA%3D%3D; ICNet[MemLevel]=vr6FgP0HOFFlWZ7ITXdhIw%3D%3D; ICNet[AutoLogin]=OrC3pJzrPuG-OQnnIUROkA%3D%3D; ICNet[LoginType_og]=WOnX0mQLH9z8sarx6_Ye3A%3D%3D; ICNet[ValidDate]=aNdhjS4zvC8G7T3W9IPlqmJV92d7DcH8EYid_X6950E%3D; ICNet[Version]=0vGCusZTfN81WWMFuenh3Q%3D%3D; ICNet[ICNetVersion2]=3.1; ICNet[LoginType]=9djdei9qSou56XVLfue19Q%3D%3D; ICNet[UserBehavior]=XrLLZ2EqkNG67iJG8s_rLA%3D%3D; ICNet[ICNETUUID]=KXKaIScvsaGKEXVY8apuNO_MWCfDN536JJGYVV44214%3D; PHPSESSID=a4thqcgccps2tpgctljek8etg6; ICNet[SearchLog][0]=MC74HC1G14DFT2G; ICNet[SearchLog][1]=STM32F103C8T6; ICNet[sct]=59af177e5516ba900c999cb93d120d7491f030be; gdxidpyhxdE=pNY54%5CQdvdpv5WLnSGI%2FmfL34xRXR1KIIv%5CMIv6Uu6jCgxv0uIckOChJ9hX3C4tj9lI5QTvBijvOh7mBVetvUES2A2q23E%5CbIq7h4gp3fDjvwZ81oAc8P51ValaR40Yn0xCODia2h1O%2FKHQXjEotYYRPS6%5CQl2rZ0RNhP6hT4b3kVmOi%3A1705997297238; ICNet[jpk]=%5B%22zWn%22%5D; ICNet[sgj]=%5B%22zcPUAzzS%22%2C%22zcHcAznP%22%2C%22zLHzAzHU%22%2C%22zszSAzcz%22%2C%22zcLUAznL%22%2C%22zHLPAzUP%22%2C%22znczAzsH%22%2C%22zzLWAWSS%22%2C%22zPSHAWsz%22%2C%22sLPAnWS%22%2C%22snWAncP%22%2C%22szUAnLs%22%2C%22LLnASnz%22%2C%22LUWAScP%22%2C%22LHSAHPs%22%2C%22LHWAHSc%22%2C%22LScAHLH%22%2C%22LnLAUnP%22%2C%22LncAUnL%22%2C%22LncAUSc%22%2C%22LSPAUSs%22%2C%22LSHAUHz%22%2C%22LHPAUHz%22%2C%22LUWAUHP%22%2C%22sPnAUSH%22%2C%22sSPAUSn%22%2C%22zPWnAUnn%22%2C%22zzWLAUzc%22%2C%22zWWUAUPP%22%2C%22znWzAHcs%22%2C%22znssAHUP%22%2C%22zSUcAHnL%22%2C%22zSLSAHnS%22%2C%22zHzsAHWL%22%2C%22zHUzAHzs%22%2C%22zUPnAHzn%22%2C%22zUnHAHPs%22%2C%22zUUcAHPL%22%2C%22zczSAHPs%22%2C%22zcUnAHzW%22%2C%22zcsWAHzS%22%2C%22zLPnAHzU%22%2C%22zLPHAHzs%22%2C%22zLPSAHWn%22%2C%22zcscAHWs%22%2C%22zcLHAHnU%22%2C%22zccUAHSW%22%2C%22zcULAHSU%22%2C%22zcUzAHSs%22%2C%22zcHWAHHW%22%2C%22zcSzAHHS%22%2C%22zcWsAHHH%22%2C%22zcWWAHHH%22%2C%22zcWzAHHH%22%2C%22zcWzAHHH%22%2C%22zcWPAHHH%22%2C%22zczLAHHS%22%2C%22zczcAHHS%22%2C%22zczUAHHz%22%2C%22zczSAHnU%22%2C%22zczWAHzH%22%2C%22zcPLASLc%22%2C%22zcPWASUP%22%2C%22zUsLASnn%22%2C%22zUsSASPc%22%2C%22zUsPAnLz%22%2C%22zULUAnHP%22%2C%22zULPAnzn%22%2C%22zUczAWUc%22%2C%22zUULAWnz%22%2C%22zUUHAWPz%22%2C%22zUUnAzcU%22%2C%22zUHsAzSz%22%2C%22zUHLAznW%22%2C%22zUHHAzzH%22%2C%22zUHnAzPW%22%2C%22zUHWAsz%22%2C%22zUHPAcL%22%2C%22zUHPAUn%22%2C%22zUHzASH%22%2C%22zUHWAWc%22%2C%22zUHUAU%22%2C%22zUHsAP%22%2C%22zcPnAWs%22%2C%22zcPHAHc%22%2C%22zcPUAzzW%22%2C%22zcPUAzcL%22%2C%22zcPSAWSH%22%2C%22zcPSAnPL%22%2C%22zcPSAnUn%22%2C%22zcPWASzz%22%2C%22zcPWASWH%22%2C%22zcPPASnc%22%2C%22zcPPASSW%22%2C%22zUSSASzW%22%2C%22zUSnASzz%22%2C%22zUSWASzz%22%2C%22zUSzASzz%22%2C%22zUnLASzz%22%2C%22zUncASzz%22%5D'
        ua = UserAgent()
        for url in self.start_urls:
            headers = {
                "User-Agent": ua.random,
                "Cookie": cookies
            }
            yield scrapy.Request(url, headers=headers, dont_filter=True)

    def parse(self, response):
        post_nodes = response.css("#resultList > li:nth-child(5) > div.result_supply > a")
        print(post_nodes)
