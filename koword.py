import kostr


def concat(*s):
    return "|".join(s).strip('|')


# S: Stem(어간) (dropped variable final consonant) 
# can be modified to predicate(좋다), AVC(좋아서), AVM(좋게), adjective(좋은)
KW_Sa = '나ㅃ|바ㅃ'  # 나쁘다, 나빠서, 나쁘게, 나쁜
KW_Sb = '귀여|해로'  # 귀엽다, 귀여워서, 귀엽게, 귀여운
KW_Sd = '다' # 달다, 달아서, 달게, 단
KW_Se = '예ㅃ'  # 예쁘다, 예뻐서, 예쁘게, 예쁜
KW_Sg = '착'  # 착하다, 착해서, 착하게, 착한
KW_Sj = '낮|높|좋' # 낮다, 낮아서, 낮게, 낮은
KW_Sl = '섣부' # 섣부르다, 섣불러서, 섣불리, 섣부른
KW_Sn= '낯서' # 낯설다, 낯설어서, 낯설게, 낯선
KW_Ss = '나'  # 낫다, 나아서, 낫게, 나은 
KW_Sx = 'ㅆ|ㅋ' # 쓰다, 써서, 쓰게, 쓴

# AdVerb - Cause (이유를 나타내는 부사)
KW_AVC = '|'.join(sorted(
        [kostr.concat(w, 'ㅏ', '서') for w in KW_Sa.split('|')]
        + [kostr.concat(w, '워', '서') for w in KW_Sb.split('|')]
        + [kostr.concat(w, 'ㄹ', '아서') for w in KW_Sd.split('|')]
        + [kostr.concat(w, 'ㅓ', '서') for w in KW_Se.split('|')]
        + [kostr.concat(w, '해서') for w in KW_Sg.split('|')]
        + [kostr.concat(w, '아서') for w in KW_Sj.split('|')]
        + [kostr.concat(w, 'ㄹ', '러서') for w in KW_Sl.split('|')]
        + [kostr.concat(w, 'ㄹ', '어서') for w in KW_Sn.split('|')]
        + [kostr.concat(w, '아서') for w in KW_Ss.split('|')]
        + [kostr.concat(w, 'ㅓ', '서') for w in KW_Sx.split('|')]
        ))

# Adverb - Manner (태도, 방법을 나타내는 부사)
KW_AVM = '|'.join(
    sorted(
        ['함부로']
        + [kostr.concat(w, 'ㅡ', '게') for w in KW_Sa.split('|')]
        + [kostr.concat(w, 'ㅂ', '게') for w in KW_Sb.split('|')]
        + [kostr.concat(w, 'ㄹ', '게') for w in KW_Sd.split('|')]
        + [kostr.concat(w, 'ㅡ', '게') for w in KW_Se.split('|')]
        + [kostr.concat(w, '하', '게') for w in KW_Sg.split('|')]
        + [kostr.concat(w, '게') for w in KW_Sj.split('|')]
        + [kostr.concat(w, 'ㄹ', '리') for w in KW_Sl.split('|')]
        + [kostr.concat(w, 'ㄹ', '게') for w in KW_Sn.split('|')]
        + [kostr.concat(w, 'ㅅ', '게') for w in KW_Ss.split('|')]
        + [kostr.concat(w, 'ㅡ', '게') for w in KW_Sx.split('|')]
    )
)

KW_AV = concat(KW_AVC, KW_AVM)

# Adjective (형용사)
KW_ADJ = '|'.join(
    sorted(
        [kostr.concat(w, 'ㅡ', 'ㄴ') for w in KW_Sa.split('|')]
        + [kostr.concat(w, '운') for w in KW_Sb.split('|')]
        + [kostr.concat(w, 'ㄴ') for w in KW_Sd.split('|')]
        + [kostr.concat(w, 'ㅡ', 'ㄴ') for w in KW_Se.split('|')]
        + [kostr.concat(w, '한') for w in KW_Sg.split('|')]
        + [kostr.concat(w, '은') for w in KW_Sj.split('|')]
        + [kostr.concat(w, '른') for w in KW_Sl.split('|')]
        + [kostr.concat(w, 'ㄴ') for w in KW_Sn.split('|')]
        + [kostr.concat(w, 'ㅡ', 'ㄴ') for w in KW_Sx.split('|')]
        + [kostr.concat(w, '은') for w in KW_Ss.split('|')]
    )
)

# https://jojal-jojalkorean.tumblr.com/post/623900718717452288/korean-grammar-final-ending%EC%96%B4%EB%A7%90-%EC%96%B4%EB%AF%B8
# Eomi - Final - Statement
KW_EFS = "다\\b|습니다|이다"

# Eomi - Final - Question 
KW_EFQ = "나\\b|니\\b|는가\\b"

# Eomi - Final - Order
KW_EFO = "라\\b|거라\\b"

# Eomi - Final - Request
KW_EFR = "자\\b|세\\b"

# Eomi - Final - Exclamination
KW_EFE = "구나\\b|세\\b"

# Eomi - Final(종결 어미)
KW_EF = concat(KW_EFS, KW_EFQ, KW_EFO, KW_EFR, KW_EFE)

# Eomi - Conjunction - Coordinate
KW_ECC = "고\\b|으며\\b|며\\b"

# Eomi - Conjunction - Subordinate
KW_ECS = "[으]면|[으]므로"

# Eomi - Conjunction - Auxiliary
KW_ECA = "게\\b|지\\b|어\\b"

# Eomi - Conjunctive(연결 어미)
KW_EC = concat(KW_ECC, KW_ECS, KW_ECA)

# Eomi - Derivational/Modifier - Noun
KW_EDN = "기\\b|음\\b|ㅁ\\b"

# Eomi - Derivational/Modifier - Adnominal
KW_EDA = "은\\b|ㄴ\\b|을\\b|ㄹ\\b"

# Eomi - Derivational/Modifier - adVerbial
KW_EDV = "도록|게\\b"

# Eomi - Derivational/Modifier (전성 어미)
KW_ED = concat(KW_EDN, KW_EDA, KW_EDV)

# Eomi - Ending(어말 어미)
KW_E = concat(KW_EF, KW_EC, KW_ED)

# Eomi - Pre-final(선어말어미)
KW_PF = "시|었|더|겠"

# http://90daykorean.com/korean-particles/

# particle (Josa) - Additive
KW_JA = "도\\b"

# particle (Josa) - possesive ("oF")
KW_JF = "의\\b"

# particle (Josa) - Giving
KW_JG = "께|에게|한테"

# Particle (Josa) - LinKing
KW_JK = "와\\b|과\\b|이랑|랑\\b|하고|고\\b"

# particle (Josa) - Location
KW_JL = "에\\b|에서|부터|으로|로\\b|에\\b|까지"

# particle (Josa) - Plural (More than one)
KW_JM = "들"

# particle (Josa) - Object
KW_JO = "을\\b|를\\b"

# particle (Josa) - Subject
KW_JS = "이\\b|가\\b"

# particle (Josa) - Topic marker
KW_JT = "은\\b|는\\b"

# particle (Josa) - only (Unique)
KW_JU = "만"

# particle (Josa) - adVerb
KW_JV = "고|라고|보다|에게|에로|에서|와|으로서|으로써"


### activity nouns (which can be followed by both '~하다(hada)' and '~을/를 하다')

# NAO: activity nouns (original Korean)
KW_NAOf = "[가증]감|곱|[건입]국|[연체]결|[총포]괄|[담배]당|[노입출]력|[수제훈]련|[기수]록|[개선]발|[구작형]성|[연학]습|[지]원|[반운투]영|[사이적포활]용|[교훈]육|수[출]?입|[결설수한]정|선언|선정|제창|수출|선택|[동수실연]행|[면입]학|포함|[결취]합|[구실재]현|"  # f: has final consonant
KW_NAOv = "참가|[연]구|제기|[고]려|치료|처리|연마|[공기]부|[반발조]사|[개배증해]설|[기참]여|[논합]의|[성]취|[배설]치"  # v: ends with vowel (does not have final consonant)
KW_NAO = concat(KW_NAOf, KW_NAOv)

# NAF: activity noun derived from foreign language
KW_NAFf = "게임|로깅|모니터링"
KW_NAFv = "마사지"
KW_NAF = concat(KW_NAFf, KW_NAFv)

# NAT: all activity nouns
KW_NATf = concat(KW_NAOf, KW_NAFf)
KW_NATv = concat(KW_NAOv, KW_NAFv)
KW_NAT = concat(KW_NATf, KW_NATv)

# NST: status nouns
KW_NSTf = "건강|긴장|동일|둔감|민감|병약|불성실|성실|함몰"
KW_NSTv = "상이"
KW_NST = concat(KW_NSTf, KW_NSTv)

# NAS: activity nouns + status nouns
KW_NASf = concat(KW_NATf, KW_NSTf)
KW_NASv = concat(KW_NATv, KW_NSTv)
KW_NAS = concat(KW_NASf, KW_NASv)

# ND: Nouns - Dependant
KW_ND = "밖|뿐"

# NPE: nouns - person by Existance
KW_NPEf = "사람|인[간물]"
KW_NPEv = "인류"

#  NPN: nouns - person by biological or phisical conditioN
KW_NPNf = "[비]?장애인|어른"
KW_NPNv = "감염자|[고남여병환]자|[동양이]성애자|바보|아기"

# NPJ: nouns - person by Job title or membership
KW_NPJf = "감독[관]?[님]?|강사님|과장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|사원|[사소의회]장[님]?|시인|작[곡사]?가님|직장인|학생|[수해]병|초대 회장|회사원"
KW_NPJv = "강사|교[사수]|대[리표]|작[곡사]?가"
KW_NPJ = concat(KW_NPJf, KW_NPJv)

# NPK: nouns - person by ranK
NW_NPKf = "[경병부차]장[님]?|[상이일]병|[대중소준][령장]|사령관|통수권자"
NW_NPKv = "경[사위]|[대중소준][위좌]|[상중하]사"

# NPR: nouns - person by social Relation
KW_NPRf = "아들|동문|조상|자손|식솔|[처]자식|[부장]인|자제|동창|[일사삼오육칠팔]촌|남편"
KW_NPRv = "[식친]구|처남|자녀|아내|아주머니|[어할]머니|아줌마|엄마|[고대부이]모|동료|며느리|[대형]부|아빠|[제형]수|아저씨|애인|사위|저|[처형]제|[할]아버지|제부|처형"

# NPA: nouns - person by Activity
KW_NPAf = "군인|경찰|동호인|애[견묘]인|[증행]인"
KW_NPAv = "감독자|감시자|강[연의]자|관[계련찰]자|글쓴이|당[사직]자|반[려역]자|발[제표]자|수집가|아마추어|엮은이|애호가|응시자|[원]작자|지은이|프로|협력자"

# NPS: nouns - person
KW_NPSf = concat(KW_NPEf, KW_NPNf, KW_NPJf, KW_NPRf, KW_NPAf)
KW_NPSv = concat(KW_NPEv, KW_NPNv, KW_NPJv, KW_NPRv, KW_NPAv)
KW_NPS = concat(KW_NPSf, KW_NPSv)

# NNC: Nouns - Number - derived from Chinese
KW_NNCf = "일|삼|육|칠|팔"
KW_NNCv = "이|사|오|구"
KW_NNC = concat(KW_NNCf, KW_NNCv)

## NND: Nouns - Number - positional value in Decimal system
KW_NNDf = "[십백천만억경]"
KW_NNDv = "조"
KW_NND = concat(KW_NNDf, KW_NNDv)

## NNM: Nouns - Number - Arabic
KW_NNA = "[1-9]?[0-9,]*"

## NNM: Nouns - Number - Mixed
KW_NNMf = KW_NNA + KW_NNDf
KW_NNMv = KW_NNA + KW_NNDv
KW_NNM = concat(KW_NNMf, KW_NNMv)

# NNK: nouns - Number - pure Korean
KW_NNKf = '|'.join(
    [
        x + y
        for x in [''] + "열|스물|서른|마흔|쉰|예순|일흔|여든|아흔".split('|')
        for y in [''] + "한|둘|석|셋|넉|넷|다섯|댓|여섯|일곱|여덟|아홉".split('|')
    ]
).strip('|')

KW_NNKv = '|'.join(
    [
        x + y
        for x in [''] + "열|스물|서른|마흔|쉰|예순|일흔|여든|아흔".split('|')
        for y in "하나|두|세|네".split('|')
    ]
).strip('|')

KW_NNK = concat(KW_NNKf, KW_NNKv)

KW_NN = concat(KW_NNC, KW_NND, KW_NNK)   

# NUS: Nouns - Units - Stuff 
KW_NUSF = "그릇|달|명|방울|벌|시간|쪽"
KW_NUSV = "가지|마리|박스|봉지|채|페이지|회"
KW_NUS = concat(KW_NUSF, KW_NUSV)

# NUT: Nouns - Units - Time
KW_NUTF = "분|시간|일|달|개월|년|세기"
KW_NUTV = "밀리초|초"
KW_NUT = concat(KW_NUTF, KW_NUTV)

# NUD: Nouns - Units - Distance
KW_NUDF = "광년"
KW_NUDV = "미터|킬로미터"
KW_NUD = concat(KW_NUDF, KW_NUDV)

# NU: nouns - Units - Weight
KW_NUWF = "그램|킬로그램|평"
KW_NUWV = "밀리리터|데시리터|리터|킬로리터|파운드"
KW_NUW = concat(KW_NUWF, KW_NUWV)

# NUG: Nouns - Units - weiGht in symbol
KW_NUGF = "[mk]?g" 
KW_NUGV = "[k]?[LlMm]"
KW_NUG = concat(KW_NUGF, KW_NUGV)

# NU: Nouns - Units - aRea
KW_NURF = "평"
KW_NURV = "제곱미터|평방미터"
KW_NUR = concat(KW_NURF, KW_NURV)

# NUV: Nouns - Units - Volume
KW_NUVF = ""
KW_NUVV = "세제곱미터"
KW_NUV = concat(KW_NUVF, KW_NUVV)

KW_NU = concat(KW_NUS, KW_NUT, KW_NUD, KW_NUW, KW_NUG, KW_NUR, KW_NUV)

# NL: nouns - animaL - Domestic
KW_NLDF = "말" 
KW_NLDV = "개|고양이|돼지|소|오리" 
KW_NLD = concat(KW_NLDF, KW_NLDV)

# NL: nouns - animaL - Insects
KW_NLIF = "개미|딱정벌레|지네"
KW_NLIV = "[꿀]벌|[여]왕벌"
KW_NLI = concat(KW_NLIF, KW_NLIV)


# PR: Pronouns - Person
KW_PRP = "너희|내|우리|저희"
KW_PRN = KW_PRP

# verb: roots of verb -- these are not nouns
KW_VRB = "걸|갈|나누|넣|말|박|빼|졸|숨|재"

# verb: transive
KW_VTG = "[당숨]"  # ~기다(gida)
KW_VTL = "[되][돌살]|[쳐]올|[내때]"  # ~리다(lida)
KW_VTI = "[드]높|[보죽]|되뇌" # ~이다(ida)
KW_VTP = "[보]살피다"  # ~피다(pida)
KW_VTC = "[내망외]"  # ~치다(chida)
KW_VTX = "[낮늦]"  # ~추다(chuda)
KW_VTW = "[치채]"  # ~우다(wuda)
KW_VTD = "[받쳐]들다|[내]밀다|[박빨쪼찍]다" # ~다(da)

# verb: intransive
KW_VII = "숨죽이다"  # ~이다(ida)
KW_VID = "[살죽]다"  # ~다(da)

# verb: passive
KW_VPL = "갈리다"  # ends with '~리다(lida)'
KW_VPI = "쓰이다"  # ends with '~이다(ida)'
KW_VPH = "먹|붙잡|잡"  # ends with '~히다(hida)'



