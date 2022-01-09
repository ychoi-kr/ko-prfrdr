import kosound as ks


""" Korean letters """

# Unicode decimal of the first korean letter ('가')
_FIRST_ = 44032

# ALL letters ('가'-'힣')
KL_ALL = "".join(
    [
        chr(_FIRST_ + (len(ks.VOWELS) * (len(ks.FINAL_CONSONANTS) + 1) * i) + ((len(ks.FINAL_CONSONANTS) + 1) * j) +  k)
        for i in range(len(ks.FIRST_CONSONANTS))
        for j in range(len(ks.VOWELS))
        for k in range(len(ks.FINAL_CONSONANTS) + 1)
    ]
)

# letters without final consonants
KL_NFC = ''.join(
    [
        chr(_FIRST_ + (len(ks.VOWELS) * (len(ks.FINAL_CONSONANTS) + 1) * i) + ((len(ks.FINAL_CONSONANTS) + 1) * j))
        for i in range(len(ks.FIRST_CONSONANTS))
        for j in range(len(ks.VOWELS))
    ]
)

# letters with final consonants
KL_WFC = ''.join(sorted(set(KL_ALL) - set(KL_NFC)))

# letters with final consonants except '들'(letter that represents plural)
KL_WFS = ''.join(sorted(set(KL_WFC) - set(['들'])))

# letters with final lieul
KL_WFL = ''.join([chr(ord(c) + 8) for c in KL_NFC])

# letters with final nieun
KL_WFN = ''.join([chr(ord(c) + 4) for c in KL_NFC])

# letters without final lieul
KL_NFL = ''.join(sorted(set(KL_ALL) - set(KL_WFL)))

# letters without final nieun
KL_NFN = ''.join(sorted(set(KL_ALL) - set(KL_WFN)))

