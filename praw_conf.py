import praw

r = praw.Reddit(user_agent='comment archiver')

r.config.log_requests       = 0
r.config.store_json_result  = True
