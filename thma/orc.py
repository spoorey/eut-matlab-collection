import CoolProp.CoolProp as CP

fluid = 'Isopentane'

tk = 50+273
tv = 150+273

power_vaporizer = 650e3
eta_turbine = 0.85
eta_regenerator = 0.75
q_turbine_entry = 1

states = [None] * 7
for key, value in enumerate(states):
    states[key] = dict()

states[4]['T'] = tv
states[4]['Q'] = q_turbine_entry
states[1]['T'] = tk
states[1]['Q'] = 0

def get_property(property: str, state: dict, fluid: str):
    value = None
    arguments = map_properties(state)
    #print(arguments)

    value = CP.PropsSI(property, arguments[0], arguments[1], arguments[2], arguments[3], fluid)
    message = property + ' = ' + str(value) + ' for "' + fluid + '" at '
    for key in state.keys():
        message += key + '=' + str(state[key]) + '; '
    print(message)

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

'''
print('superheated:')
superheated =  {'P': 101e3, 'T': 323}
complete_state(superheated, fluid)
print('subcooled:')
subcooled = {'P': 300e3, 'T': 273}
complete_state(subcooled, fluid)
'''


complete_state(states[4], fluid)
complete_state(states[1], fluid)

states[2]['S'] = states[1]['S']
states[5]['P'] = states[1]['P']
states[6]['P'] = states[1]['P']

states[3]['P'] = states[4]['P']
states[2]['P'] = states[4]['P']

states[3]['Q'] = 0


#enthalpy_vaporizer = states[4]['H'] - states[3]['H']
#mass_flow = power_vaporizer/enthalpy_vaporizer

#print(mass_flow, 'kg/s')
