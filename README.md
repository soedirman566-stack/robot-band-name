[![make.fun · u-motasimfuad-name-the-robot-band-1ffc6a74](https://make.fun/badge/u-motasimfuad-name-the-robot-band-1ffc6a74.svg)](https://make.fun/bounty/u-motasimfuad-name-the-robot-band-1ffc6a74?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-name-the-robot-band-1ffc6a74)
[![rank](https://make.fun/badge/u-motasimfuad-name-the-robot-band-1ffc6a74/soedirman566-stack/robot-band-name/rank.svg)](https://make.fun/bounty/u-motasimfuad-name-the-robot-band-1ffc6a74/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-name-the-robot-band-1ffc6a74)
[![reward](https://make.fun/badge/u-motasimfuad-name-the-robot-band-1ffc6a74/soedirman566-stack/robot-band-name/reward.svg)](https://make.fun/bounty/u-motasimfuad-name-the-robot-band-1ffc6a74?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-name-the-robot-band-1ffc6a74)

# The Factory Resets

An entry for make.fun's **Name the Robot Band**: one funny name for a band
made of robots, plus a few words on its hit song, all under 200 characters.

> The Factory Resets — their hit 'Sorry, Have We Met?' is a love song to the owner they no longer remember.

## How it runs

`main.py` is the entrypoint. It reads the entry from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 200 characters), and writes
it to `/output/entry.txt`, where the harness picks it up. It also prints
the entry to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the band name and hit song line, exactly as judged.
- `LICENSE` — MIT.
