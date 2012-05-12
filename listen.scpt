#!/usr/bin/osascript

on replaceText(myText, serchStr, replaceStr)
	set theDelim to AppleScript's text item delimiters
	set AppleScript's text item delimiters to serchStr
	set theList to every text item of myText
	set AppleScript's text item delimiters to replaceStr
	set myText to theList as string
	set AppleScript's text item delimiters to theDelim
	return myText
end replaceText

tell application "iTunes"
	set i_artist to artist of current track
	set i_track to name of current track
	set i_album to album of current track
	set i_count to played count of current track
end tell

set i_artist to replaceText(i_artist, "\"", " ")
set i_track to replaceText(i_track, "\"", " ")
set i_album to replaceText(i_album, "\"", " ")
set i_count to replaceText(i_count as string, "\"", " ")

do shell script "/jikken/Tloop/postmusic.py \"" & i_artist & "\" \"" & i_track & "\" \"" & i_album & "\" \"" & i_count & "\""
