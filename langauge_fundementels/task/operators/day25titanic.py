"""
 q1 : number of survived passengers
# q2 : displau unique passenger class 
# q3 number of female passengers
# q4: number of survived childs 
# q5: name whose fare > 30
# q6: number survived female
# q7:top fare
# q8 : survived peoples name
# q9:survived classes
# q10:female survival rate
"""
# titanic_data = [
#     {"id": 1, "survived": 0, "pclass": 3, "class": "Third", "name": "Braund, Mr. Owen Harris", "sex": "male", "age": 22, "fare": 7.25},
#     {"id": 2, "survived": 1, "pclass": 1, "class": "First", "name": "Cumings, Mrs. John Bradley (Florence)", "sex": "female", "age": 38, "fare": 71.28},
#     {"id": 3, "survived": 1, "pclass": 3, "class": "Third", "name": "Heikkinen, Miss. Laina", "sex": "female", "age": 26, "fare": 7.92},
#     {"id": 4, "survived": 1, "pclass": 1, "class": "First", "name": "Futrelle, Mrs. Jacques Heath (Lily)", "sex": "female", "age": 35, "fare": 53.10},
#     {"id": 5, "survived": 0, "pclass": 3, "class": "Third", "name": "Allen, Mr. William Henry", "sex": "male", "age": 35, "fare": 8.05},
#     {"id": 6, "survived": 0, "pclass": 3, "class": "Third", "name": "Moran, Mr. James", "sex": "male", "age": 28, "fare": 8.45},
#     {"id": 7, "survived": 0, "pclass": 1, "class": "First", "name": "McCarthy, Mr. Timothy J", "sex": "male", "age": 54, "fare": 51.86},
#     {"id": 8, "survived": 0, "pclass": 3, "class": "Third", "name": "Palsson, Master. Gosta Leonard", "sex": "male", "age": 2, "fare": 21.07},
#     {"id": 9, "survived": 1, "pclass": 3, "class": "Third", "name": "Johnson, Mrs. Oscar W (Elisabeth)", "sex": "female", "age": 27, "fare": 11.13},
#     {"id": 10, "survived": 1, "pclass": 2, "class": "Second", "name": "Nasser, Mrs. Nicholas (Adele)", "sex": "female", "age": 14, "fare": 30.07},
#     {"id": 11, "survived": 1, "pclass": 3, "class": "Third", "name": "Sandstrom, Miss. Marguerite Rut", "sex": "female", "age": 4, "fare": 16.70},
#     {"id": 12, "survived": 1, "pclass": 1, "class": "First", "name": "Bonnell, Miss. Elizabeth", "sex": "female", "age": 58, "fare": 26.55},
#     {"id": 13, "survived": 0, "pclass": 3, "class": "Third", "name": "Saundercock, Mr. William Henry", "sex": "male", "age": 20, "fare": 8.05},
#     {"id": 14, "survived": 0, "pclass": 3, "class": "Third", "name": "Andersson, Mr. Anders Johan", "sex": "male", "age": 39, "fare": 31.27},
#     {"id": 15, "survived": 0, "pclass": 3, "class": "Third", "name": "Vestrom, Miss. Hulda Amanda Adolfina", "sex": "female", "age": 14, "fare": 7.85},
#     {"id": 16, "survived": 1, "pclass": 2, "class": "Second", "name": "Hewlett, Mrs. (Mary D Kingcome)", "sex": "female", "age": 55, "fare": 16.00},
#     {"id": 17, "survived": 0, "pclass": 2, "class": "Second", "name": "Williams, Mr. Charles Eugene", "sex": "male", "age": 28, "fare": 13.00}
# ]
# survived_pasn=[di for di in titanic_data if di.get("survived")==1]
# print("no of survived passenger:",len(survived_pasn))
# passn_class={di.get("class") for di in titanic_data}
# print(passn_class)
# fem_pass=[di for di in titanic_data if di.get("sex")=="female"]
# print("num of female passnger",len(fem_pass))
# sur_childs=[di for di in titanic_data if di.get("survived")==1 and di.get("age")<=13]
# print("num of survived child:",len(sur_childs))
# name=[di.get("name") for di in titanic_data if di.get("fare")>30]
# print(name)
# sur_female=[di for di in titanic_data if di.get("sex")=="female" and di.get("survived")==1]
# print("no of suvived female:",len(sur_female))
# fare=max([di.get("fare",0) for di in titanic_data ])
# print("top fare:",fare)
# sur_people=[di.get("name") for di in titanic_data if di.get("survived")==1]
# print(sur_people)
# sur_class={di.get("class") for di in titanic_data if di.get("survived")==1}
# print(sur_class)
# fem_sur_rate=[di.get("sex") for di in titanic_data if di.get("sex")=="female" and di.get("survived")==1]
# print(round(fem_sur_rate.count("female")/len(fem_pass)*100,2))
"""

"""
leads = [
    {"source": "LinkedIn", "status": "New", "title": "Data Analyst", "course": "Advanced SQL & Python", "created_date": "15-02-26"},
    {"source": "Organic Search", "status": "Contacted", "title": "Software Engineer", "course": "Full-Stack Development", "created_date": "16-02-26"},
    {"source": "Referral", "status": "Qualified", "title": "Project Manager", "course": "Agile Methodologies", "created_date": "16-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "Marketing Specialist", "course": "Digital Growth Hacking", "created_date": "17-02-26"},
    {"source": "Webinar", "status": "Nurturing", "title": "Student", "course": "Introduction to Machine Learning", "created_date": "17-02-26"},
    {"source": "LinkedIn", "status": "Unqualified", "title": "HR Manager", "course": "Data Visualization", "created_date": "18-02-26"},
    {"source": "Direct Traffic", "status": "Converted", "title": "Freelance Designer", "course": "UI/UX Design Masterclass", "created_date": "18-02-26"},
    {"source": "Google Ads", "status": "New", "title": "Business Analyst", "course": "Tableau for Beginners", "created_date": "19-02-26"},
    {"source": "Organic Search", "status": "Nurturing", "title": "Systems Admin", "course": "Cloud Architecture (AWS)", "created_date": "19-02-26"},
    {"source": "Referral", "status": "Contacted", "title": "Product Owner", "course": "Scrum Certification", "created_date": "20-02-26"},
    {"source": "LinkedIn", "status": "Qualified", "title": "Junior Developer", "course": "React & Next.js", "created_date": "20-02-26"},
    {"source": "Twitter", "status": "New", "title": "Content Creator", "course": "Video Editing Pro", "created_date": "21-02-26"},
    {"source": "Webinar", "status": "New", "title": "Operations Lead", "course": "Lean Six Sigma", "created_date": "21-02-26"},
    {"source": "Facebook Ads", "status": "Unqualified", "title": "Retail Associate", "course": "Cybersecurity Fundamentals", "created_date": "22-02-26"},
    {"source": "Direct Traffic", "status": "Converted", "title": "Backend Dev", "course": "Go Programming", "created_date": "22-02-26"},
    {"source": "LinkedIn", "status": "Nurturing", "title": "Data Scientist", "course": "Deep Learning Specialization", "created_date": "23-02-26"},
    {"source": "Google Ads", "status": "Contacted", "title": "Sales Manager", "course": "CRM Automation", "created_date": "23-02-26"},
    {"source": "Organic Search", "status": "New", "title": "IT Consultant", "course": "Ethical Hacking", "created_date": "24-02-26"},
    {"source": "Referral", "status": "Converted", "title": "CTO", "course": "Executive Leadership", "created_date": "24-02-26"},
    {"source": "Webinar", "status": "Qualified", "title": "QA Engineer", "course": "Automated Testing", "created_date": "25-02-26"},
    {"source": "LinkedIn", "status": "New", "title": "UX Researcher", "course": "Design Thinking", "created_date": "25-02-26"},
    {"source": "Organic Search", "status": "Nurturing", "title": "Financial Analyst", "course": "Excel Macros & VBA", "created_date": "25-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "Small Business Owner", "course": "Social Media Marketing", "created_date": "26-02-26"},
    {"source": "Twitter", "status": "Unqualified", "title": "Accountant", "course": "Python for Finance", "created_date": "26-02-26"},
    {"source": "Google Ads", "status": "Contacted", "title": "Network Engineer", "course": "Cisco CCNA Prep", "created_date": "26-02-26"},
    {"source": "LinkedIn", "status": "New", "title": "Full Stack Dev", "course": "Node.js Microservices", "created_date": "27-02-26"},
    {"source": "Direct Traffic", "status": "Qualified", "title": "Graphic Designer", "course": "Motion Graphics", "created_date": "27-02-26"},
    {"source": "Referral", "status": "New", "title": "Graduate Student", "course": "Data Science Boot Camp", "created_date": "27-02-26"},
    {"source": "Webinar", "status": "Nurturing", "title": "SEO Specialist", "course": "Advanced SEO 2024", "created_date": "01-02-26"},
    {"source": "LinkedIn", "status": "Converted", "title": "Technical Writer", "course": "API Documentation", "created_date": "02-02-26"},
    {"source": "Organic Search", "status": "Contacted", "title": "Security Analyst", "course": "CompTIA Security+", "created_date": "03-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "E-commerce Manager", "course": "Shopify Mastery", "created_date": "04-02-26"},
    {"source": "Google Ads", "status": "Qualified", "title": "Database Admin", "course": "NoSQL Databases", "created_date": "05-02-26"},
    {"source": "Twitter", "status": "New", "title": "Copywriter", "course": "AI for Writing", "created_date": "06-02-26"},
    {"source": "LinkedIn", "status": "Nurturing", "title": "App Developer", "course": "SwiftUI & iOS", "created_date": "07-02-26"},
    {"source": "Webinar", "status": "Unqualified", "title": "Teacher", "course": "EdTech Integration", "created_date": "08-02-26"},
    {"source": "Referral", "status": "Contacted", "title": "VP of Engineering", "course": "Scaling Tech Teams", "created_date": "09-02-26"},
    {"source": "Direct Traffic", "status": "New", "title": "Web Designer", "course": "Webflow Mastery", "created_date": "10-02-26"},
    {"source": "Organic Search", "status": "Qualified", "title": "Risk Analyst", "course": "Quantitative Finance", "created_date": "11-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "Artist", "course": "NFT & Crypto Art", "created_date": "12-02-26"},
    {"source": "LinkedIn", "status": "Converted", "title": "Cloud Architect", "course": "Google Cloud Professional", "created_date": "13-02-26"},
    {"source": "Google Ads", "status": "Nurturing", "title": "Marketing Director", "course": "Omnichannel Strategy", "created_date": "14-02-26"},
    {"source": "Webinar", "status": "New", "title": "Logistics Coordinator", "course": "Supply Chain Mgmt", "created_date": "15-02-26"},
    {"source": "Twitter", "status": "Contacted", "title": "Blogger", "course": "Affiliate Marketing", "created_date": "16-02-26"},
    {"source": "Referral", "status": "New", "title": "HR Specialist", "course": "Conflict Resolution", "created_date": "17-02-26"},
    {"source": "Direct Traffic", "status": "Qualified", "title": "Frontend Dev", "course": "Vue.js Framework", "created_date": "18-02-26"},
    {"source": "LinkedIn", "status": "Nurturing", "title": "DevOps Engineer", "course": "Kubernetes in Practice", "created_date": "19-02-26"},
    {"source": "Organic Search", "status": "Converted", "title": "Product Manager", "course": "Product Analytics", "created_date": "20-02-26"},
    {"source": "Facebook Ads", "status": "Unqualified", "title": "Chef", "course": "Culinary Management", "created_date": "21-02-26"},
    {"source": "Google Ads", "status": "New", "title": "Legal Assistant", "course": "Legal Tech & AI", "created_date": "22-02-26"}
]
"""
"""
all_source={l.get("source")for l in leads}
# print("all sources",all_source)

all_source_lst=[l.get("source")for l in leads]
source_count={l:all_source_lst.count(l)for l in all_source_lst}
# print(source_count)

qualified_leads=[l.get("status") for l in leads]
# print(len(qualified_leads))
status_count={l:qualified_leads.count(l) for l in qualified_leads}
# print(status_count)


qualified_rate= status_count.get("Qualified",1)/sum(status_count.values())
# print(qualified_rate)
conv_rate=status_count.get("Converted",1)/sum(status_count.values())*100
# print(conv_rate)
un_qualified_rate=status_count.get("Unqualified",1)/sum(status_count.values())*100
# print(un_qualified_rate)
"""
"""
google_ad_qf=[l.get("status") for l in leads if l.get("source")=="Google Ads"]
google_ad={l:google_ad_qf.count(l) for l in google_ad_qf}
google_ad_qf_rate=google_ad.get("Converted",0)/sum(google_ad.values())
print(google_ad_qf_rate)
"""
"""
# courses_lead=[l.get("course")for l in leads]
# courses_lead_count={l:courses_lead.count(l) for l in courses_lead}
# print(courses_lead_count)