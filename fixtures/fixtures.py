import requests
import random
import string
import json
import lemoncheesecake.api as lcc


@lcc.fixture(scope="session")
def url():
    return 'http://www.fruityvice.com/api/fruit/'


@lcc.fixture(scope="test")
def new_fruit():
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(16))
    return {
        "genus": "Fragaria",
        "name": name,
        "family": "Rosaceae",
        "order": "Rosales",
        "nutritions": {
            "carbohydrates": 5,
            "protein": 5,
            "fat": 5,
            "calories": 5,
            "sugar": 5
        }
    }


@lcc.fixture(scope="test")
def put_new_fruit(url, new_fruit):
    response = requests.put(url=url,
                            headers={'Content-Type': 'application/json'},
                            data=json.dumps(new_fruit),
                            verify=False)
    return new_fruit, response
