from functions import complete_state
import math

fluid = 'Isopentane'

tk = 40+273
tv = 150+273

power_vaporizer = 650e3
eta_turbine_isentrop = 0.85
eta_regenerator = 0.75
q_turbine_entry = 1


state1 = dict()
state2 = dict()
state3 = dict()
state4 = dict()
state5 = dict()
state6 = dict()
state5s = dict()
statePT2 = dict()


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

state5s['S'] = state4['S']
state5s['P'] = state1['P']


complete_state(state5s, fluid)
complete_state(state2, fluid)

state5['H'] = eta_turbine_isentrop * (state5s['H'] - state4['H']) + state4['H']
complete_state(state5, fluid)

statePT2['P'] = state6['P']
statePT2['T'] = state2['T']
complete_state(statePT2, fluid)

# (state3['H']-state2['H']) / (state5['H']-statePT2['H']) == eta_regenerator
state3['H']  = eta_regenerator *(state5['H']-statePT2['H']) + state2['H']
complete_state(state3, fluid)

delta_h_regenerator = state3['H']-state2['H']
state6['H'] = state5['H'] - delta_h_regenerator
complete_state(state6, fluid)

enthalpy_vaporizer = state4['H'] - state3['H']
mass_flow = power_vaporizer/enthalpy_vaporizer

power_generator = (state4['H'] - state5['H']) * mass_flow

print('state1:')
print(state1)
print('state2:')
print(state2)
print('state3:')
print(state3)
print('state4:')
print(state4)
print('state5:')
print(state5)
print('state6:')
print(state6)
print('state5s:')
print(state5s)
print('statePT2:')
print(statePT2)

print(round(power_generator/1000, 2), ' kW')
print(round(mass_flow, 2), 'kg/s')
print('Eta_Machine = ', round(power_generator/power_vaporizer, 3))
