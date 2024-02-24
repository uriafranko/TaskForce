from crews.meeting_prep.crew import MeetingPrepCrew
from lib.interfaces.TestInterface import TestCrewInterface


class MeetingPrepTest(TestCrewInterface):
    participants = "uria franko, john doe, jane doe"
    context = "We meet to discuss the new product launch"
    objective = "To prepare for the upcoming product launch"

    def init_class(self):
        crew = MeetingPrepCrew(
            participants=self.participants, context=self.context, objective=self.objective
        )
        return crew

    def test_crew_company(self):
        crew = self.init_class()
        assert crew.participants == self.participants
        assert crew.context == self.context
        assert crew.objective == self.objective

    def test_crew_agents(self):
        crew = self.init_class()
        assert len(crew.agents) > 0

    def test_crew_tasks(self):
        crew = self.init_class()
        assert len(crew.tasks) > 0
