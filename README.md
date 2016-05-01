# Terminal Calendar
Google calendar in terminal.

# Installation
1. Use this <a target="_blank" href="https://developers.google.com/google-apps/calendar/quickstart/python">link</a> to setup Google Calendar API. (Complete Step 1 & 2 and leave the others)
2. Edit `mycalendar.sh` file and set your `mycalendar.py` file path.
3. Make the scripts executable by issuing this command: `chmod +x mycalendar.sh mycalendar.py`.
4. Now symlink by using: `ln -s /path/to/your/mycalendar.sh /usr/local/bin/mycalendar`.
5. Run `mycalendar` command. If you're running this command for the first time, the API will generate a link for you to browse. Copy & paste it in your browser. Then allow it to access your google calendar.
6. Run `mycalendar` command again to get all your items in your terminal.

