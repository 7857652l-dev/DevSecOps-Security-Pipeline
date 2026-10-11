"""Tests for password-policy assessment."""

from security_pipeline import __main__ as cli
from security_pipeline.password_policy import assess_password

TEST_PASSWORD = "TEST-ONLY-Example9!"


def test_accepts_password_that_meets_all_requirements() -> None:
    assessment = assess_password(TEST_PASSWORD)

    assert assessment.is_acceptable
    assert assessment.score == 5
    assert assessment.feedback == ()


def test_reports_each_missing_requirement() -> None:
    assessment = assess_password("short")

    assert not assessment.is_acceptable
    assert assessment.score == 1
    assert assessment.feedback == (
        "Используйте не менее 12 символов.",
        "Добавьте заглавную букву.",
        "Добавьте цифру.",
        "Добавьте специальный символ.",
    )


def test_whitespace_does_not_count_as_a_special_character() -> None:
    assessment = assess_password("Long enough 123aA")

    assert "Добавьте специальный символ." in assessment.feedback


def test_empty_password_fails_all_requirements() -> None:
    assessment = assess_password("")

    assert not assessment.is_acceptable
    assert assessment.score == 0
    assert len(assessment.feedback) == 5


def test_cli_does_not_print_the_password(monkeypatch, capsys) -> None:
    monkeypatch.setattr(cli, "getpass", lambda _: TEST_PASSWORD)

    assert cli.main() == 0
    assert TEST_PASSWORD not in capsys.readouterr().out


def test_cli_returns_failure_for_password_that_does_not_meet_policy(
    monkeypatch, capsys
) -> None:
    monkeypatch.setattr(cli, "getpass", lambda _: "weak")

    assert cli.main() == 1
    assert "не соответствует" in capsys.readouterr().out
