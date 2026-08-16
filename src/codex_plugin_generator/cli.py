"""Command-line interface for Codex Plugin Generator."""

import click
import os
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from typing import Optional

from codex_plugin_generator.generator import PluginGenerator
from codex_plugin_generator.config import Config

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def main() -> None:
    """🚀 Codex Plugin Generator - Create production-ready Codex plugins."""
    pass


@main.command()
@click.option("--type", "-t", "plugin_type", 
              type=click.Choice(["mcp", "skill", "full"]),
              help="Plugin type to generate")
@click.option("--name", "-n", help="Plugin name")
@click.option("--description", "-d", help="Plugin description")
@click.option("--author", "-a", help="Author name")
@click.option("--output", "-o", help="Output directory")
@click.option("--no-tests", is_flag=True, help="Skip test generation")
@click.option("--no-ci", is_flag=True, help="Skip CI/CD configuration")
def generate(
    plugin_type: Optional[str],
    name: Optional[str],
    description: Optional[str],
    author: Optional[str],
    output: Optional[str],
    no_tests: bool,
    no_ci: bool,
) -> None:
    """Generate a new Codex plugin."""
    
    # Load config
    config = Config.load()
    
    # Interactive mode if missing options
    if not plugin_type:
        console.print("\n[bold cyan]🎨 Plugin Type[/bold cyan]")
        plugin_type = Prompt.ask(
            "What type of plugin?",
            choices=["mcp", "skill", "full"],
            default="skill"
        )
    
    if not name:
        console.print("\n[bold cyan]📝 Plugin Name[/bold cyan]")
        name = Prompt.ask("Plugin name (lowercase-with-dashes)")
        
    if not description:
        description = Prompt.ask(
            "Short description",
            default=f"A Codex {plugin_type} plugin"
        )
    
    if not author:
        author = config.author or Prompt.ask("Your name", default="Anonymous")
    
    if not output:
        output = os.getcwd()
    
    # Prepare generation options
    options = {
        "plugin_type": plugin_type,
        "name": name,
        "description": description,
        "author": author,
        "email": config.email,
        "github": config.github,
        "include_tests": not no_tests and config.include_tests,
        "include_ci": not no_ci and config.include_ci,
    }
    
    # Confirm
    console.print(f"\n[bold green]✨ Generating {plugin_type} plugin:[/bold green]")
    console.print(f"  Name: {name}")
    console.print(f"  Description: {description}")
    console.print(f"  Output: {output}/{name}")
    console.print(f"  Tests: {'Yes' if options['include_tests'] else 'No'}")
    console.print(f"  CI/CD: {'Yes' if options['include_ci'] else 'No'}")
    
    if not Confirm.ask("\nProceed?", default=True):
        console.print("[yellow]Cancelled[/yellow]")
        return
    
    # Generate
    try:
        generator = PluginGenerator(options)
        output_path = generator.generate(Path(output))
        
        console.print(f"\n[bold green]✅ Success![/bold green]")
        console.print(f"\nPlugin created at: [cyan]{output_path}[/cyan]")
        console.print("\n[bold]Next steps:[/bold]")
        console.print(f"  cd {output_path}")
        
        if plugin_type == "mcp":
            console.print("  pip install -e .")
            console.print("  # Add your MCP tools in src/tools.py")
        elif plugin_type == "skill":
            console.print("  # Edit SKILL.md with your skill instructions")
        else:
            console.print("  pip install -e .")
            console.print("  # Develop your plugin")
        
        console.print("\n  git init")
        console.print("  git add .")
        console.print('  git commit -m "Initial commit"')
        console.print("\n🚀 Happy coding!")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise


@main.command()
def init_config() -> None:
    """Initialize plugin generator configuration."""
    config_path = Path.home() / ".plugin-generator.json"
    
    if config_path.exists():
        if not Confirm.ask("Config already exists. Overwrite?"):
            return
    
    console.print("\n[bold cyan]🛠️  Plugin Generator Configuration[/bold cyan]\n")
    
    author = Prompt.ask("Your name", default="")
    email = Prompt.ask("Your email", default="")
    github = Prompt.ask("Your GitHub username", default="")
    
    config = Config(
        author=author,
        email=email,
        github=github,
    )
    
    config.save()
    console.print(f"\n[green]✓[/green] Configuration saved to {config_path}")


@main.command()
def list_templates() -> None:
    """List available templates."""
    console.print("\n[bold cyan]📚 Available Templates[/bold cyan]\n")
    
    templates = [
        {
            "name": "mcp",
            "title": "MCP Server",
            "description": "Full Model Context Protocol server with tools and resources"
        },
        {
            "name": "skill",
            "title": "Skill",
            "description": "Codex skill with SKILL.md documentation"
        },
        {
            "name": "full",
            "title": "Full Plugin",
            "description": "Complete plugin with MCP server, skills, and documentation"
        }
    ]
    
    for template in templates:
        console.print(f"[bold green]{template['title']}[/bold green] ({template['name']})")
        console.print(f"  {template['description']}\n")


if __name__ == "__main__":
    main()
