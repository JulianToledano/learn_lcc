# suites/get_all.py contents

import requests

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *


@lcc.suite("GET all fruityvice fruits")
class GetFruits:

    @lcc.test("Get all fruits")
    def get_all_fruits(self, url):
        url = ''.join([url, 'all'])
        lcc.log_info('GET %s' % url)
        response = requests.get(url=url, verify=False)
        check_that("response code", response.status_code, equal_to(200))