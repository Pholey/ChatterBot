from .logic import LogicAdapter
from fuzzywuzzy import process


class ClosestMatchAdapter(LogicAdapter):

    def get(self, text, list_of_statements):
        """
        Takes a statement string and a list of statement strings.
        Returns the closest matching statement from the list.
        """

        # Check if an exact match exists
        if text in list_of_statements:
            return text

        # Get the closest matching statement from the database
        return process.extract(text, list_of_statements, limit=1)[0][0]
