from app.commands import Command

class SubtractCommand(Command):
    """Command to perform subtraction."""

    def execute(self, a, b):
        """Execute the subtraction operation."""
        return a - b
