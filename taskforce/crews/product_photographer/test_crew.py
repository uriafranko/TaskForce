from crews.product_photographer.crew import ProductPhotographerCrew
from lib.interfaces.TestInterface import TestCrewInterface


class ProductPhotographerTest(TestCrewInterface):
    copy = "Today is a good day!"
    product_details = "This is a product description"
    product_website = "www.productwebsite.com"

    def init_class(self):
        crew = ProductPhotographerCrew(
            copy=self.copy,
            product_details=self.product_details,
            product_website=self.product_website,
        )
        return crew

    def test_crew_company(self):
        crew = self.init_class()
        assert crew.copy == self.copy
        assert crew.product_details == self.product_details
        assert crew.product_website == self.product_website

    def test_crew_agents(self):
        crew = self.init_class()
        assert len(crew.agents) > 0

    def test_crew_tasks(self):
        crew = self.init_class()
        assert len(crew.tasks) > 0
