from crews.product_photographer.agents import ProductPhotographerAgents
from crews.product_photographer.tasks import ProductPhotographerTasks
from lib.interfaces.CrewManager import CrewManager


class ProductPhotographerCrew(CrewManager):
    """
    Crew for product photography,
    Given a copy, product website and product details,
    the crew will generate text-2-image paragraphs for the copy
    """

    def __init__(self, copy: str, product_website: str, product_details: str):
        self.copy = copy
        self.product_website = product_website
        self.product_details = product_details

        super().__init__()

    def _set_agents(self):
        agents = ProductPhotographerAgents()
        self.agents = {
            "senior_photographer_agent": agents.senior_product_photographer_agent(),
        }

    def _set_tasks(self):
        tasks = ProductPhotographerTasks()
        self.tasks = [
            tasks.product_photograph_task(
                self.agents["senior_photographer_agent"],
                self.copy,
                self.product_website,
                self.product_details,
            )
        ]
