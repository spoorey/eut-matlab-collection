import CoolProp.CoolProp as CP

fluid = 'Isopentane'
tk = 50
tv = 150

states = [dict()] * 6

states[4]['T'] = tv
states[4]['Q'] = 1

def get_property(property: str, properties: dict, fluid: str):
    print(properties)
    arguments = []
    for key in properties.keys():
        arguments.append(key)
        arguments.append(properties[key])

    print(arguments)
    if len(properties) == 2:
        value = CP.PropsSI(property, arguments[0], arguments[1], arguments[2], arguments[3], fluid)
        print(
            property + ' = ' + str(value) +
            ' for "' + fluid + '" at ' +
            arguments[0] + '=' + str(arguments[1]) + '; ' +
            arguments[2] + '=' + str(arguments[3])
)

get_property('H', states[4], fluid)

pressure_at_critical_point = CP.PropsSI(fluid,'pcrit')
print(pressure_at_critical_point)

# Massic volume (in m^3/kg) is the inverse of density
# (or volumic mass in kg/m^3). Let's compute the massic volume of liquid
# at 1bar (1e5 Pa) of pressure
vL = 1/CP.PropsSI('D','P',1e5,'Q',0,fluid)
# Same for saturated vapor
vG = 1/CP.PropsSI('D','P',1e5,'Q',1,fluid)