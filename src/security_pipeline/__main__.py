"""Run the password-policy checker from the command line."""

from getpass import getpass

from security_pipeline.password_policy import assess_password


def main() -> int:
    """Prompt for a password and display policy feedback."""
    password = getpass("Введите пароль для локальной проверки: ")
    assessment = assess_password(password)

    print(f"Оценка политики: {assessment.score}/5")
    if assessment.is_acceptable:
        print("Пароль соответствует проверяемой политике.")
        return 0

    print("Пароль не соответствует проверяемой политике:")
    for message in assessment.feedback:
        print(f"- {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
