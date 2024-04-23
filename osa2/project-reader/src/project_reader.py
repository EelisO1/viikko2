from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        
        toml_dict = toml.loads(content)        
        name = toml_dict["tool"]["poetry"]["name"]
        desc = toml_dict["tool"]["poetry"]["description"]
        license = toml_dict["tool"]["poetry"]["license"]
        authors = toml_dict["tool"]["poetry"]["authors"]
        dependencies = list(toml_dict["tool"]["poetry"]["dependencies"])
        dev_dependencies = list(toml_dict["tool"]["poetry"]["group"]["dev"]["dependencies"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, license, authors, dependencies, dev_dependencies)