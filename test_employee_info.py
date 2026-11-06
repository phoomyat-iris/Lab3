import employee_info


def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(24, 33)
    names = [item["name"] for item in result]
    assert names == ["John", "Jane", "Mike"]


def test_get_employees_by_age_range_excludes_limits():
    # limits are exclusive: age 30 is not returned for range 30 to 35
    result = employee_info.get_employees_by_age_range(30, 35)
    names = [item["name"] for item in result]
    assert names == ["Mike"]


def test_get_employees_by_age_range_none():
    result = employee_info.get_employees_by_age_range(50, 60)
    assert result == []


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert result == 361000 / 6


def test_get_employees_by_dept_sales():
    result = employee_info.get_employees_by_dept("Sales")
    names = [item["name"] for item in result]
    assert names == ["John", "Peter"]


def test_get_employees_by_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")
    names = [item["name"] for item in result]
    assert names == ["Chloe", "Mike"]


def test_get_employees_by_dept_invalid():
    result = employee_info.get_employees_by_dept("HR")
    assert result == []