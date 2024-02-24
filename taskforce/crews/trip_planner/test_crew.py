from crews.trip_planner.crew import TripPlannerCrew
from lib.interfaces.TestInterface import TestCrewInterface


class TripPlannerTest(TestCrewInterface):
    origin = "San Francisco"
    cities = "New York"
    date_range = "2024-01-01 - 2024-01-07"
    interests = "museums, parks, restaurants, shopping"

    def init_class(self):
        crew = TripPlannerCrew(
            origin=self.origin,
            cities=self.cities,
            date_range=self.date_range,
            interests=self.interests,
        )
        return crew

    def test_crew_company(self):
        crew = self.init_class()
        assert crew.origin == self.origin
        assert crew.cities == self.cities
        assert crew.date_range == self.date_range
        assert crew.interests == self.interests

    def test_crew_agents(self):
        crew = self.init_class()
        assert len(crew.agents) > 0

    def test_crew_tasks(self):
        crew = self.init_class()
        assert len(crew.tasks) > 0
