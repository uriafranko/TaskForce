from abc import ABC, abstractmethod

from crewai import Agent, Crew, Task


class CrewManager(ABC):
    """
    CrewManager is an abstract class that provides a blueprint for creating a Crew.
    """

    crew: Crew
    agents: dict[str, Agent]
    tasks: list[Task]

    def __init__(self):
        self._set_agents()
        self._set_tasks()

    def run(self):
        # check if agents are created and in right type
        if not isinstance(self.agents, dict) or len(self.agents.items()) < 1:
            raise Exception("Agents not created")
        if not isinstance(self.tasks, list) or len(self.tasks) < 1:
            raise Exception("Tasks not created")

        crew = Crew(agents=list(self.agents.values()), tasks=self.tasks)
        return crew.kickoff()

    @abstractmethod
    def _set_agents(cls):
        pass

    @abstractmethod
    def _set_tasks(cls):
        pass

    @property
    def description(self):
        return self.__doc__
