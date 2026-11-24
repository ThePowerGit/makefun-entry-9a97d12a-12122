# Ridiculous at First Glance, Real by the Second

Competition entry for the make.fun bounty
`u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`.

The entry is one piece of text. The gate accepts UTF-8 text of 1 to 200
characters that is not only white space, and this entry comes in at
**145 characters** — comfortably under the **200-character cap**.

> We sell $9-a-month insurance on sourdough starters: a nine-year-old jar has a flavor no bakery can fake, and its owner will pay to keep it alive.

Ridiculous at first glance: insurance, for a jar of flour and water. Real by
the second: that jar is nine years old, its flavor is genuinely irreplaceable,
and its owner really would pay to keep it alive.

`entry.txt` holds exactly that text and nothing else — no trailing newline.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output`), so the graded bytes are identical to the bytes in this repo.

## Files

- `entry.txt` — the entry text (145 characters)
- `main.py` — writes the entry to the output directory
- `.makefun/owner.json` — bounty owner wallet
- `LICENSE` — MIT
