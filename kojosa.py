from utils import joinseq

########################
# Korean Josa (postposition or particle)

## Case(격 조사)

### As
KJ_CA = "으로서"

### Compare
KJ_CC = "보다\\b"

### possesive ("oF")
KJ_CF = "의\\b"

### Giving
KJ_CG = "께|에게|한테"

### LinKing
KJ_CK = "와\\b|과\\b|이랑|랑\\b|하고|고\\b"

### location
KJ_CL = "에\\b|에게\\b|에서"

### Made of
KJ_CM = "로\\b|으로\\b|으로써"

### Object
KJ_CO = "을\\b|를\\b"

### Quote
KJ_CQ = "라고|고\\b"

### Subject
KJ_CS = "이\\b|가\\b"

### toward
KJ_CT = "로\\b|에로\\b|으로\\b"

KJ_C = joinseq(KJ_CA, KJ_CC, KJ_CF, KJ_CG, KJ_CK, KJ_CL, KJ_CM, KJ_CO, KJ_CQ, KJ_CS, KJ_CT)

## Information(보조사)

### Additive
KJ_IA = "도\\b"

### Contrast
KJ_IC = "은\\b|는\\b"

### Plural (More than one)
KJ_IM = "들"

### Range
KJ_IR = "부터|까지"

### Unique
KJ_IU = "만"

KJ_I = joinseq(KJ_IA, KJ_IC, KJ_IM, KJ_IR, KJ_IU)

KJ = joinseq(KJ_C, KJ_I)

