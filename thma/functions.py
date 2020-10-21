import CoolProp.CoolProp as CP

def get_property(property: str, state: dict, fluid: str):
    arguments = map_properties(state)
    #print(arguments)

    value = CP.PropsSI(property, arguments[0], arguments[1], arguments[2], arguments[3], fluid)
    message = property + ' = ' + str(value) + ' for "' + fluid + '" at '
    for key in state.keys():
        message += key + '=' + str(state[key]) + '; '
    #print(message)

    return value


def get_phase(state: dict, fluid):
    arguments = map_properties(state)
    return CP.PhaseSI(arguments[0], arguments[1], arguments[2], arguments[3], fluid)


def complete_state(state: dict, fluid: str):
    required_properties = ['T', 'P', 'H', 'S']
    for property in required_properties:
        if not property in state:
            state[property] = get_property(property, state, fluid)

    phase = get_phase(state, fluid)
    state['phase'] = phase
    if (phase == 'twophase'):
        state['Q'] = get_property('Q', state, fluid)


def map_properties(properties: dict):
    arguments = []

    for key in properties.keys():
        arguments.append(key)
        arguments.append(properties[key])

    return arguments