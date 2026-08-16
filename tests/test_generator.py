"""Tests for plugin generator."""

import pytest
from pathlib import Path
import tempfile
import shutil
from codex_plugin_generator.generator import PluginGenerator


@pytest.fixture
def temp_output_dir():
    """Create temporary output directory."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


def test_generate_mcp_plugin(temp_output_dir):
    """Test MCP plugin generation."""
    options = {
        'plugin_type': 'mcp',
        'name': 'test-plugin',
        'description': 'Test MCP plugin',
        'author': 'Test Author',
        'email': 'test@example.com',
        'github': 'testuser',
        'license': 'MIT',
        'include_tests': True,
        'include_ci': True,
    }
    
    generator = PluginGenerator(options)
    output_path = generator.generate(temp_output_dir)
    
    # Check structure
    assert output_path.exists()
    assert (output_path / "README.md").exists()
    assert (output_path / "pyproject.toml").exists()
    assert (output_path / "src" / "test_plugin" / "server.py").exists()
    assert (output_path / "tests" / "test_server.py").exists()
    assert (output_path / ".github" / "workflows" / "test.yml").exists()
    
    # Check content
    readme = (output_path / "README.md").read_text()
    assert "Test Plugin" in readme
    assert "Test MCP plugin" in readme


def test_generate_skill_plugin(temp_output_dir):
    """Test skill plugin generation."""
    options = {
        'plugin_type': 'skill',
        'name': 'test-skill',
        'description': 'Test skill',
        'author': 'Test Author',
        'email': 'test@example.com',
        'license': 'MIT',
    }
    
    generator = PluginGenerator(options)
    output_path = generator.generate(temp_output_dir)
    
    # Check structure
    assert output_path.exists()
    assert (output_path / "SKILL.md").exists()
    assert (output_path / "README.md").exists()
    assert (output_path / "plugin.json").exists()
    assert (output_path / "examples" / "example.md").exists()


def test_kebab_to_title():
    """Test kebab case to title conversion."""
    assert PluginGenerator._kebab_to_title("test-plugin") == "Test Plugin"
    assert PluginGenerator._kebab_to_title("my-awesome-tool") == "My Awesome Tool"


def test_kebab_to_snake():
    """Test kebab case to snake case conversion."""
    assert PluginGenerator._kebab_to_snake("test-plugin") == "test_plugin"
    assert PluginGenerator._kebab_to_snake("my-tool") == "my_tool"
