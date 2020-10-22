import CoolProp.CoolProp as CP
from CoolProp.Plots.SimpleCycles import StateContainer
from CoolProp.Plots import PropertyPlot


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

    return state

def create_ts_plot(states: list, fluid: str):
    cycle_states = StateContainer()

    # plot only displays a dot for the state if it occurs twice
    merged_states = []
    for state in states:
        merged_states.append(state['data'])
        if state['marker']:
            merged_states.append(state['data'])

    states = merged_states

    i = 0
    for state in states:
        cycle_states[i, 'P'] = state['P']
        cycle_states[i]['T'] = state['T']
        cycle_states[i]['S'] = state['S']
        cycle_states[i]['H'] = state['H']
        i += 1

    plot = PropertyPlot(fluid, 'TS', tp_limits='ORC')
    plot.calc_isolines(CP.iQ, num=2)
    plot.calc_isolines(CP.iP)

    style = {}
    '''
    style = {
        'marker': 'o',
        'markerfacecolor': 'blue',
        'markeredgecolor': 'blue',
        'color': matplotlib.colors.to_rgba('#ff0000'),
    }
    '''

    plot.draw_process(cycle_states, line_opts=style)

    return plot

def map_properties(properties: dict):
    arguments = []

    for key in properties.keys():
        arguments.append(key)
        arguments.append(properties[key])

    return arguments