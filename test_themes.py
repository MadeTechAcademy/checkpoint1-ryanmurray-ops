from themes import duties

def test_duties_length():
    assert len(duties) == 13 # Validate all duties are present

def test_duties_numbering():
    for duty_number, duty_text in enumerate(duties, start=1):
        assert f"Duty {duty_number}" in duty_text

    