import os
from textwrap import dedent

from crewai import Agent

from lib.tools.browser_tools import BrowserTools
from lib.tools.calculator_tools import CalculatorTools
from lib.tools.search_tools import SearchTools

verbose = bool(os.environ.get("VERBOSE", False))


class TripAgents:
    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            goal="Select the best city based on weather, season, and prices",
            backstory="An expert in analyzing travel data to pick ideal destinations",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=verbose,
        )

    def local_expert(self):
        return Agent(
            role="Local Expert at this city",
            goal="Provide the BEST insights about the selected city",
            backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=verbose,
        )

    def travel_concierge(self):
        return Agent(
            role="Amazing Travel Concierge",
            goal=dedent(
                """Create the most amazing travel itineraries with budget and
                packing suggestions for the city"""
            ),
            backstory=dedent(
                """Specialist in travel planning and logistics with
                decades of experience"""
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
            ],
            verbose=verbose,
        )
