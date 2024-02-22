import os
from textwrap import dedent

from crewai import Agent, Task

verbose = bool(os.environ.get("VERBOSE", False))


class TemplateTasks:
    def say_nothing(self, agent: Agent):
        return Task(
            description=dedent(
                f"""
        Tell the user that you are just an agent and you can't do anything.
        {self.__tip_section()}
      """
            ),
            agent=agent,
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
