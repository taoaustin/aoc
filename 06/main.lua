-- just manually enter the input
local times = {45, 98, 83, 73}
local distances = {295, 1734, 1278, 1210}

local function findDistance(holdTime, totalTime)
    return (totalTime - holdTime) * holdTime
end

local silver = 1

for i = 1, 4, 1 do
    local beatingTimes = 0
    for j = 0, times[i], 1 do
        local curRun = findDistance(j, times[i])
        if (curRun > distances[i]) then
            beatingTimes = beatingTimes + 1
        end
    end
    silver = silver * beatingTimes
end

print("Part 1: " .. silver)

local time2 = 45988373
local distance2 = 295173412781210
local gold = 0
for j = 0, time2, 1 do
    local curRun = findDistance(j, time2)
    if (curRun > distance2) then
        gold = gold + 1
    end
end

print("Part 2: " .. gold)

