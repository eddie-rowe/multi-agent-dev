import argparse
import importlib
import os
import sys
from typing import Dict, Any, List, Optional


def discover_modules(directory: str) -> Dict[str, str]:
    """Discover Python modules in the specified directory."""
    modules = {}
    if not os.path.exists(directory):
        return modules
        
    for item in os.listdir(directory):
        if item.endswith('.py') and not item.startswith('__'):
            module_name = item[:-3]  # Remove .py extension
            module_path = f"{directory.replace('/', '.')}.{module_name}"
            modules[module_name] = module_path
    
    return modules


def list_available_components() -> None:
    """List all available components in the project."""
    component_types = {
        "Individuals": "individuals",
        "Teams": "teams",
        "Tasks": "tasks",
        "Consensus Mechanisms": "consensus",
        "Tools": "tools",
        "Triggers": "triggers"
    }
    
    print("Available Components:")
    print("====================")
    
    for component_type, directory in component_types.items():
        modules = discover_modules(directory)
        if modules:
            print(f"\n{component_type}:")
            for name in modules.keys():
                print(f"  - {name}")
        else:
            print(f"\n{component_type}: None available")


def run_individual(name: str, args: Optional[List[str]] = None) -> Any:
    """Run an individual agent."""
    modules = discover_modules("individuals")
    if name not in modules:
        print(f"Error: Individual '{name}' not found")
        return None
    
    module = importlib.import_module(modules[name])
    if hasattr(module, "run"):
        return module.run(args or [])
    else:
        print(f"Error: Individual '{name}' does not have a run function")
        return None


def run_team(name: str, args: Optional[List[str]] = None) -> Any:
    """Run a team of agents."""
    modules = discover_modules("teams")
    if name not in modules:
        print(f"Error: Team '{name}' not found")
        return None
    
    module = importlib.import_module(modules[name])
    if hasattr(module, "run"):
        return module.run(args or [])
    else:
        print(f"Error: Team '{name}' does not have a run function")
        return None


def run_task(name: str, args: Optional[List[str]] = None) -> Any:
    """Run a specific task."""
    modules = discover_modules("tasks")
    if name not in modules:
        print(f"Error: Task '{name}' not found")
        return None
    
    module = importlib.import_module(modules[name])
    if hasattr(module, "run"):
        return module.run(args or [])
    else:
        print(f"Error: Task '{name}' does not have a run function")
        return None


def main() -> None:
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Multi-Agent Development Framework")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List available components")
    
    # Individual command
    individual_parser = subparsers.add_parser("individual", help="Run an individual agent")
    individual_parser.add_argument("name", help="Name of the individual to run")
    individual_parser.add_argument("args", nargs="*", help="Arguments to pass to the individual")
    
    # Team command
    team_parser = subparsers.add_parser("team", help="Run a team of agents")
    team_parser.add_argument("name", help="Name of the team to run")
    team_parser.add_argument("args", nargs="*", help="Arguments to pass to the team")
    
    # Task command
    task_parser = subparsers.add_parser("task", help="Run a specific task")
    task_parser.add_argument("name", help="Name of the task to run")
    task_parser.add_argument("args", nargs="*", help="Arguments to pass to the task")
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command == "list":
        list_available_components()
    elif args.command == "individual":
        run_individual(args.name, args.args)
    elif args.command == "team":
        run_team(args.name, args.args)
    elif args.command == "task":
        run_task(args.name, args.args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()