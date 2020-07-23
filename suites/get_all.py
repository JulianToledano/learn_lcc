# suites/get_all.py contents

import requests

import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

@lcc.suite("GET all fruityvice fruits")
class GetFruits:

    @lcc.test("Get all fruits")
    def key_already_exists(self):
        response = requests.get(
            url='http://www.fruityvice.com/api/fruit/all')
        check_that("response code", response.status_code, equal_to(200))
