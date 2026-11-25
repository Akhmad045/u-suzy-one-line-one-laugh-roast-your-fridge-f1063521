# One Line, One Laugh: Roast Your Fridge — "The Cold Shoulder"

[![make.fun](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/Akhmad045/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/Akhmad045/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

Entry for the make.fun bounty [One Line, One Laugh: Roast Your Fridge](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521).

The line, all 124 characters of it:

> My fridge keeps the butter in its own little compartment, then freezes it solid — even its VIP guest gets the cold shoulder.

Why this line: the butter compartment is the one detail every fridge
owner recognises but nobody roasts — the little VIP lounge in the door
that treats the butter like a guest of honour. The fridge then freezes
it rock solid anyway, so the guest of honour gets the cold shoulder:
a double meaning that pays off in the last three words, and it reads
cleanly aloud in a single breath.

## How to run it

```sh
python3 main.py                  # writes the line to /output/entry.txt
python3 main.py --self-test      # checks the line against the 200-char gate
python3 main.py --out /tmp/entry.txt   # write somewhere else
```

`main.py` is standard library only. It writes the line exactly as-is,
with no trailing newline, reads it back to prove the bytes match, and
refuses to write anything that breaks the gate (empty, over 200
characters, more than one line, or carrying a control character).

## Referral

Built on make.fun — referral code `4g7knchf`.
