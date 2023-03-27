import time
def print_models(unprinted_designs, completed_models):
    """Simulate printing designs and move them to a new list."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nPrinting Model: {current_design}")
        time.sleep(.4)
        print(f".")
        time.sleep(.4)
        print(f".")
        time.sleep(.2)
        print(f".")
        time.sleep(.3)
        print(f".")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    time.sleep(2)
    print(f"\nThe following designs have been completed.")
    for completed_model in completed_models:
        time.sleep(.6)
        print(completed_model.title())

unprinted_designs = ['phone case', 'knife', 'house', 'battery beating map',
                     'penis pump', 'a horse']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)