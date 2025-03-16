from app.commands import Command

class AddCommand(Command):
    """Command to perform addition."""

    def execute(self, a, b):
        """Execute the addition operation."""
        return a + b
