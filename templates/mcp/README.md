# {{ plugin_name }}

{{ description }}

## Installation

```bash
pip install -e .
```

## Configuration

Add to your MCP settings:

```json
{
  "mcpServers": {
    "{{ plugin_name }}": {
      "command": "python",
      "args": ["-m", "{{ plugin_name }}.server"]
    }
  }
}
```

## Usage

See [server.py](server.py) for implementation details.

## Author

{{ author }}

## License

MIT
