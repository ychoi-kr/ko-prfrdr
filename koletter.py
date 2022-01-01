import kosound as ks


""" Korean letters """

# Unicode decimal of the first korean letter ('가')
_FIRST_ = 44032

# ALL letters
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

# letters with final consonants which is singular
KL_WFS = ''.join(sorted(set(KL_WFC) - set(['들'])))

# letters with final lieul
KL_WFL = ''.join([chr(ord(c) + 8) for c in KL_NFC])

# letters with final consonants but lieul
KL_WFB = ''.join(sorted(set(KL_NFC) - set(KL_WFL)))

# letters without final consonants or with final lieul
KL_NFL = ''.join(sorted(KL_NFC + KL_WFL))


