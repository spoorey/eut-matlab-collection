from functions import complete_state

fluid = 'Isopentane'

tk = 40+273
tv = 150+273

power_vaporizer = 650e3
eta_turbine = 0.85
eta_regenerator = 0.75
q_turbine_entry = 1

states = [dict()] * 7
for key, value in enumerate(states):
    states[key] = dict()

states[4]['T'] = tv
states[4]['Q'] = q_turbine_entry
states[1]['T'] = tk
states[1]['Q'] = 0

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



complete_state(states[2], fluid)

print('state1:')
print(states[1])
print('state2:')
print(states[2])
print('state4:')
print(states[4])



#enthalpy_vaporizer = states[4]['H'] - states[3]['H']
#mass_flow = power_vaporizer/enthalpy_vaporizer

#print(mass_flow, 'kg/s')
