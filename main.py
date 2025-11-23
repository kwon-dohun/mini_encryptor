from mini_encryptor import caesar_encrypt, caesar_decrypt


def get_shift_value():
    """shift 값을 정수로 안전하게 입력받기"""
    while True:
        value = input("이동 거리(shift)를 입력하세요: ")
        if value.isdigit():
            return int(value)
        print("숫자를 입력하세요!")


def main():
    print("=== mini_encryptor ===")
    print("※ 이 프로그램은 영어 알파벳(A–Z, a–z)과 숫자(0–9)만 암호화됩니다.\n")

    # 1. 사용자 문자열 입력
    original_text = input("암호화/복호화할 문자열을 입력하세요: ")

    # 2. shift 입력
    shift = get_shift_value()

    # 3. 비밀번호 설정
    password = input("설정할 비밀번호를 입력하세요: ")

    # 4. 원본 문자열을 암호화하여 내부 보관
    encrypted_text = caesar_encrypt(original_text, shift)
    print("\n입력하신 데이터가 암호화되었습니다.")


    print("\n--- 비밀번호 검증 단계 ---")
    print("비밀번호를 맞게 입력하면 → 기존 데이터를 볼 수 있습니다.")
    print("비밀번호가 틀리면 → 암호화된 데이터를 보여줍니다.")
    print("프로그램 종료: end 입력\n")

    # 5. 비밀번호 검증 반복
    while True:
        entered_pw = input("비밀번호를 입력하세요: ")

        if entered_pw.lower() == "end":
            print("프로그램을 종료합니다.")
            return

        if entered_pw == password:
            decrypted_text = caesar_decrypt(encrypted_text, shift)
            print("\n🔓 비밀번호가 맞습니다.")
            print(f"기존 데이터 : {decrypted_text}\n")
            break

        else:
            print("\n🔐 비밀번호가 틀렸습니다. 다시 시도하세요.")
            print(f"암호화된 결과 : {encrypted_text}\n")


if __name__ == "__main__":
    main()
