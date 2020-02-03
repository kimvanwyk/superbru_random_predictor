from collections import namedtuple
import random

PREDICTION = namedtuple('Prediction', ('direction', 'point_difference'))
NUM_PREDICTIONS = 7

random.seed()

def make_random_prediction():
    return PREDICTION(random.choice(('left', 'right')), random.randint(1,20))

def make_predictions(num_predictions = NUM_PREDICTIONS):
    return [make_random_prediction() for i in range(num_predictions)]

for (n,p) in enumerate(make_predictions(),1):
    print(f'Prediction {n:02}: {p[0]:5} by {p[1]}')
