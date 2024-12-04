local function findDistance(holdTime, totalTime)
    return (totalTime - holdTime) * holdTime
end

local time2 = 45988373
local distance2 = 295173412781210

local left = 1
local right = time2 // 2
local mid = (left + right) // 2
while (left < right) do
    if (findDistance(mid, time2) > distance2) then
        right = mid - 1
    elseif (findDistance(mid, time2) < distance2) then
        left = mid + 1
    else
        break
    end
    mid = (left + right) // 2
end
mid = mid
local gold = (time2 - mid) - mid - 1
print("Part 2: " .. gold)

-- more efficient solution for gold using bin-search. although brute force works relatively quickly
-- Winning times will always be a contiguous block centered around the middle
-- We find the minimum holding time to beat the record,
-- so we know all holding times from min, to total_time - min will beat the time (watch for off-by-one errors)
