import unittest

from load_dotenv import load_dotenv

from lib.interfaces.CrewManager import CrewManager

load_dotenv()


class TestCrewInterface(unittest.TestSuite):
    crew_class = CrewManager

    def init_class(self):
        pass

    def test_crew_agents(self):
        pass

    def test_crew_tasks(self):
        pass
