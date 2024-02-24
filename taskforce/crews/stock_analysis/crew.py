from crews.stock_analysis.agents import StockAnalysisAgents
from crews.stock_analysis.tasks import StockAnalysisTasks
from lib.interfaces.CrewManager import CrewManager


class StockAnalysisCrew(CrewManager):
    """
    Crew for financial analysis,
    Given a company,
    the crew will run a financial analysis on the company and provide a report
    """

    def __init__(self, company):
        self.company = company

        super().__init__()

    def _set_agents(self):
        agents = StockAnalysisAgents()
        self.agents = {
            "research_analyst": agents.research_analyst(),
            "financial_analyst": agents.financial_analyst(),
        }

    def _set_tasks(self):
        tasks = StockAnalysisTasks()
        self.tasks = [
            tasks.research(self.agents["research_analyst"], self.company),
            tasks.financial_analysis(self.agents["financial_analyst"]),
        ]
