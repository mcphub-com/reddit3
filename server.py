import requests
from datetime import datetime
from typing import Union
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/sparior/api/reddit3'

mcp = FastMCP('reddit3')

@mcp.tool()
def v1_search(search: Annotated[str, Field(description='The search term. Example: Investing')],
              subreddit: Annotated[Union[str, None], Field(description='A subreddit to search within. Leave blank to search sitewide. Example: wallstreetbets')] = None,
              filter: Annotated[Union[str, None], Field(description="The type of content to filter ('posts', 'comments', 'media', 'users', or 'communities'). Users and communities are available sitewide only. Default: post")] = None,
              timeFilter: Annotated[Union[str, None], Field(description="The time period to filter by ('all', 'year', 'month', 'week', 'day', or 'hour'). Only applicable when sortType is relevance or comments. Default: all")] = None,
              sortType: Annotated[Union[str, None], Field(description="The sorting type ('relevance', 'hot','top', 'new', or 'comments'). Default: relevance")] = None) -> dict: 
    '''Search specific topics on Reddit and filter results based on posts, comments, users, and communities. This endpoint also allows you to sort the results based on relevant, hot, new, rising, and time frame.'''
    url = 'https://reddit3.p.rapidapi.com/v1/reddit/search'
    headers = {'x-rapidapi-host': 'reddit3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
        'subreddit': subreddit,
        'filter': filter,
        'timeFilter': timeFilter,
        'sortType': sortType,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def v1_posts(url: Annotated[str, Field(description='Enter a valid subreddit url')],
             filter: Annotated[Union[str, None], Field(description='Enter: hot or new or top (default: hot)')] = None) -> dict: 
    '''Get Reddit hot, new, and top posts from a post URL.'''
    url = 'https://reddit3.p.rapidapi.com/v1/reddit/posts'
    headers = {'x-rapidapi-host': 'reddit3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'filter': filter,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def v1_post_details(url: Annotated[str, Field(description='Enter a single post URL')]) -> dict: 
    '''Get post content such as thread content, upvotes, comments, etc...'''
    url = 'https://reddit3.p.rapidapi.com/v1/reddit/post'
    headers = {'x-rapidapi-host': 'reddit3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def v1_user_data(username: Annotated[str, Field(description='Provide a valid username. Example: Real_Grapefruit_5570')],
                 filter: Annotated[Union[str, None], Field(description="The type of content to filter ('posts', 'comments', 'media', 'users', or 'communities'). Users and communities are available sitewide only. Default: post")] = None,
                 sortType: Annotated[Union[str, None], Field(description="The sorting type ('relevance', 'hot','top', 'new', or 'comments'). Default: relevance")] = None) -> dict: 
    '''Get posts and comments from a given user. This endpoint also allows you to sort the results based on hot, top, and new.'''
    url = 'https://reddit3.p.rapidapi.com/v1/reddit/user-data'
    headers = {'x-rapidapi-host': 'reddit3.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'filter': filter,
        'sortType': sortType,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()



if __name__ == '__main__':
   mcp.run(transport="stdio")
