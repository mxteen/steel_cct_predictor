import dearpygui.dearpygui as dpg

c, si, mn, cr, ni, cu, mo, v = 0, 0, 0, 0, 0, 0, 0, 0
composition = c, si, mn, cr, ni, cu, mo, v
element_names = ['C', 'Si', 'Mn', 'Cr', 'Ni', 'Cu', 'Mo', 'V']

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
    composition = get_composition(composition_ui_elements)
    # temporary
    for element, content in zip(element_names, composition):
        print(element, content)

def reset_btn_action():
    print('reset_btn_action')
    for ui_el in composition_ui_elements:
        dpg.set_value(ui_el, 0)


primary_window_tag = 'Primary window'
viewport_title = "CCT calculator"

dpg.create_context()

with dpg.window(tag=primary_window_tag):
    dpg.add_text("Continious cooling transformation diagram calculator")
    input_c = dpg.add_input_float(
        label='C', min_value=0, max_value=0.8, step=0.01)
    input_si = dpg.add_input_float(
        label='Si', min_value=0, max_value=1, step=0.01)
    input_mn = dpg.add_input_float(
        label='Mn', min_value=0, max_value=1.5, step=0.01)
    input_cr = dpg.add_input_float(
        label='Cr', min_value=0, max_value=2, step=0.01)
    input_ni = dpg.add_input_float(
        label='Ni', min_value=0, max_value=3, step=0.01)
    input_cu = dpg.add_input_float(
        label='Cu', min_value=0, max_value=0.5, step=0.01)
    input_mo = dpg.add_input_float(
        label='Mo', min_value=0, max_value=1, step=0.01)
    input_v = dpg.add_input_float(
        label='V', min_value=0, max_value=0.2, step=0.01)
    composition_ui_elements = (
        input_c, input_si, input_mn, input_cr,
        input_ni, input_cu, input_mo, input_v
    )

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