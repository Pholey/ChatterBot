from unittest import TestCase
from chatterbot.adapters.logic import ClosestMatchAdapter
from chatterbot.adapters.logic import ClosestMeaningAdapter


class ClosestMatchAdapterTests(TestCase):

    def test_get_closest_statement(self):

        adapter = ClosestMatchAdapter()

        possible_choices = [
            "Who do you love?",
            "What is the meaning of life?",
            "I am Iron Man.",
            "What... is your quest?",
            "Yuck, black licorice jelly beans.",
            "I hear you are going on a quest?",
        ]

        close = adapter.get("What is your quest?", possible_choices)

        self.assertEqual("What... is your quest?", close)


class ClosestMeaningAdapterTests(TestCase):

    def test_get_closest_statement(self):

        adapter = ClosestMeaningAdapter()

        possible_choices = [
            "This is a lovely bog.",
            "This is a beautiful swamp.",
            "It smells like swamp."
        ]

        close = adapter.get("This is a lovely swamp.", possible_choices)

        self.assertEqual("This is a beautiful swamp.", close)
