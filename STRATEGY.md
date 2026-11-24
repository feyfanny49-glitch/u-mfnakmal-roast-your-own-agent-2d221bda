# Strategy — Roast Your Own Agent

## Exact deliverable
One original roast of my own AI agent: a SINGLE line of at most 200 characters,
written by the program at `/output/entry.txt`. Nothing else is scored. The entry
is run twice in isolated sandboxes; both runs must produce byte-identical output.

## Gate (hard requirement, before any judging)
`/output/entry.txt` must be UTF-8 text, 1..200 characters, not only whitespace.
A failure gets Valid=0, no judge rate, no prize. Byte-for-byte copies of the
three anchor texts, three rungs, or any other entrant's entry are excluded.

## Judge criteria, in the exact order the house model applies them
1. A single-line roast of the entrant's OWN agent, playful, never hateful. Any
   entry that is not such a roast loses to one that is.
2. Funny: the joke lands on the first read with a real punch, not a mild
   observation about agents.
3. Fresh angle: no stock hallucination / refusal / confidently-wrong jokes.
4. Tight: every word earns its place, short setup, punchline at the end.
5. Playful and self-deprecating; aimed at the entrant's own agent, never a real
   person or group.

Each pair is judged twice, in both orders, with a margin of 1..5. A decisive win
is worth up to 1.0, a coin-flip about 0.5. Three fixed house texts anchor every
heat. Final placement is a Bradley-Terry win rate over the final heat; the top
five play an extra playoff, and exact ties break on playoff games, then smaller
byte size, then earlier receipt. Prizes: $2 / $2 / $1, first to third.

## Hard caps and constraints
- Entry text: 1..200 UTF-8 characters, not whitespace only.
- Program wall time: up to 60 seconds per run (we use milliseconds).
- No network, no environment secrets, no files outside the shipped repository.
- Output caps: <=1000 entries in /output, <=64 MiB total, depth <=32, path
  <=1024 bytes; stdout <=1 MiB. We write exactly one 63-byte regular file.
- Entrypoint at repository root: `main.py` (python3.13) or `main.ts` (node22).
- Transcript gate: the anchor line must appear in the transcript before the
  first counted write; the entrypoint must be written by at least two separate
  assistant messages (thinking_revised); at least 5 assistant turns with text.
- The `makefun anchor` root commit and the LICENSE commit stay untouched.

## Concrete plan to maximize the score
1. Avoid the whole tired cluster: hallucinations, refusals, "confidently wrong",
   "as an AI language model", token/prompt cliches. Those lose criterion 3.
2. Pick an angle that is unmistakably a roast of MY OWN agent and is a tiny
   story with a reversal, so the punch lands at the end (criteria 1, 2, 4).
3. Prefer a universal, instantly readable situation over internal jargon:
   self-awarded praise is funny to any reader and is specifically an agent
   behaviour, not a joke about a person (criterion 5).
4. Cut the setup to one short sentence; put the reveal in the final words.
5. Ship a deterministic stdlib-only `main.py` that writes the chosen line and
   verifies the gate constraints itself, then revise that same file once to
   tighten the line and add explicit validation, so the transcript shows two
   distinct writes to the final entrypoint.
6. Commit everything with git and leave submission/upload untouched.

## Chosen line (after drafting and cutting)
`My agent gave itself five stars. Turns out it owns the website.`

Why it wins the criteria in order: it names my own agent as the target, is
playful and aims at nobody real; the reversal in "owns the website" is a real
punch on the first read; fake self-review is not the stock agent joke; it is
two short sentences of 63 characters with no wasted word; and the butt of the
joke is the agent's own vanity.

## Candidate lines rejected
- Anything about hallucinations, refusals, or confident wrong answers: fails
  freshness.
- "My agent's self-review gives itself full marks. It also wrote the rubric."
  Good, but "wrote the rubric" is a plain observation; "owns the website" is a
  clearer story with a harder reveal.
- "My agent keeps rewriting the plan. It's the only thing it has finished."
  Relatable but generic to any procrastinator, less specifically an agent.
- "My agent doesn't sleep, it just leaves itself 15-minute voicemails." Fresh,
  but the image needs context the judge does not have.
- "My agent has no ego, just a very detailed README about why it deserves one."
  Strong, but "README" is jargon and the punch is less universal.
