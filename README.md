# undertale save analyzer

an older python project i worked on for reading and analyzing undertale save files. i'm only uploading it to github now because apparently my old projects deserve to see the light of day too.

## what it does

the program reads data directly from an undertale `file0` save and turns some of the raw values into actually readable information about the playthrough.

so far it can:

- read the raw save file
- extract player stats like LV, HP, EXP, gold and kills
- read kill counters from different areas
- check values related to genocide progression
- determine whether the save is pacifist-compatible, neutral or following genocide progression

## project structure

`01save_reader/`  
reads the raw `file0` save and displays its contents.

`02player_stats/`  
extracts basic player information from the save.

`03game_state/`  
looks at game state and route-related information.

`data/`  
where the save file goes locally. the actual `file0` is ignored by git because i probably shouldn't upload my undertale save to the internet.

## running it

DESPITE EVEEYTHING, ITS STILL PYTHON!!!!

```bash
python 02player_stats/player_stats.py