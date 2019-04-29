#!../ENV/bin/python
# Testing classes

import unittest
from class_survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        # The setUp function makes it so that new objects don't have to be
        # initialized while running the tests
        """Create a survey and responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        # Create a new variable for the current object (self.var=obj)
        # which is an object of the class we have to test
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            # Use the function of the class to test in the current object
            # self.var.function()
            self.my_survey.store_response(response)
        for response in self.responses:
            # Use the assertIn function
            # self.assertIn()
            self.assertIn(response, self.my_survey.responses)

unittest.main()
