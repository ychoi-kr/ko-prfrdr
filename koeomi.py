from utils import joinseq

#############
# Korean Eomi

## Finalize
KE_FE = "구나\\b|세\\b"  # exclamination
KE_FO = "라\\b|거라\\b"  # order
KE_FQ = "나\\b|니\\b|는가\\b"  # question
KE_FR = "자\\b|세\\b"  # request
KE_FS = "다\\b|습니다|이다"  # statement
KE_F = joinseq(KE_FE, KE_FO, KE_FQ, KE_FR, KE_FS)

## Conjunctive(연결)
KE_Ca = "게\\b|지\\b|어\\b"  # auxiliary
KE_Cc = "고\\b|으며\\b|며\\b"  # coordinate
KE_Cs = "[으]면|[으]므로"  # subordinate
KE_C = joinseq(KE_Ca, KE_Cc, KE_Cs)

## Derivational/Modifier(전성)
KE_Da = "은\\b|ㄴ\\b|을\\b|ㄹ\\b"  # adnominal
KE_Dn = "기\\b|음\\b|ㅁ\\b"  # noun
KE_Dv = "도록|게\\b"  # adVerbial
KE_D = joinseq(KE_Da, KE_Dn, KE_Dv)

## Ending(어말)
KE_E = joinseq(KE_F, KE_C, KE_D)

## Pre-final(선어말)
KE_P = "시|었|더|겠"
