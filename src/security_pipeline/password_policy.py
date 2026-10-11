"""Basic password-policy checks for the command-line demo."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PasswordAssessment:
    """Result of checking a password without retaining its value."""

    is_acceptable: bool
    score: int
    feedback: tuple[str, ...]


def assess_password(password: str) -> PasswordAssessment:
    """Check a password against a small, transparent set of requirements."""
    checks = (
        (len(password) >= 12, "Используйте не менее 12 символов."),
        (any(character.islower() for character in password), "Добавьте строчную букву."),
        (any(character.isupper() for character in password), "Добавьте заглавную букву."),
        (any(character.isdigit() for character in password), "Добавьте цифру."),
        (
            any(not character.isalnum() and not character.isspace() for character in password),
            "Добавьте специальный символ.",
        ),
    )
    feedback = tuple(message for passed, message in checks if not passed)

    return PasswordAssessment(
        is_acceptable=not feedback,
        score=len(checks) - len(feedback),
        feedback=feedback,
    )
