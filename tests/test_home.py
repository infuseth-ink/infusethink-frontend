"""Unit tests for home page components."""

from src.pages.home import CounterModel


class TestCounterModel:
    """Test the observable business logic."""

    def test_initial_state(self):
        """Test initial counter state."""
        model = CounterModel()
        assert model.counter == 0

    def test_increment(self):
        """Test incrementing counter."""
        model = CounterModel()
        model.increment()
        assert model.counter == 1

        model.increment()
        assert model.counter == 2

    def test_decrement(self):
        """Test decrementing counter."""
        model = CounterModel()
        model.counter = 5

        model.decrement()
        assert model.counter == 4

    def test_reset(self):
        """Test resetting counter."""
        model = CounterModel()
        model.counter = 42

        model.reset()
        assert model.counter == 0

    def test_multiple_operations(self):
        """Test combining multiple operations."""
        model = CounterModel()

        # Start with increment
        model.increment()
        model.increment()
        assert model.counter == 2

        # Decrement once
        model.decrement()
        assert model.counter == 1

        # Reset to zero
        model.reset()
        assert model.counter == 0
