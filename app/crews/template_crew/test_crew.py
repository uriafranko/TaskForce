from crews.stock_analysis.crew import StockAnalysisCrew
from lib.interfaces.TestInterface import TestCrewInterface


class StockAnalysisTest(TestCrewInterface):
    crew_class = StockAnalysisCrew

    company_name = "Apple Inc."

    def init_class(self):
        self.crew_class(self.company_name)

    def test_crew_company(self):
        crew = self.crew_class(self.company_name)
        assert crew.company == self.company_name

    def test_crew_agents(self):
        crew = self.crew_class(self.company_name)
        assert len(crew.agents) > 0

    def test_crew_tasks(self):
        crew = self.crew_class(self.company_name)
        assert len(crew.tasks) > 0
