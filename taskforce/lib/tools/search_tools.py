import json
import os

import requests
from langchain.tools import tool


class SearchTools:
    @staticmethod
    def needed_env_vars():
        return ["SERPER_API_KEY"]

    @tool("Search the internet")
    @staticmethod
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()["organic"]
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append(
                    "\n".join(
                        [
                            f"Title: {result['title']}",
                            f"Link: {result['link']}",
                            f"Snippet: {result['snippet']}",
                            "\n-----------------",
                        ]
                    )
                )
            except KeyError:
                continue

        return "\n".join(string)

    @tool("Search news on the internet")
    @staticmethod
    def search_news(query):
        """Useful to search news about a company, stock or any other
    topic and return relevant results""" ""
        top_result_to_return = 4
        url = "https://google.serper.dev/news"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()["news"]
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append(
                    "\n".join(
                        [
                            f"Title: {result['title']}",
                            f"Link: {result['link']}",
                            f"Snippet: {result['snippet']}",
                            "\n-----------------",
                        ]
                    )
                )
            except KeyError:
                continue

        return "\n".join(string)

    @tool("Search instagram")
    def search_instagram(query):
        """Useful to search for instagram post about a given topic and return relevant
        results."""
        query = f"site:instagram.com {query}"
        return SearchTools.search_internet(query)
