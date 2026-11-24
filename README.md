# news-image-20261124 — The World in One Image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Herman-234/mend-news-image-24-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Herman-234/mend-news-image-24-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the [make.fun bounty "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124) — $100 prize pool, 50 paid places, closes 26 Nov 2026 07:00 WIB.

## The image

A front-page-style infographic summing up Tuesday 24 November 2026 in five stories:

1. **COP31 ends without a deal** — climate talks in Antalya close with no agreement on fossil fuels.
2. **Factory fire in Indonesia** — fire in Banten kills at least 24; rescuers search for about 30 missing.
3. **Ukraine war grinds on** — Russian drone strike hits the Kyiv region; Russian war dead put above 700,000.
4. **India–Nepal rail link opens** — Modi and Shah flag off the Saryu–Kamala Express; India pledges a Rs 15,000-crore package.
5. **Wall Street tumbles** — stocks shed $1 trillion after the Democrats' midterm win; Trump blames Democrats.

## How it works

- `build_image.py` renders `entry.png` (1024×1024 PNG, Pillow, no network, deterministic — same input, same bytes).
- `main.py` copies the pre-rendered `entry.png` to the output directory.

```sh
python3 build_image.py   # regenerate entry.png
python3 main.py          # write /output/entry.png
```

## Sources

Headlines checked against public news reports of 24 November 2026 from Jagran Josh, StudMentor, ObserverVoice and Global24.

## License

MIT — see [LICENSE](LICENSE).
