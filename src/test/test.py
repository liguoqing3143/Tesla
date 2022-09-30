# import re
import os
print(r'\logs\x.xlsx')
print(os.getcwd()+r'\logs\x.xlsx')
print( os.path.join(os.getcwd(),'\\logs\\x.xlsx'))






# str ="<p class=\"MsoNormal\">You are&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>Customer-centric above all: You have an&#160;entrepreneurial spirit and you always act with the customer in mind. You have a background within sales or customer service, and you love to deliver an excellent customer experience</li><li>Eager to learn: We don&#8217;t require you to be an automotive expert, but we expect you to have a genuine interest in cars and technology and be eager to learn</li><li>An excellent communicator: You communicate clearly and respectfully in English and Norwegian</li><li>Flexible team player: You like collaborating closely with different kinds of people and can work in shifts to support your team. This may include weekends as well as morning and evening shifts.</li><li>Target oriented: You are resilient, and you like to meet your deadlines and goals</li><li>Safe to drive: We require you to hold a full valid driver&#8217;s license</li></ul><p><br></p><p>We offer&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>Customer-centric above all: You have an&#160;entrepreneurial spirit and you always act with the customer in mind. You have a background within sales or customer service, and you love to deliver an excellent customer experience</li><li>Eager to learn: We don&#8217;t require you to be an automotive expert, but we expect you to have a genuine interest in cars and technology and be eager to learn</li><li>An excellent communicator: You communicate clearly and respectfully in English and Norwegian</li><li>Flexible team player: You like collaborating closely with different kinds of people and can work in shifts to support your team. This may include weekends as well as morning and evening shifts.</li><li>Target oriented: You are resilient, and you like to meet your deadlines and goals</li><li>Safe to drive: We require you to hold a full valid driver&#8217;s license</li></ul><p><br></p><p>We offer&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>A dynamic and fast-paced environment where inclusion, learning and collaboration are key to success</li><li>The chance to work with the world&#8217;s most innovative products and technology</li><li>Ongoing training and development to help you grow your skills and career</li><li>A competitive compensation and benefits package</li><li>A safe, clean and fun workplace</li></ul><p><br>Join the mission.<br><br>Apply today.<br><br>Note that applications must be submitted online and contain an English CV.<br><br>To be considered for our roles in Norway it is required that you already have the right to work within Norway/ EU/ EEA.</p>"
# str =	"<p class=\"MsoNormal\">You will&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>Act as a Tesla&#160;ambassador: You will generate excitement about our products and build awareness about our mission, by welcoming customers to our stores, proactively networking,&#160;capturing new leads and conducting sales events</li><li>Manage the full 360 sales process: You will give customers an excellent experience: you will provide information and expert advice about products, perform test-drives, arrange financing solutions, and guide customers through the order process, up to the delivery of their new Tesla vehicles</li><li>Be a trusted partner for customers and for your colleagues: You will ensure effective&#160;collaboration,&#160;smooth communication and timely support</li></ul>"
# # str = 	"Do you want to help accelerate the world&#8217;s transition to sustainable energy?<br><br>At Tesla, that&#8217;s our mission.<br><br>Our Tesla Advisors&#160;are our front-line experts in accelerating the world&#8217;s transition to sustainable energy, giving customers a personalized experience as memorable as our products themselves."

# r =re.compile(r'<[^>]+>')#regular expression    <p class=\"MsoNormal\">  </p>
# p=r.sub("",str).strip()
# print(p)
# r =re.compile(r'&#.*?;')#regular expression &#8230;
# p=r.sub(" ",p)
# print(p)

# import argparse

# def main():
#     parser = argparse.ArgumentParser(description="Demo of argparse")
#     parser.add_argument('-n','--name', default=' Li ')
#     parser.add_argument('-y','--year', default='20')
#     args = parser.parse_args()
#     print(args)
#     name = args.name
#     year = args.year
#     print('Hello {}  {}'.format(name,year))
# # ————————————————
# # 版权声明：本文为CSDN博主「骑着蜗牛向前跑」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# # 原文链接：https://blog.csdn.net/yy_diego/article/details/82851661


"""lookup <class 'str'> 
types  layer1 type:dict
{'1': 'fulltime', '2': 'parttime', '3': 'intern', '4': 'seasonal'} layer2 type:dict
1   
fulltime    layer3 type:str
2
parttime
3
intern
4
seasonal
"""
# if k=="lookup":
#     for k1 in jsonfile["lookup"]:
#         print(type(k1))
#         print(k1)
#         print(jsonfile["lookup"][k1])
#         for kk1 in jsonfile["lookup"][k1]:
#             print(type(kk1))
#             print(kk1)
#             print(jsonfile["lookup"][k1][kk1])
"""departments <class 'str'> 
14  layer1  type:str --> lookup['departments']
['1', '2'] layer2 type:list
"""
# if k=="departments":
#     for k1 in jsonfile["departments"]:
#         print(type(k1))
#         print(k1)
#         print(jsonfile["departments"][k1])
#         for kk1 in jsonfile["departments"][k1]:
#             print(type(kk1))
#             print(kk1)
            

"""geo <class 'str'> 
14  layer1  -->type:dict
['1', '2'] layer2
"""
# if k == "geo":
#     for k1 in jsonfile["geo"]:
#         print(type(k1))#<class 'dict'>
#         #print(k1) 
#         for kk1 in k1:
#             print(type(kk1))#<class 'str'>
#             print(kk1)
#             print(k1[kk1])
#             if len(k1[kk1])>1:# layer2
#                 for kkk1 in k1[kk1]:
#                     print(type(kkk1))#<class 'str'>
#                     if isinstance(kkk1,str):
#                         print(k1[kk1][kkk1])
#                         if len(k1[kk1][kkk1])>1:# layer3
#                             for kkkk1 in k1[kk1][kkk1]:
#                                 if isinstance(kkkk1,str):
#                                     print(k1[kk1][kkk1][kkkk1])
#                                 elif isinstance(kkkk1,dict):
#                                     print(kkkk1)
#                     elif isinstance(kkk1,dict) :                            
#                         print(kkk1)
#                         for kkkd1 in kkk1:
#                                 if isinstance(kkkd1,str):
#                                     print(kkk1[kkkd1])
#                                 elif isinstance(kkkd1,dict):
#                                     print(kkkd1)        
"""listings <class 'str'> 
14  layer1  -->
['1', '2'] layer2
"""