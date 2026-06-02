# /quick-dev

Rapid throwaway prototype mode. Opt-in permission to move fast without production-quality constraints.

## When to use

- Validating a technical hypothesis before committing to a full implementation
- Building a working demo for a stakeholder decision
- Exploring an unfamiliar API, library, or pattern before designing the real integration
- Time-boxed spikes where the goal is learning, not shipping

## How it works

Invoking `/quick-dev` explicitly activates throwaway mode for the current task. This changes the operating rules:

**In quick-dev mode, the following are explicitly skipped:**
- Unit and integration tests
- Error handling and edge case coverage
- Abstraction and separation of concerns
- Documentation
- Code review
- Performance optimization

**What is NOT skipped regardless of mode:**
- Understanding what the code is supposed to do
- A working demo that actually runs
- A clear summary of what would need to change before this code is production-ready

## Time box

Hard cap: **2 hours**. If the spike can't produce a working demo in 2 hours, stop and reassess the approach — don't extend the time box.

## Output format

Every `/quick-dev` session ends with:

```
SPIKE SUMMARY — [date]

What was built: [one paragraph]
Does it work: [yes / partially / no]

What would need to change for production:
1. [specific item]
2. [specific item]
3. [specific item]

Recommendation: [proceed with full implementation / revisit approach / abandon]
```

And always ends with the mandatory disclaimer:

> **This is a spike. Rebuild before shipping.**

## When NOT to use

- Database migrations
- Authentication or session management
- Billing or payment flows
- Anything that touches production data
- Infrastructure changes
- Security-sensitive code paths

If `/quick-dev` is invoked for any of the above, reject the request and explain why.

## Rules

- The throwaway nature must be explicitly communicated to anyone who sees the output.
- Quick-dev code must never be merged to main without a full rebuild.
- If the spike reveals the approach won't work, that's a success — document why and stop.
