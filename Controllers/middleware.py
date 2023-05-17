import re

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def filterCase(r):
    switcher = {
        'auto': 'auto',
        '240p':'240p',
        '360p': '360p',
        '480p': '480p',
        '720p': '720p',
        '1080p': '1080p',
        'audio': 'audio'
    }
    return switcher.get(r,"Invalid filter!")