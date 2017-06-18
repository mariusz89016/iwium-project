class Pest(object):
    def __init__(self, klass, attributes):
        super().__init__()
        self.klass = klass
        self.attributes = attributes