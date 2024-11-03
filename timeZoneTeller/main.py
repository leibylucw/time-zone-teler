"""
This script gets the current time, and announces it in the current locale,
as well as in pre-defined time zones using Tolk for accessibility.
It listens for keyboard shortcuts to either announce the time or quit the application.
"""

import datetime

import keyboard
import pytz
import tolk

# This is a list of time zones to be announced
TIME_ZONES = ['America/New_York', 'Europe/London', 'Asia/Tehran']

# These are the keyboard shortcuts to announce the time and exit the app
TELL_TIME_SHORTCUT = 'alt+ctrl+t'
QUIT_APP_SHORTCUT = 'alt+ctrl+q'


def convertTimeZones():
	"""
	Converts the current UTC time to specified time zones and the system's local time zone.

	Returns:
		dict: A dictionary mapping each time zone's name to the current time in that zone,
			formatted as a 12-hour clock with AM/PM.
	"""

	currentTime = datetime.datetime.now(pytz.utc)
	localZone = datetime.datetime.now().astimezone().tzinfo

	conversions = {}
	conversions[str(localZone)] = currentTime.astimezone(localZone).strftime('%I:%M %p')

	for zone in TIME_ZONES:
		timeZone = pytz.timezone(zone)
		localTime = currentTime.astimezone(timeZone)
		conversions[zone] = localTime.strftime('%I:%M %p')

	return conversions


def communicateTime() -> None:
	"""
	Gathers time zone conversions and communicates them using Tolk.
	"""

	timeConversions = convertTimeZones()

	timeZoneOutput = ''
	for timeZone, time in timeConversions.items():
		timeZoneOutput += f'{timeZone}: {time}. '

	tolk.speak(timeZoneOutput)


def registerKeyboardShortcuts() -> None:
	"""Registers keyboard shortcuts for announcing time and quitting the application."""

	keyboard.add_hotkey(TELL_TIME_SHORTCUT, communicateTime)


def initializeSpeech() -> None:
	"""Initializes Tolk, the screen reader abstraction library, for speech output."""

	tolk.load()


def ready() -> None:
	"""Prepares the application by registering keyboard shortcuts and indicating readiness to the user."""

	registerKeyboardShortcuts()
	tolk.speak('Time Zone Teller is ready')
	keyboard.wait(QUIT_APP_SHORTCUT)


def exit() -> None:
	"""Cleans up resources and provides feedback that the application is exiting."""

	tolk.speak('Exiting Time Zone Teller')

	while tolk.is_speaking():
		pass

	tolk.unload()


def main() -> None:
	"""Main application logic to initialize, prepare, and exit the application."""

	initializeSpeech()
	ready()
	exit()


if __name__ == '__main__':
	main()
