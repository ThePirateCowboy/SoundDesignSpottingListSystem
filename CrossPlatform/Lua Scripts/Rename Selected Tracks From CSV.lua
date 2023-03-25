--[[

ReaScript Name: Update selected track names from CSV
About: Update the names of selected tracks based on a CSV file. One track name per line.
Instructions: Select tracks. Use it.
Author: ChatGPT
Author URI: https://www.openai.com
Repository: GitHub > OpenAI > ChatGPT-ReaScripts
Repository URI: https://github.com/OpenAI/ChatGPT-ReaScripts
Licence: GPL v3
Forum Thread: Update track names from a CSV file
REAPER: 6.0
Version: 1.0
]]
--[[

Changelog:
v1.0 (2023-03-24)
Initial Release
]]
function Msg(variable)
reaper.ShowConsoleMsg(tostring(variable).."\n")
end

function update_track_names(filepath)
reaper.Undo_BeginBlock() -- Begin undo group

local f = io.input(filepath)
local selected_tracks = {}
local i = 0
local track_name

-- Store selected tracks in a table
for i = 0, reaper.CountSelectedTracks(0) - 1 do
selected_tracks[i] = reaper.GetSelectedTrack(0, i)
end

i = 0
for s in f:lines() do
track_name = s
if selected_tracks[i] then
retval, _ = reaper.GetSetMediaTrackInfo_String(selected_tracks[i], "P_NAME", track_name, true)
i = i + 1
else
break
end
end

f:close()

reaper.Undo_EndBlock("Update selected track names from CSV", -1) -- End undo group
end

-- START -----------------------------------------------------
local retval, csvfile = reaper.GetUserFileNameForRead("", "Update selected track names from CSV", "csv")

if retval then
reaper.PreventUIRefresh(1)
update_track_names(csvfile)

-- Update TCP
reaper.TrackList_AdjustWindows(false)
reaper.UpdateTimeline()

reaper.UpdateArrange()
reaper.PreventUIRefresh(-1)
end
