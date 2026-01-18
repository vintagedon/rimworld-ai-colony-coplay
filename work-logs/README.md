# Work Logs

Phase worklogs documenting project development history. Each milestone gets a subfolder with a README synthesizing decisions, outcomes, and artifacts.

---

## Structure

```
work-logs/
├── 01-ideation-and-setup/      # M01: Repo scaffolding, docs
├── 02-extractor-phase-01/      # M02a: Initial streaming extractor
├── 03-extractor-phase-02/      # M02b: Schema discovery, v2.2 extractor
├── milestones-one-and-two-procedures.md
└── README.md                   # This file
```

---

## Milestones

| Folder | Phase | Status |
|--------|-------|--------|
| [01-ideation-and-setup/](01-ideation-and-setup/README.md) | M01: Repository Setup | ✅ Complete |
| [02-extractor-phase-01/](02-extractor-phase-01/README.md) | M02a: Initial Extractor (streaming) | ✅ Complete |
| [03-extractor-phase-02/](03-extractor-phase-02/README.md) | M02b: Schema Discovery + v2.2 | ✅ Complete |

---

## Procedure

See [milestones-one-and-two-procedures.md](milestones-one-and-two-procedures.md) for M01/M02 execution patterns.

Use `docs/documentation-standards/worklog-readme-template.md` for phase READMEs.

---

## Conventions

- Folder naming: `NN-phase-name` (zero-padded, hyphenated)
- Each folder contains a `README.md` documenting that phase
- Scripts, configs, and artifacts live alongside the README
- Worklogs are synthesis documents (outcomes, not session transcripts)

---

## Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent |
| [Memory Bank](../.kilocode/rules/memory-bank/README.md) | Agent context |
