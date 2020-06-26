from django.core.management.base import BaseCommand
from ...models.submission import Submission
from tweet_commune.submission_actions import SubmissionActions
from ...logger.tweet_logger import TweetLogger


class Command(BaseCommand):
    """
    Management command to post Submission to Twitter
    """

    help = "Post the top submission"

    def handle(self, *args, **options):
        try:
            submission = Submission.queue.top()
            if submission:
                actions = SubmissionActions(submission)
                actions.post()
            else:
                TweetLogger.empty_queue()
        except Exception as e:
            TweetLogger.critical(e)
