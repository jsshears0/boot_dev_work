from dragon_postional import *

run_cases = [
    (
        [Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Draco", 2, 2, 3),
        2,
        3,
        ["Cian", "Andrew"],
    ),
]

submit_cases = run_cases + [
    (
        [
            Unit("Carbry", 2, 1),
            Unit("Yvor", 1, 0),
            Unit("Eoin", 2, 0),
            Unit("Edwin", 10, 10),
        ],
        Dragon("Fafnir", 1, 1, 1),
        1,
        1,
        ["Carbry", "Yvor", "Eoin"],
    ),
    (
        [Unit("Nicholas", 0, 1), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Hydra", 0, 0, 2),
        0,
        1,
        ["Nicholas"],
    ),
    (
        [
            Unit("Yvor", 1, 0),
            Unit("Nicholas", 0, 1),
            Unit("Eoin", 2, 0),
            Unit("Cian", 3, 3),
            Unit("Andrew", -1, 4),
            Unit("Baran", -6, 5),
            Unit("Carbry", 2, 1),
        ],
        Dragon("Smaug", 6, 6, 2),
        1,
        1,
        ["Yvor", "Nicholas", "Eoin", "Cian", "Carbry"],
    ),
]


def test(units, dragon, x_target, y_target, expected_hit_units):
    print("---------------------------------")
    print(f"Testing Dragon {dragon.name} at ({dragon.pos_x}, {dragon.pos_y})")
    for unit in units:
        print(f"Unit {unit.name} at ({unit.pos_x}, {unit.pos_y})")
    print(f"Breathing fire at ({x_target}, {y_target})")
    print(f"Expecting hit units: {expected_hit_units}")
    hit_units = dragon.breathe_fire(x_target, y_target, units)
    hit_unit_names = [unit.name for unit in hit_units]
    print(f"Actual hit units: {hit_unit_names}")
    if set(hit_unit_names) == set(expected_hit_units):
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
