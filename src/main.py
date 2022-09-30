#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author：liguoqing
# @Creat Date：2022-09-27
# @description :
# @Update Date  : 2022-09-27

import time
import pandas as pd
import random
import sys
import os

from parsejobjson import ParseTelsaJobJson
from parseurl import CrawlUrl
#self-define 
 
       
if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1)
        print(arg2)
    #https://www.tesla.com/careers/search/
    crawl_teslajob =CrawlUrl("https://www.tesla.com/cua-api/apps/careers/state")    
    jsonfile = crawl_teslajob.getpage()
    # print (type(jsonfile))  #<class 'dict'>
    # print(len(jsonfile))
    for k in jsonfile:        
        # print(type(k))  #<class 'str'>
        # print(k)                      
        data_tesla_title,data_tesla_requirements,data_tesla_timeType =[],[],[]
        data_tesla_department,data_tesla_family,data_tesla_location,data_tesla_description =[],[],[],[]
        data_tesla_url,data_tesla_responsibilities =[],[]
        
        dict_tesla={'Position Title':data_tesla_title,
            'Departments':data_tesla_department,
            'jobFamily':data_tesla_family,
            'location':data_tesla_location,
            'jobDescription':data_tesla_description,
            'jobResponsibilities':data_tesla_responsibilities,
            'jobRequirements':data_tesla_requirements,
            'timeType':data_tesla_timeType,
            'Url':data_tesla_url,}  #url json  = https://www.tesla.com/cua-api/careers/job/151627 
        
        if k=="listings":
            # print(len(jsonfile["listings"]))
            counters=0
            for k1 in jsonfile["listings"]:
                # print(type(k1))  #<class 'dict'>
                # print(k1)                
                tesla_job =CrawlUrl(r'https://www.tesla.com/cua-api/careers/job/'+k1['id'])
                counters+=1
                job_json = tesla_job.getpage()
                if job_json:
                    job_x = ParseTelsaJobJson(job_json)
                    data_tesla_requirements.append(job_x.jobRequirements)
                    data_tesla_timeType.append(job_x.timeType)
                    data_tesla_department.append(job_x.department)
                    data_tesla_family.append(job_x.jobFamily)
                    data_tesla_location.append(job_x.location)
                    data_tesla_description.append(job_x.description)
                    # data_tesla_url.append(job_x.applyUrl)
                    data_tesla_responsibilities.append(job_x.jobResponsibilities)
                    data_tesla_title.append(job_x.title)                                
                    data_tesla_url.append(r'https://www.tesla.com/careers/search/job/'+k1['id'])      
                    print("Total: "+str(len(jsonfile["listings"]))+"/"+str(counters)+": id"+k1['id']+"  Success!")
                else:
                    
                    data_tesla_requirements.append("job_x.jobRequirements")
                    data_tesla_timeType.append("job_x.timeType")
                    data_tesla_department.append("job_x.department")
                    data_tesla_family.append("job_x.jobFamily")
                    data_tesla_location.append("job_x.location")
                    data_tesla_description.append("job_x.description")
                    # data_tesla_url.append(job_x.applyUrl)
                    data_tesla_responsibilities.append("job_x.jobResponsibilities")
                    data_tesla_title.append(k1['t'])                                
                    data_tesla_url.append(r'https://www.tesla.com/careers/search/job/'+k1['id'])      
                    print("Total: "+str(len(jsonfile["listings"]))+"/"+str(counters)+": id"+k1['id']+"  Fail!")
                                   
                # time.sleep(random.uniform(0.2,2))
                # if counters >1 :
                #     break
            df = pd.DataFrame(dict_tesla)
            path = 'telsa%s.xlsx'%(round(time.time()))      
            df.to_excel(os.getcwd()+'\\logs\\'+path)
        