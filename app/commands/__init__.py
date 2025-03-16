class Command:
    """Base class for all commands."""
    
    def execute(self, *args):
        """Execute the command (to be overridden)."""
        raise NotImplementedError("Execute method must be implemented by subclasses")

class CommandHandler:
    """Handles command registration and execution."""
    
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Register a new command."""
        if not isinstance(command, Command):
            raise ValueError(f"Command {name} must be an instance of the Command class")
        self.commands[name] = command

    def unregister_command(self, name):
        """Unregister a command."""
        if name in self.commands:
            del self.commands[name]

    def execute_command(self, name, *args):
        """Execute a registered command."""
        command = self.commands.get(name)
        if command:
            return command.execute(*args)
        return f"Unknown command: {name}"

    def list_commands(self):
        """Return a list of all registered command names."""
        return list(self.commands.keys())

    def reset_commands(self):
        """Reset the command registry (useful for testing)."""
        self.commands.clear()
