import pandas as pd

generator0 = ['Fall of person (from work at height)', 
'Fall of objects', 
'Slips Trips  & Housekeeping',
'Manual handling operations', 
'Display screen equipment']

generator1 = [
    'Lighting levels',
    'Heating & ventilation',
    'Layout , storage,  space, obstructions',
    'Welfare facilities',
    'Electrical Equipment',
]
generator2 = ['Use of portable tools / equipment',
'Fixed machinery  or lifting equipment',
'Pressure vessels',
'Noise or Vibration',
'Fire hazards & flammable material'
]
generator3 = ['Vehicles / driving at work',
'Outdoor work / extreme weather',
'Fieldtrips / field work',
'Work with lasers ',
'Radiation sources'
]
generator4 = [
    'Hazardous fumes,',
'chemicals, dust',
'Hazardous biological agent',
'Confined space / asphyxiation risk',
'Condition of Buildings & glazing',
'Food preparation'

]
generator5 = [
    'Occupational stress',
'Violence to staff / verbal assault',
'Work with animals ',
'Lone working / work out of hours',
'Other Hazards specific to your work.'
]

example_table = pd.DataFrame(generator0)
example_table[1] = pd.DataFrame([i for i in range(5)])
example_table[2] = pd.DataFrame(generator1)
example_table[3] = pd.DataFrame([i for i in range(5,10)])
example_table[4] = pd.DataFrame(generator2)
example_table[5] = pd.DataFrame([i for i in range(10,15)])
example_table[6] = pd.DataFrame(generator3)
example_table[7] = pd.DataFrame([i for i in range(15,20)])
example_table[8] = pd.DataFrame(generator4)
example_table[9] = pd.DataFrame([i for i in range(20,25)])
example_table[10] = pd.DataFrame(generator5)
example_table[11] = pd.DataFrame([i for i in range(25,30)])

example_table.to_html('example_table.html')