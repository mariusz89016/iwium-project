import numpy as np

from fpenv.pest_generator.Pest import Pest

STATE_SPACE_SIZE = 2 * 2 * 3 * 3

size_attr = {0: lambda: 10 if np.random.random() > 0.6 else 40,
             1: lambda: 10 if np.random.random() > 0.6 else 40,
             2: lambda: 10 if np.random.random() > 0.5 else 40,
             3: lambda: 10 if np.random.random() > 0.4 else 40,
             4: lambda: 10 if np.random.random() > 0.5 else 40,
             5: lambda: 10 if np.random.random() > 0.5 else 40,
             6: lambda: 10 if np.random.random() > 0.6 else 40,
             7: lambda: 10 if np.random.random() > 0.5 else 40}

legs_attr = {0: lambda: 30 if np.random.random() > 0.9 else 40,
             1: lambda: 30 if np.random.random() > 0.8 else 40,
             2: lambda: 30 if np.random.random() > 1.0 else 40,
             3: lambda: 30 if np.random.random() > 0.9 else 40,
             4: lambda: 30 if np.random.random() > 0.1 else 40,
             5: lambda: 30 if np.random.random() > 0.2 else 40,
             6: lambda: 30 if np.random.random() > 0.0 else 40,
             7: lambda: 30 if np.random.random() > 0.1 else 40}

speed_attr = {0: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.8 else 40),
              1: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.7 else 40),
              2: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.8 else 40),
              3: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.0 else 40),
              4: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.05 else 40),
              5: lambda: 10 if np.random.random() > 1.0 else (20 if np.random.random() > 0.0 else 40),
              6: lambda: 10 if np.random.random() > 0.1 else (20 if np.random.random() > 0.0 else 40),
              7: lambda: 10 if np.random.random() > 0.2 else (20 if np.random.random() > 0.1 else 40)}

jump_attr = {0: lambda: 10 if np.random.random() > 1.0 else (20 if np.random.random() > 0.8 else 40),
             1: lambda: 10 if np.random.random() > 0.95 else (20 if np.random.random() > 0.05 else 40),
             2: lambda: 10 if np.random.random() > 0.2 else (20 if np.random.random() > 0.05 else 40),
             3: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.8 else 40),
             4: lambda: 10 if np.random.random() > 0.85 else (20 if np.random.random() > 0.05 else 40),
             5: lambda: 10 if np.random.random() > 0.2 else (20 if np.random.random() > 0.05 else 40),
             6: lambda: 10 if np.random.random() > 0.9 else (20 if np.random.random() > 0.8 else 40),
             7: lambda: 10 if np.random.random() > 0.85 else (20 if np.random.random() > 0.05 else 40)}


class PestGenerator(object):
    def __init__(self, no_attrs=3):
        super().__init__()
        self.no_attrs = no_attrs

    def generate(self, assign_class_fun):
        generated_attributes = np.random.random(self.no_attrs)
        assigned_class = assign_class_fun(generated_attributes)
        return Pest(assigned_class, generated_attributes)


class PestGenerator2(object):
    def generate(self):
        klass = np.random.randint(0, 8)
        generated_attributes = [size_attr[klass](), legs_attr[klass](), speed_attr[klass](), jump_attr[klass]()]
        return Pest(klass, generated_attributes)
