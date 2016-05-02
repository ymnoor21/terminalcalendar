# Terminal Calendar
Google calendar in terminal.

# Installation
1. Use this <a target="_blank" href="https://developers.google.com/google-apps/calendar/quickstart/python">link</a> to setup Google Calendar API. (Complete Step 1 & 2 and leave the others)
2. Edit `mycalendar.sh` file and set your `mycalendar.py` file path.
3. Make the scripts executable by issuing this command: `chmod +x mycalendar.sh mycalendar.py`.
4. Run `python mycalendar.py` to setup API.
5. Now symlink by using: `ln -s /path/to/your/mycalendar.sh /usr/local/bin/mycalendar`.
6. Run `mycalendar` command. If you're running this command for the first time, the API will generate a link for you to browse. Copy & paste it in your browser. Login into your google account. Then allow it to access your google calendar.

# Usage
Run `mycalendar --help` or `mycalendar -h` to see the command line usage.
1. `-d` where `-d` specifies the date which want to lookup
2. 

# Sample Command(s)
1. `mycalendar`
2. `mycalendar -d 2016-04-01`

