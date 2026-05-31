# START_HERE.md

# Learning Journey OS Lite

## Read This First

This file is the single source of truth for this repository.

Before making any code, architecture, database, UI, documentation, or feature decisions:

READ THIS FILE FIRST.

If another document conflicts with this file, this file wins.

---

# Founder Story

I am a software developer, data science student, AI engineer, educator, and lifelong learner.

Over the last several years I have learned from:

* BS Degree in Data Science
* Flask projects
* AI and Machine Learning projects
* Google Colab notebooks
* Kaggle notebooks
* GitHub repositories
* Online courses
* Certificates
* Research papers
* Documentation
* YouTube
* Coding platforms

Examples of work already completed:

* Flask Applications
* Music Streaming App
* Quiz Master Project
* Stock Prediction Project
* AI and ML Assignments
* Competitive Programming Practice
* Educational Content Creation

---

# The Core Problem

I learn a lot.

I build a lot.

I document a lot.

But everything is scattered.

Examples:

* Python notes are stored in folders.
* Colab notebooks are in Google Drive.
* GitHub repositories contain important learnings.
* Certificates exist across multiple platforms.
* Code snippets exist inside old projects.
* Learning notes are difficult to locate.
* Project documentation is inconsistent.
* Learning history is fragmented.

As time passes I forget:

* Where I learned something.
* Which project used a technology.
* Where a notebook is stored.
* Which course taught a topic.
* Where a useful code snippet exists.
* What I learned months ago.

The problem is NOT lack of learning.

The problem is knowledge fragmentation.

---

# Project Mission

Build a personal Learning Operating System.

The system should become my:

* Knowledge Vault
* Learning Tracker
* Project Archive
* Certificate Vault
* Resource Directory
* Search Engine
* Professional Portfolio

One place to store everything.

---

# Definition Of Success

Six months from now I should be able to answer:

* Where did I learn Flask Security?
* Which project used Redis?
* What do I know about LangGraph?
* Show all resources about RAG.
* Which certificate covered MLOps?
* Which notebook contains vector database experiments?
* What did I learn in 2026?

without manually searching folders.

If I can answer those questions, the project is successful.

---

# Version 1 Goal

Version 1 is intentionally small.

This is NOT:

* A startup
* A SaaS platform
* An AI product
* A multi-user system

Version 1 exists to solve my own problem first.

---

# MVP Features

## Dashboard

Show:

* Total Assets
* Total Projects
* Total Notes
* Total Certificates
* Total Links
* Recent Activity

---

## Asset System

Everything is an Asset.

Examples:

* Note
* Course
* Project
* Certificate
* Link

Every asset should support:

* Title
* Description
* Tags
* Source
* URL
* Local Path
* Date Created

---

## Search

Search everything.

Search should work across:

* Titles
* Descriptions
* Tags

The search experience is one of the most important features.

---

## Links Hub

Store important links.

Examples:

* GitHub
* LinkedIn
* Kaggle
* LeetCode
* HackerRank
* Google Colab
* YouTube Playlists
* Documentation

---

## Timeline

Create a chronological learning history.

Examples:

2024

* Flask
* Upload App

2025

* Music App
* Quiz Master

2026

* AI Agents
* ADK
* LangGraph

---

## Markdown Notes

Store learning notes.

Support:

* Markdown
* Code Blocks
* Learning Documentation

---

# Non Goals

Do NOT implement:

* RAG
* LangGraph
* Google ADK
* Agent Systems
* ChromaDB
* Embeddings
* PostgreSQL
* Multi-user SaaS

Not now.

---

# Technology Stack

Frontend

* Jinja2
* Bootstrap 5

Backend

* Flask

Database

* SQLite

ORM

* SQLAlchemy

Migrations

* Flask-Migrate

Testing

* Pytest

Version Control

* Git
* GitHub

Documentation

* Markdown

---

# Architecture Principles

## Principle 1

Everything Is An Asset.

---

## Principle 2

Every Asset Is Searchable.

---

## Principle 3

Every Asset Can Be Tagged.

---

## Principle 4

Every Asset Can Appear On Timeline.

---

## Principle 5

Simple Is Better Than Complex.

---

## Principle 6

Future AI Integration Must Remain Possible.

---

# Git Workflow

Branches:

main

develop

feature/*

Examples:

feature/project-setup

feature/asset-system

feature/search

feature/dashboard

feature/timeline

feature/links-hub

Never commit directly to main.

---

# Commit Convention

Use:

feat:
fix:
docs:
refactor:
test:
style:
chore:

Examples:

feat: implement asset model

feat: add search page

docs: update project roadmap

fix: resolve search filtering bug

---

# Documentation Discipline

Every feature must update:

* TASKS.md
* CHANGELOG.md
* LEARNING_LOG.md

This repository should document both:

1. The product
2. My learning journey

---

# Codex Instructions

Before writing code:

Read:

* START_HERE.md
* PROJECT_DOCUMENT.md
* CODEX.md
* AGENTS.md
* ARCHITECTURE_DECISIONS.md
* CODING_STANDARDS.md
* ROADMAP.md
* TASKS.md
* CHANGELOG.md

Summarize understanding.

Create implementation plan.

Wait for approval if requirements are unclear.

---


# Code Documentation Philosophy

Code should be self-documenting whenever possible.

Use descriptive names.

Good:

get_asset_by_id()

Bad:

ga()

---

Every public function should have a docstring.

Example:

"""
Create a learning asset and generate
a corresponding timeline event.
"""

---

Comments should explain:

- Why something exists
- Business logic
- Architectural decisions
- Future extension points

Comments should NOT explain obvious code.

Bad:

# Increment counter
counter += 1

Good:

# Timeline events are stored separately to support
# future AI-generated learning summaries.

# GitHub Workflow

Never commit directly to main.

Development Flow:

main
← stable releases

develop
← integration branch

feature/*
← active work

---

Feature Development Process

1. Create feature branch
2. Implement feature
3. Update documentation
4. Commit changes
5. Push branch
6. Merge into develop

---

Every feature should update:

- TASKS.md
- CHANGELOG.md
- LEARNING_LOG.md

# Learning First Development

This project is not only software.

It is also a learning artifact.

Future me should understand:

- What was built
- Why it was built
- What was learned
- What challenges occurred
- How challenges were solved

Every major feature should be documented.

The repository should become:

- Portfolio
- Documentation
- Learning Archive
- Engineering Journal

at the same time.

intead of 
feat:
fix:
docs:

add examples 

feat: implement asset creation page

feat: add search functionality

fix: resolve asset filtering issue

docs: update roadmap for sprint 2

refactor: move asset logic into service layer

test: add asset model tests

chore: configure flask migration setup



# Final Rule

When choosing between:

A complicated solution

and

A simple maintainable solution

Choose the simple solution.

The purpose of this project is to solve knowledge fragmentation and preserve learning history.


