import kostem as ks
from utils import joinseq
from kostr import concat


"""Korean Words"""

# Korean Conjucation (strings can be used for Conjugation)
KC_D = "[되된돼됐]"
KC_H = "[하한합할해했]"

def conjugate(stems, *postfix):
    result = []
    for rt in stems.split('|'):
        args = [rt] + list(postfix)
        result.append(concat(*args))
    return result


# Korean Words

def monosyllables(psv):
    return '|'.join([s for s in psv.split('|') if len(s) == 1])

## Nouns - Status
KW_NSf = "가능|근면|깔끔|건강|곤란|동일|둔감|부지런|민감|병약|[불]?성실|부실|부족|[부]?적절"
KW_NSv = "부패|상이|수요|중대|중요|필요"
KW_NS = joinseq(KW_NSf, KW_NSv)


## Adjective - Status

### these are Already words as themselves(ie. '달아') and also can be conjugated further (ie. '달아요')
KW_ASA = '|'.join(sorted(
        conjugate(ks.KS_Aa, 'ㅏ')          # 나ㅃ+ㅏ(지다), 바ㅃ+ㅏ(지다), ...
        + conjugate(ks.KS_Ab, '워')        # 귀여+워(지다), ...
        + conjugate(ks.KS_Ac, '아')        # 맑+아(지다), ...
        + conjugate(ks.KS_Ad, 'ㄹ', '아')  # 다+ㄹ+아(지다)(be sweety), ...
        + conjugate(ks.KS_Ae, 'ㅓ')        # 예ㅃ+ㅓ(지다), ...
        + conjugate(ks.KS_Af, 'ㄹ', '라')  # 다+ㄹ+라(지다)(be differentiated), ...
        + conjugate(ks.KS_Ah, '해')        # 착+해(지다), ...
        + conjugate(ks.KS_Ai, '어')        # 붉+어(지다), ...
        + conjugate(ks.KS_Aj, '아')        # 낮+아(지다), ...
        + conjugate(ks.KS_Am, '어')        # 맛있+어(지다), ...
        + conjugate(ks.KS_An, 'ㄹ', '어')  # 머+ㄹ+어(지다), ...
        + conjugate(ks.KS_Ao, '어')        # 넓+어(지다), ...
        + conjugate(ks.KS_Ap, '어')        # 희+어(지다), ...
        + conjugate(ks.KS_Ar, '와')        # 이로+와(지다), ...
        + conjugate(ks.KS_As, '아')        # 나+아(지다), ...
        + conjugate(ks.KS_Aw, '와')        # 고+와(지다), ...
        + conjugate(ks.KS_Ay, 'ㅙ')        # 못ㄷ+ㅙ(지다), ...
        + conjugate(KW_NS, '해')        # 필요+해(지다), ...
    )
)

### ends with Lieul ('ㄹ')
KW_ASL = '|'.join(sorted(
        conjugate(ks.KS_Aa, 'ㅡ', 'ㄹ')          # 나ㅃ+ㅡ+ㄹ
        + conjugate(ks.KS_Ab, '울')              # 귀여+울
        + conjugate(ks.KS_Ac, '을')              # 맑+을
        + conjugate(ks.KS_Ad, 'ㄹ')              # 다+ㄹ(sweet)
        + conjugate(ks.KS_Ae, 'ㅡ', 'ㄹ')        # 예ㅃ+ㅡ+ㄹ
        + conjugate(ks.KS_Af, 'ㄹ', 'ㅡ', 'ㄹ')  # 다+ㄹ+ㅡ+ㄹ(different)
        + conjugate(ks.KS_Ah, '할')              # 착+할
        + conjugate(ks.KS_Ai, '을')              # 붉+을
        + conjugate(ks.KS_Aj, '을')              # 낮+을
        + conjugate(ks.KS_Am, '을')              # 맛있+을
        + conjugate(ks.KS_An, 'ㄹ')              # 머+ㄹ
        + conjugate(ks.KS_Ao, '을')              # 넓+을
        + conjugate(ks.KS_Ap, 'ㄹ')              # 희+ㄹ
        + conjugate(ks.KS_Ar, '울')              # 이로+울
        + conjugate(ks.KS_As, '을')              # 나+을
        + conjugate(ks.KS_Aw, '울')              # 고+울
        + conjugate(ks.KS_Ay, 'ㅚ', 'ㄹ')        # 못ㄷ+ㅚ+ㄹ
        + conjugate(KW_NS, '할')                 # 필요+할
    )
)

### ends with Nien ('ㄴ')
KW_ASN = '|'.join(sorted(
        conjugate(ks.KS_Aa, 'ㅡ', 'ㄴ')          # 나ㅃ+ㅡ+ㄴ
        + conjugate(ks.KS_Ab, '운')              # 귀여+운
        + conjugate(ks.KS_Ac, '은')              # 맑+은
        + conjugate(ks.KS_Ad, 'ㄴ')              # 다+ㄴ(sweet)
        + conjugate(ks.KS_Ae, 'ㅡ', 'ㄴ')        # 예ㅃ+ㅡ+ㄴ
        + conjugate(ks.KS_Af, 'ㄹ', 'ㅡ', 'ㄴ')  # 다+ㄹ+ㅡ+ㄴ(different)
        + conjugate(ks.KS_Ah, '한')              # 착+한
        + conjugate(ks.KS_Ai, '은')              # 붉+은
        + conjugate(ks.KS_Aj, '은')              # 낮+은
        + conjugate(ks.KS_Am, '는')              # 맛있+는
        + conjugate(ks.KS_An, 'ㄴ')              # 머+ㄴ
        + conjugate(ks.KS_Ao, '은')              # 넓+은
        + conjugate(ks.KS_Ap, 'ㄴ')              # 희+ㄴ
        + conjugate(ks.KS_Ar, '운')              # 이로+운
        + conjugate(ks.KS_As, '은')              # 나+은
        + conjugate(ks.KS_Aw, '운')              # 고+운
        + conjugate(ks.KS_Ay, 'ㅚ', 'ㄴ')        # 못ㄷ+ㅚ+ㄴ
        + conjugate(KW_NS, '한')                 # 필요+한
    )
)

KW_AS = joinseq(KW_ASA, KW_ASL, KW_ASN)
KW_A = joinseq(KW_AS)
KW_A1 = monosyllables(KW_A)

### Pre-nouns(관형사)
#### VT - No-tense
KW_PVTN = '|'.join(
    sorted(
        conjugate(ks.KS_VTg, '던')
        + conjugate(ks.KS_VTh, '던')
        + conjugate(ks.KS_VTi, '던')
        + conjugate(ks.KS_VTl, 'ㄹ', '던')
        + conjugate(ks.KS_VTm, 'ㄹ', '던')
        + conjugate(ks.KS_VTn, 'ㄹ', '던')
        + conjugate(ks.KS_VTy, 'ㅜ', '던')
    )
)

#### VT - Past
KW_PVTP = '|'.join(
    sorted(
        conjugate(ks.KS_VTg, '았던')
        + conjugate(ks.KS_VTh, '었던')
        + conjugate(ks.KS_VTi, '았던')
        + conjugate(ks.KS_VTl, 'ㄹ', '았던')
        + conjugate(ks.KS_VTm, 'ㄹ', '었던')
        + conjugate(ks.KS_VTn, 'ㄹ', '았던')
        + conjugate(ks.KS_VTy, 'ㅜ', '었던')
        + conjugate(ks.KS_VTy, 'ㅝ', 'ㅆ', '던')
    )
)

KW_PVT = joinseq(KW_PVTN, KW_PVTP)

#### Adjective - No tense
KW_PAN = '|'.join(
    sorted(
        conjugate(ks.KS_Aa, 'ㅡ', 'ㄴ')    # 나ㅃ+ㅡ+ㄴ
        + conjugate(ks.KS_Ab, '운')
        + conjugate(ks.KS_Ac, '은')
        + conjugate(ks.KS_Ad, 'ㄴ')
        + conjugate(ks.KS_Ae, 'ㅡ', 'ㄴ')
        + conjugate(ks.KS_Af, '른')
        + conjugate(ks.KS_Ah, '한')
        + conjugate(ks.KS_Ai, '은')
        + conjugate(ks.KS_Aj, '은')
        + conjugate(ks.KS_Al, '른')
        + conjugate(ks.KS_Am, '는')
        + conjugate(ks.KS_An, 'ㄴ')
        + conjugate(ks.KS_Ao, '은')
        + conjugate(ks.KS_Ap, 'ㄴ')
        + conjugate(ks.KS_Ar, '운')
        + conjugate(ks.KS_As, '은') 
        + conjugate(ks.KS_Aw, '운')
        + conjugate(ks.KS_Ay, 'ㅚ', 'ㄴ') 
        + conjugate(KW_NS, '한')
    )
)

#### Adjective - Past
KW_PAP = '|'.join(
    sorted(
        conjugate(ks.KS_Aa, 'ㅏ', 'ㅆ', '던')
        + conjugate(ks.KS_Ab, '웠던')
        + conjugate(ks.KS_Ac, '았던')
        + conjugate(ks.KS_Ad, 'ㄹ', '았던')
        + conjugate(ks.KS_Ae, 'ㅓ', 'ㅆ', '던')
        + conjugate(ks.KS_Af, 'ㄹ', '랐던')
        + conjugate(ks.KS_Ah, '했던')
        + conjugate(ks.KS_Ai, '었던')
        + conjugate(ks.KS_Aj, '았던')
        + conjugate(ks.KS_Al, 'ㄹ', '렀던')
        + conjugate(ks.KS_Am, '었던')
        + conjugate(ks.KS_An, 'ㄹ', '었던')
        + conjugate(ks.KS_Ao, '었던')
        + conjugate(ks.KS_Ap, '었던')
        + conjugate(ks.KS_Ar, '웠던')
        + conjugate(ks.KS_As, '았던') 
        + conjugate(ks.KS_Aw, '왔던')
        + conjugate(ks.KS_Ay, 'ㅚ', '었던') 
        + conjugate(ks.KS_Ay, 'ㅙ', 'ㅆ', '던') 
        + conjugate(KW_NS, '했던')
    )
)

KW_PA = joinseq(KW_PAN, KW_PAP)

## Busa(adverB)
### Cause(이유)
KW_BC = '|'.join(sorted(
        ['일부러']
        + conjugate(ks.KS_Aa, 'ㅏ', '서')
        + conjugate(ks.KS_Ab, '워서')
        + conjugate(ks.KS_Ac, '아서')
        + conjugate(ks.KS_Ad, 'ㄹ', '아서')
        + conjugate(ks.KS_Ae, 'ㅓ', '서')
        + conjugate(ks.KS_Af, 'ㄹ', '라서')
        + conjugate(ks.KS_Ah, '해서')
        + conjugate(ks.KS_Ai, '어서')
        + conjugate(ks.KS_Aj, '아서')
        + conjugate(ks.KS_Al, 'ㄹ', '러서')
        + conjugate(ks.KS_An, 'ㄹ', '어서')
        + conjugate(ks.KS_Ao, '어서')
        + conjugate(ks.KS_Ap, '어서')
        + conjugate(ks.KS_Ar, '와서')
        + conjugate(ks.KS_As, '아서')
        + conjugate(ks.KS_Aw, '와서')
        + conjugate(ks.KS_Ay, 'ㅙ', '서')
        ))

### Degree (정도)
KW_BD = '더|훨씬'

### Manner(태도, 방법)
KW_BM = '|'.join(
    sorted(
        ['함부로']
        + conjugate(ks.KS_Aa, 'ㅡ', '게')
        + conjugate(ks.KS_Ab, 'ㅂ', '게')
        + conjugate(ks.KS_Ac, '게')
        + conjugate(ks.KS_Ad, 'ㄹ', '게')
        + conjugate(ks.KS_Ae, 'ㅡ', '게')
        + conjugate(ks.KS_Af, '르게')
        + conjugate(ks.KS_Ah, '하게')
        + conjugate(ks.KS_Ai, '게')
        + conjugate(ks.KS_Aj, '게')
        + conjugate(ks.KS_Al, '르게')
        + conjugate(ks.KS_An, 'ㄹ', '게')
        + conjugate(ks.KS_Ao, '게')
        + conjugate(ks.KS_Ap, '게')
        + conjugate(ks.KS_Ar, 'ㅂ', '게')
        + conjugate(ks.KS_As, 'ㅅ', '게')
        + conjugate(ks.KS_Aw, 'ㅂ', '게')
        + conjugate(ks.KS_Ay, 'ㅚ', '게')
    )
)

### Negative 
KW_BN = '|'.join(
    sorted(
        conjugate(ks.KS_Ah, '하지')
        + conjugate(ks.KS_Aa, 'ㅡ', '지')
        + conjugate(ks.KS_Ab, 'ㅂ', '지')
        + conjugate(ks.KS_Ac, '지')
        + conjugate(ks.KS_Ad, 'ㄹ', '지')
        + conjugate(ks.KS_Ae, 'ㅡ', '지')
        + conjugate(ks.KS_Af, '르지')
        + conjugate(ks.KS_Ai, '지')
        + conjugate(ks.KS_Aj, '지')
        + conjugate(ks.KS_Al, '르지')
        + conjugate(ks.KS_An, 'ㄹ', '지')
        + conjugate(ks.KS_Ao, '지')
        + conjugate(ks.KS_Ap, '지')
        + conjugate(ks.KS_Ar, 'ㅂ', '지')
        + conjugate(ks.KS_As, 'ㅅ', '지')
        + conjugate(ks.KS_Aw, 'ㅂ', '지')
        + conjugate(ks.KS_Ay, 'ㅚ', '지')
    )
)
KW_B = joinseq(KW_BD, KW_BM, KW_BN)
KW_B1 = monosyllables(KW_B)

## Forein Words

KW_Ff = "(\\w*)(all|ell|earn|one)"  # f: has final consonant in Korean
KW_Fv = "(\\w*)(ice|ocks|old|uy)"  # v: ends with vowel (does not have final consonant) in Korean

## Nouns - Activity (can be verb with '-하다/-되다' or used in form of '~을/를 하다')
### Original (Korean + Hanja)
KW_NAOf = "생각|[가증]감|가공|곱|[건입]국|[연체]결|[총포]괄|가늠|[담배]당|가동|[노입출]력|[수제훈]련|[기수]록|[발변설연작제조증]명|주목|함몰|고민|[개선]발|체벌|[손향]상|개선|발생|[개배연증해]설|[구생작완형]성|[연학]습|[예해]약|오염|[반운투]영|[사이적통포활]용|훈육|[지]원|[도수]입|[수]?출입|시작|긴장|발전|[결설수측한]정|선언|선정|[도장부탈]착|제창|[도수연인창추]출|예측|[간선채]택|[면입]학|분할|포함|[결취]합|[구실재표]현|[동수실연진]행"
KW_NAOv = "[인증추참평]가|[제탈]거|[공소]개|[연촉]구|[상연제]기|이야기|시도|[고]려|[완치]료|[관수처]리|마무리|연마|소모|[공기]부|[반발조]사|[감축]소|[감준회]수|[기참]여|[긴소중필]요|[논유합]의|폐지|대체|[성]취|[납배설]치|저하|\\w+화|이해"
KW_NAO = joinseq(KW_NAOf, KW_NAOv)

## can be Both of active(-하다) and passive(-받다)
KW_NABf = "교육|주목|할당"
KW_NABv = "강요|오해"
KW_NAB = joinseq(KW_NABf, KW_NABv)

### derived from Foreign language
KW_NAFf = "게임|로그아웃|로그인|로깅|모니터링|로딩|인덱싱|샘플링|컴파일|클릭|튜닝|필터링"
KW_NAFv = "다운로드|릴리스|마사지|업로드|업데이트|테스트|트리거|팔로우|폴로|플레이"
KW_NAF = joinseq(KW_NAFf, KW_NAFv)

### all
KW_NAf = joinseq(KW_NAOf, KW_NAFf)
KW_NAv = joinseq(KW_NAOv, KW_NAFv)
KW_NA = joinseq(KW_NAf, KW_NAv)

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
KW_NNAf = "[0-9]*[0-9,.]*[136780]"
KW_NNAv = "[0-9]*[0-9,.]*[2459]"
KW_NNA = "[0-9]?[0-9,.]+"

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
KW_VACi = conjugate(KW_ASA, '지')  # idea (ex: 나빠+지(다))
KW_VACn = conjugate(KW_ASA, '진')  # progress (ex: 나빠+진(다))
KW_VACp = conjugate(KW_ASA, '졌')  # past (ex: 나빠+졌(다))

### Passive
KW_VPl = "갈리다"  # ends with '~리다(lida)'
KW_VPi = "쓰이다"  # ends with '~이다(ida)'

KW_VIn = '|'.join(
    sorted(
        conjugate(ks.KS_VIa, 'ㄴ', '다')
        + conjugate(ks.KS_VIe, 'ㄴ', '다')
        + conjugate(ks.KS_VIy, 'ㄴ', '다')
        + conjugate(ks.KS_VIl, 'ㄴ', '다')
        + conjugate(ks.KS_VIl, 'ㄴ', '다')
    )
)
