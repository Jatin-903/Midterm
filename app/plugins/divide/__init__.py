from app.commands import Command

class DivideCommand(Command):
    """Command to perform division."""

    def execute(self, a, b):
        """Execute the division operation."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
