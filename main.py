from utils import fill_missing_elements
from transformations import Steel_CCT_Calculator, CCT_Fractions
from plotting import CCT_Plotter

# Input parameters
grain_size = 7
cooling_rates = [10**n for n in range(-3, 3)]
composition_dict = {'C':0.5,'Si':0.2,'Mn':0.6,'Ni':0.05,'Cr':0.05,'Mo':0.05}

fill_missing_elements(composition_dict, inplace=True)
print('filled missing elements')

cct_raw_data = Steel_CCT_Calculator(composition_dict, grain_size, cooling_rates)
print('calculated cct_raw_data')

# CCT_Plotter(cct_raw_data, composition_dict, cooling_rates)
