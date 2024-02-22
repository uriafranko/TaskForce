from crews.meeting_prep.agents import MeetingPreparationAgents
from crews.meeting_prep.tasks import MeetingPreparationTasks
from lib.interfaces.CrewManager import CrewManager


class MeetingPrepCrew(CrewManager):
    """
    Crew for meeting preparation,
    Given a list of participants, context, and objective,
    the crew will help you prepare for the meeting by researching, analyzing and strategizing.
    """

    def __init__(self, participants: str, context: str, objective: str):
        self.participants = participants
        self.context = context
        self.objective = objective

        super().__init__()

    def _set_agents(self):
        agents = MeetingPreparationAgents()
        self.agents = {
            "researcher_agent": agents.research_agent(),
            "industry_analyst_agent": agents.industry_analysis_agent(),
            "meeting_strategy_agent": agents.meeting_strategy_agent(),
            "summary_and_briefing_agent": agents.summary_and_briefing_agent(),
        }

    def _set_tasks(self):
        tasks = MeetingPreparationTasks()
        # Create Tasks
        research = tasks.research_task(
            self.agents["researcher_agent"], self.participants, self.context
        )
        industry_analysis = tasks.industry_analysis_task(
            self.agents["industry_analyst_agent"], self.participants, self.context
        )
        meeting_strategy = tasks.meeting_strategy_task(
            self.agents["meeting_strategy_agent"], self.context, self.objective
        )
        summary_and_briefing = tasks.summary_and_briefing_task(
            self.agents["summary_and_briefing_agent"], self.context, self.objective
        )
        self.tasks = [
            research,
            industry_analysis,
            meeting_strategy,
            summary_and_briefing,
        ]
