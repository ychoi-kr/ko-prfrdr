from utils import joinseq

#############
# Korean Eomi

## Ending(어말 어미)

### Conjunctive(연결)
KE_ECa = "게\\b|지\\b|어\\b"  # Help auxiliary(보조)
KE_ECc = "고\\b|으며\\b|며\\b|지마는|지만"  # coordinate(대등) 
KE_ECs = "리만치\\b|어야|[으]면|[으]므로"  # subordinate(종속)
KE_EC = joinseq(KE_ECa, KE_ECc, KE_ECs)

### Derivational/Modifier(전성)
KE_EDa = "은\\b|ㄴ\\b|을\\b|ㄹ\\b"  # adnominal
KE_EDn = "기\\b|음\\b|ㅁ\\b"  # noun
KE_EDv = "도록|게\\b"  # adVerbial
KE_ED = joinseq(KE_EDa, KE_EDn, KE_EDv)

### Finalize(종결)
KE_EFE = "구나\\b|세\\b"  # exclamination
KE_EFO = "라\\b|거라\\b"  # order
KE_EFQ = "나\\b|니\\b|는가\\b"  # question
KE_EFR = "자\\b|세\\b"  # request
KE_EFS = "다\\b|습니다|야|이다"  # statement
KE_EF = joinseq(KE_EFE, KE_EFO, KE_EFQ, KE_EFR, KE_EFS)

KE_E = joinseq(KE_EC, KE_ED, KE_EF)


## Pre-final(선어말)
KE_P = "시|었|더|겠"

KE = joinseq(KE_E, KE_P)
