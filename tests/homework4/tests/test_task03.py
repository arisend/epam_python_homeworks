import sys
import io

from homework_04.hw.task_3_get_print_output import my_precious_logger


def test_positive_case():
    """Testing info case"""
    old_stdout = sys.stdout  # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()
    my_precious_logger("OK")
    what_was_printed = buffer.getvalue()
    assert "OK" in what_was_printed
    sys.stdout = old_stdout  # Put the old stream back in place
    buffer.close()


def test_negative_case():
    """Testing error case"""
    old_stderr = sys.stderr  # Memorize the default stdout stream
    sys.stderr = buffer = io.StringIO()
    my_precious_logger("error: file not found")
    what_was_printed = buffer.getvalue()
    assert "error: file not found" in what_was_printed
    sys.stdout = old_stderr  # Put the old stream back in place
    buffer.close()
