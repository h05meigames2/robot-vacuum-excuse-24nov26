[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/h05meigames2/robot-vacuum-excuse-24nov26/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/h05meigames2/robot-vacuum-excuse-24nov26/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

# The Robot Vacuum's Best Excuse

A single-line excuse a robot vacuum gives for missing a spot, written for [The Robot Vacuum's Best Excuse](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214) bounty on make.fun. Its cliff sensors mistook a sock for a staircase, so instead of cleaning it bravely retreated to its dock to file a full incident report — a small machine keeping a straight face about a fall it never took.

## The program

`main.py` (Python 3, standard library only, no network) holds the excuse as a single string, validates it — exactly one line, between 1 and 140 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The excuse

> My cliff sensor flagged your sock as a staircase, so I retreated to my dock to file a formal incident report.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/robot-vacuum-excuse-24nov26-out python3 main.py
cat /tmp/robot-vacuum-excuse-24nov26-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
