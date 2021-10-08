import unittest
from ner_client import NamedEntityClient


class TestNerClient(unittest.TestCase):

    # {ents: [{...}]},
    # html: '<span>>...'}

    def test_get_ents_returns_dictionary_given_empty_string(self):
        model = NerModelTestDouble('eng')
        ner = NamedEntityClient(model)
        ents = ner.get_ents('')
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_string(self):
        ner = NamedEntityClient(model)
        ents = ner.get_ents('Autin is the capitol of Texas')
        self.assertIsInstance(ents, dict)
