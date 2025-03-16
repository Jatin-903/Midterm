from app.commands import Command

class MenuCommand(Command):
    """Command to display available commands."""

    def __init__(self, command_handler):
        """Initialize with access to registered commands."""
        self.command_handler = command_handler

    def execute(self):
        """Return a list of available commands."""
        return "Available commands: " + ", ".join(self.command_handler.list_commands())
