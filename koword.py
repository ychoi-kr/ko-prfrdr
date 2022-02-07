from koroot import *
from kojosa import *
from koeomi import *
from utils import joinseq
from kostr import concat


def conjugate(roots, *postfix):
    result = []
    for rt in roots.split('|'):
        args = [rt] + list(postfix)
        result.append(concat(*args))
    return result


##############
# Korean Words

## Adjective - Status
KW_AS = '|'.join(sorted(
        conjugate(KR_Aa, 'ㅏ')          # 나ㅃ+ㅏ(지다), 바ㅃ+ㅏ(지다), ...
        + conjugate(KR_Ab, '워')        # 귀여+워(지다), ...
        + conjugate(KR_Ac, '아')        # 맑+아(지다), ...
        + conjugate(KR_Ad, 'ㄹ', '아')  # 다+ㄹ+아(지다)(be sweety), ...
        + conjugate(KR_Ae, 'ㅓ')        # 예ㅃ+ㅓ(지다), ...
        + conjugate(KR_Af, 'ㄹ', '라')  # 다+ㄹ+라(지다)(be differentiated), ...
        + conjugate(KR_Ah, '해')        # 착+해(지다), ...
        + conjugate(KR_Ai, '어')        # 붉+어(지다), ...
        + conjugate(KR_Aj, '아')        # 낮+아(지다), ...
        + conjugate(KR_Am, '어')        # 맛있+어(지다), ...
        + conjugate(KR_An, 'ㄹ', '어')  # 머+ㄹ+어(지다), ...
        + conjugate(KR_Ao, '어')        # 넓+어(지다), ...
        + conjugate(KR_Ap, '어')        # 희+어(지다), ...
        + conjugate(KR_Ar, '와')        # 이로+와(지다), ...
        + conjugate(KR_As, '아')        # 나+아(지다), ...
        + conjugate(KR_Aw, '와')        # 고+와(지다), ...
        + conjugate(KR_Ax, 'ㅓ')        # ㅋ+ㅓ+(지다), ...
        + conjugate(KR_Ay, 'ㅙ')        # 못ㄷ+ㅙ+(지다), ...
        ))


## Adjective - Status - modifies Noun (형용사의 관형사형)
KW_ASN = '|'.join(
    sorted(
        conjugate(KR_Aa, 'ㅡ', 'ㄴ')    # 나ㅃ+ㅡ+ㄴ
        + conjugate(KR_Ab, '운')
        + conjugate(KR_Ac, '은')
        + conjugate(KR_Ad, 'ㄴ')
        + conjugate(KR_Ae, 'ㅡ', 'ㄴ')
        + conjugate(KR_Af, '른')
        + conjugate(KR_Ah, '한')
        + conjugate(KR_Ai, '은')
        + conjugate(KR_Aj, '은')
        + conjugate(KR_Al, '른')
        + conjugate(KR_Am, '는')
        + conjugate(KR_An, 'ㄴ')
        + conjugate(KR_Ao, '은')
        + conjugate(KR_Ap, 'ㄴ')
        + conjugate(KR_Ar, '운')
        + conjugate(KR_As, '은') 
        + conjugate(KR_Aw, '운')
        + conjugate(KR_Ax, 'ㅡ', 'ㄴ')
        + conjugate(KR_Ay, 'ㅚ', 'ㄴ') 
    )
)

## AdVerb - Cause (이유를 나타내는 부사)
KW_AVC = '|'.join(sorted(
        ['일부러']
        + conjugate(KR_Aa, 'ㅏ', '서')
        + conjugate(KR_Ab, '워서')
        + conjugate(KR_Ac, '아서')
        + conjugate(KR_Ad, 'ㄹ', '아서')
        + conjugate(KR_Ae, 'ㅓ', '서')
        + conjugate(KR_Af, 'ㄹ', '라서')
        + conjugate(KR_Ah, '해서')
        + conjugate(KR_Ai, '어서')
        + conjugate(KR_Aj, '아서')
        + conjugate(KR_Al, 'ㄹ', '러서')
        + conjugate(KR_An, 'ㄹ', '어서')
        + conjugate(KR_Ao, '어서')
        + conjugate(KR_Ap, '어서')
        + conjugate(KR_Ar, '와서')
        + conjugate(KR_As, '아서')
        + conjugate(KR_Aw, '와서')
        + conjugate(KR_Ax, 'ㅓ', '서')
        + conjugate(KR_Ay, 'ㅙ', '서')
        ))

## Adverb - Manner (태도, 방법을 나타내는 부사)
KW_AVM = '|'.join(
    sorted(
        ['함부로']
        + conjugate(KR_Aa, 'ㅡ', '게')
        + conjugate(KR_Ab, 'ㅂ', '게')
        + conjugate(KR_Ac, '게')
        + conjugate(KR_Ad, 'ㄹ', '게')
        + conjugate(KR_Ae, 'ㅡ', '게')
        + conjugate(KR_Af, '르게')
        + conjugate(KR_Ah, '하게')
        + conjugate(KR_Ai, '게')
        + conjugate(KR_Aj, '게')
        + conjugate(KR_Al, '르게')
        + conjugate(KR_An, 'ㄹ', '게')
        + conjugate(KR_Ao, '게')
        + conjugate(KR_Ap, '게')
        + conjugate(KR_Ar, 'ㅂ', '게')
        + conjugate(KR_As, 'ㅅ', '게')
        + conjugate(KR_Aw, 'ㅂ', '게')
        + conjugate(KR_Ax, 'ㅡ', '게')
        + conjugate(KR_Ay, 'ㅚ', '게')
    )
)

## Adverb - Negative 
KW_AVN = '|'.join(
    sorted(
        conjugate(KR_Ah, '하지')
        + conjugate(KR_Aa, 'ㅡ', '지')
        + conjugate(KR_Ab, 'ㅂ', '지')
        + conjugate(KR_Ac, '지')
        + conjugate(KR_Ad, 'ㄹ', '지')
        + conjugate(KR_Ae, 'ㅡ', '지')
        + conjugate(KR_Af, '르지')
        + conjugate(KR_Ai, '지')
        + conjugate(KR_Aj, '지')
        + conjugate(KR_Al, '르지')
        + conjugate(KR_An, 'ㄹ', '지')
        + conjugate(KR_Ao, '지')
        + conjugate(KR_Ap, '지')
        + conjugate(KR_Ar, 'ㅂ', '지')
        + conjugate(KR_As, 'ㅅ', '지')
        + conjugate(KR_Aw, 'ㅂ', '지')
        + conjugate(KR_Ax, 'ㅡ', '지')
        + conjugate(KR_Ay, 'ㅚ', '지')
    )
)
KW_AV = joinseq(KW_AVC, KW_AVM, KW_AVN)

## Forein Words

KW_Ff = "(\\w*)(ice|ocks|old|uy)"  # f: has final consonant in Korean
KW_Fv = "(\\w*)(all|ell)"  # v: ends with vowel (does not have final consonant) in Korean

## Nouns - Activity (can be verb with '-하다/-되다' or used in form of '~을/를 하다')
### Original Korean
KW_NAOf = "생각|[가증]감|가공|곱|[건입]국|[연체]결|[총포]괄|가늠|[담배]당|가동|[노입출]력|[수제훈]련|[기수]록|[발변설연작제조증]명|함몰|고민|[개선]발|체벌|[손향]상|[개배연증해]설|[구생작완형]성|[연학]습|[예해]약|오염|[반운투]영|[사이적통포활]용|[교훈]육|[지]원|[도수]입|[수]?출입|시작|긴장|발전|[결설수측한]정|선언|선정|[도장부탈]착|제창|[수연인창]출|예측|[간선채]택|[동수실연]행|[면입]학|포함|[결취]합|[구실재표]현"
KW_NAOv = "[인추참평]가|[제탈]거|[공소]개|[연촉]구|[상연제]기|이야기|시도|[고]려|치료|[관수처]리|연마|[공기]부|[반발조]사|[감축]소|[감준회]수|[기참]여|[긴소중필]요|[논합]의|폐지|대체|[성]취|[납배설]치|\\w+화|이해"
KW_NAO = joinseq(KW_NAOf, KW_NAOv)

### derived from Foreign language
KW_NAFf = "게임|다운로딩|로그아웃|로그인|로깅|모니터링|[업]?로딩|인덱싱|컴파일|필터링"
KW_NAFv = "다운로드|릴리스|마사지|[업]?로드|업데이트|트리거|플레이"
KW_NAF = joinseq(KW_NAFf, KW_NAFv)

### all
KW_NAf = joinseq(KW_NAOf, KW_NAFf)
KW_NAv = joinseq(KW_NAOv, KW_NAFv)
KW_NA = joinseq(KW_NAf, KW_NAv)

## Nouns - STatus (can be adjective with '-하다')
KW_NSf = "가능|깔끔|건강|곤란|동일|둔감|부지런|민감|병약|[불]?성실|[부]?적절"
KW_NSv = "상이"
KW_NS = joinseq(KW_NSf, KW_NSv)

## Nouns (Activity + Status)
#KW_NASf = joinseq(KW_NAf, KW_NSTf)
#KW_NASv = joinseq(KW_NAv, KW_NSTv)
#KW_NAS = joinseq(KW_NASf, KW_NASv)

## Nouns - Dependant
KW_ND = "밖|뿐"


## Nouns - Person
### by Existance
KW_NPEf = "사람|인[간물]"
KW_NPEv = "인류"

### by biological or phisical conditioN
KW_NPNf = "[비]?장애인|어른"
KW_NPNv = "감염자|[고남여병환]자|[동양이]성애자|바보|아기"

### by Job title or membership
KW_NPJf = "감독[관]?[님]?|강사님|과장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|사원|[사소의회]장[님]?|시인|작[곡사]?가님|직장인|학생|[수해]병|초대 회장|회사원"
KW_NPJv = "강사|교[사수]|대[리표]|작[곡사]?가"
KW_NPJ = joinseq(KW_NPJf, KW_NPJv)

### by ranK
NW_NPKf = "[경병부차]장[님]?|[상이일]병|[대중소준][령장]|사령관|통수권자"
NW_NPKv = "경[사위]|[대중소준][위좌]|[상중하]사"

### by social Relation
KW_NPRf = "아들|동문|조상|자손|식솔|[처]?자식|[부장]인|동창|[일사삼오육칠팔]촌|남편"
KW_NPRv = "[식친]구|처남|자녀|아내|아주머니|[어할]머니|아줌마|엄마|[고대부이]모|동료|며느리|[대형]부|아빠|[제형]수|아저씨|애인|사위|저|[자처형]제|[할]아버지|제부|처형"

### by Activity
KW_NPAf = "군인|경찰|동호인|애[견묘]인|[증행]인"
KW_NPAv = "감독자|감시자|강[연의]자|관[계련찰]자|글쓴이|당[사직]자|반[려역]자|발[제표]자|수집가|아마추어|엮은이|애호가|응시자|[원]작자|지은이|팬|프로|협력자"

### all
KW_NPf = joinseq(KW_NPEf, KW_NPNf, KW_NPJf, KW_NPRf, KW_NPAf)
KW_NPv = joinseq(KW_NPEv, KW_NPNv, KW_NPJv, KW_NPRv, KW_NPAv)
KW_NP = joinseq(KW_NPf, KW_NPv)


## Nouns - Number
### derived from Chinese
#KW_NNCf = "일|삼|육|칠|팔"
#KW_NNCv = "이|사|오|구"
#KW_NNC = joinseq(KW_NNCf, KW_NNCv)
KW_NNC = "[일이삼사오육칠팔구십백천만]*[일이삼사오육칠팔구십백천만억조경]"

### positional value in Decimal system
KW_NNDf = "십|백|천|만|억|경"
KW_NNDv = "조"
KW_NND = joinseq(KW_NNDf, KW_NNDv)

### Arabic
KW_NNA = "[1-9]?[0-9,]*"

### Mixed
KW_NNMf = KW_NNA + KW_NNDf
KW_NNMv = KW_NNA + KW_NNDv
KW_NNM = joinseq(KW_NNMf, KW_NNMv)

### pure Korean
KW_NNK = "[열스서마쉰예일여아백]?[한두세네섯댓곱덟홉]"

### all
KW_NN = joinseq(KW_NNC, KW_NND, KW_NNK)   


## Nouns - Unit
### Currency
KW_NUCf = "루블|엔|원|위안"
KW_NUCv = "달러|리라|유로|페소"
KW_NUC = joinseq(KW_NUCf, KW_NUCv)

### Distance
KW_NUDf = "광년"
KW_NUDv = "미터|리|킬로미터"
KW_NUD = joinseq(KW_NUDf, KW_NUDv)

### weiGht in symbol
KW_NUGf = "[mk]?g" 
KW_NUGv = "[k]?[LlMm]"
KW_NUG = joinseq(KW_NUGf, KW_NUGv)

### Multiplication
KW_NUM = "배"

### aRea
KW_NURf = "평"
KW_NURv = "제곱미터|평방미터"
KW_NUR = joinseq(KW_NURf, KW_NURv)

### Stuff 
KW_NUSf = "그릇|달|명|방울|벌|쪽"
KW_NUSv = "가지|개|마리|박스|봉지|채|페이지|회"
KW_NUSd = "대" # should be handled carefully: '세 대(three device)' vs '3세대(third generation)' 
KW_NUS = joinseq(
    KW_NUSf, KW_NUSv#, KW_NUSd
)

### Time
KW_NUTf = "분|시간|일|달|개월|년"
KW_NUTv = "밀리초|세기|세대|초"
KW_NUT = joinseq(KW_NUTf, KW_NUTv)

### Volume
KW_NUVf = ""
KW_NUVv = "세제곱미터"
KW_NUV = joinseq(KW_NUVf, KW_NUVv)

### Weight
KW_NUWf = "그램|킬로그램|평"
KW_NUWv = "밀리리터|데시리터|리터|킬로리터|파운드"
KW_NUW = joinseq(KW_NUWf, KW_NUWv)

### all
KW_NU = joinseq(KW_NUD, KW_NUG, KW_NUM, KW_NUR, KW_NUS, KW_NUT, KW_NUV, KW_NUW)


## Nouns - animaL
### Domestic
KW_NLDf = "말" 
KW_NLDv = "개|고양이|돼지|소|오리" 
KW_NLD = joinseq(KW_NLDf, KW_NLDv)

### Insects
KW_NLIf = "개미|딱정벌레|지네"
KW_NLIv = "[꿀]벌|[여]왕벌"
KW_NLI = joinseq(KW_NLIf, KW_NLIv)


## Pronouns
### Person
KW_PP = "너희|내|우리|저희"
### all
KW_P = joinseq(KW_PP)

## Verb
### from Adjective
### Change of status
KW_VACi = conjugate(KW_AS, '지')  # idea (ex: 나빠+지(다))
KW_VACn = conjugate(KW_AS, '진')  # progress (ex: 나빠+진(다))
KW_VACp = conjugate(KW_AS, '졌')  # past (ex: 나빠+졌(다))

### Passive
KW_VPl = "갈리다"  # ends with '~리다(lida)'
KW_VPi = "쓰이다"  # ends with '~이다(ida)'

