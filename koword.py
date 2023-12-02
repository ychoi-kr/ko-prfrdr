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

## Nouns - From Adjective
KW_NF = '|'.join(sorted(
        conjugate(ks.KS_Ab, '움')
        + conjugate(ks.KS_Ac, '음')
        + conjugate(ks.KS_Ae, 'ㅡ', 'ㅁ')
        + conjugate(ks.KS_Ai, '음')
        + conjugate(ks.KS_Aj, '음')
        + conjugate(ks.KS_Ak, '음')
        + conjugate(ks.KS_Al, '름')
        + conjugate(ks.KS_Am, '음')
        + conjugate(ks.KS_Am, 'ㅁ')
        + conjugate(ks.KS_Ao, '음')
        + conjugate(ks.KS_Ap, 'ㅁ')
        + conjugate(ks.KS_Ar, '움')
        + conjugate(ks.KS_As, '음')
        + conjugate(ks.KS_Aw, '움')
    )
)

## Nouns - Status  # do not add stems(KS_Ag) or busa(KW_BA) here
KW_NSf = "심각|[둔민]감|건강|간결|깔끔|[불]?가능|근면|정밀|곤란|부지런|무기력|이상|[단온지]순|비슷|[불]?성실|부실|[불]?확실|다양|치열|편안|동일|부족|[부]?적절|나태|공평|[명정]확"
KW_NSv = "명료|무의미|유사|[자섬]세|간소|[거장중]대|[중필]요|분포|난해"
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
        + conjugate(ks.KS_Af, '른')              # 다+ㄹ+ㅡ+ㄴ(different)
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
KW_NIf = "공간|느낌|맛|멋|판매량|확률|이름|성별|식|날짜"
KW_NIn = "차원"
KW_NIv = "몸무게|크기|빈도|나이"
KW_NI = joinseq(KW_NIf, KW_NIn, KW_NIv)

## Busa(부사, adverb)

### Busa by itself while can be Adjective with ‘-하다’
KW_BA = "가득|들쑥날쑥"

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
        ['그대로', '서로', '함부로']
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

### Busa by itself while can be Verb with ‘-하다’
KW_BVa = "시들"              # -거리다, -하다(-해지다), -대다
KW_BVb = "굽신|생글"         # -거리다, -하다, -대다
KW_BVc = "이러쿵저러쿵"      # -하다
KW_BV = joinseq(KW_BVa, KW_BVb, KW_BVc)

### With
KW_BW = '|'.join(
    sorted(
        conjugate(KW_NIf, '로')
        + conjugate(KW_NIn, '으로')
        + conjugate(KW_NIv, '로')
    )
)

KW_B = joinseq(KW_BD, KW_BM, KW_BN, KW_BI, KW_BV, KW_BW)
KW_B1 = monosyllables(KW_B)

## Forein Words
KW_Fc = "[A-Za-z0-9]*earn|[A-Za-z0-9]*ime|[A-Za-z0-9]*one|LIME|VPN"
KW_Fl = "[A-Za-z0-9]*all|[A-Za-z0-9]*e[l]{1,2}|[A-Z]*ML|URL"
KW_Ff = joinseq(KW_Fc, KW_Fl)
KW_Fv = "[A-Za-z0-9]*ice|[A-Za-z0-9]*ocks|[A-Za-z0-9]*old|[A-Za-z0-9]*uy|[A-Za-z0-9]*dog|[A-Za-z0-9]*uire|[A-Za-z]*[a-z]+ter|[A-Z]*TP|DARPA|[D]?NS|ENQUIRE|UDP|URI|config"
KW_F = joinseq(KW_Ff, KW_Fv)

## Thing(무정물)
### Abstract
KW_NTAfc = "값|관측값|물건|[자지]금|학년|게놈|성능|돈|[능출]력|연령|프로그램|걸음|목적|전략|칼럼|입력|기록|블록|그룹|스트림|화면|별명|[품항]목|[구논]문|방법|재산|명산|[세형]상|인생|성|창의성|[속특]성|데이터셋|솔루션|커넥션|애플리케이션|웹 애플리케이션|[공방상지형]식|방안|직업|앱|영역|[내비]용|차원|웹|마음|도메인|디자인|요인|타입|점|규정|[단시장지]점|수준|알고리즘|인터넷|군집|대책|층|명칭|토큰|스택|스텝|시스템|패턴|팀|상품|토픽|국민[ ]?평형|모형|힙|DOM"
KW_NTAfl = "채널|모델|모듈|행렬|말|물|[동식]물|동식물|테이블|기술|현실|배열|연관 배열|[이]?메일|파일|스타일|품질|튜플" # ends with letter which has ㄹ(lieul) as final consonant
KW_NTAf = joinseq(KW_NTAfc, KW_NTAfl)
KW_NTAv = "선전 포고|[과근선]거|결과|[용정]도|가이드|메서드|스레드|코드|사용료|미래|[자재]료|시류|메모리|라이브러리|카테고리|멤버|리뷰|경영비|의사|[요축]소|[난변소인홍함]수|[극]?소수|부동소수점수|분위수|[순질]서|마이크로서비스|서비스|시퀀스|인덱스|클래스|[단언]어|레이어|소프트웨어|아이디어|하드웨어|수요|범위|차이|글자|현재|일자|이미지|[시절]차|아키텍처|피처|[객물신옥형]체|가중치|관측치|배치|네트워크|에포크|태스크|세태|데이터|벡터|학습 데이터|[상형]태|세그먼트|이벤트|컴포넌트|크레이트|폰트|전자파|[분세점]포|[목좌]표|면허|번호|비밀번호|변화|기회"
KW_NTA = joinseq(KW_NTAf, KW_NTAv)

### can Be(‘-화’)
KW_NTBf = "시각|구간|모듈|간략|[대경]량|[병직]렬|[무유]료|그룹|일반|세분|공산|[가형]상|활성|간소|[가고]속|캡슐|상식|최신|현실|중앙|집약|공용|차원|일원|효율|균일|복잡|최적|다중|계층|패턴|디지털|공통|파편|현행|[대모소]형"
KW_NTBv = "체계|정규|카탈로그|[동무초]기|[극최]대|고도|의무|정보|[극최]소|독립변수|변수|특수|인스턴스|가시|해시|구조|민주|범주|내재|[고기액]체|수치|도커|[암복]호|무효"
KW_NTB = joinseq(KW_NTBf, KW_NTBv)


### maChine, instrument, tool, furniture
KW_NTCf = "Babel|NPM|레즈넷|레티나넷|로봇|모바일넷|런타임|툴|논리 풀"
KW_NTCv = "API|CPU|GPU|Grunt|gulp|기계|비행기|생성기|판별기|항공기|침대|[디인]코더|로더|마이크로 프런트엔드|백엔드|서버|웹[ ]?서버|장비|데이터베이스|브라우저|웹[ ]?브라우저|스토리지|[객기마열]?차|자동차|웹 워커|컴퓨터|클라이언트|태스크 러너|프런트엔드"
KW_NTC = joinseq(KW_NTCf, KW_NTCv)

### District unit
KW_NTDf = "군|동|면|읍|지역|현"
KW_NTDv = "국가|구|시군구|도|리|부|시|주|카운티"
KW_NTD = joinseq(KW_NTDf, KW_NTDv)

### Entertainment
KW_NTEf = "연극|소설|공연|책|웹툰"
KW_NTEv = "드라마|콘서트|영화"
KW_NTE = joinseq(KW_NTEf, KW_NTEv)

### Food
KW_NTFf = "국|귤|라면|밥|빵"
KW_NTFv = "국수|망고|바나나|배|사과|오렌지"
KW_NTF = joinseq(KW_NTFf, KW_NTFv)

### Guyeok (행정구역명)
KW_NTGf = "가남|강릉|경남|경북|곡성|광명|군산|김천|남원|논산|단양|대전|마산|만종|밀양|부발|부산|상봉|서울|세종|수원|순천|아산|양평|여천|오송|용산|울산|익산|인천|장호원|전남|전북|정동진|정읍|제천|창원|천안|청량리|충남|충북|포항|풍기|평창|행신|횡성"
KW_NTGv = "공주|광주|구미|구례|구포|김포|김해|나주|대구|동해|둔내|목포|묵호|영주|원주|전주|진주|충주"
KW_NTG = joinseq(KW_NTGf, KW_NTGv)

### metapHor (~같다)
KW_NTHf = "한결|대궐|당금|불꽃|꿈|[끌놋]날|실낱|득달|댕돌|득돌|찰떡|똑|쥐똥|굴뚝|[다벼]락|벽력|전반|철벽|불|쥐뿔|[쏜]?살|추상|[목철]석|박속|장승|굴왕신|귀신|[개쥐]?좆|[감금깜무]쪽|주옥|악착|억척|왕청|[딴분철]통|바둑판|떡판"
KW_NTHv = "개코|감태|생때|신청부|생파리|납덩이|옴포동이|뚱딴지|불티|비호|성화"
KW_NTH = joinseq(KW_NTHf, KW_NTHv)

### derived from adjective in English
KW_NTIf = "로컬|피지컬|멘털"
KW_NTI = KW_NTIf

### Jeok('적')
KW_NTJf = "비관|[비소적희]극|저돌|낭만|폭발|[이일추]상|[계부세영종지]속|실용|[대집]중|낙천"
KW_NTJv = "단계|[선영]구|대내|현대|실리|진보|보수|[도원임한]시|대외|행위|독자|경제|[민자]주|[구실자총]체|향토|사회"
KW_NTJ = joinseq(KW_NTJf, KW_NTJv)

### Language

#### Artificial
KW_NTLAf = "파이썬|C#|HTML|Python|SQL|XML"
KW_NTLAv = "루비|자바|자바스크립트|타입스크립트|솔리디티|C|C[+][+]|Java|Java[Ss]cript|PHP"

#### Natural
KW_NTLNv = "독일어|북한어|스페인어|영어|이탈리아어|일본어|자연어|중국어|터키어|한국어"

KW_NTLf = KW_NTLAf
KW_NTLv = joinseq(KW_NTLAv, KW_NTLNv)
KW_NTL = joinseq(KW_NTLf, KW_NTLv)

### Measure(dimension)
KW_NTMf = "폭" 
KW_NTMv = "개수|너비|넓이|높이|단위|수|숫자|크기" 
KW_NTM = joinseq(KW_NTMf, KW_NTMv)

### Nation
KW_NTNf = "[미영중한]국|대만|대한민국|일본|스페인|독일|[남북]한"
KW_NTNv = "이탈리아|터키|호주|프랑스"
KW_NTN = joinseq(KW_NTNf, KW_NTNv)

### Organization
KW_NTOf = "Amazon|Google|공군|구글|기관|삼성|아마존|애플|육군|은행|인스타그램|해군"
KW_NTOv = "Microsoft|Tesla|군대|마이크로소프트|발행사|업소|엔비디아|위원회|테슬라|해병대|학교|한라|회사"
KW_NTO = joinseq(KW_NTOf, KW_NTOv)

### Place
KW_NTPf = "공원|공항|광장|극장|기차역|놀이터|선착장|승강장|영화관|주차장|플랫폼"
KW_NTPv = "출입구|항구"
KW_NTP = joinseq(KW_NTPf, KW_NTPv)

### Scenary
KW_NTSf = "그림|[경상시전]황|[국장화]면"
KW_NTSv = "뷰" 
KW_NTS = joinseq(KW_NTSf, KW_NTSv)

### Team
KW_NTTf = "개발|시설|영업|운영|고객 지원|판촉|마케팅"
KW_NTTv = "회계|관리|[노법재총]무|인사|경제"
KW_NTT = joinseq(KW_NTTf, KW_NTTv)

### Usual stuffs
KW_NTUf = "잔|컵|현수막|화투짝"
KW_NTUv = "장대|접시|샴푸"
KW_NTU = joinseq(KW_NTUf, KW_NTUv)

### eVent
KW_NTVf = "개학|생일|월드컵|올림픽"
KW_NTVv = "유세|콘퍼런스|대회|운동회"
KW_NTV = joinseq(KW_NTVf, KW_NTVv)

### can be used with ‘~을(를) 짓다’
KW_NTWf = "말|매듭|일단락|결론|이름|밥|한숨|소설|[보]?약|옷|표정|줄|집|짝|아침"
KW_NTWv = "관계|노래|떼|[마]?무리|농사|미소|시|[중]?죄"
KW_NTW = joinseq(KW_NTWf, KW_NTWv)

### UI/UX
KW_NTXf = "탭|라디오[ ]?버튼|폼"
KW_NTXv = "체크[ ]?박스"
KW_NTX = joinseq(KW_NTXf, KW_NTXv)

### tYpe
KW_NTYf = "문자[열]?형|불[린]?형|숫자형|정수형"
KW_NTY = KW_NTYf

KW_NTf = joinseq(KW_NTAf, KW_NTBf, KW_NTCf, KW_NTDf, KW_NTEf, KW_NTFf, KW_NTGf, KW_NTHf, KW_NTIf, KW_NTJf, KW_NTLf, KW_NTMf, KW_NTNf, KW_NTOf, KW_NTSf, KW_NTTf, KW_NTUf, KW_NTVf, KW_NTWf, KW_NTXf, KW_NTYf)
KW_NTv = joinseq(KW_NTAv, KW_NTBv, KW_NTCv, KW_NTDv, KW_NTEv, KW_NTFv, KW_NTGv, KW_NTHv,          KW_NTJv, KW_NTLv, KW_NTMv, KW_NTNv, KW_NTOv, KW_NTSv, KW_NTTv, KW_NTUv, KW_NTVv, KW_NTWv, KW_NTXv,         )
KW_NT = joinseq(KW_NTf, KW_NTv)

## Nouns - Activity (can be verb with '-하다/-되다' or used in form of '~을/를 하다')
### Original (Korean + Hanja)

#### Intransive
KW_NAOIf1 = "벌|찡|참"
KW_NAOIf2 = "일관|[입출]국|집권|[접출]근|기능|도달|탈락|[운]동|[중후]략|[노]력|[관]련|수렴|소멸|연명|[괄]목|함몰|[재폭]발|체벌|중복|손상|발생|연설|소송|통신|작업|[긴등성출퇴]장|경쟁|산적|[도발회]전|근접|방중|[부승약]진|[면유입재]학|방한|[동비서유]행"
KW_NAOIf3 = "불구경|수소문|하소연"
KW_NAOIf4 = "자리매김"
KW_NAOIf = joinseq(KW_NAOIf1, KW_NAOIf2, KW_NAOIf3, KW_NAOIf4)
KW_NAOIv1 = "묘|화"
KW_NAOIv2 = "[증참]가|[경방]과|붕괴|[경]기|연대|복무|방미|[공식퇴]사|감소|소외|[긴중필]요|합의|주지|[부실]패|저하|[전통]화"
KW_NAOIv4 = "대동소이"
KW_NAOIv = joinseq(KW_NAOIv1, KW_NAOIv2, KW_NAOIv4)
KW_NAOI = joinseq(KW_NAOIf, KW_NAOIv)

#### Transive
KW_NAOTf1 = "곱"
KW_NAOTf2 = "수감|[생착]각|보간|[가증]감|점검|공격|[가동연체]결|[구변]경|[가제]공|[건]국|[총포]괄|송금|[공언지취]급|가늠|[차판]단|[배전]달|[담배해]당|[가기이작]동|[납취획]득|누락|사랑|[생]략|[입출]력|[마수제훈]련|[기수]록|[발변설소작제조증]명|[주지]목|[주질]문|고민|위반|[개선]발|식별|[반]복|구분|[계연]산|[상연향]상|[검수탐]색|[재]생|[분해]석|개선|[건개배증해]설|[구생작완형]성|[계상접]속|[방배전]송|[기저]술|[연학]습|[발송수임]신|의심|[장파]악|[고보제]안|[계예해]약|선언|[수성영작]업|검역|[구시재지]연|[나배사]열|오열|오염|[반운촬투]영|[사응이작적통포허활]용|[교훈]육|[기지]원|[대불]응|[방유]일|통일|[기도수출투]입|[동시조짐]작|[저]장|[누지축]적|[운]전|이전|조절|[가개걱검결규선설수조지추측한확]정|[마]중|검증|증진|[결매모수편]집|[도장부집탈]착|칭찬|제창|[신요]청|[구압]축|[검구누도산수연인제진창추호]출|[계예]측|[강이]탈|[간선채]택|국한|분할|포함|[결부조취]합|[미발수시실운연진]행|[시실]험|[구실재표]현|[반변소전]환|[계구기노]획"
KW_NAOTf3 = "경원시|동일시|등한시|송수신|수출입|시운전|재기동|재실행"
KW_NAOTf = joinseq(KW_NAOTf1, KW_NAOTf2, KW_NAOTf3)
KW_NAOTv1 = "요"
KW_NAOTv2 = "[인추평]가|[공소전]개|[제준탈]거|설계|비교|[복연촉]구|[대분상연제표]기|안내|[임증초확]대|[시유주]도|계류|[고]려|신뢰|[완종치]료|[관격분수정처]리|연마|구매|소모|근무|확보|[공거기발]부|준비|[감반발복수조]사|[기축]소|[감준회]수|[감실제출표]시|제어|[기부참]여|[제]외|[소]요|[논유정주회]의|투자|복제|[변참창]조|[감유의정중차폐]지|[기탑]재|[교대]체|[갈성수탈편]취|[납배설위]치|검토|돌파|배포|발표|보호|[분이화]해"
KW_NAOTv3 = "이야기|[재전후]처리|마무리|금기시|당연시|도외시|등한시|문제시|범죄시|신성시|유력시|중요시|확실시|재정의|재투자"
KW_NAOTv4 = "반신반의"
KW_NAOTv = joinseq(KW_NAOTv1, KW_NAOTv2, KW_NAOTv3, KW_NAOTv4)
KW_NAOT = joinseq(KW_NAOTf, KW_NAOTv)

KW_NAOf1 = joinseq(KW_NAOIf1, KW_NAOTf1)
KW_NAOf2 = joinseq(KW_NAOIf2, KW_NAOTf2)
KW_NAOf3 = joinseq(KW_NAOIf3, KW_NAOTf3)
KW_NAOf4 = KW_NAOIf4
KW_NAOfz = joinseq(KW_NAOf2, KW_NAOf3, KW_NAOf4)
KW_NAOf = joinseq(KW_NAOf1, KW_NAOfz)

KW_NAOh = '|'.join(conjugate("강|미|융|특", '화') + conjugate(ks.KS_Az, '화') + conjugate(KW_NTB, '화'))
KW_NAOv1 = joinseq(KW_NAOIv1, KW_NAOTv1)
KW_NAOv2 = joinseq(KW_NAOIv2, KW_NAOTv2)
KW_NAOv3 = KW_NAOTv3
KW_NAOv4 = joinseq(KW_NAOIv4, KW_NAOTv4)
KW_NAOvz = joinseq(KW_NAOv2, KW_NAOv3, KW_NAOv4)
KW_NAOv = joinseq(KW_NAOv1, KW_NAOvz, KW_NAOh)

KW_NAOz = joinseq(KW_NAOfz, KW_NAOvz)
KW_NAO = joinseq(KW_NAOf, KW_NAOv)

#### can be Both of active(-하다) and passive(-받다)
KW_NABf = "비난|감동|처단|할당|[입출]력|주목|처방|[처]?벌|축복|상속|전송|제안|교육|환영|구원|[승확]인|위임|대입|연장|판정|강종|칭찬|추천|신청|부탁|선택|심판|반환|시험"
KW_NABv = "용서|계시|강요|기부|보조|오해"
KW_NAB = joinseq(KW_NABf, KW_NABv)

### derived from Foreign language
# Don't use '*팅' instead of '부팅' for case like: 디스켓으로부팅한후 --> 디스켓으로 부팅한 후
KW_NAFf1 = "[킥킵핑]"
KW_NAFf2 = "\\w{1}[깅닝딩링밍션싱징킹팅핑]|게임|클릭"  
KW_NAFf3 = "\\w{2}[깅닝딩링밍션싱징킹팅핑]|임베딩|렌더링|로그인|컨트롤|컴파일"
KW_NAFf4 = "\\w{3}[깅닝딩링밍션싱징킹팅핑]|로그아웃"
KW_NAFf5 = "\\w{4}[깅닝딩링밍션싱징킹팅핑]"
KW_NAFf6 = "\\w{5}[깅닝딩링밍션싱징킹팅핑]"
KW_NAFf7 = "\\w{6}[깅닝딩링밍션싱징킹팅핑]"
KW_NAFfz = joinseq(KW_NAFf2, KW_NAFf3, KW_NAFf4, KW_NAFf5, KW_NAFf6)
KW_NAFf = joinseq(KW_NAFf1, KW_NAFfz)

KW_NAFv2 = "빌드|폴로|메모|캐시|링크"
KW_NAFv3 = "트리거|업로드|릴리스|팔로우|플레이|마사지|마운트|시프트|임포트|카운트|테스트"
KW_NAFv4 = "다운로드|리사이즈|노코멘트|언마운트|업데이트"
KW_NAFv5 = "다운사이즈|로컬라이즈"
KW_NAFv6 = "커스터마이즈"
KW_NAFvz = joinseq(KW_NAFv2, KW_NAFv3, KW_NAFv4, KW_NAFv5, KW_NAFv6)
KW_NAFv = KW_NAFvz

KW_NAF1 = KW_NAFf1
KW_NAFz = joinseq(KW_NAFfz, KW_NAFvz)
KW_NAF = joinseq(KW_NAFf, KW_NAFv)

KW_NAHf = joinseq(KW_NABf, KW_NAFf, KW_NAOf)
KW_NAHv = joinseq(KW_NABv, KW_NAFv, KW_NAOv)
KW_NAH = joinseq(KW_NAHf, KW_NAHv)

### abstract(like Emotion), can be used with ‘-받다’
KW_NAEf = "각광|고난|고통|눈총|미움|버림|벌|복|사랑|영향"
KW_NAEv = "상처|죄"
KW_NAE = joinseq(KW_NAEf, KW_NAEv)

KW_NAf = joinseq(KW_NAFf, KW_NAOf)
KW_NAv = joinseq(KW_NAFv, KW_NAOv)
KW_NAz = joinseq(KW_NAFz, KW_NAOz)
KW_NA = joinseq(KW_NAf, KW_NAv)


## Noun phrases listed in 우리말샘
## Consisting of a common noun and an active noun

### Cannot be affixed directly with '-하다'
### Use with '(-을/를) 하다'
### When you omit josa, use with space like '~ 하다' 
KW_NXf = "보충 학습|자율 학습|복수 지원"
KW_NXv = "학습 지도|군 복무"
KW_NX = joinseq(KW_NXf, KW_NXv)

### Uncertain whether can be affixed with '-하다'
KW_NYf = "보충학습|자율학습|고객지원|교차지원|수시지원"
KW_NYv = "학습지도|군복무"
KW_NY = joinseq(KW_NYf, KW_NYv)


## Nouns - Color
KW_NC = "녹색"

## Nouns - Dependant
KW_ND = "것|밖|뿐"

## Nouns - Person
### by Existance
KW_NPEf = "사람|인[간물]"
KW_NPEv = "인류"

### Family name
KW_NPFf = "김|박|정|강|윤|장|임|한|신|권|황|안|송|류|전|홍|문|양|손|백|남|심|곽|성|민|진|엄|원|천|방|공|현|함|변|염|석|선|설|길|연|명|반|왕|금|옥|육|인|맹|남궁|탁|국|은|편|용|예|경|봉|황보|복|목|형|두|감|제갈|음|빈|동|온|사공|호|범|선우|팽|승|간|상|갈|서문|단|견|당|화|창|옹|순|빙|종|풍|엽|궁|평|독고|랑|판|로|궉|동방|묵|근|점|탄|만|필|돈|운|곡|섭|담|뢰|학|총|삼|독|관|영|등|란|산|증|난|망절|어금|무본|번|완|등정|탕|황목"
KW_NPFv = "이|최|조|오|서|고|배|허|유|노|하|차|주|우|구|라|지|채|여|추|도|소|마|위|기|표|제|모|어|사|가|부|태|계|피|좌|시|대|아|내|매|초|해|야|자|포|후|수|나|요|애|묘|미|비|무|교|다|보"
KW_NPF = joinseq(KW_NPFf, KW_NPFv)

### by biological or phisical conditioN
KW_NPNf = "[비]?장애인|어른|소년"
KW_NPNv = "어린이|감염자|[고남여병환]자|[동양이]성애자|바보|아기|아이"
KW_NPN = joinseq(KW_NPNf, KW_NPNv)

### by Job title or membership
KW_NPJf = "감독[관]?[님]?|강사님|[과대부팀회]장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|마을 사람|[사의]원|[사소의회]장[님]?|시인|작[곡사]?가님|정치인|직장인|고교생|[대중]?학생|초등학생|[수해]병|이사장|초대 회장|회사원|군인|경찰|동호인"
KW_NPJv = "프로그래머|간호사|[강검의판]사|과학자|교[사수]|대[리표]|작[곡사]?가|전문가|개발자|데이터[ ]?분석가"
KW_NPJ = joinseq(KW_NPJf, KW_NPJv)

### by ranK
KW_NPKf = "[경병부차]장[님]?|[상이일]병|[대중소준][령장]|사령관|경찰청장"
KW_NPKv = "경[사위]|[대중소준][위좌]|[상중하]사|장교|통수권자"

### by social Relation
KW_NPRf = "아들|아저씨|동문|조상|자손|식솔|[처]?자식|[부장]인|동창|[일사삼오육칠팔]촌|남편"
KW_NPRv = "[식친]구|처남|자녀|아내|아주머니|[어할]머니|아줌마|엄마|[고대부이]모|동료|며느리|[대형]부|아빠|[제형]수|아저씨|애인|사위|저|[자처형]제|[할]?아버지|제부|처형"
KW_NPR = joinseq(KW_NPRf, KW_NPRv)

### by Activity, accident, crime
KW_NPAf = "거지|고객|손님|애[견묘]인|[증행]인"
KW_NPAv = "수집가|애호가|프로|아마추어|글쓴이|엮은이|지은이|감[독시]자|강[연의]자|관[계련찰]자|당[사직]자|반[려역]자|발[제표]자|[사이]용자|소유자|운전자|응시자|[원]작자|제공자|참[가관석여]자|투자자|협력자|[가피]해자|팬"
KW_NPA = joinseq(KW_NPAf, KW_NPAv)

### all
KW_NPf = joinseq(KW_NPEf, KW_NPFf, KW_NPNf, KW_NPJf, KW_NPKf, KW_NPRf, KW_NPAf)
KW_NPv = joinseq(KW_NPEv, KW_NPFv, KW_NPNv, KW_NPJv, KW_NPKv, KW_NPRv, KW_NPAv)
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
KW_NUAf = "건|번"
KW_NUAv = "뭉치|회"
KW_NUA = joinseq(KW_NUAf, KW_NUAv)

### Book
KW_NUBf = "글자|단어|단원|문|문장|장|절|줄|항|행"
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
KW_NUSf = "그릇|권|달|명|방울|벌|병|쌍|장|줄|쪽|통"
KW_NUSv = "가지|개|구|마리|박스|봉지|채|페이지"
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
        ["느낀", "다룬", "배운"]
        + conjugate(KW_NAO, '된')
    )
)
KW_MV = joinseq(KW_MVl, KW_MVn)

KW_M = joinseq(KW_MD, KW_MV, KW_MA)


## Pronouns
### Person
KW_PPf = "당신|여러분"
KW_PPv = "[너저][희]?|내|우리"
KW_PP = joinseq(KW_PPf, KW_PPv)

### Thing
KW_PTf = "[그이저]것"
KW_PTv = "[그이저]"
KW_PT = joinseq(KW_PTf, KW_PTv)

### all
KW_P = joinseq(KW_PP, KW_PT)

## Verb

### Active
### Did
KW_VADw = '|'.join(
    sorted(
        conjugate(ks.KS_VAw, '웠다')     # 키 + 웠다
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

## Transive(타동)
### by using Causative(사동)

#### -추
KW_VTCc = '|'.join(
    sorted(
        conjugate(ks.KS_VCc, '추')
    )
)

#### -기
KW_VTCg = '|'.join(
    sorted(
        conjugate(ks.KS_VCf, '기')
        + conjugate(ks.KS_VCg, '기')
    )
)

#### -히
KW_VTCh = '|'.join(
    sorted(
        conjugate(ks.KS_VCh, '히')
    )
)

#### -이
KW_VTCi = '|'.join(
    sorted(
        conjugate(ks.KS_VCi, '이')
        + conjugate(ks.KS_VCj, '이')
        + conjugate(ks.KS_VCe, '이')
        + conjugate(ks.KS_VCr, 'ㄹ', '이')
    )
)

#### -구
KW_VTCk = '|'.join(
    sorted(
        conjugate(ks.KS_VCk, '구')
    )
)

#### -리
KW_VTCl = '|'.join(
    sorted(
        conjugate(ks.KS_VCl, 'ㄹ', '리')
        + conjugate(ks.KS_VCm, 'ㄹ', '리')
    )
)

#### -우
KW_VTCu = '|'.join(
    sorted(
        conjugate(ks.KS_VCu, '우')
    )
)

KW_VTC = joinseq(KW_VTCc, KW_VTCg, KW_VTCh, KW_VTCi, KW_VTCk, KW_VTCl, KW_VTCu)

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
