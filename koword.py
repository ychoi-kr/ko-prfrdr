import kostem as ks
from utils import joinseq
from kostr import concat


"""Korean Words"""

# Korean Conjucation (strings can be used for Conjugation)
KC_D = "[되된돼됐]"
KC_H = "하[고니며지]|한[다]?|함[을]?|함이다|함입니다|합니다|할[지]?[도]?|해[서요]?|했고[요]?|했는데[요]?|했다[만]?|했습니다[만]?|했으[니면][서]?|했지[만]?[요]?"

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
KW_NSf = "둔감|건강|간결|깔끔|가능|근면|곤란|[장졸]렬|동일|민감|병약|[단온지]순|참신|[불]?성실|부실|복잡|부족|[부]?적절|공평"
KW_NSv = "[자섬]세|상이|수요|[장중]대|진부|[긴중필]요|부패"
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
        + conjugate(ks.KS_Ag, '해')        # 착+해(지다), ...
        + conjugate(ks.KS_Ah, '해')        # 깔끔+해(지다), ...
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
        + conjugate(ks.KS_Ag, '할')              # 착+할
        + conjugate(ks.KS_Ah, '할')              # 깔끔+할
        + conjugate(ks.KS_Ai, '을')              # 붉+을
        + conjugate(ks.KS_Aj, '을')              # 낮+을
        + conjugate(ks.KS_Al, '를')              # 맛있+을
        + conjugate(ks.KS_Am, '을')              # 맛있+을
        + conjugate(ks.KS_An, 'ㄹ')              # 머+ㄹ
        + conjugate(ks.KS_Ao, '을')              # 넓+을
        + conjugate(ks.KS_Ap, 'ㄹ')              # 희+ㄹ
        + conjugate(ks.KS_Ar, '울')              # 이로+울
        + conjugate(ks.KS_As, '을')              # 나+을
        + conjugate(ks.KS_Aw, '울')              # 고+울
        + conjugate(ks.KS_Ay, 'ㅚ', 'ㄹ')        # 못ㄷ+ㅚ+ㄹ
        + conjugate(ks.KS_VTk, '를')             # 모+를
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
        + conjugate(ks.KS_Ag, '한')              # 착+한
        + conjugate(ks.KS_Ah, '한')              # 깔끔+한
        + conjugate(ks.KS_Ai, '은')              # 붉+은
        + conjugate(ks.KS_Aj, '은')              # 낮+은
        + conjugate(ks.KS_Al, '는')              # 섣부+른 
        + conjugate(ks.KS_Am, '는')              # 맛있+는
        + conjugate(ks.KS_An, 'ㄴ')              # 머+ㄴ
        + conjugate(ks.KS_Ao, '은')              # 넓+은
        + conjugate(ks.KS_Ap, 'ㄴ')              # 희+ㄴ
        + conjugate(ks.KS_Ar, '운')              # 이로+운
        + conjugate(ks.KS_As, '은')              # 나+은
        + conjugate(ks.KS_Aw, '운')              # 고+운
        + conjugate(ks.KS_Ay, 'ㅚ', 'ㄴ')        # 못ㄷ+ㅚ+ㄴ
        + conjugate(ks.KS_VTk, '는')             # 모+르는
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
        + conjugate(ks.KS_Ag, '한')
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
        + conjugate(ks.KS_VTk, '르는')
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
        + conjugate(ks.KS_Ag, '했던')
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
        + conjugate(ks.KS_VTk, 'ㄹ', '랐던')
        + conjugate(KW_NS, '했던')
    )
)

KW_PA = joinseq(KW_PAN, KW_PAP)

## Nouns - Idea
KW_NIf = "확률"
KW_NIn = "차원"
KW_NIv = "수치"
KW_NI = joinseq(KW_NIf, KW_NIn, KW_NIv)

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
        + conjugate(ks.KS_Ag, '해서')
        + conjugate(ks.KS_Ah, '해서')
        + conjugate(ks.KS_Ai, '어서')
        + conjugate(ks.KS_Aj, '아서')
        + conjugate(ks.KS_Al, 'ㄹ', '러서')
        + conjugate(ks.KS_Am, '어서')
        + conjugate(ks.KS_An, 'ㄹ', '어서')
        + conjugate(ks.KS_Ao, '어서')
        + conjugate(ks.KS_Ap, '어서')
        + conjugate(ks.KS_Ar, '와서')
        + conjugate(ks.KS_As, '아서')
        + conjugate(ks.KS_Aw, '와서')
        + conjugate(ks.KS_Ay, 'ㅙ', '서')
        + conjugate(ks.KS_VTk, 'ㄹ', '라서')
        ))

### Degree (정도)
KW_BD = '가장|그다지|더|많이|별로|약간|얼마간|잘|조금|훨씬'

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
        + conjugate(ks.KS_Ag, '하게')
        + conjugate(ks.KS_Ah, '하게')
        + conjugate(ks.KS_Ai, '게')
        + conjugate(ks.KS_Aj, '게')
        + conjugate(ks.KS_Al, '르게')
        + conjugate(ks.KS_Am, '게')
        + conjugate(ks.KS_An, 'ㄹ', '게')
        + conjugate(ks.KS_Ao, '게')
        + conjugate(ks.KS_Ap, '게')
        + conjugate(ks.KS_Ar, 'ㅂ', '게')
        + conjugate(ks.KS_As, 'ㅅ', '게')
        + conjugate(ks.KS_Aw, 'ㅂ', '게')
        + conjugate(ks.KS_Ay, 'ㅚ', '게')
        + conjugate(ks.KS_VTk, '르게')
    )
)

### Negative 
KW_BN = '|'.join(
    sorted(
        conjugate(ks.KS_Aa, 'ㅡ', '지')
        + conjugate(ks.KS_Ab, 'ㅂ', '지')
        + conjugate(ks.KS_Ac, '지')
        + conjugate(ks.KS_Ad, 'ㄹ', '지')
        + conjugate(ks.KS_Ae, 'ㅡ', '지')
        + conjugate(ks.KS_Af, '르지')
        + conjugate(ks.KS_Ag, '하지')
        + conjugate(ks.KS_Ah, '하지')
        + conjugate(ks.KS_Ai, '지')
        + conjugate(ks.KS_Aj, '지')
        + conjugate(ks.KS_Al, '르지')
        + conjugate(ks.KS_Am, '지')
        + conjugate(ks.KS_An, 'ㄹ', '지')
        + conjugate(ks.KS_Ao, '지')
        + conjugate(ks.KS_Ap, '지')
        + conjugate(ks.KS_Ar, 'ㅂ', '지')
        + conjugate(ks.KS_As, 'ㅅ', '지')
        + conjugate(ks.KS_Aw, 'ㅂ', '지')
        + conjugate(ks.KS_Ay, 'ㅚ', '지')
        + conjugate(ks.KS_VTk, '르지')
    )
)

### ‘-이/-히’
KW_BI = '|'.join(
    sorted(
        conjugate(ks.KS_Ac, '이')
        + conjugate(ks.KS_Af, 'ㄹ', '리')
        + conjugate(ks.KS_Ah, '히')
        + conjugate(ks.KS_Ak, '이')
        + conjugate(ks.KS_Al, 'ㄹ', '리')
        + conjugate(ks.KS_Aw, '이')
    )
)

### With
KW_BW = '|'.join(
    sorted(
        conjugate(KW_NIf, '로')
        + conjugate(KW_NIn, '으로')
        + conjugate(KW_NIv, '로')
    )
)

KW_B = joinseq(KW_BD, KW_BM, KW_BN, KW_BI)
KW_B1 = monosyllables(KW_B)

## Forein Words

KW_Ff = "(\\w*)(all|ell|earn|one)"  # f: has final consonant in Korean
KW_Fv = "(\\w*)(ice|ocks|old|uy)"  # v: ends with vowel (does not have final consonant) in Korean


# Modifier(관형어)

## Adjective
KW_MA = "다를"

## Determiners(관형사)
KW_MD = "새|헌"  

## Verb
KW_MVl = "나아갈|부릴|어찌할"
KW_MVn= "느낀|배운"
KW_MV = joinseq(KW_MVl, KW_MVn)

KW_M = joinseq(KW_MD, KW_MV, KW_MA)


## Nouns - Activity (can be verb with '-하다/-되다' or used in form of '~을/를 하다')
### Original (Korean + Hanja)
KW_NAOf = "생각|[가수증]감|가공|곱|[건입]국|[연체]결|[총포]괄|접근|가늠|[담배]당|가동|[노]력|[수제훈]련|[기수]록|[발변설연작제조증]명|괄목|함몰|고민|[개선]발|체벌|[반중]복|[손연향]상|개선|발생|[건개배연증해]설|[구생작완형]성|[연학]습|[장파]악|[예해]약|[구시재]연|오염|[반운투]영|[사이적통포활]용|훈육|[지]원|확인|[도수]입|[수]?출입|시작|[긴등성저]장|[발회]전|조절|[결설수지측한]정|검증|선언|[개선수]정|[도장부탈]착|칭찬|제창|[도수연인창추]출|[계예]측|[간선채]택|[면입]학|국한|분할|포함|[결취]합|[구실재표]현|[비서진]행|[재]?실행|[동수연진]행"
KW_NAOh = "가시화|간소화|강화|경량화|공산화|도커화|민주화|소형화|수치화|세분화|시각화|융화|인스턴스화|중앙화|첨예화|초기화|최[신적]화|캡슐화|파편화|패턴화|특[수]?화|현[실행]화|[0-9]+차원화|형상화"
KW_NAOv = "[인증추참평]가|[제탈]거|[공소]개|[연촉]구|[대상연제]기|이야기|시도|[고]려|[완치]료|[관격수처]리|마무리|연마|소모|근무|[공기]부|[감반발조]사|[감기축]소|[감준회]수|제시|제어|[기참]여|[긴소중필]요|[논유합]의|[주차폐]지|대체|[성]취|[납배설]치|검토|저하|이해|" + KW_NAOh 
KW_NAO = joinseq(KW_NAOf, KW_NAOv)

## can be Both of active(-하다) and passive(-받다)
KW_NABf = "주목|처단|할당|[입출]력|주목|처방|[처]?벌|전송|교육|위임|추천|연장|강종|심판|반환"
KW_NABv = "강요|기부|보조|오해"
KW_NAB = joinseq(KW_NABf, KW_NABv)

## abstract(like Emotion), can be used with ‘-받다’
KW_NAEf = "감동|고통|눈총|미움|버림|벌|복|사랑|영향"
KW_NAEv = "상처|죄"
KW_NAE = joinseq(KW_NAEf, KW_NAEv)

### derived from Foreign language
KW_NAFf = "\\w+깅|\\w+닝|\\w+딩|\\w+링|\\w+싱|\\w+킹|\\w+핑|게임|로그아웃|로그인|컨트롤|컴파일|클릭"
KW_NAFv = "다운로드|릴리스|마사지|업로드|[언]?마운트|업데이트|임포트|테스트|트리거|팔로우|폴로|플레이"
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
KW_NPNv = "어린이|감염자|[고남여병환]자|[동양이]성애자|바보|아기"

### by Job title or membership
KW_NPJf = "감독[관]?[님]?|강사님|과장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|사원|[사소의회]장[님]?|시인|작[곡사]?가님|직장인|학생|[수해]병|초대 회장|회사원"
KW_NPJv = "간호사|[강검의판]사|교[사수]|대[리표]|작[곡사]?가|전문가"
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
KW_NNAf = "[136780]|[0-9]*[0-9,.]*[136780]"
KW_NNAv = "[2459]|[0-9]*[0-9,.]*[2459]"
KW_NNA = "[0-9]|[0-9]+[0-9,.]*[0-9]+"

### Mixed
KW_NNMf = KW_NNA + KW_NNDf
KW_NNMv = KW_NNA + KW_NNDv
KW_NNM = joinseq(KW_NNMf, KW_NNMv)

### pure Korean
KW_NNK = "[다여일아열스서마쉰예백]?[한두세네섯댓곱덟홉]"

### all
KW_NN = joinseq(KW_NNC, KW_NND, KW_NNK)   


## Nouns - Resource
KW_NRH = "http[s]?[:]//[A-Za-z0-9./\-_%#]+"  # HTTP
KW_NR = KW_NRH


## Nouns - Unit

### Abstract
KW_NUAf = "건"
KW_NUAv = "뭉치"
KW_NUA = joinseq(KW_NUAf, KW_NUAv)

### Book
KW_NUBf = "글자|단어|단원|문|문장|장|절|항"
KW_NUBv = "부|파트"
KW_NUB = joinseq(KW_NUBf, KW_NUBv)

### Currency
KW_NUCf = "루블|엔|원|위안"
KW_NUCv = "달러|리라|유로|페소"
KW_NUC = joinseq(KW_NUCf, KW_NUCv)

### Distance
KW_NUDf = "광년"
KW_NUDv = "미터|리|킬로미터"
KW_NUD = joinseq(KW_NUDf, KW_NUDv)

### unit in symbol
KW_NUGf = "[mk]?g" 
KW_NUGv = "[k]?[LlMm]"
KW_NUG = joinseq(KW_NUGf, KW_NUGv)

### Information
KW_NUIf = "큐빗"
KW_NUIv = "기[가비]바이트|메[가비]바이트|바이트|비트|엑사바이트|제타바이트|키비바이트|킬로바이트|테[라비]바이트"
KW_NUI = joinseq(KW_NUIf, KW_NUIv)

### Multiplication
KW_NUMf = "곱"
KW_NUMv = "배"
KW_NUM = joinseq(KW_NUMf, KW_NUMv)

### aRea
KW_NURf = "평"
KW_NURv = "제곱미터|평방미터"
KW_NUR = joinseq(KW_NURf, KW_NURv)

### Stuff 
KW_NUSf = "그릇|달|명|방울|벌|쌍|장|줄|쪽"
KW_NUSv = "가지|개|마리|박스|봉지|채|페이지|회"
KW_NUSd = "대" # should be handled carefully: '세 대(three device)' vs '3세대(third generation)' 
KW_NUS = joinseq(
    KW_NUSf, KW_NUSv#, KW_NUSd
)

### Time
KW_NUTf = "분|시간|일|달|개월|년"
KW_NUTv = "밀리초|반기|분기|세기|세대|초"
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
KW_NUf = joinseq(KW_NUAf, KW_NUBf, KW_NUCf, KW_NUDf, KW_NUGf, KW_NUIf, KW_NUMf, KW_NURf, KW_NUSf, KW_NUTf, KW_NUVf, KW_NUWf)
KW_NUv = joinseq(KW_NUAv, KW_NUBv, KW_NUCv, KW_NUDv, KW_NUGv, KW_NUIv, KW_NUMv, KW_NURv, KW_NUSv, KW_NUTv, KW_NUVv, KW_NUWv)
KW_NU = joinseq(KW_NUf, KW_NUv)


## Nouns - animaL
### Domestic
KW_NLDf = "말" 
KW_NLDv = "개|고양이|돼지|소|오리" 
KW_NLD = joinseq(KW_NLDf, KW_NLDv)

### Insects
KW_NLIf = "개미|딱정벌레|지네"
KW_NLIv = "[꿀]벌|[여]왕벌"
KW_NLI = joinseq(KW_NLIf, KW_NLIv)

KW_NLf = joinseq(KW_NLDf, KW_NLIf)
KW_NLv = joinseq(KW_NLDv, KW_NLIv)
KW_NL = joinseq(KW_NLf, KW_NLv)


## Thing
### Abstract
KW_NTAf = "걸음|명산|모델|모형|모듈|방법|스텝|알고리즘|애플리케이션|앱|입력|전략|점|차원|채널|출력|층|토큰|토픽|튜플|특성|프로그램|함수|행렬"
KW_NTAv = "가중치|글자|단어|데이터|리뷰|메모리|변화|배치|벡터|시류|요소|인수|자체|절차|정도|차이|처리|축소|코드|폰트|학습 데이터|형태"
KW_NTA = joinseq(KW_NTAf, KW_NTAv)

### maChine
KW_NTCf = "툴"
KW_NTCv = "기계|장비|컴퓨터"

### Food
KW_NTFf = "국|귤|라면|밥|빵"
KW_NTFv = "국수|망고|바나나|배|사과|오렌지"
KW_NTF = joinseq(KW_NTFf, KW_NTFv)

### Measure
KW_NTMf = "폭" 
KW_NTMv = "개수|너비|넓이|높이|단위|수|숫자|크기" 
KW_NTM = joinseq(KW_NTMf, KW_NTMv)

### Scenary
KW_NTSf = "그림|[경상시전]황|[국장화]면"
#KW_NTFv = 


### Usual
KW_NTUf = "잔|컵|현수막|화투짝"
KW_NTUv = "접시"
KW_NTU = joinseq(KW_NTUf, KW_NTUv)

KW_NTf = joinseq(KW_NTAf, KW_NTCf, KW_NTFf, KW_NTMf, KW_NTSf,  KW_NTUf)
KW_NTv = joinseq(KW_NTAv, KW_NTCv, KW_NTFv, KW_NTMv, KW_NTUv)
KW_NT = joinseq(KW_NTf, KW_NTv)


## Pronouns
### Person
KW_PP = "너희|내|우리|저희"
### all
KW_P = joinseq(KW_PP)

## Verb

### Active
### Did
KW_VADw = '|'.join(
    sorted(
        conjugate(ks.KS_VAw, '우', '웠다')     # 키 + 웠다
    )
)

##### inG 
KW_VAGw = '|'.join(
    sorted(
        conjugate(ks.KS_VAw, '우', 'ㄴ', '다')  # 키우 + ㄴ + 다
    )
)

KW_VA = joinseq(KW_VADw, KW_VAGw)


### adJective
#### Change of status
KW_VJCi = conjugate(KW_ASA, '지')  # idea (ex: 나빠+지(다))
KW_VJCn = conjugate(KW_ASA, '진')  # progress (ex: 나빠+진(다))
KW_VJCp = conjugate(KW_ASA, '졌')  # past (ex: 나빠+졌(다))

### Passive
KW_VPl = "갈리다"  # ends with '~리다(lida)'
KW_VPi = "쓰이다"  # ends with '~이다(ida)'

KW_VIn = '|'.join(
    sorted(
        conjugate(ks.KS_VIa, 'ㄴ', '다')
        + conjugate(ks.KS_VIe, 'ㄴ', '다')        # 여무 + ㄴ + 다
        + conjugate(ks.KS_VIy, 'ㅣ', 'ㄴ', '다')  # 숨죽ㅇ + ㅣ + ㄴ + 다
        + conjugate(ks.KS_VIl, 'ㄴ', '다')        # 조 + ㄴ + 다
    )
)

#### Verb Transive haO-che
KW_VTO = '|'.join(
    sorted(
        map(lambda x: x + '시',
            ['하', '보이']
            + conjugate(KW_NAO, '하')       # 가공 + 하 + 시
            + conjugate(ks.KS_VTg, '으')    # 박 + 으 + 시
            + conjugate(ks.KS_VTh, '으')
            + conjugate(ks.KS_VTi, '')
            + conjugate(ks.KS_VTl, '')
            + conjugate(ks.KS_VTm, '')
            + conjugate(ks.KS_VTn, '')
            + conjugate(ks.KS_VTy, 'ㅜ')
        )
    )
)

##### Verb Transive haO-che Imperative
KW_VTOI = conjugate(KW_VTO, '오')
