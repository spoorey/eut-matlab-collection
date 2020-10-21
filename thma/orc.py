from functions import complete_state

fluid = 'Isopentane'

tk = 40+273
tv = 150+273

power_vaporizer = 650e3
eta_turbine = 0.85
eta_regenerator = 0.75
q_turbine_entry = 1


state1 = dict()
state2 = dict()
state3 = dict()
state4 = dict()
state5 = dict()
state6 = dict()
state5s = dict()


state4['T'] = tv
state4['Q'] = q_turbine_entry

state1['T'] = tk
state1['Q'] = 0


'''
print('superheated:')
superheated =  {'P': 101e3, 'T': 323}
complete_state(superheated, fluid)
print('subcooled:')
subcooled = {'P': 300e3, 'T': 273}
complete_state(subcooled, fluid)
'''


complete_state(state4, fluid)
complete_state(state1, fluid)

state2['S'] = state1['S']
state5['P'] = state1['P']
state6['P'] = state1['P']

state3['P'] = state4['P']
state2['P'] = state4['P']



complete_state(state2, fluid)

print('state1:')
print(state1)
print('state2:')
print(state2)
print('state4:')
print(state4)



#enthalpy_vaporizer = state4]['H'] - state3]['H']
#mass_flow = power_vaporizer/enthalpy_vaporizer

#print(mass_flow, 'kg/s')
