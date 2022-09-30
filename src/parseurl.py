import requests
import time
import json   

class CrawlUrl :
    def __init__(self,url):
        self.url = url
        self.headers = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
                        }

    def getpage (self):
        try :
            t = requests.get(self.url,headers=self.headers)
            print(t.status_code)
            if t.status_code == 200 :
                return t.json()
            else:
                # while True :
                    time.sleep(20)
                    t = requests.get(self.url,headers=self.headers)
                    
                    if t.status_code == 200 :
                        print(t.status_code)
                        return t.json()
                        # break
                    else:
                        print(t.status_code)
                        return None
                        # raise Exception
                # return t.json()
                
        except Exception as e:
            print("except:",e)
            print(t)
            print(self.url)
        # finally:
        #     print("exception finally")
    
    def parse(self,jsonfile):
        if jsonfile:
            print (jsonfile)
            return True
    def save2json(self,jsonfile):
        tempjsonfile = json.dumps(jsonfile,ensure_ascii=True)
        with open("job.json", 'w') as f:
            f.write(tempjsonfile)
            f.close()                    
    
    def run(self):
       jsonfile = self.getpage()
       self.parse(jsonfile)
       self.save2json(jsonfile)