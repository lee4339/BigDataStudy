def is_palindrome(test_string):
    # 1. 알파벳 단위 리스트로 쪼개기
    s1 = list(test_string)

    # 2. 리스트 순서 reverse --> method 참조.
    s1.reverse()

    # 3. 뒤집은 리스트를 문자열로 합치기
    s1_str = ''.join(s1)
    
    # 4. 합친 문자열이 str1과 같으면 ....palindrome.
    if test_string == s1_str :
        return True
    else :
        return False