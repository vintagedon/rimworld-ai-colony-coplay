<!--
---
title: "Shared Utilities"
description: "Cross-project utilities and scripts"
author: "VintageDon"
date: "2026-01-18"
version: "1.0"
status: "Active"
tags:
  - type: directory-readme
  - domain: utilities
  - tech: python
---
-->

# Shared

Cross-project utilities and scripts used consistently across repositories.

---

## 1. Contents

```
shared/
├── generate_tree.py    # Directory tree generator for documentation
└── README.md           # This file
```

---

## 2. Tools

| File | Purpose |
|------|---------|
| `generate_tree.py` | Generate directory tree output for documentation |

---

## 3. Usage

```powershell
# Generate tree for current directory
python shared/generate_tree.py .

# Generate tree for specific path
python shared/generate_tree.py D:\development-repositories\rimworld-ai-colony-coplay
```

---

## 4. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
