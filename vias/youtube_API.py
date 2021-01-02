from django.conf import settings


class Youtube:
    youtube = settings.YOUTUBE_URL_OUTH + settings.YOUTUBE_CLIENT_ID + settings.YOUTUBE_REDIRECT_URI + settings.YOUTUBE_SCOPE + settings.RESPONSE_TYPE + settings.ACCESS_TYPE
    print(youtube)
    
