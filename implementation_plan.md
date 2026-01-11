Implementation Plan

Automotive Workshop Kaizen Dashboard

1. Project Context and Objectives

This application was designed to simulate a real-world automotive workshop operational environment, focusing on visibility, organization, and continuous improvement rather than full ERP complexity.

The main objective was to create a lightweight decision-support tool that:

Reflects how workshops actually operate day-to-day

Supports supervisors, technical leaders, and trainers

Enables discussion around performance, efficiency, and improvement opportunities

The project intentionally avoids overengineering in favor of clarity, usability, and training value.

2. Design Principles

The implementation follows these core principles:

Operational realism
Data structures, task flows, and metrics mirror common workshop dynamics (task assignment, standard vs real time, retrabajos, Kaizen actions).

Visual management
Information is presented in dashboards and grouped views to support fast interpretation, similar to physical workshop boards.

Kaizen mindset
The system highlights deviations, inefficiencies, and improvement opportunities instead of focusing only on outputs.

Training-oriented structure
The app is suitable not only for daily operations but also for technical training, leadership workshops, and process analysis sessions.

3. Architecture Overview
Technology Stack

Streamlit for rapid development and interactive UI

Pandas for in-memory data modeling

Session State to simulate persistent operational data

CSS customization to achieve a professional, industrial-oriented interface

Data Model

The application is structured around three main entities:

Technicians

Skill level, specialty, availability

Tasks

Type, assigned technician, standard vs real time, status, retrabajo flag

Kaizen Actions

Problem identification, proposed solution, impact category, status tracking

This modular structure allows easy future expansion.

4. Key Functional Modules
Dashboard

High-level KPIs (efficiency, retrabajos, active Kaizen actions)

Task distribution and productivity visualization

Designed for daily or weekly operational reviews

Task Management

Creation and assignment of work orders

Status updates and real-time tracking

Comparison between standard and actual execution time

Technician Management

Registration and classification by seniority and specialty

Visibility of active workforce

Basis for performance and workload analysis

Quality & Retrabajo Analysis

Automatic detection of significant deviations

Manual retrabajo flagging

Root-cause analysis support

Kaizen Module

Structured improvement proposal workflow

Simple Kanban-style progression

Focus on small, actionable improvements

5. Assumptions and Scope Decisions

To keep the application focused and realistic:

Data persistence is simulated in memory (no database)

Metrics are indicative, not financial

User roles and authentication are intentionally omitted

The app represents a conceptual and educational tool, not a production ERP

These decisions were made deliberately to prioritize:

Speed of understanding

Training applicability

Portfolio clarity

6. Future Enhancements (Optional Roadmap)

Potential improvements include:

Persistent storage (SQLite / PostgreSQL)

User roles (manager, supervisor, technician)

Exportable reports (PDF / Excel)

Integration with training modules or LMS platforms

KPI benchmarking over time

These were intentionally left out to maintain scope control and conceptual clarity.

7. Intended Use Cases

Technical leadership training

Workshop process analysis

Kaizen methodology demonstrations

Operational management simulations

Portfolio demonstration of applied operational thinking

8. Closing Note

This project reflects a hybrid profile combining:

Field experience in automotive operations

Technical data handling

Educational and training-oriented thinking

Continuous improvement methodologies

The implementation prioritizes how people work, not just how systems compute.