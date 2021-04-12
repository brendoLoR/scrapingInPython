import findInUrl as fd

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
    'Posted few days ago')
print(finder.find())