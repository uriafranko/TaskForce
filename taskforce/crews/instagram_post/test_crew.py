from crews.instagram_post.crew import InstagramPostCrew
from lib.interfaces.TestInterface import TestCrewInterface


class InstagramPostTest(TestCrewInterface):
    objective = "To promote a product"
    product_details = "This is a product description"
    product_website = "www.productwebsite.com"

    def init_class(self):
        crew = InstagramPostCrew(
            objective=self.objective,
            product_details=self.product_details,
            product_website=self.product_website,
        )
        return crew

    def test_crew_company(self):
        crew = self.init_class()
        assert crew.objective == self.objective
        assert crew.product_details == self.product_details
        assert crew.product_website == self.product_website

    def test_crew_agents(self):
        crew = self.init_class()
        assert len(crew.agents) > 0

    def test_crew_tasks(self):
        crew = self.init_class()
        assert len(crew.tasks) > 0
