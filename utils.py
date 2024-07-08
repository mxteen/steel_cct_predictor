import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def mass2mole(mass):
    molweight = {
        'Fe':55.85, 'C':12.01, 'Si':28.09, 'Mn':54.94, 'Ni':58.69, 'Cr':52,
        'Mo':95.94, 'W':183.85, 'Co':58.93, 'V':50.94, 'Nb':92.91, 'Cu':63.55,
        'Al':26.98,'Ti':47.88,'O':16,'N':14.01,'B':10.81,'P':30.97,'S':32.06,
        'As':74.92}
    if 'Fe' in mass.keys():
        pass
    else:
        mass['Fe'] = 100 - sum(mass.values())
    a = []
    for elm in mass.keys():
        mole = mass[elm]/molweight[elm]
        a.append(mole)
    tot_moles = sum(a)
    moles = {}
    n = 0
    for mol in a:
        moles[list(mass.keys())[n]] = mol/tot_moles
        n += 1
    return moles

def roundup(x):
    return x if x % 1000 == 0 else x + 1000 - x % 1000


def fill_missing_elements(
        composition: dict[str, float], inplace: bool = True) -> dict[str, float] | None:
    """
    Fills missing elements in a chemical composition dictionary with zeros.

    Parameters:
    composition (dict[str, float]): A dictionary representing the chemical
                                    composition, where keys are element symbols
                                    and values are their respective amounts.
    inplace (bool): If True, modifies the input dictionary in place. If False,
                    returns a new dictionary with the missing values filled.
                    Default is True.

    Returns:
    dict[str, float] | None: If inplace is False, returns a new dictionary with
                             the missing values filled. If inplace is True,
                             returns None.
    """
    # List of standard elements to check for in the composition
    elements = ['C', 'Si', 'Mn', 'P', 'Cr', 'Ni', 'Cu',
                'Mo', 'Al', 'V', 'Ti', 'Co', 'W', 'As']

    if inplace:
        # Fill missing elements with zero in the original composition dictionary
        for e in elements:
            composition.setdefault(e, 0)
        # Return None as the operation is done in place
        return None
    else:
        # Create a copy of the original composition dictionary
        composition_filled = composition.copy()
        # Fill missing elements with zero in the new composition dictionary
        for e in elements:
            if e not in composition_filled:
                composition_filled[e] = 0
        # Return the new dictionary with missing values filled
        return composition_filled
