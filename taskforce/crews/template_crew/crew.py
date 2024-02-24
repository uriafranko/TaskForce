from crews.template_crew.agents import TemplateAgents
from crews.template_crew.tasks import TemplateTasks
from lib.interfaces.CrewManager import CrewManager


class TemplateCrew(CrewManager):
    """
    Crew for as a template,
    Given an example,
    the crew will say it can't do anything.
    """

    def __init__(self, example: str):
        self.example = example

        super().__init__()

    def _set_agents(self):
        agents = TemplateAgents()
        self.agents = {
            "template_agent": agents.template_agent(),
        }

    def _set_tasks(self):
        tasks = TemplateTasks()
        self.tasks = [
            tasks.say_nothing(self.agents["template_agent"]),
        ]
