import requests

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *


@lcc.suite("GET all fruits from a family")
class GetFruits:

    @lcc.test("Get all Rutaceae fruits")
    def get_rutaceae(self):
        family = 'Rutaceae'
        url = ''.join(['http://www.fruityvice.com/api/fruit/family/', family])
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))

    @lcc.test("Get all Bromeliaceae fruits")
    def get_bromeliaceaeg(self):
        family = 'Bromeliaceae'
        url = ''.join(['http://www.fruityvice.com/api/fruit/family/', family])
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))


class CheckByFamily(object):

    def __init__(self, url):
        self.url = url

    def __call__(self):
        response = requests.get(url=self.url, verify=False)
        check_that("response code", response.status_code, equal_to(200))


@lcc.suite("Get by family")
class get:

    def __init__(self):
        data = [
            'Musaceae', 'Anacardiaceae', 'Rutaceae', 'Cucurbitaceae',
            'Solanaceae', 'Bromeliaceae', 'Rosaceae'
        ]
        for family in data:
            url = ''.join(
                ['http://www.fruityvice.com/api/fruit/family/', family])
            test = lcc.Test(family, ''.join(['Get all by ', family]),
                            CheckByFamily(url))
            lcc.add_test_into_suite(test, self)
