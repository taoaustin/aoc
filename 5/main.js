import fs, { readFileSync } from 'fs';

const readFileMaps = filename => 
  readFileSync(filename, 'utf8').split(/\n.*:\n/);

const parseMap = mapStr => 
  mapStr.split('\n')
    .filter(line => line !== "")
    .map(strLine => strLine.split(" ").map(str => parseInt(str)))
    .map(arrLine => new Array(arrLine[1], arrLine[1] + arrLine[2], arrLine[0] - arrLine[1]));

const findLocation = (seed, map) =>
    map.reduce((intermVal, map) => {
      for (var i = 0; i < map.length; i++) {
        let interval = map[i];
        if (intermVal >= interval[0] && intermVal < interval[1]) {
          return intermVal + interval[2];
        }
      }
      return intermVal;
    }, seed);

const maps = readFileMaps('input.txt');
const seeds = maps[0].split(": ")[1].split(" ").map(strVal => parseInt(strVal));
const parsedMaps = maps.slice(1).map(strMap => parseMap(strMap));
// console.log(parsedMaps);
const seedLocations = seeds.map(seed => findLocation(seed, parsedMaps));
const part1Result = seedLocations.reduce((curMin, curLoc) => Math.min(curMin, curLoc));
console.log(`Part 1: ${part1Result}`);


function bruteFindSeed(i, map) {
    return map.toReversed().reduce((intermVal, map) => {
      for (var i = 0; i < map.length; i++) {
        let interval = map[i];
        if (intermVal - interval[2] >= interval[0] && intermVal - interval[2] < interval[1]) {
          return intermVal - interval[2];
        }
      }
      return intermVal;
    }, i);
}
const seedIntervals = [...maps[0].split(": ")[1].matchAll(/\d+ \d+/g)]
  .map(match => match[0].split(" ").map(str => parseInt(str)))
  .map(arrLine => new Array(arrLine[0], arrLine[0] + arrLine[1]));

let min_loc = 0;
let flag = true;
while (flag) {
  let test = bruteFindSeed(min_loc, parsedMaps);
  for (var i = 0; i < seedIntervals.length; i++) {
    if (test >= seedIntervals[i][0] && test < seedIntervals[i][1]) {
      console.log(`Part 2: ${min_loc}`);
      flag = false;
    }
  }
  min_loc++;
}
