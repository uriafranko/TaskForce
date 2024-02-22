import os
from textwrap import dedent

from crewai import Agent
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

from lib.tools.browser_tools import BrowserTools
from lib.tools.calculator_tools import CalculatorTools
from lib.tools.search_tools import SearchTools
from lib.tools.sec_tools import SECTools

verbose = bool(os.environ.get("VERBOSE", False))


class StockAnalysisAgents:
    def financial_analyst(self):
        return Agent(
            role="The Best Financial Analyst",
            goal=dedent(
                """Impress all customers with your financial data
                and market trends analysis"""
            ),
            backstory=dedent(
                """The most seasoned financial analyst with
                lots of expertise in stock market analysis and investment
                strategies that is working for a super important customer."""
            ),
            verbose=verbose,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k,
            ],
        )

    def research_analyst(self):
        return Agent(
            role="Staff Research Analyst",
            goal=dedent(
                """Being the best at gather, interpret data and amaze
                your customer with it"""
            ),
            backstory=dedent(
                """Known as the BEST research analyst, you're
                skilled in sifting through news, company announcements,
                and market sentiments. Now you're working on a super
                important customer"""
            ),
            verbose=verbose,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool(),
                SECTools.search_10q,
                SECTools.search_10k,
            ],
        )

    def investment_advisor(self):
        return Agent(
            role="Private Investment Advisor",
            goal=dedent(
                """Impress your customers with full analyses over stocks
                and completer investment recommendations"""
            ),
            backstory=dedent(
                """You're the most experienced investment advisor
                and you combine various analytical insights to formulate
                strategic investment advice. You are now working for
                a super important customer you need to impress."""
            ),
            verbose=verbose,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool(),
            ],
        )
