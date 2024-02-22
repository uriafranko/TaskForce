from crews.trip_planner.agents import TripAgents
from crews.trip_planner.tasks import TripTasks
from lib.interfaces.CrewManager import CrewManager


class TripPlannerCrew(CrewManager):
    """
    Crew for trip planning,
    Given a city, interests, and date range,
    the crew will plan a trip for the user to the city with the given interests
    using local experts and travel concierge
    """

    def __init__(self, origin: str, cities: str, date_range: str, interests: str):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range

        super().__init__()

    def _set_agents(self):
        agents = TripAgents()
        self.agents = {
            "city_selection_agent": agents.city_selection_agent(),
            "local_expert": agents.local_expert(),
            "travel_concierge": agents.travel_concierge(),
        }

    def _set_tasks(self):
        tasks = TripTasks()
        self.tasks = [
            tasks.identify_task(
                self.agents["city_selection_agent"],
                self.origin,
                self.cities,
                self.interests,
                self.date_range,
            ),
            tasks.gather_task(
                self.agents["local_expert"], self.origin, self.interests, self.date_range
            ),
            tasks.plan_task(
                self.agents["travel_concierge"], self.origin, self.interests, self.date_range
            ),
        ]
