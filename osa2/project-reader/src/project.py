class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: \n{self.name}"
            f"\nDescription: \n{self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors: \n{self.authors or '-'}\n"
            f"\nDependencies: \n{self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}\n"
        )