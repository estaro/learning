# -*- coding: utf-8 -*-

"""
    api_lib_sample.py
"""

from ConfigParser import ConfigParser
from logging import getLogger, DEBUG, basicConfig
import sys

from github import Github
from jenkinsapi import jenkins
from jira import JIRA
from slacker import Slacker


# --------------------------------------------------------------------------
# Preprocessing
# --------------------------------------------------------------------------
basicConfig(level=DEBUG)
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# --------------------------------------------------------------------------
# setting
# --------------------------------------------------------------------------
config = ConfigParser()
config.read('setting.ini')

# --------------------------------------------------------------------------
# functions
# --------------------------------------------------------------------------
def api_slack():
    logger.info("slack --------------------------------")
    slack = Slacker(token=config.get('slack', 'token'))
    channels = slack.channels.list()
    logger.info(channels)
    for channel in channels.body['channels']:
        logger.info(channel['name'])  # general, etc...

def api_jira():
    logger.info("jira --------------------------------")
    basic_auth = (config.get('jira', 'username'), config.get('jira', 'password'))
    jira = JIRA(server=config.get('jira', 'server'), basic_auth=basic_auth)
    issues = jira.search_issues('project=' + config.get('jira', 'project'))
    logger.info(issues)
    for issue in issues:
        logger.info(issue.fields.summary)

def api_github():
    logger.info("github --------------------------------")
    github = Github(login_or_token=config.get('github', 'token'))

def api_jenkins():
    logger.info("jenkins --------------------------------")
    jenkins = jenkins.Jenkins(baseurl, username, password)

# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
if __name__ == "__main__":
    api_slack()
    api_jira()
    api_github()
    api_jenkins()
