command="cd $(pwd)"
echo $command
osascript -e 'tell app "Terminal"
    set command to "cd $(pwd)"
    do script command
end tell'
#osascript -e 'tell app "Terminal" to do script "cd \"$(currentPath)\""'
#osascript -e 'tell application \"Terminal\" to do script \"echo '$variable'\"'
#&& source hltb_env/bin/activate"'
#osascript -e 'tell app "Terminal" to do script "cd "$(dirname "$0")" python ./HLTB_API/manage.py runserver"'
