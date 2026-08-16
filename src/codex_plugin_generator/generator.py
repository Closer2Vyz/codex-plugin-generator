"""Plugin generation logic."""

from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os


class PluginGenerator:
    """Generate Codex plugins from templates."""
    
    def __init__(self, options: Dict[str, Any]):
        self.options = options
        
        # Get templates directory
        templates_dir = Path(__file__).parent / 'templates'
        
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Add filters
        self.env.filters['kebab_to_title'] = self._kebab_to_title
        self.env.filters['kebab_to_snake'] = self._kebab_to_snake
        
        # Add globals
        self.env.globals['now'] = datetime.now()
    
    def generate(self, output_dir: Path) -> Path:
        """Generate plugin in output directory."""
        plugin_name = self.options['name']
        plugin_type = self.options['plugin_type']
        plugin_path = output_dir / plugin_name
        
        # Create plugin directory
        plugin_path.mkdir(parents=True, exist_ok=True)
        
        # Generate based on type
        if plugin_type == "mcp":
            self._generate_mcp(plugin_path)
        elif plugin_type == "skill":
            self._generate_skill(plugin_path)
        elif plugin_type == "full":
            self._generate_full(plugin_path)
        
        return plugin_path
    
    def _generate_mcp(self, path: Path) -> None:
        """Generate MCP server plugin."""
        package_name = self.options['name'].replace('-', '_')
        
        # Create structure
        (path / "src" / package_name).mkdir(parents=True, exist_ok=True)
        
        if self.options.get('include_tests', True):
            (path / "tests").mkdir(exist_ok=True)
        
        (path / "examples").mkdir(exist_ok=True)
        
        # Generate files
        self._render_file("mcp/README.md.j2", path / "README.md")
        self._render_file("mcp/pyproject.toml.j2", path / "pyproject.toml")
        self._render_file("mcp/server.py.j2", 
                         path / "src" / package_name / "server.py")
        self._render_file("mcp/__init__.py.j2", 
                         path / "src" / package_name / "__init__.py")
        self._render_file("common/gitignore.j2", path / ".gitignore")
        self._render_file("common/LICENSE.j2", path / "LICENSE")
        
        if self.options.get('include_tests', True):
            self._render_file("mcp/test_server.py.j2", path / "tests" / "test_server.py")
            # Create __init__.py for tests
            (path / "tests" / "__init__.py").touch()
        
        if self.options.get('include_ci', True):
            (path / ".github" / "workflows").mkdir(parents=True, exist_ok=True)
            self._render_file("common/ci.yml.j2", path / ".github" / "workflows" / "test.yml")
    
    def _generate_skill(self, path: Path) -> None:
        """Generate skill plugin."""
        # Create structure
        (path / "examples").mkdir(exist_ok=True)
        
        # Generate files
        self._render_file("skill/plugin.json.j2", path / "plugin.json")
        self._render_file("skill/SKILL.md.j2", path / "SKILL.md")
        self._render_file("skill/README.md.j2", path / "README.md")
        self._render_file("skill/example.md.j2", path / "examples" / "example.md")
        self._render_file("common/gitignore.j2", path / ".gitignore")
        self._render_file("common/LICENSE.j2", path / "LICENSE")
    
    def _generate_full(self, path: Path) -> None:
        """Generate full plugin."""
        # Generate MCP server
        self._generate_mcp(path)
        
        # Add skill
        (path / "skills" / "main-skill").mkdir(parents=True, exist_ok=True)
        self._render_file("skill/SKILL.md.j2", path / "skills" / "main-skill" / "SKILL.md")
        
        # Add extra docs
        self._render_file("full/CONTRIBUTING.md.j2", path / "CONTRIBUTING.md")
        (path / "docs").mkdir(exist_ok=True)
    
    def _render_file(self, template_name: str, output_path: Path) -> None:
        """Render template to file."""
        template = self.env.get_template(template_name)
        content = template.render(**self.options)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(content)
    
    @staticmethod
    def _kebab_to_title(s: str) -> str:
        """Convert kebab-case to Title Case."""
        return ' '.join(word.capitalize() for word in s.split('-'))
    
    @staticmethod
    def _kebab_to_snake(s: str) -> str:
        """Convert kebab-case to snake_case."""
        return s.replace('-', '_')
