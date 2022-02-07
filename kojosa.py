from utils import joinseq

########################
# Korean Josa (particle)

## Additive
KJ_A = "도\\b"

## possesive ("oF")
KJ_F = "의\\b"

## Giving
KJ_G = "께|에게|한테"

## LinKing
KJ_K = "와\\b|과\\b|이랑|랑\\b|하고|고\\b"

## Location
KJ_L = "에\\b|에서|부터|으로|로\\b|에\\b|까지"

# Plural (More than one)
KJ_M = "들"

# Object
KJ_O = "을\\b|를\\b"

# Subject
KJ_S = "이\\b|가\\b"

# Topic marker
KJ_T = "은\\b|는\\b"

# Unique
KJ_U = "만"

# adVerb
KJ_V = "고|라고|보다|에게|에로|에서|와|으로서|으로써"

# Josa
KJ = joinseq(KJ_A, KJ_F, KJ_G, KJ_K, KJ_L, KJ_M, KJ_O, KJ_S, KJ_T, KJ_U, KJ_V)
