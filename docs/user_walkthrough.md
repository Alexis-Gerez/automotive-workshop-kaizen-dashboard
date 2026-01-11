User Walkthrough

Automotive Workshop Kaizen Dashboard

1. Purpose of This Walkthrough

This document provides a guided walkthrough of the Automotive Workshop Kaizen Dashboard from a user perspective.

It is intended for:

Recruiters and technical reviewers

Workshop supervisors or trainers

Anyone evaluating the application as a functional prototype

No prior technical knowledge is required.

2. Getting Started
Launching the Application

Open a terminal in the project root directory.

Activate the virtual environment.

Run the application:

streamlit run app.py


The app will open automatically in your browser.

The system starts in simulation mode, with preloaded sample data to ensure immediate usability.

3. Navigation Overview

The application is organized through a left-side navigation panel, which includes:

Dashboard General

Gestión de Tareas

Técnicos

Calidad & Retrabajos

Mejora Continua (Kaizen)

Each section represents a common operational area in an automotive workshop.

4. Dashboard General

This is the main operational overview.

What the user sees:

Total tasks registered for the period

Global efficiency indicator

Retrabajo (rework) rate

Number of active Kaizen opportunities

How to use it:

Quickly assess workshop performance

Identify potential inefficiencies

Support daily or weekly operational meetings

The dashboard emphasizes visual management, similar to physical shop-floor boards.

5. Gestión de Tareas (Task Management)

This module simulates the core operational workflow.

Create a New Task

Select task type (service, brakes, diagnostics, etc.)

Assign a technician

Define standard time

Add observations if needed

View Task History

Filter tasks by status

Review execution times

Track task progression

This section reflects how work orders are typically managed in real workshops.

6. Técnicos (Team Management)

This section provides visibility into the human side of operations.

Features:

View registered technicians

Add new technicians

Classify by specialty and seniority

Monitor active workforce

This module supports:

Resource planning

Training discussions

Leadership and team organization exercises

7. Calidad & Retrabajos (Quality Control)

This module focuses on process quality, not blame.

Key elements:

Automatic detection of time deviations

Identification of potential quality issues

Manual retrabajo registration with cause description

It is designed to:

Encourage root-cause analysis

Support continuous improvement discussions

Reinforce quality awareness in teams

8. Mejora Continua (Kaizen)

The Kaizen module represents the continuous improvement culture.

Workflow:

Register a detected problem

Assign area and impact category

Propose a solution

Track status (Pending → In Progress → Implemented)

Usage scenarios:

Team improvement meetings

Training sessions on Kaizen methodology

Simulation of real improvement cycles

The focus is on small, actionable improvements, aligned with Kaizen principles.

9. Typical Usage Scenarios

This application can be used for:

Workshop operational simulations

Leadership and supervision training

Technical education support

Process optimization discussions

Demonstration of data-driven decision-making

10. Notes for Reviewers

All data is simulated and stored in session memory

The application prioritizes clarity over complexity

The goal is to demonstrate applied operational thinking, not a full ERP system

11. Closing

This walkthrough reflects a practical approach to:

Workshop operations

Technical leadership

Continuous improvement culture

The application is designed to start conversations, support learning, and visualize processes — not just display data.