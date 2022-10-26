import kostem as ks
from utils import joinseq
from kostr import concat


"""Korean Words"""

# Korean Conjugation (strings can be used for Conjugation)
KC_D = "[되된돼됐]"
KC_H = "하고[는자]?|하[겠였]\\w+|하기|하[는니다며여]|하도록|하려[고는]?|하[?]면|하여[야]?|하지[만]?|한 [것뒤적후]|한 다음|한다[고는니며지]?|할|할까[요]?|할래|할지[도]?[요]?|함[을]?|함이다|함입니다|합니다|해보[니다면]|해볼[까래]?|해[서야요]?|해준다|했고[요]?|했기|했는데[요]?|했다[만]?|했습니다[만]?|했으[니면][서]?|했을[지]?|했지[만]?[요]?"

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

KW_NSf = "심각|[둔민]감|건강|간결|깔끔|매끈|[불]?가능|간단|못마땅|가득|근면|곤란|부지런|[장졸]렬|지저분|[단온지]순|비슷|참신|[불]?성실|부실|[미병심]약|치열|편안|동일|복잡|부족|[부]?적절|착|공평|[명정]확"
KW_NSv = "유사|[자섬]세|간소|상이|수요|[거장중]대|진부|[긴중필]요"
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
        + conjugate(KW_NS, '한')                 # 필요+한
    )
)

KW_AS = joinseq(KW_ASA, KW_ASL, KW_ASN)
KW_A = joinseq(KW_AS)
KW_A1 = monosyllables(KW_A)

### Pre-nouns(관형사)

#### Verb - Active - No-tense
KW_PVAN = '|'.join(
    sorted(
        ["하는"]
        + conjugate(ks.KS_VAd, '는')             # 넣+는
        + conjugate(ks.KS_VAh, '하는')           # 가까이+하는
        + conjugate(ks.KS_VAi, 'ㅣ', '는')       # 외ㅊ+ㅣ+는
        + conjugate(ks.KS_VAj, '는')             # 만드+는
        + conjugate(ks.KS_VAk, '르는')           # 모+르는
        + conjugate(ks.KS_VAl, '리는')           # 올+리는
        + conjugate(ks.KS_VAm, '는')             # 빼+는
        + conjugate(ks.KS_VAn, '는')             # 만나+는
        + conjugate(ks.KS_VAr, '는')             # 내미+는
        + conjugate(ks.KS_VAu, 'ㅜ', '는')       # 낮ㅊ+ㅜ+는
        + conjugate(ks.KS_VAw, '우', '는')       # 치+우+는
    )
)

#### Verb - Active - Past
KW_PVAP = '|'.join(
    sorted(
        ["했던"]
        + conjugate(ks.KS_VAd, '었던')             # 넣+었
        + conjugate(ks.KS_VAh, '했던')             # 가까이+했
        + conjugate(ks.KS_VAi, 'ㅕ', 'ㅆ', '던')   # 외ㅊ+ㅕ+ㅆ
        + conjugate(ks.KS_VAj, 'ㄹ', '었던')       # 만드+ㄹ+었
        + conjugate(ks.KS_VAk, 'ㄹ', '랐던')       # 모+ㄹ+랐
        + conjugate(ks.KS_VAl, '렸던')             # 올+렸
        + conjugate(ks.KS_VAm, 'ㅆ', '던')         # 빼+ㅆ
        + conjugate(ks.KS_VAn, 'ㅆ', '던')         # 만나+ㅆ
        + conjugate(ks.KS_VAr, 'ㄹ', '었던')       # 내미+ㄹ+었
        + conjugate(ks.KS_VAu, '췄던')             # 낮췄
        + conjugate(ks.KS_VAw, '웠던')             # 치+웠
    )
)

KW_PVA = joinseq(KW_PVAN, KW_PVAP)

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
        + conjugate(KW_NS, '했던')
    )
)

KW_PA = joinseq(KW_PAN, KW_PAP)

## Nouns - Idea
KW_NIf = "확률|이름"
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
        + conjugate(ks.KS_VAk, 'ㄹ', '라서')
        ))

### Degree (정도)
KW_BD = '가장|거의|그다지|더|많이|별로|약간|얼마간|자주|잘|조금|훨씬'

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
        + conjugate(ks.KS_VAk, '르게')
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
        + conjugate(ks.KS_VAk, '르지')
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

### f: has final consonant in Korean (BUT NOT IN ENGLISH)
KW_Ff = "[A-Za-z0-9]*all|[A-Za-z0-9]*ell|[A-Za-z0-9]*earn|[A-Za-z0-9]*ime|[A-Za-z0-9]*one|[A-Z]*ML|LIME|URL|VPN"

### v: ends with vowel (does not have final consonant) in Korean (BUT NOT IN ENGLISH)
KW_Fv = "[A-Za-z0-9]*ice|[A-Za-z0-9]*ocks|[A-Za-z0-9]*old|[A-Za-z0-9]*uy|[A-Za-z0-9]*dog|[A-Za-z0-9]*uire|[A-Z]*TP|DARPA|[D]?NS|ENQUIRE|UDP|URI"

## Thing(무정물)
### Abstract
KW_NTAfc = "관측값|공간|물건|학년|기능|[능출]력|연령|프로그램|명산|걸음|전략|칼럼|입력|블록|그룹|[품항]목|논문|방법|형상|성|특성|솔루션|커넥션|애플리케이션|현실|직업|앱|차원|도메인|요인|타입|점|규정|[시지]점|수준|알고리즘|군집|층|토큰|스텝|시스템|패턴|팀|상품|토픽|모형"
KW_NTAfl = "채널|모델|모듈|행렬|메일|스타일|튜플"
KW_NTAf = joinseq(KW_NTAfc, KW_NTAfl)
KW_NTAv = "정도|메서드|스레드|코드|시류|메모리|처리|카테고리|리뷰|[요축]소|[난변인함]수|부동소수점수|분위수|순서|마이크로서비스|서비스|클래스|[단언]어|레이어|소프트웨어|하드웨어|범위|차이|글자|일자|범주|[시절]차|아키텍처|피처|[고기물신액옥자형]체|가중치|관측치|배치|네트워크|에포크|태스크|데이터|벡터|학습 데이터|형태|세그먼트|이벤트|컴포넌트|크레이트|폰트|분포|번호|비밀번호|변화|기회"
KW_NTA = joinseq(KW_NTAf, KW_NTAv)

### can Be(‘-화’)
KW_NTBf = "시각|구간|모듈|[대경]량|[무유]료|그룹|일반|세분|공산|[가형]상|가속|캡슐|최신|현실|중앙|집약|차원|일원|효율|균일|최적|다중|계층|패턴|디지털|파편|현행|[대소]형"
KW_NTBv = "체계|[동초]기|고도|의무|독립변수|변수|특수|인스턴스|가시|해시|구조|민주|내재|수치|도커|[암복]호"
KW_NTB = joinseq(KW_NTBf, KW_NTBv)


### maChine, instrument, tool
KW_NTCf = "로봇|툴"
KW_NTCv = "API|CPU|GPU|기계|비행기|생성기|판별기|항공기|로더|서버|웹[ ]?서버|장비|브라우저|웹[ ]?브라우저|스토리지|차|기차|자동차|컴퓨터|클라이언트"
KW_NTC = joinseq(KW_NTCf, KW_NTCv)

### District
KW_NTDf = "군|동|면|읍|지역|현"
KW_NTDv = "국가|구|시군구|도|리|부|시|주|카운티"
KW_NTD = joinseq(KW_NTDf, KW_NTDv)

### Entity
KW_NTEf = "[미영중한]국|기관|대만|일본|삼성|스페인|독일|애플|[남북]한|은행"
KW_NTEv = "학교|테슬라|발행사|회사|업소|엔비디아|이탈리아|한라|호주"
KW_NTE = joinseq(KW_NTEf, KW_NTEv)

### Food
KW_NTFf = "감|국|귤|라면|밥|빵"
KW_NTFv = "국수|망고|바나나|배|사과|오렌지"
KW_NTF = joinseq(KW_NTFf, KW_NTFv)

### metapHor (~같다)
KW_NTHf = "한결|대궐|당금|불꽃|꿈|[끌놋]날|실낱|득달|댕돌|득돌|찰떡|똑|쥐똥|굴뚝|[다벼]락|벽력|전반|철벽|불|쥐뿔|[쏜]?살|추상|[목철]석|박속|장승|굴왕신|귀신|[개쥐]?좆|[감금깜무]쪽|주옥|악착|억척|왕청|[딴분철]통|바둑판|떡판"
KW_NTHv = "개코|감태|하나|생때|신청부|생파리|납덩이|옴포동이|뚱딴지|불티|비호|성화"
KW_NTH = joinseq(KW_NTHf, KW_NTHv)

### Language
KW_NTLf = "파이썬"
KW_NTLv = "자바스크립트"
KW_NTL = joinseq(KW_NTLf, KW_NTLv)

### Place
KW_NTP = "가남|강릉|곡성|공주|광명|광주|구미|구례|구포|군산|김천|김포|김해|나주|남원|논산|단양|대구|대전|동해|둔내|마산|만종|목포|묵호|밀양|부발|부산|상봉|서울|세종|수원|순천|아산|양평|여천|영주|오송|용산|울산|원주|익산|인천|장호원|전주|정동진|정읍|제천|진주|창원|천안|청량리|충주|포항|풍기|평창|행신|횡성"

### Scenary
KW_NTSf = "그림|[경상시전]황|[국장화]면"
KW_NTSv = "뷰" 
KW_NTS = joinseq(KW_NTSf, KW_NTSv)

### Team
KW_NTTf = "개발|시설|영업|운영|고객 지원|판촉|마케팅"
KW_NTTv = "회계|관리|[노법재총]무|인사|경제"
KW_NTT = joinseq(KW_NTTf, KW_NTTv)

### Usual
KW_NTUf = "잔|컵|현수막|화투짝"
KW_NTUv = "접시"
KW_NTU = joinseq(KW_NTUf, KW_NTUv)

### eVent
KW_NTVf = "개학|생일|월드컵|올림픽"
KW_NTVv = "유세|콘퍼런스|대회|운동회"
KW_NTV = joinseq(KW_NTVf, KW_NTVv)

### Measure(dimension)
KW_NTMf = "폭" 
KW_NTMv = "개수|너비|넓이|높이|단위|수|숫자|크기" 
KW_NTM = joinseq(KW_NTMf, KW_NTMv)

KW_NTf = joinseq(KW_NTAf, KW_NTBf, KW_NTCf, KW_NTDf, KW_NTEf, KW_NTFf, KW_NTHf, KW_NTLf, KW_NTMf, KW_NTSf, KW_NTTf, KW_NTUf, KW_NTVf)
KW_NTv = joinseq(KW_NTAv, KW_NTBv, KW_NTCv, KW_NTDv, KW_NTEv, KW_NTFv, KW_NTHv, KW_NTLv, KW_NTMv, KW_NTSv, KW_NTTv, KW_NTUv, KW_NTVv)
KW_NT = joinseq(KW_NTf, KW_NTv)


## Nouns - Activity (can be verb with '-하다/-되다' or used in form of '~을/를 하다')
### Original (Korean + Hanja)
KW_NAOf = "생각|보간|[가수증]감|곱|[가제]공|[건입출]국|공격|[연체]결|변경|[총포]괄|집권|[접출]근|송금|지급|가늠|기능|[도전]달|[담배]당|[가기이작]동|[납취획]득|누락|[노]력|[관마수제훈]련|[기수]록|[발변설연작제조증]명|[괄주지]목|함몰|질문|고민|위반|[개선]발|체벌|[반중]복|구분|준비|계산|[손연향]상|발생|[분해]석|개선|[건개배연증해]설|[구생작완형]성|[계상접]속|[방소]송|[기저]술|[연학]습|[송수]신|송수신|임신|[장파]악|[고제]안|[계예해]약|선언|[수성영작]업|[구시재]연|오염|[반운촬투]영|[사이작적통포활]용|훈육|[기지]원|불응|방일|통일|[기도수투]입|[수]?출입|[동시조]작|[긴등성저출]장|경쟁|산적|[발운회]전|조절|[걱검결설수지추측한]정|참조|방중|검증|감지|부진|선언|[개선수확]정|[도장부집탈]착|칭찬|제창|구축|[도산수연인제진창추]출|[계예]측|강탈|[간선채]택|[면유입재]학|국한|방한|분할|포함|[결부취]합|[동발비서시수운연진]행|[재]?실행|[구실재표]현|[반변]환|계획"
KW_NAOh = '|'.join(conjugate("강|미|융|특", '화') + conjugate(ks.KS_Az, '화') + conjugate(KW_NTB, '화'))
KW_NAOv = "[인증추참평]가|[제탈]거|[공소전]개|[경방]과|[복연촉]구|[경대상연제표]기|이야기|[시유]도|[고]려|신뢰|[완치]료|[관격분수]리|[전후]?처리|마무리|연마|구매|소모|근무|방미|[공거기]부|[감공반발수식조퇴]사|[감기축]소|[감준회]수|[실제출]시|제어|[기참]여|[긴소중필]요|[논유정주합회]의|[재]?정의|복제|[유주차폐]지|[기탑]재|대체|[갈성수탈편]취|[납배설]치|검토|돌파|[부실]패|배포|발표|[저전통]화|[분이]해|" + KW_NAOh 
KW_NAO = joinseq(KW_NAOf, KW_NAOv)

## can be Both of active(-하다) and passive(-받다)
KW_NABf = "비난|감동|처단|할당|[입출]력|주목|처방|[처]?벌|축복|상속|전송|제안|교육|환영|구원|[승확]인|위임|대입|연장|판정|강종|칭찬|추천|신청|부탁|선택|심판|반환|시험"
KW_NABv = "용서|계시|강요|기부|보조|오해"
KW_NAB = joinseq(KW_NABf, KW_NABv)

### derived from Foreign language
# Don't use '*팅' instead of '부팅' for case like: 디스켓으로부팅한후 --> 디스켓으로 부팅한 후
KW_NAFf = "\\w+[깅닝딩링밍싱킹핑]|게임|로그아웃|로그인|마케팅|컨트롤|컴파일|클릭|부팅"  
KW_NAFv = "다운로드|릴리스|마사지|업로드|[언]?마운트|업데이트|임포트|카운트|테스트|트리거|팔로우|폴로|플레이"
KW_NAF = joinseq(KW_NAFf, KW_NAFv)

KW_NAHf = joinseq(KW_NABf, KW_NAFf, KW_NAOf)
KW_NAHv = joinseq(KW_NABv, KW_NAFv, KW_NAOv)
KW_NAH = joinseq(KW_NAHf, KW_NAHv)

## abstract(like Emotion), can be used with ‘-받다’
KW_NAEf = "고난|고통|눈총|미움|버림|벌|복|사랑|영향"
KW_NAEv = "상처|죄"
KW_NAE = joinseq(KW_NAEf, KW_NAEv)


### all
KW_NAf = joinseq(KW_NAOf, KW_NAFf)
KW_NAv = joinseq(KW_NAOv, KW_NAFv)
KW_NA = joinseq(KW_NAf, KW_NAv)

## Nouns (Activity + Status)
#KW_NASf = joinseq(KW_NAf, KW_NSTf)
#KW_NASv = joinseq(KW_NAv, KW_NSTv)
#KW_NAS = joinseq(KW_NASf, KW_NASv)

## Nouns - Color
KW_NC = "녹색"

## Nouns - Dependant
KW_ND = "밖|뿐"

## Nouns - Person
### by Existance
KW_NPEf = "사람|인[간물]"
KW_NPEv = "인류"

### by biological or phisical conditioN
KW_NPNf = "[비]?장애인|어른|소년"
KW_NPNv = "어린이|감염자|[고남여병환]자|[동양이]성애자|바보|아기|아이"

### by Job title or membership
KW_NPJf = "감독[관]?[님]?|강사님|과장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|[사의]원|[사소의회]장[님]?|시인|작[곡사]?가님|직장인|고교생|[대중]?학생|초등학생|[수해]병|초대 회장|회사원|군인|경찰|동호인"
KW_NPJv = "프로그래머|간호사|[강검의판]사|교[사수]|대[리표]|작[곡사]?가|전문가|개발자"
KW_NPJ = joinseq(KW_NPJf, KW_NPJv)

### by ranK
KW_NPKf = "[경병부차]장[님]?|[상이일]병|[대중소준][령장]|사령관|통수권자"
KW_NPKv = "경[사위]|[대중소준][위좌]|[상중하]사"

### by social Relation
KW_NPRf = "아들|동문|조상|자손|식솔|[처]?자식|[부장]인|동창|[일사삼오육칠팔]촌|남편"
KW_NPRv = "[식친]구|처남|자녀|아내|아주머니|[어할]머니|아줌마|엄마|[고대부이]모|동료|며느리|[대형]부|아빠|[제형]수|아저씨|애인|사위|저|[자처형]제|[할]아버지|제부|처형"

### by Activity, accident, crime
KW_NPAf = "고객|손님|애[견묘]인|[증행]인"
KW_NPAv = "수집가|애호가|프로|아마추어|글쓴이|엮은이|지은이|감[독시]자|강[연의]자|관[계련찰]자|당[사직]자|[사이]용자|소유자|반[려역]자|발[제표]자|응시자|[원]작자|참[가석여]자|협력자|[가피]해자|팬"

### all
KW_NPf = joinseq(KW_NPEf, KW_NPNf, KW_NPJf, KW_NPKf, KW_NPRf, KW_NPAf)
KW_NPv = joinseq(KW_NPEv, KW_NPNv, KW_NPJv, KW_NPKv, KW_NPRv, KW_NPAv)
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
KW_NUSf = "그릇|권|달|명|방울|벌|쌍|장|줄|쪽|통"
KW_NUSv = "가지|개|구|마리|박스|봉지|채|페이지|회"
KW_NUSd = "대" # should be handled carefully: '세 대(three device)' vs '3세대(third generation)' 
KW_NUS = joinseq(
    KW_NUSf, KW_NUSv#, KW_NUSd
)

### Time
KW_NUTf = "분|시간|일|달|주|월|개월|년|연도"
KW_NUTv = "밀리초|반기|분기|세기|세대|초"
KW_NUT = joinseq(KW_NUTf, KW_NUTv)

### Volume
KW_NUVv = "세제곱미터"
KW_NUV = KW_NUVv

### Weight
KW_NUWf = "그램|킬로그램|평"
KW_NUWv = "밀리리터|데시리터|리터|킬로리터|파운드"
KW_NUW = joinseq(KW_NUWf, KW_NUWv)

### all
KW_NUf = joinseq(KW_NUAf, KW_NUBf, KW_NUCf, KW_NUDf, KW_NUGf, KW_NUIf, KW_NUMf, KW_NURf, KW_NUSf, KW_NUTf, KW_NUWf)
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


## Nouns from Verb
### -음
KW_NVAm = '|'.join(
    sorted(
        conjugate(ks.KS_VAd, '음')          # 넣+음
        + conjugate(ks.KS_VAh, '함')        # 가까이+함
        + conjugate(ks.KS_VAi, 'ㅣ', 'ㅁ')  # 외ㅊ+ㅣ+ㅁ
        + conjugate(ks.KS_VAk, '름')        # 모+름
        + conjugate(ks.KS_VAl, '림')        # 돌+림
        + conjugate(ks.KS_VAm, 'ㅁ')        # 빼+ㅁ
        + conjugate(ks.KS_VAn, 'ㅁ')        # 만나+ㅁ
        + conjugate(ks.KS_VAr, 'ㄻ')        # 내미+ㄻ
        + conjugate(ks.KS_VAu, 'ㅜ', 'ㅁ')  # 늦ㅊ+ㅜ+ㅁ
        + conjugate(ks.KS_VAw, '움')        # 치+움    
    )
)

KW_NVm = KW_NVAm

### -기

KW_NVAk = '|'.join(
    sorted(
        conjugate(ks.KS_VAd, '기')          # 넣+기
        + conjugate(ks.KS_VAh, '하기')      # 가까이+하기
        + conjugate(ks.KS_VAi, 'ㅣ', '기')  # 외ㅊ+ㅣ+기
        + conjugate(ks.KS_VAk, '르', '기')  # 모+르+기
        + conjugate(ks.KS_VAl, '리기')      # 돌+리기
        + conjugate(ks.KS_VAm, '기')        # 빼+기
        + conjugate(ks.KS_VAn, '기')        # 만나+기
        + conjugate(ks.KS_VAr, 'ㄹ', '기')  # 내미+ㄹ+기
        + conjugate(ks.KS_VAu, 'ㅜ', '기')  # 늦ㅊ+ㅜ+기
        + conjugate(ks.KS_VAw, '우기')      # 치+우기   
    )
)

KW_NVIk = '|'.join(
    sorted(
        conjugate(ks.KS_VIa, '기')          # 가+기
        + conjugate(ks.KS_VId, 'ㄷ', '기')  # 거+ㄷ+기
        + conjugate(ks.KS_VIe, 'ㄹ', '기')  # 여무+ㄹ+기
        + conjugate(ks.KS_VIl, 'ㄹ', '기')  # 조+ㄹ+기
        + conjugate(ks.KS_VIn, '기')        # 가+기
        + conjugate(ks.KS_VIy, 'ㅣ', '기')  # 생ㄱ+ㅣ+기
    )
)

KW_NVTk = '|'.join(
    sorted(
        conjugate(ks.KS_VTg, '기')          # 잡+기
        + conjugate(ks.KS_VTh, '기')        # 먹+기
        + conjugate(ks.KS_VTi, '기')        # 보+기
        + conjugate(ks.KS_VTl, 'ㄹ', '기')  # 가+ㄹ+기
        + conjugate(ks.KS_VTm, 'ㄹ', '기')  # 드+ㄹ+기
        + conjugate(ks.KS_VTn, 'ㄹ', '기')  # 빠+ㄹ+기
        + conjugate(ks.KS_VTn, 'ㅜ', '기')  # 나ㄴ+ㅜ+기
    )
)

KW_NVk = joinseq(KW_NVAk, KW_NVIk, KW_NVTk)
KW_NV = joinseq(KW_NVm, KW_NVk)


# Modifier(관형어)

## Adjective
KW_MA = "다를"

## Determiners(관형사)
KW_MD = "새|헌"  

## Verb
KW_MVl = "나아갈|부릴|어찌할"
KW_MVn= '|'.join(
    sorted(
        ["느낀", "배운"]
        + conjugate(KW_NAO, '된')
    )
)
KW_MV = joinseq(KW_MVl, KW_MVn)

KW_M = joinseq(KW_MD, KW_MV, KW_MA)


## Pronouns
### Person
KW_PPf = "당신|여러분"
KW_PPv = "너희|내|우리|저희"
KW_PP = joinseq(KW_PPf, KW_PPv)
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
