import os
from textwrap import dedent

from crewai import Agent

from lib.tools.browser_tools import BrowserTools
from lib.tools.search_tools import SearchTools

verbose = bool(os.environ.get("VERBOSE", False))


class ProductPhotographerAgents:
    def senior_product_photographer_agent(self):
        return Agent(
            role="Senior Product Photographer",
            goal=dedent(
                """\
					Take the most amazing photographs for instagram ads that
					capture emotions and convey a compelling message."""
            ),
            backstory=dedent(
                """\
					As a Senior Photographer at a leading digital marketing
					agency, you are an expert at taking amazing photographs that
					inspire and engage, you're now working on a new campaign for a super
					important customer and you need to take the most amazing photograph."""
            ),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram,
            ],
            verbose=verbose,
        )
