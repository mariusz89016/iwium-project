def from_attrs_to_Q_state(attributes):
    size = {40: 0, 10: 1}
    legs = {40: 0, 30: 1}
    speed = {40: 0, 20: 1, 10: 2}
    jump = {40: 0, 20: 1, 10: 2}

    return size[attributes[0]] + \
           2 * legs[attributes[1]] + \
           2 * 2 * speed[attributes[2]] + \
           2 * 2 * 3 * jump[attributes[3]]