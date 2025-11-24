from themes import duties, list_duties

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
    assert output.count("\n") == len(duties) -1
    