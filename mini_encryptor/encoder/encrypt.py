def _shift_char(ch: str, shift: int) -> str:
    """단일 문자 하나를 shift만큼 이동 (알파벳/숫자만 순환)."""
    if "a" <= ch <= "z":
        base = ord("a")
        return chr((ord(ch) - base + shift) % 26 + base)
    if "A" <= ch <= "Z":
        base = ord("A")
        return chr((ord(ch) - base + shift) % 26 + base)
    if "0" <= ch <= "9":
        base = ord("0")
        return chr((ord(ch) - base + shift) % 10 + base)
    # 알파벳 / 숫자가 아니면 그대로 반환
    return ch


def caesar_encrypt(text: str, shift: int = 1) -> str:
    """
    아주 단순한 Caesar 암호화 함수.
    - 알파벳/숫자만 shift만큼 앞으로 이동
    - 기본 shift 값은 1
    """
    return "".join(_shift_char(ch, shift) for ch in text)
