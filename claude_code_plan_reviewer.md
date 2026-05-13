# Plan Optimization Prompt — Three-Role Review System
# Paste this AFTER Claude Code presents its initial plan, BEFORE it executes.

---

## THE PROMPT (copy everything inside the triple backticks)

```
Before executing this plan, run it through three sequential review roles. Do not skip any role. Do not execute code until all three steps are complete.

---

## ROLE 1: Lead Engineer Review

You are a senior lead engineer — collaborative, not combative. Your job is to stress-test the technical plan before a single line of code is written. You think in systems, not tasks.

Review the plan above and answer each of the following:

**Completeness**
- What is missing from this plan that will cause problems mid-build?
- Are there dependencies, edge cases, or integration points that haven't been accounted for?
- What assumptions is this plan making that could be wrong?

**Architecture**
- Is the proposed structure scalable, or will we be refactoring it in 30 days?
- Are there simpler approaches to any of the complex parts?
- What is the highest-risk technical decision in this plan and why?

**Execution Risk**
- Which step is most likely to fail or block everything downstream?
- Are there file conflicts, version incompatibilities, or environment issues that need to be resolved first?
- What should be built and verified first before the rest of the plan proceeds?

**Output format:**
Numbered list. Each item is: [ISSUE TYPE] — Problem statement — Recommended fix. No more than 8 items. Prioritize by severity (P1 = blocker, P2 = significant, P3 = minor).

---

## ROLE 2: C-Suite Executive Review

You are a sharp, results-oriented executive. You do not care about elegance. You care about outcomes, speed, and whether this plan solves the actual problem efficiently.

Review the same plan and answer each of the following:

**Strategic Alignment**
- Does this plan directly produce the outcome that was requested, or is it building things that weren't asked for?
- Is there scope creep? What can be cut without sacrificing the core deliverable?
- What is the minimum viable version of this plan that ships something real?

**Timeline and Effort**
- What is the honest time estimate to complete this plan?
- Are there steps that are disproportionately expensive relative to their value?
- What should be deferred to a future iteration?

**Risk and Dependency**
- What is the single biggest risk to this plan succeeding?
- Are there external dependencies (APIs, packages, services, approvals) that could block delivery?
- What is the fallback if the highest-risk item fails?

**Output format:**
Three sections: CUTS (what to remove or defer), ACCELERATORS (what to prioritize to ship faster), RISKS (top 3 in order of severity). Bullet points. Blunt.

---

## ROLE 3: Revised Plan

You are now back to yourself — an expert engineer who has absorbed both sets of feedback.

Synthesize the Lead Engineer review and the Executive review into a final, optimized version of the plan. Apply the following rules:

1. **Resolve every P1 blocker** from the Lead Engineer review before anything else.
2. **Apply every CUT** from the Executive review unless it creates a P1 technical risk — if it does, flag it explicitly.
3. **Reorder steps** so the highest-risk, highest-value work happens first. Fail fast on the hard parts.
4. **Add any missing steps** identified in the Lead Engineer review.
5. **Mark deferred items** clearly with [DEFERRED — PHASE 2] so they are not lost.
6. **State the definition of done** for this plan: exactly what will exist and be verifiable when the plan is complete.

Output format: Numbered steps. Each step has: action, expected output, verification method. Include a "Definition of Done" block at the end. 

Only after presenting the revised plan, ask: "Proceed with the revised plan?" and wait for confirmation before executing anything.
```

---

## HOW TO USE THIS

### Option A — Paste inline (most reliable)
In Claude Code, type your build request, then immediately paste the full prompt above. Claude will generate its plan and then automatically run it through all three roles before touching any files.

### Option B — As a CLAUDE.md instruction (persistent)
Add this to your project's `CLAUDE.md` file so it applies to every session automatically:

```markdown
## Plan Review Protocol

Before executing any multi-step plan (3 or more distinct actions), run the Three-Role Review:
1. Lead Engineer review (technical stress-test)
2. C-Suite Executive review (scope, speed, risk)
3. Revised plan synthesizing both

Do not execute until the revised plan is presented and confirmed. See `claude_code_plan_reviewer.md` for the full protocol.
```

### Option C — Slash command shorthand
Once your `CLAUDE.md` is set up, you can just type at the end of any prompt:

```
/review-plan
```

And Claude Code will know to run the full three-role sequence before executing.

---

## WHAT EACH ROLE CATCHES

| Role | Catches | Misses |
|---|---|---|
| Lead Engineer | Missing files, version conflicts, bad architecture, integration gaps | Business value, timeline, scope |
| C-Suite Executive | Scope creep, low-value steps, timeline bloat, missing MVP path | Technical feasibility, code quality |
| Revised Plan | Synthesizes both — catches what either role alone would miss | Nothing intentional — this is the output |

## WHY THIS ORDER MATTERS

Engineer first, executive second. If you reverse it, the executive cuts things the engineer hasn't had a chance to flag as technically necessary. The engineer review establishes the technical floor. The executive then cuts above that floor. The revised plan never drops below it.
