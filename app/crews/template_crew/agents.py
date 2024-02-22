import os
from textwrap import dedent

from crewai import Agent

from lib.tools.search_tools import SearchTools

verbose = bool(os.environ.get("VERBOSE", False))


class TemplateAgents:
    def template_agent(self):
        return Agent(
            role="You're a template agent",
            goal=dedent("""Tell me you're an agent that does something amazing."""),
            backstory=dedent(
                """\
                Tell me about your backstory. What makes you the best at what you do?
                """
            ),
            verbose=verbose,
            tools=[
                SearchTools.search_internet,
            ],
        )
