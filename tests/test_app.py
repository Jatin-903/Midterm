import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.power import PowerCommand
from app.plugins.menu import MenuCommand


# Test REPL behavior in the App class

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as exit_exception:
        app.start()
    assert exit_exception.type == SystemExit


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "Unknown command: unknown_command" in captured.out


# Test CommandHandler functionality with various commands

def test_register_and_execute_add_command():
    """Test registration and execution of the AddCommand."""
    handler = CommandHandler()
    add_command = AddCommand()

    # Register the add command
    handler.register_command("add", add_command)

    # Execute the add command
    result = handler.execute_command("add", 2, 3)

    # Assert the output is correct
    assert result == 5


def test_register_and_execute_subtract_command():
    """Test registration and execution of the SubtractCommand."""
    handler = CommandHandler()
    subtract_command = SubtractCommand()

    # Register the subtract command
    handler.register_command("subtract", subtract_command)

    # Execute the subtract command
    result = handler.execute_command("subtract", 5, 2)

    # Assert the output is correct
    assert result == 3


def test_register_and_execute_multiply_command():
    """Test registration and execution of the MultiplyCommand."""
    handler = CommandHandler()
    multiply_command = MultiplyCommand()

    # Register the multiply command
    handler.register_command("multiply", multiply_command)

    # Execute the multiply command
    result = handler.execute_command("multiply", 6, 7)

    # Assert the output is correct
    assert result == 42


def test_register_and_execute_divide_command():
    """Test registration and execution of the DivideCommand."""
    handler = CommandHandler()
    divide_command = DivideCommand()

    # Register the divide command
    handler.register_command("divide", divide_command)

    # Execute the divide command
    result = handler.execute_command("divide", 10, 2)

    # Assert the output is correct
    assert result == 5.0


def test_divide_by_zero():
    """Test that dividing by zero raises a ValueError."""
    handler = CommandHandler()
    divide_command = DivideCommand()

    # Register the divide command
    handler.register_command("divide_zero", divide_command)

    # Check that dividing by zero raises the appropriate ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        handler.execute_command("divide_zero", 10, 0)


def test_register_and_execute_power_command():
    """Test registration and execution of the PowerCommand."""
    handler = CommandHandler()
    power_command = PowerCommand()

    # Register the power command
    handler.register_command("power", power_command)

    # Execute the power command
    result = handler.execute_command("power", 2, 3)

    # Assert the output is correct (2^3 = 8)
    assert result == 8


def test_register_and_execute_menu_command():
    """Test registration and execution of the MenuCommand."""
    handler = CommandHandler()
    menu_command = MenuCommand(handler)

    # Register a sample command
    handler.register_command("sample", AddCommand())

    # Register the menu command
    handler.register_command("menu", menu_command)

    # Execute the menu command
    result = handler.execute_command("menu")

    # Assert that "sample" appears in the menu list
    assert "sample" in result


def test_execute_nonexistent_command():
    """Test executing a command that doesn't exist returns an error."""
    handler = CommandHandler()

    # Try executing a command that doesn't exist
    result = handler.execute_command("nonexistent")

    # Assert that the result matches the expected error message
    expected_message = "Unknown command: nonexistent"
    assert result == expected_message
