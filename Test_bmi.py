from Lab2 import lab2


def test_calculate_bmi_underweight():
    bmi, classification = lab2.calculate_bmi(1.75, 50)
    assert classification == -1


def test_calculate_bmi_normal():
    bmi, classification = lab2.calculate_bmi(1.75, 70)
    assert classification == 0


def test_calculate_bmi_overweight():
    bmi, classification = lab2.calculate_bmi(1.75, 90)
    assert classification == 1


def test_calculate_bmi_value():
    bmi, classification = lab2.calculate_bmi(2.0, 80)
    assert bmi == 20.0