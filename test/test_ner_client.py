import unittest

class TestNerClient(unittest.TestCase):

    # {ents: [{...}]},
    # html: '<span>>...'}

    def test_get_ents_returns_dictionary_given_empty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents('')
        self.assertIsInstance(ents, dict)