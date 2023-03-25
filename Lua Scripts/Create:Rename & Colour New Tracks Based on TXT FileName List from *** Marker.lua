--[[
 * ReaScript Name: Import tracks from txt file after "***"
 * About: Create & rename & random colour new tracks from a TXT file, starting after "***". One track name per line no line breaks.
 * Instructions: Run script -> Select the .txt file -> Tracks will be created and colours with the file names from the .txt file starting after the "***". Meant to be used in conjuction with Spotting List System by Ben Harding.
 * Author: Credit to creator X-Raym, adapted by Ben Harding & ChatGPT
 * Author URI: credit for https://www.extremraym.com
 * Licence: GPL v3
]]
function Msg(variable)
  reaper.ShowConsoleMsg(tostring(variable).."\n")
end

----------------------------------------------------------------------

function read_lines(filepath)

  reaper.Undo_BeginBlock() -- Begin undo group

  local f = io.input(filepath)
  local skip = true -- start by skipping lines until "***" is found
  repeat

    s = f:read ("*l") -- read one line

    if s then  -- if not end of file (EOF)

      if skip and s:find("***") then
        skip = false
      elseif not skip then
        count_tracks = reaper.CountTracks(0)

        i = 0

        last_track_id = count_tracks + i
        reaper.InsertTrackAtIndex(last_track_id, true)
        last_track = reaper.GetTrack(0, last_track_id)

        -- Remove newline characters from the track name
        clean_s = s:gsub("\n", "")
        clean_s = clean_s:gsub("\r", "")
        -- Replace "," with "-"
        clean_s = clean_s:gsub(",", "-")
        -- Remove special characters except "_" and "-" and keep spaces
        clean_s = clean_s:gsub("[^%w_%-%s]", "")

        retval, track_name = reaper.GetSetMediaTrackInfo_String(last_track, "P_NAME", clean_s, true)
      end

    end

  until not s  -- until end of file

  f:close()

  reaper.Undo_EndBlock("Display script infos in the console", -1) -- End undo group

end

-- START -----------------------------------------------------
local retval, filetxt = reaper.GetUserFileNameForRead("", "Import tracks from file", "txt")

if retval then

  reaper.PreventUIRefresh(1)
  read_lines(filetxt)

  -- Update TCP
  reaper.TrackList_AdjustWindows(false)
  reaper.UpdateTimeline()

  reaper.UpdateArrange()
  reaper.PreventUIRefresh(-1)

end

