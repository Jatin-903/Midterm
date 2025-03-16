import pytest
from app.commands import CommandHandler, Command

class MockCommand(Command):
    """Mock command for testing."""
    def execute(self, *args):
        return f"Mock Command Executed with args: {args}"

@pytest.fixture
def command_handler():
    """Fixture for CommandHandler."""
    return CommandHandler()

@pytest.fixture
def mock_command():
    """Fixture for a mock command."""
    return MockCommand()

def test_register_command(command_handler, mock_command):
    """Test registering a command."""
    command_handler.register_command("mock", mock_command)
    assert "mock" in command_handler.commands

def test_register_invalid_command(command_handler):
    """Test that registering an invalid command raises an error."""
    with pytest.raises(ValueError, match="Command test must be an instance of the Command class"):
        command_handler.register_command("test", "invalid_command")

def test_execute_command(command_handler, mock_command):
    """Test executing a registered command."""
    command_handler.register_command("mock", mock_command)
    assert command_handler.execute_command("mock", "arg1") == "Mock Command Executed with args: ('arg1',)"

def test_execute_unknown_command(command_handler):
    """Test executing an unknown command."""
    assert command_handler.execute_command("unknown") == "Unknown command: unknown"

def test_unregister_command(command_handler, mock_command):
    """Test unregistering a command."""
    command_handler.register_command("mock", mock_command)
    command_handler.unregister_command("mock")
    assert "mock" not in command_handler.commands

def test_list_commands(command_handler, mock_command):
    """Test listing available commands."""
    command_handler.register_command("mock", mock_command)
    assert "mock" in command_handler.list_commands()

def test_reset_commands(command_handler, mock_command):
    """Test resetting the command registry."""
    command_handler.register_command("mock", mock_command)
    command_handler.reset_commands()
    assert command_handler.list_commands() == []
