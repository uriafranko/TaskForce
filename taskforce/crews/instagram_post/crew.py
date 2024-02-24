from crews.instagram_post.agents import InstagramPostAgents
from crews.instagram_post.tasks import InstagramPostTasks
from crews.product_photographer.crew import ProductPhotographerCrew
from lib.interfaces.CrewManager import CrewManager


class InstagramPostCrew(CrewManager):
    """
    Crew for Instagram post,
    Given a product website, product details and objective,
    the crew will generate a post copy and image description.
    """

    def __init__(self, product_website, product_details, objective):
        self.product_website = product_website
        self.product_details = product_details
        self.objective = objective

        super().__init__()

    def _set_agents(self):
        agents = InstagramPostAgents()
        self.agents = {
            "product_competitor_agent": agents.product_competitor_agent(),
            "strategy_planner_agent": agents.strategy_planner_agent(),
            "creative_agent": agents.creative_content_creator_agent(),
        }

    def _set_tasks(self):
        tasks = InstagramPostTasks()
        website_analysis = tasks.product_analysis(
            self.agents["product_competitor_agent"], self.product_website, self.product_details
        )
        market_analysis = tasks.competitor_analysis(
            self.agents["product_competitor_agent"], self.product_website, self.product_details
        )
        campaign_development = tasks.campaign_development(
            self.agents["strategy_planner_agent"], self.product_website, self.product_details
        )
        write_copy = tasks.instagram_ad_copy(self.agents["creative_agent"])

        self.tasks = [
            website_analysis,
            market_analysis,
            campaign_development,
            write_copy,
        ]

    def run(self):
        post_text = self.crew.kickoff()

        post_image_description = ProductPhotographerCrew(
            copy=post_text,
            product_website=self.product_website,
            product_details=self.product_details,
        ).run()

        return {"post_copy": post_text, "post_image_description": post_image_description}
