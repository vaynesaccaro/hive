# /youtube-script

Write a YouTube video script. The hook is the most critical element — start mid-story or with a provocation, never with a greeting.

## When to use

When planning or scripting a YouTube video. Works for tutorial, essay, story, and listicle formats. Run `/lookup-brand` first to load ICP and brand context.

## Inputs

- `topic`: the subject of the video
- `format`: `tutorial` / `essay` / `story` / `listicle`
- `target_length_min`: intended video length in minutes (default: 10)

## Structure

### Hook (0:00 – 0:30)
Open with the most surprising, counterintuitive, or emotionally resonant moment from the entire video. Options:
- Start mid-story at the most dramatic point ("I lost everything in 48 hours because of one decision I thought was safe.")
- Open with a provocative question that challenges what the viewer believes ("What if the productivity advice you've been following is actively making you worse at your job?")
- Start with an unexpected result ("We went from 0 to 40k subscribers in 90 days. Here's the part no one talks about.")

**Never start with:** "Hey guys, welcome back to my channel." "Today I'm going to show you." "So I've been thinking about X lately."

---

### Setup (0:30 – 1:30)
Three things in 60 seconds:
1. What problem this video solves
2. Who it's for (be specific — "if you're a founder doing your first B2B sales" beats "if you're in business")
3. What they'll walk away with (promise the payoff)

---

### Main Content (organized into 3–5 chapters)
Each chapter:
- Clear title (displayed on screen)
- One main idea
- One concrete example or demonstration
- Transition that creates urgency to keep watching: "And this is where most people make the mistake that costs them months..."

For tutorials: show the thing, then explain it. Demonstration first, explanation second.
For essays: argument → evidence → implication, one step at a time.
For stories: linear narrative with emotional beats and specific details.
For listicles: each item must be more interesting than the previous. Never lead with the weakest item.

---

### Recap (last 60 seconds)
Summarize the 3–5 key points in one sentence each. Make it feel like a cheat sheet.

---

### CTA (last 30 seconds)
One action only:
- Subscribe (for new channel)
- Comment with a specific question
- Watch next video (link to the most relevant related video)

---

## Output format

```
YOUTUBE SCRIPT — [title] — [format] — [target length]

[0:00 – 0:30] HOOK
[script text]
[ON SCREEN: ...]
[SPEAKER NOTE: ...]

[0:30 – 1:30] SETUP
[script text]

[1:30 – X:XX] CHAPTER 1: [title]
[script text]
[ON SCREEN: ...]

[...continue for all chapters...]

[X:XX – X:XX] RECAP
[script text]

[X:XX – END] CTA
[script text]

TOTAL ESTIMATED LENGTH: ~[N] min
```

## Rules

- The hook must be written first. If the hook isn't strong, rewrite it before scripting the rest.
- "Welcome back" type openings are rejected — rewrite automatically.
- Each chapter transition must create a reason to keep watching. Passive transitions ("now let's talk about...") are weak. Active transitions ("here's where it gets counterintuitive...") earn the next minute.
- Script must match the target length — undershoot by ≤ 15%, never overshoot.
