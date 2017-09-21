import hug
from logzero import logger


valid_statuses = ['started', 'ringing', 'answered', 'complete', 'machine', 
                  'unanswered', 'busy', 'failed', 'timeout', 'rejected']


@hug.get()
def ncco():
    """Returns streaming audio example Nexmo Call Control Object"""

    return [{
        'action': 'stream',
        'streamUrl': ['https://cdn.rawgit.com/nexmo-community/nexmo-flask-call-tracking/3568455d/static/audio/calls-recorded.mp3']
    }]


@hug.post()
def events(status: hug.types.one_of(valid_statuses), conversation_uuid: hug.types.text):
    logger.debug(f'event: {status} - {conversation_uuid}')
    return 'OK'
