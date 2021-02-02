import argparse
import os
import re

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from django.conf import settings



# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

youtube = build(API_SERVICE_NAME,
                    API_VERSION,
                    developerKey=settings.API_KEY_YOUTUBE)

RATINGS = ('like', 'dislike', 'none')

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

# Add the video rating. This code sets the rating to 'like,' but you could
# also support an additional option that supports values of 'like' and
# 'dislike.'
videoId = '79DijItQXMM'

def like_video():
    youtube.videos().rate(id=videoId, rating="like").execute()