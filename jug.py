def water_jug_problem(jug1, jug2, target):
    steps = []
    jug1_current, jug2_current = 0, 0

    while jug1_current != target and jug2_current != target:
        if jug1_current == 0: jug1_current = jug1; steps.append(f"Fill Jug 1: Jug1={jug1_current}, Jug2={jug2_current}")
        elif jug2_current == jug2: jug2_current = 0; steps.append(f"Empty Jug 2: Jug1={jug1_current}, Jug2={jug2_current}")
        else: pour = min(jug1_current, jug2 - jug2_current); jug1_current -= pour; jug2_current += pour; steps.append(f"Pour from Jug 1 to Jug 2: Jug1={jug1_current}, Jug2={jug2_current}")
    return steps
# Test
for step in water_jug_problem(5, 3, 4): print(step)

