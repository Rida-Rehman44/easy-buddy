# calendar/views.py
from django.shortcuts import redirect
from django.urls import reverse
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime

def home(request):
    # Load credentials from session
    if 'credentials' not in request.session:
        return redirect('auth')  # Redirect to authentication if credentials are not available

    # Load credentials from session
    credentials = Credentials.from_authorized_user_info(request.session['credentials'])

    # If the credentials are expired, refresh them
    if credentials.expired:
        credentials.refresh(Request())

    # Build the Google Calendar service
    service = build('calendar', 'v3', credentials=credentials)

    # Get the current date and time
    now = datetime.datetime.now(datetime.timezone.utc).isoformat() + 'Z'  # 'Z' indicates UTC time

    # Fetch the next 10 events from the primary calendar
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    # Pass the events data to the template for rendering
    return render(request, '/templates/home.html', {'events': events})

def auth(request):
    flow = Flow.from_client_secrets_file(
        '/home/dci-student/final/project/easy-buddy/event_calendar/client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        redirect_uri='http://127.0.0.1:8000/calendar/auth/callback/'
    )
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    request.session['state'] = state
    return redirect(authorization_url)

def auth_callback(request):
    state = request.session.pop('state', None)
    flow = Flow.from_client_secrets_file(
        '/home/dci-student/final/project/easy-buddy/event_calendar/client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        state=state,
        redirect_uri='http://127.0.0.1:8000/calendar/auth/callback/'
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    # Store or use credentials.access_token for making API requests
    return redirect(reverse('/'))
