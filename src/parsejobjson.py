import re
class ParseTelsaJobJson :
    
    def __init__(self, job_json):
        self.id=job_json['id']
        self.title=job_json['title']
        self.department=job_json['department']
        self.jobFamily=job_json['jobFamily']
        self.location=job_json['location']
        self.description=job_json['description']
        self.jobDescription=self.regulartitle(job_json['jobDescription'])
        self.jobResponsibilities=self.regulartitle(job_json['jobResponsibilities'])
        self.jobRequirements=self.regulartitle(job_json['jobRequirements'])
        self.jobCompensationAndBenefits=job_json['jobCompensationAndBenefits']
        self.applicationType=job_json['applicationType']
        self.isGrohmann=job_json['isGrohmann']
        self.timeType=job_json['timeType']
        self.subWorkerType=job_json['subWorkerType']
        self.url=job_json['url']
        self.applyUrl=job_json['applyUrl']
        
    def regulartitle(self,str):
        r =re.compile(r'<[^>]+>')#regular expression    <p class=\"MsoNormal\">  </p>
        ret_str=r.sub("",str).strip()    
        r =re.compile(r'&#.*?;')#regular expression &#8230;
        return r.sub(" ",ret_str).strip()