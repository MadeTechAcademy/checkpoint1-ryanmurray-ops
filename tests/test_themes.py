from themes import duties, list_duties, Theme

def test_duties_length():
    assert len(duties) == 13 # Validate all duties are present

def test_duties_numbering():
    for duty_number, duty_text in enumerate(duties, start=1):
        assert f"Duty {duty_number}" in duty_text

def test_list_duties_output():
    # list_duties() should return a string containing all duties
    output = list_duties()
    assert isinstance(output, str)
    for duty in duties:
        assert duty in output

def test_list_duties_line_breaks():
    output = list_duties()
    assert output.count("\n") == len(duties) - 1

def test_no_empty_duties():
    for duty in duties:
        assert duty.strip() != ""


# --------------------------
# Tests for the Theme class
# --------------------------

def test_theme_has_correct_name_and_numbers():
    bootcamp = Theme("Bootcamp", [1, 2, 3, 4, 13], duties)
    assert bootcamp.name == "Bootcamp"
    assert bootcamp.duty_numbers == [1, 2, 3, 4, 13]