# coding:utf-8


import os
import logging
import traceback
import requests
from slack import Slack


def get_target_urls():
    target_urls = []
    for i in range(1, 11):
        if 'url_' + str(i) in os.environ:
            target_urls.append(os.environ['url_' + str(i)])
    return target_urls


def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    slack = Slack()

    try:
        target_urls = get_target_urls()
        message_template = '{url} status is {code}'

        for url in target_urls:
            response = requests.get(url)
            code = response.status_code

            logger.info(code)

            if code != 200:
                slack.sendMessage(
                    message_template.format(
                        url=url,
                        code=code
                    ),
                    '#notify'
                )

    except Exception as e:
        slack.sendMessage(traceback.format_exc(), '#error')
        logger.error(traceback.format_exc())
        raise(traceback.format_exc())