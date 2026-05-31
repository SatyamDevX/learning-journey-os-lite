# Project Document

## Project Name

Learning Journey OS Lite

## Project Summary

Learning Journey OS Lite is a personal knowledge and learning archive built with Flask and SQLite. It stores learning assets such as notes, projects, courses, certificates, links, and notebooks so they can be searched, tagged, reviewed, and connected to a chronological learning timeline.

The project exists to solve one personal problem: learning history and project knowledge are scattered across folders, GitHub repositories, Google Drive, certificates, notebooks, and online platforms.

## Mission

Build a simple personal Learning Operating System that acts as a:

- Knowledge vault
- Learning tracker
- Project archive
- Certificate vault
- Resource directory
- Search engine
- Professional portfolio foundation

## Success Definition

The project is successful when it can answer questions such as:

- Where did I learn Flask security?
- Which project used Redis?
- What do I know about LangGraph?
- Show all resources about RAG.
- Which certificate covered MLOps?
- Which notebook contains vector database experiments?
- What did I learn in 2026?

The answer should be discoverable without manually searching folders.

## Target User

Version 1 is for one user: the project founder and maintainer.

This is not a startup, SaaS product, multi-user platform, or AI product in the MVP stage.

## Core Concept

Everything is an asset.

An asset may represent:

- Note
- Course
- Project
- Certificate
- Link
- Notebook
- Documentation resource
- Coding platform profile

Each asset should support:

- Title
- Description
- Tags
- Source
- URL
- Local path
- Date created

## MVP Features

### Dashboard

Show high-level learning archive metrics:

- Total assets
- Total projects
- Total notes
- Total certificates
- Total links
- Recent activity

### Asset System

Create, view, update, delete, tag, and classify learning assets.

### Search

Search across:

- Titles
- Descriptions
- Tags

Search is one of the most important experiences in the product.

### Links Hub

Store and organize important links, including:

- GitHub
- LinkedIn
- Kaggle
- LeetCode
- HackerRank
- Google Colab
- YouTube playlists
- Documentation

### Timeline

Show a chronological learning history by year and asset activity.

### Markdown Notes

Store learning notes with Markdown and code block support.

## Non Goals

Do not implement these in Version 1:

- RAG
- LangGraph
- Google ADK
- Agent systems
- ChromaDB
- Embeddings
- PostgreSQL
- Multi-user SaaS features

## Technology Stack

- Flask
- Jinja2
- Bootstrap 5
- SQLite
- SQLAlchemy
- Flask-Migrate
- Pytest
- Markdown documentation
- Git and GitHub

## Documentation Expectations

This repository is both software and a learning artifact. Major work should record:

- What was built
- Why it was built
- What was learned
- What challenges occurred
- How challenges were solved

Every feature must update `TASKS.md`, `CHANGELOG.md`, and `LEARNING_LOG.md`.
