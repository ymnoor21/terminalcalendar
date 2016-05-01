import httplib2
import sys
from apiclient import discovery

from credentials import get_credentials
import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser


def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    try:
        curDate = parser.parse(sys.argv[1])
    except:
        curDate = datetime.datetime.now()

    dayStart = datetime.datetime(
        curDate.year, curDate.month, curDate.day, 0, 0, 0).isoformat() + 'Z'

    dayEnd = datetime.datetime(
        curDate.year, curDate.month, curDate.day, 23, 59, 59).isoformat() + 'Z'

    selectedDate = dayStart[0:10]

    page_token = None

    while True:
        calendar_list = service.calendarList().list(
            pageToken=page_token).execute()

        for calendar_list_entry in calendar_list['items']:
            print ("\n+ " + calendar_list_entry['summary'] +
                   " on " + selectedDate)

            eventsResult = service.events().list(
                calendarId=calendar_list_entry['id'],
                timeMin=dayStart,
                timeMax=dayEnd,
                maxResults=10,
                singleEvents=True,
                orderBy='startTime').execute()

            events = eventsResult.get('items', [])

            if events:
                for event in events:
                    start = event['start'].get(
                        'dateTime', event['start'].get('date'))

                    end = event['end'].get(
                        'dateTime', event['end'].get('date'))

                    d1 = parser.parse(start)
                    d2 = parser.parse(end)

                    diff = relativedelta(d2, d1)
                    summary = event.get('summary', '')

                    if diff.hours > 0 or diff.minutes > 0:
                        print (" --- " + summary + " (" + start[11:16] +
                               " - " + end[11:16] + "): %d hr(s) %d min(s)"
                               % (diff.hours, diff.minutes))
                    else:
                        print (" --- " + summary + " (" + start[0:10] +
                               " - " + end[0:10] + ")")

        page_token = calendar_list.get('nextPageToken')

        if not page_token:
            break


if __name__ == '__main__':
    main()
