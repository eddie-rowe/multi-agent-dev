# multi-agent-dev

A flexible framework for creating, configuring, and orchestrating AI agents that can work individually or collaboratively to accomplish complex tasks through defined workflows and consensus mechanisms.

## Next steps for me

1. Refine spreadsheet of archetypes
2. Create each individual archetype and the team in `sandbox\jungian_acp_council.py`
3. Iterate until it works as expected
4. Deploy to a location where some individual members run on `cron` schedules (Options: n8n, GH Actions, home assistant w/pyscript)
5. Modify the file so you can send `tasks` in via webhook (If you want to trigger the script over a network, you can set it up as a simple web server using Flask, or another web framework, to accept HTTP POST requests.)

## Objectives

- **Agent Flexibility**: Create reusable AI agent roles with specialized capabilities for various tasks.
- **Dynamic Collaboration**: Enable dynamic team formation with clear responsibility allocation based on task requirements.
- **Workflow Structure**: Define structured workflows for efficient task completion.
- **Consensus Assurance**: Implement consensus protocols for group decision-making to ensure alignment in team efforts.
- **Extensibility**: Provide an extensible architecture that allows for the integration of custom functionalities and tools.

## User Requirements

- **Agent Role Definition**: Define individual agent roles encapsulating specific capabilities and behaviors.
- **Team Composition Mechanism**: Compose teams from individual agents, dynamically modifying as tasks change.
- **Workflow Design and Execution**: Enable users to design, configure, and execute task workflows.
- **Consensus Configuration**: Configure and select consensus mechanisms for team decisions based on specific use cases.
- **Monitoring and Evaluation Tools**: Monitor agent and team performance metrics effectively.
- **Extensible Framework**: Allow for the easy extension of the framework with custom tools, agents, triggers, and workflows.

## Core Features

1. **Individual Agent Management**
   - **Role Definition**: Support for defining agent roles in separate configuration files.
   - **Tool Registration**: Facilitate registration of tools used by agents, linked to their roles.
   - **Model Configuration**: Allow each agent to configure and load their models through individual Python files for easy updates and management.

2. **Team Composition**
   - **Dynamic Team Formation**: Include mechanisms for dynamically forming teams based on agent availability and task requirements.
   - **Role Assignment**: Automate role assignment while allowing manual overrides.
   - **Communication Protocols**: Establish standardized communication protocols for agents to interact efficiently.

3. **Task Execution**
   - **Task Definition Schema**: Provide a flexible schema for defining tasks, which can be extended as needed.
   - **Workflow Engine**: Integrate a workflow engine that uses Python files for defined tasks and workflows.
   - **Progress Tracking**: Include functionality for tracking task progress and managing states through a central controller.

4. **Consensus Mechanisms**
   - **Voting Systems**: Implement various voting methods (e.g., majority, weighted).
   - **Conflict Resolution**: Define clear protocols for resolving conflicts that arise during decision-making.
   - **Decision Verification**: Create mechanisms to verify decisions made by consensus to ensure accountability.

5. **Output Customization**
   - **Output Formats**: Support customizable output formats (e.g., Markdown, JSON).
   - **Custom Destinations**: Enable outputs to be directed to various destinations such as local filesystems, databases, or external APIs.

6. **Prompts and Triggers**
   - **Prompt Management**: Allow users to define and customize prompts to guide agent behavior and responses.
   - **Trigger Mechanisms**: Implement systems that trigger actions or workflows based on specific conditions or events in the environment.

## Technical Requirements

- **Modular Architecture**: Adopt a modular approach with clearly defined interfaces for individual components (agents, teams, tools, tasks, consensus, outputs, prompts, and triggers).
- **Standardized Communication Formats**: Utilize standardized protocols (like JSON or Protocol Buffers) for communication between agents.
- **Comprehensive Logging System**: Implement a centralized logging system to track actions, decisions, and state changes.
- **Fault Tolerance**: Incorporate fault tolerance mechanisms to maintain system stability during errors.
- **Extensible Tool Integration**: Use plugin interfaces for integrating third-party tools and functionalities easily.

## Success Metrics

- **Task Completion**: Measure task completion rate and quality through feedback loops and metrics.
- **Decision-Making Efficiency**: Evaluate the speed and accuracy of decisions made based on established consensus mechanisms.
- **Framework Adoption**: Gauge developer adoption through API usage, community engagement, and contributions.
- **System Reliability**: Test and measure the system's reliability under varying operational conditions and stress tests.

## Implementation Structure

To promote adherence to the modular architecture, ensure that the project is organized with each object residing in its own directory/file structure, as follows:

```python
multi-agent-dev/
│
├── main.py                    # The main entry point of the application
│
├── individuals/               # Directory for individual agent classes
│   ├── agent.py               # Base agent class
│   ├── specific_role.py       # Example of a specific agent role
│   └── ...
│
├── teams/                     # Directory for team composition and management
│   ├── team.py                # Base team class
│   └── ...
│
├── tools/                     # Directory for tool registrations and definitions
│   ├── tool.py                # Base tool class
│   └── ...
│
├── tasks/                     # Directory for task definitions and workflows
│   ├── task.py                # Base task class
│   └── ...
│
├── prompts/                   # Directory for managing prompts
│   ├── prompt.py              # Base prompt class
│   └── ...
|
├── consensus/                 # Directory for consensus protocols
│   ├── voting.py              # Implementation of voting systems
│   ├── conflict_resolution.py  # Implementation of conflict resolution mechanisms
│   └── ...
|
├── triggers/                  # Directory for trigger mechanisms
│   ├── trigger.py             # Base trigger class
│   └── ...
│
└── outputs/                   # Directory for output handling and customization
    ├── output.py              # Base output class
    └── ...
```


