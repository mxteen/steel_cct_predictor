import dearpygui.dearpygui as dpg

c, si, mn, cr, ni, cu, mo, v = 0, 0, 0, 0, 0, 0, 0, 0
composition = c, si, mn, cr, ni, cu, mo, v
element_names = ['C', 'Si', 'Mn', 'Cr', 'Ni', 'Cu', 'Mo', 'V']
element_max_values = [0.8, 1, 1.5, 2, 3, 0.5, 1, 0.2]

def get_composition(ui_elements: tuple) -> tuple[float]:
    """_summary_

    Args:
        ui_elements (tuple): _description_

    Returns:
        tuple[float]: _description_
    """
    values = tuple([round(dpg.get_value(value), 3) for value in ui_elements])
    return values

def calc_btn_action():
    # changing the 'composition' from the global scope
    composition = get_composition(input_elements)
    # temporary
    for element, content in zip(element_names, composition):
        print(element, content)
    print(input_elements)
    print(type(input_elements[0]))

def reset_btn_action():
    print('reset_btn_action')
    for el in input_elements:
        dpg.set_value(el, 0)


primary_window_tag = 'Primary window'
viewport_title = "CCT calculator"

dpg.create_context()

with dpg.window(tag=primary_window_tag):
    dpg.add_text("Continious cooling transformation diagram calculator")
    input_elements = [
        dpg.add_input_float(label=name, tag=name, min_value=0,
                            max_value=max_val, step=0.01)
        for name, max_val in zip(element_names, element_max_values)
    ]

    # Create the actions for the 'Calculate' button
    calc_btn = dpg.add_button(label='Calculate')
    dpg.set_item_callback(calc_btn, calc_btn_action)

    # Create the actions for the 'Reset' button
    reset_btn = dpg.add_button(label='Reset')
    dpg.set_item_callback(reset_btn, reset_btn_action)

dpg.set_primary_window(primary_window_tag, True)
dpg.create_viewport(title=viewport_title, width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
