import re
#str ="<p class=\"MsoNormal\">You are&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>Customer-centric above all: You have an&#160;entrepreneurial spirit and you always act with the customer in mind. You have a background within sales or customer service, and you love to deliver an excellent customer experience</li><li>Eager to learn: We don&#8217;t require you to be an automotive expert, but we expect you to have a genuine interest in cars and technology and be eager to learn</li><li>An excellent communicator: You communicate clearly and respectfully in English and Norwegian</li><li>Flexible team player: You like collaborating closely with different kinds of people and can work in shifts to support your team. This may include weekends as well as morning and evening shifts.</li><li>Target oriented: You are resilient, and you like to meet your deadlines and goals</li><li>Safe to drive: We require you to hold a full valid driver&#8217;s license</li></ul><p><br></p><p>We offer&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>Customer-centric above all: You have an&#160;entrepreneurial spirit and you always act with the customer in mind. You have a background within sales or customer service, and you love to deliver an excellent customer experience</li><li>Eager to learn: We don&#8217;t require you to be an automotive expert, but we expect you to have a genuine interest in cars and technology and be eager to learn</li><li>An excellent communicator: You communicate clearly and respectfully in English and Norwegian</li><li>Flexible team player: You like collaborating closely with different kinds of people and can work in shifts to support your team. This may include weekends as well as morning and evening shifts.</li><li>Target oriented: You are resilient, and you like to meet your deadlines and goals</li><li>Safe to drive: We require you to hold a full valid driver&#8217;s license</li></ul><p><br></p><p>We offer&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>A dynamic and fast-paced environment where inclusion, learning and collaboration are key to success</li><li>The chance to work with the world&#8217;s most innovative products and technology</li><li>Ongoing training and development to help you grow your skills and career</li><li>A competitive compensation and benefits package</li><li>A safe, clean and fun workplace</li></ul><p><br>Join the mission.<br><br>Apply today.<br><br>Note that applications must be submitted online and contain an English CV.<br><br>To be considered for our roles in Norway it is required that you already have the right to work within Norway/ EU/ EEA.</p>"
#str =	"<p class=\"MsoNormal\">You will&#8230;</p><ul class=\"tds-list tds-list--unordered\"><li>Act as a Tesla&#160;ambassador: You will generate excitement about our products and build awareness about our mission, by welcoming customers to our stores, proactively networking,&#160;capturing new leads and conducting sales events</li><li>Manage the full 360 sales process: You will give customers an excellent experience: you will provide information and expert advice about products, perform test-drives, arrange financing solutions, and guide customers through the order process, up to the delivery of their new Tesla vehicles</li><li>Be a trusted partner for customers and for your colleagues: You will ensure effective&#160;collaboration,&#160;smooth communication and timely support</li></ul>"
# str = 	"Do you want to help accelerate the world&#8217;s transition to sustainable energy?<br><br>At Tesla, that&#8217;s our mission.<br><br>Our Tesla Advisors&#160;are our front-line experts in accelerating the world&#8217;s transition to sustainable energy, giving customers a personalized experience as memorable as our products themselves."
def RegularTitle(str):
    r =re.compile(r'<[^>]+>')#regular expression    <p class=\"MsoNormal\">  </p>
    ret_str=r.sub("",str).strip()    
    r =re.compile(r'&#.*?;')#regular expression &#8230;
    return r.sub(" ",ret_str).strip()