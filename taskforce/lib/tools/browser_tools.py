import json
import os
from textwrap import dedent

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html


class BrowserTools:
    @staticmethod
    def needed_env_vars():
        return ["BROWSERLESS_API_KEY"]

    @tool("Scrape website content")
    @staticmethod
    def scrape_and_summarize_website(website, use_browserless=False):
        """Useful to scrape and summarize a website content"""
        if use_browserless:
            response = browserless(website)
        else:
            response = requests.get(website)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        content = [content[i : i + 8000] for i in range(0, len(content), 8000)]
        summaries = []
        for chunk in content:
            agent = Agent(
                role="Principal Researcher",
                goal=dedent(
                    """Do amazing research and summaries
                    based on the content you are working with"""
                ),
                backstory=dedent(
                    """You're a Principal Researcher at a big company
                        and you need to do research about a given topic."""
                ),
                allow_delegation=False,
            )
            task = Task(
                agent=agent,
                description=dedent(
                    f"""Analyze and summarize the content below,
            make sure to include the most relevant information in the summary,
            return only the summary nothing else.
            \n\nCONTENT\n----------\n{chunk}"""
                ),
            )
            summary = task.execute()
            summaries.append(summary)
        return "\n\n".join(summaries)

    @tool("Scrape website content using browserless")
    @staticmethod
    def scrape_and_summarize_website_browserless(website):
        """Useful to scrape and summarize a website content using browserless"""
        return BrowserTools.scrape_and_summarize_website(website, use_browserless=True)


def browserless(website):
    url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    payload = json.dumps({"url": website})
    headers = {
        "cache-control": "no-cache",
        "content-type": "application/json",
    }
    return requests.request("POST", url, headers=headers, data=payload)
