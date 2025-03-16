from app.commands import Command

class MultiplyCommand(Command):
    """Command to perform multiplication."""

    def execute(self, a, b):
        """Execute the multiplication operation."""
        return a * b
