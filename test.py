import findInUrl as fd
import database as db


def testFinder():

    tag_name={
        'root': 'li',
        'apply_link': 'h2',
        'published_date':'span',
        'company_name': 'h3',
        'skills':'span'}
    class_name={
        'root': 'clearfix job-bx wht-shd-bx',
        'apply_link': '',
        'published_date':'sim-posted',
        'company_name': 'joblist-comp-name',
        'skills':'srp-skills'}

    finder = fd.FindInUrl(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=",
        tag_name,
        class_name,
        'Posted few days ago').find()
    return finder

def testDbConnection():
    print(db.connect("scrapingdb"))

def testInserts():
    jobList = testFinder()
    for job in jobList:
        print(db.insert('scrapingdb', 'jobs_offers',
                        ('SITE_ID', 'COMPANY_NAME', 'SKILLS', 'APPLY_LINK'),
                        ('0',job['company_name'],job['skills'], job['apply_link'])))
testInserts()