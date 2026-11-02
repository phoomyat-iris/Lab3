from Lab2 import lab2 as bmi


def test_bmi_under_weight():
    value, classification = bmi.calculate_bmi(1.75, 50)
    assert classification == -1


def test_bmi_normal_weight():
    value, classification = bmi.calculate_bmi(1.75, 70)
    assert classification == 0


def test_bmi_over_weight():
    value, classification = bmi.calculate_bmi(1.75, 90)
    assert classification == 1