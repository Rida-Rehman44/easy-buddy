from google.auth import credentials
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient.discovery

def get_calendar_service(credentials):
    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    service = googleapiclient.discovery.build(
        'calendar', 'v3', credentials=credentials)
    return service

def get_calendar_events(calendar_id):
    # Get credentials (you need to implement this part)
    credentials = get_credentials()
    
    # Build the Calendar API service
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # Fetch events from the calendar
    events_result = service.events().list(calendarId=calendar_id, timeMin='2022-01-01T00:00:00Z',
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events
