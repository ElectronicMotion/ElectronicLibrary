Infos about MicroTicketSystem

Description:
MTS (MicroTicketSystem) is a command-line Ticketsystem for personal use.
It will be extended through out some time.
It uses SQLite3 and Python 3.5.


Included Features:
Tickets with the following Informations:
        - Title
        - Description
        - Date
        - Status
        - Comments


Planned Features:
        - Session mode
        - Users
        - Delete Comments
	- Add Timestamp to Comments and Tickets, not only date
	  Timestamp will be shown only in comments or in Detail
	- Path to Database should be changable
	- User and Path - config will need a config file
	- New Statuses for Tickets:
		- Hold
		- Assigned
		- Blocked
	- Visuals Rework
	- Namechange

Known Issues:
	- Display breaks with too long description.
	- If more than the expected 2 Arguments on comment are used, it will
	  create a blank entry in the database.

Updated: 25.02.2019

