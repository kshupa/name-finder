class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """

    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)


class DocTestDouble:
    """
    Test double for spaCy Doc
    """

    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent["text"])]
