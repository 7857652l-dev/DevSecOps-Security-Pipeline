
import hashlib
import subprocess
import pickle


def weak_hash(password: str) -> str:
    # Намеренно слабый алгоритм для демонстрации Bandit
    return hashlib.md5(password.encode()).hexdigest()


def run_command(user_input: str) -> None:
    # Намеренно небезопасно: ввод попадает в shell-команду
    subprocess.call("echo " + user_input, shell=True)


def load_data(data: bytes):
    # Намеренно небезопасно: pickle может выполнять код при загрузке
    import io
    return pickle.load(io.BytesIO(data))


if __name__ == "__main__":
    print("MD5 demo:", weak_hash("demo-password"))
    print("Security demo loaded.")
