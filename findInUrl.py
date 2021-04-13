from bs4 import BeautifulSoup
import requests


class FindInUrl:

    def __init__(self, url: str, tag_name: dict, class_name: dict, key_word: str):
        """
        :param url: site's url that you want
        :param tag_name:
                tag_name={
                root:"root html tag to filter content",
                apply_link:"tag name of apply button",
                published_date:"tag or date filter"
                company_name:"tag of company name, like h3, h2, h4...",
                skills:"tag to identify wanted skills"
            }
        :param class_name:
            tag_name={
                root:"root html class to filter content",
                apply_link:"class name of apply button",
                published_date:"class of date filter"
                company_name:"class of company name, like h3, h2, h4...",
                skills:"class to identify wanted skills"
            }
        :param key_word: "String to identify only new contents",
        :return: use the method find() to get jobs -> [company_name, skills, published_date, apply_link]
        """
        self.url = url
        self.tag_name = tag_name
        self.class_name = class_name
        self.key_word = key_word

    @staticmethod
    def get_html(url: str) -> str:
        """
        :rtype: str
        """
        return requests.get(url).text

    @staticmethod
    def http_soup(html_text):

        return BeautifulSoup(html_text, 'lxml')

    def http_filter(self, http_text, filters):
        """
        :param http_text: str
        :type filters: dict
        :rtype: BeautifulSoup
        :param filters: has to be a dict in this structure -> {name:"tag html", kwargs:"class_="classes name""
        """
        filtered = self.http_soup(http_text).find_all(filters['name'], class_=filters["class_"])
        return filtered

    def find(self):
        http_text: str = self.get_html(self.url)
        filters = dict(name=self.tag_name["root"], class_=self.class_name["root"])
        # noinspection PyTypeChecker
        tags = self.http_filter(http_text, filters)
        jobs = []

        for tag in tags:
            published_date = tag.find(self.tag_name['published_date'], class_=self.class_name['published_date']).text \
                .replace('\r', '').replace('\n', '')

            if self.key_word in published_date:
                apply_link = tag.find(self.tag_name['apply_link']).a['href']
                company_name = tag.find(self.tag_name['company_name'], class_=self.class_name['company_name']).text \
                    .replace(' ', '').replace('\r', '').replace('\n', '')
                skills = tag.find(self.tag_name['skills'], class_=self.class_name['skills']).text.replace(' ', '') \
                    .replace('\r', '').replace('\n', '')

                jobs.insert(0, {'company_name':company_name,
                                'skills':skills,
                                'published_date':published_date,
                                'apply_link':apply_link})

        return jobs
