import time

from lemoncheesecake.project import Project

# TODO: create the ssl cert.
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FruityviceProject(Project):

    def build_report_info(self):
        return [("app", "FV REST"), ('version', "0.0.0")]

    def build_report_title(self):
        return "Fruityvice backend REST API %s" % time.asctime()


project = FruityviceProject()
