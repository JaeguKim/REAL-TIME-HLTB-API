tell application "Terminal"
	reopen
	activate
	set currentDir to POSIX path of ((path to me as text) & "::")
	do script "cd " & currentDir in front window
	do script "source hltbAPI_env/bin/activate" in front window
	do script "cd HLTB_API" in front window
	do script "python manage.py runserver" in front window
	my makeTab()
	do script "cd " & currentDir in front window
	do script "source hltbAPI_env/bin/activate" in front window
	do script "cd HLTB_API" in front window
	do script "celery -A HLTB_API worker -l info" in front window
	my makeTab()
	do script "export PATH=$PATH:/usr/local/opt/rabbitmq/sbin" in front window
	do script "rabbitmq-server" in front window
end tell

on makeTab()
	tell application "System Events" to keystroke "t" using {command down}
	delay 0.2
end makeTab