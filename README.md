<!--
---
title: "RimWorld AI Colony Co-Play"
description: "External AI advisor for RimWorld colony management via save file analysis"
author: "VintageDon"
date: "2026-01-18"
version: "0.2.0"
status: "Development"
tags:
  - type: project-root
  - domain: gaming
  - domain: ai-integration
  - tech: python
  - tech: lxml
  - tech: xml-parsing
related_documents:
  - "[GDR Report](.internal-files/rimworld-1_6-save-file-xml.md)"
  - "[Memory Bank](.kilocode/rules/memory-bank/README.md)"
---
-->

# 🎯 RimWorld AI Colony Co-Play

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![RimWorld](https://img.shields.io/badge/RimWorld-1.6-orange)](https://rimworldgame.com)
[![Claude](https://img.shields.io/badge/Claude-Desktop-blueviolet)](https://claude.ai)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> External AI advisor that reads RimWorld colony state and provides strategic guidance through natural conversation.

RimWorld AI Colony Co-Play enables Claude to serve as an intelligent colony advisor without modifying the game. By parsing save files and maintaining historical context, Claude can answer questions about colonist status, identify emerging risks, and suggest optimizations grounded in actual game data rather than general knowledge.

---

## 🔭 Overview

This project explores a novel human-AI collaboration pattern: co-playing a complex simulation game where the AI has persistent memory of colony history and provides advice based on real game state. If you're familiar with RimWorld modding and just want to run the extractor, skip to [Quick Start](#-quick-start).

### The Problem

Existing RimWorld AI mods (like RimAI Framework/Core) add in-game terminals and UI elements that change the gameplay experience. There's no solution for using an external AI assistant that simply reads game state and advises without modifying the game itself.

Additionally, getting useful AI advice about a specific colony currently requires manually describing the situation — tedious, incomplete, and loses context between sessions.

### The Solution

This project takes a different approach: Claude operates as an external advisor reading autosave files. The system extracts colony state into structured data Claude can query, maintains timestamped snapshots for trend analysis, and preserves context across play sessions.

The result is an AI companion that knows your colonists by name, remembers that Viktor had a mental break last week, notices your steel reserves declining, and can warn you about the skill gaps in your colony composition.

---

## 🎯 Target Audience

| Audience | Use Case |
|----------|----------|
| RimWorld Players | AI-assisted colony optimization and strategic planning |
| AI Experimenters | Novel human-AI collaboration patterns in gaming |
| Developers | Reference implementation for game state extraction |

---

## 📊 Project Status

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 1a: Save Extraction | ✅ Complete | lxml streaming extractor producing JSON/Markdown |
| Phase 1b: Database Storage | ⬜ Planned | PostgreSQL with pgvector on pgsql01 |
| Phase 1c: MCP Integration | ⬜ Planned | CrystalDB MCP for Claude queries |
| Phase 2: Export Mod | ⬜ Future | C# mod for real-time state export |
| Phase 3: Interaction | ⬜ Future | Limited game interaction capabilities |

### Current Capabilities

The extractor successfully processes 22MB modded save files in ~2 seconds:

| Component | Status | Values (Test Colony) |
|-----------|--------|---------------------|
| Game Version | ✅ | 1.6.4633 (Odyssey) |
| Mods | ✅ | 267 mods |
| Game Time | ✅ | Year 5501, Day 113, Decembary |
| World Info | ✅ | Colony: Algenib, Seed: intestines |
| Factions | ✅ | 20 with goodwill relations |
| Colonists | ✅ | 11 with skills, traits, needs |
| Animals | ✅ | 34 colony animals |
| Resources | ✅ | 65 item types categorized |
| Research | ✅ | 310 completed projects |

---

## 🏗️ Architecture

The system operates as a read-only external observer, progressing toward a Context Augmented Generation (CAG) architecture.

### Current Data Flow (Phase 1a)

```
RimWorld Autosave (.rws)
        │
        ▼
   [lxml Extractor]  ←── Manual CLI
        │
        ├──► state/snapshots/colony_{timestamp}.json
        └──► state/snapshots/colony_{timestamp}.md
                    │
                    ▼
              [Claude FS MCP]
                    │
                    ▼
             Advisory Conversation
```

### Target Architecture (Phase 1b+)

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ RimWorld        │     │ pgsql01          │     │ Claude          │
│ (autosaves)     │     │ 10.25.20.8       │     │                 │
│                 │────▶│ ┌──────────────┐ │◀────│ CrystalDB MCP   │
│ Saves folder    │     │ │ rimworld_db  │ │     │                 │
│ watched by      │     │ │ + pgvector   │ │     │ "How's morale   │
│ Python daemon   │     │ └──────────────┘ │     │  trending?"     │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### Components

| Component | Technology | Status |
|-----------|------------|--------|
| Save Extractor | Python 3.10+ / lxml | ✅ Working |
| State Storage | JSON/Markdown | ✅ Working |
| Database | PostgreSQL + pgvector | ⬜ Planned |
| File Watcher | Python watchdog | ⬜ Planned |
| Claude Integration | CrystalDB MCP | ⬜ Planned |

---

## 📁 Repository Structure

```
rimworld-ai-colony-coplay/
├── 📂 game-saves/            # Colony save files (gitignored)
│   └── deserters-of-the-rim/ # Test colony
├── 📂 .kilocode/             # Agent memory bank
│   └── rules/memory-bank/    # Context files
├── 📂 .internal-files/       # Dev artifacts (gitignored)
│   └── rimworld-1_6-save-file-xml.md  # GDR research
├── 📂 tools/                 # Python tooling
│   ├── extractor/            # Save file parser ✅
│   │   ├── rimworld_extractor.py
│   │   └── parsers/          # Section parsers
│   └── watcher/              # File watcher (planned)
├── 📂 state/                 # Extracted game state (gitignored)
│   └── snapshots/            # JSON/Markdown output
├── 📂 mod/                   # C# mod source (Phase 2+)
├── 📚 docs/                  # Documentation
├── 📂 work-logs/             # Development milestones
├── 📄 LICENSE
└── 📄 README.md              # This file
```

---

## 🎮 Extraction Capabilities

### Currently Implemented ✅

| Category | Data Extracted |
|----------|----------------|
| Meta | Game version, mod list (267 mods) |
| Game Time | Year, day, quadrum, season |
| World | Colony name, seed, coverage |
| Factions | 20 factions with LoadID resolution |
| Relations | Goodwill integers, relation kinds |
| Colonists | Name, age, skills (12), traits, needs |
| Animals | Species, faction, master assignment |
| Resources | 65 item types in 6 categories |
| Research | Current project, 310 completed |

### Planned 🔲

| Category | Data Extracted |
|----------|----------------|
| Buildings | Key structures, power grid, defenses |
| Zones | Stockpiles, growing zones, restrictions |
| Threats | Active raids, mechanoids, infestations |
| Events | Recent incidents, upcoming triggers |

### Known Limitations

| Limitation | Notes |
|------------|-------|
| Storyteller/Difficulty | Nested deeper in save, not yet extracted |
| Gender (modded) | Stored in genes/body type, returns "Unknown" |
| Compressed world data | `*Deflate` tags ignored (not needed for advisor) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- lxml library (`pip install lxml`)
- RimWorld 1.6 with autosave enabled
- Claude Desktop with FS MCP access to this repository

### Quick Start

```powershell
# Clone repository
git clone https://github.com/vintagedon/rimworld-ai-colony-coplay.git
cd rimworld-ai-colony-coplay

# Install dependencies
pip install lxml

# Run extraction
cd tools/extractor
python rimworld_extractor.py "..\..\game-saves\deserters-of-the-rim\Deserters of the Rim#§#Hoeaia.rws" -o ..\..\state\snapshots\

# Review output
Get-Content ..\..\state\snapshots\colony_*.md | Select-Object -First 50
```

### Configuration

RimWorld saves are located at:
```
C:\Users\{username}\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Saves\
```

Configure autosave frequency in RimWorld options for more granular state tracking.

---

## 🔬 Related Projects

| Project | Relationship |
|---------|--------------|
| [RimAI Framework](https://github.com/rimworld-ai/RimAI.Framework) | Reference for LLM integration patterns |
| [RimAI Core](https://github.com/rimworld-ai/RimAI.Core) | Reference for game state extraction |

These mods take the in-game terminal approach. This project studies their implementation for reference while pursuing the external advisor pattern.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Ludeon Studios** — RimWorld and its moddable architecture
- **RimAI Team** — Reference implementations for AI integration
- **Anthropic** — Claude and the MCP ecosystem
- **lxml Project** — Efficient XML streaming parser

---

Last Updated: 2026-01-18 | Phase 1a Complete
