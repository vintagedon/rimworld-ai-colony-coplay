<!--
---
title: "Export Mod"
description: "C# RimWorld mod for real-time state export (Phase 2)"
author: "VintageDon"
date: "2026-01-17"
version: "1.0"
status: "Future"
tags:
  - type: directory-readme
  - domain: modding
  - tech: csharp
  - tech: unity
---
-->

# Export Mod

C# RimWorld mod for real-time state export. **Phase 2** — not yet implemented.

---

## 1. Purpose

Phase 1 extracts state from autosave files, which limits granularity to save intervals (1-5 minutes). This mod will enable real-time state export from the running game.

### Design Goals

- **Minimal footprint** — Export only, no UI additions
- **Configurable interval** — Write state every N game ticks
- **JSON output** — Same format as Python extractor
- **No gameplay impact** — Pure observation, no game modifications

---

## 2. Planned Structure

```
mod/
├── About/
│   ├── About.xml
│   └── Preview.png
├── Source/
│   ├── RimAI.Export.csproj
│   └── ...
├── Assemblies/
│   └── RimAI.Export.dll
└── README.md               # This file
```

---

## 3. Reference Implementation

The `.reference-data/` directory contains RimAI Framework and Core source code for reference:

| Component | Useful Patterns |
|-----------|-----------------|
| `WorldDataService` | Game state extraction approaches |
| `Tooling/Execution/` | How to query colonists, resources, etc. |
| `Persistence/` | Serialization patterns |

---

## 4. Prerequisites (Future)

- Visual Studio 2022 or Rider
- .NET Framework 4.7.2 (RimWorld target)
- RimWorld Assembly references
- Harmony library

---

## 5. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [.reference-data/](../.reference-data/) | RimAI source for reference |
| [tools/extractor/](../tools/extractor/README.md) | Phase 1 alternative |
