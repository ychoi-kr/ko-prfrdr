from utils import joinseq

########################
# Korean Josa (postposition or particle)

## Case(격 조사)

### As
KJ_CA = "으로서"

### compare('Boda')
KJ_CB = "보다"

### metaphor('Cheorum')
KJ_CC = "처럼"

### possesive ("oF")
KJ_CF = "의"

### Giving
KJ_CG = "께|에게|한테"

## predicative('Ida')
KJ_CI = "이다|이어야|이었[다던]|인가[는도를에]?|일"

### linKing
KJ_CK = "와|과|이[고면]|이랑|랑|하고|고"

### Location
KJ_CL = "게|에|에게|에서"

### Made of
KJ_CM = "로|으로|으로써"

### Object
KJ_CO = "을|를"

### Quote
KJ_CQ = "라고|고"

### Subject
KJ_CS = "이|가"

### toward
KJ_CT = "로|에로|으로"

KJ_C = joinseq(KJ_CA, KJ_CB, KJ_CC, KJ_CF, KJ_CG, KJ_CI, KJ_CK, KJ_CL, KJ_CM, KJ_CO, KJ_CQ, KJ_CS, KJ_CT)

## Information(보조사)

### Additive
KJ_IA = "도"

### Contrast
KJ_IC = "은|는"

### Discussion
KJ_ID = "이란|란"

### Each
KJ_IE = "마다"

### Plural
KJ_IM = "들"

### not the preferred Option
KJ_IO = "라도|이라도"

### Polite
KJ_IP = "요"

### Range
KJ_IR = "부터|까지"

### Unique
KJ_IU = "만"


KJ_I = joinseq(KJ_IA, KJ_IC, KJ_ID, KJ_IE, KJ_IM, KJ_IO, KJ_IP, KJ_IR, KJ_IU)

KJ = joinseq(KJ_C, KJ_I)

