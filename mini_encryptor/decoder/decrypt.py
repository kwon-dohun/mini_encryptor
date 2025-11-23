from mini_encryptor.encoder.encrypt import _shift_char


def caesar_decrypt(text: str, shift: int = 1) -> str:
    """
    Caesar 암호로 암호화된 문자열을 복호화.
    - encrypt에서 사용한 shift 값과 같은 값을 사용해야 원래 문자열 복원.
    """
    # -shift로 다시 되돌림
    return "".join(_shift_char(ch, -shift) for ch in text)
