import kostr


def concat(*s):
    return "|".join(s).strip('|')

# R: root(어근)
KW_Sh = '깔끔|매끈|복잡|비슷|착|지저분'   # -하다, -해서, -한, -하다
KW_Sg = '야물' # -거리다, -거려서, -거리는, -거린다
KW_S = concat(KW_Sh, KW_Sg)

# A: Adjective (removed final consonant which will be dropped during conjugatation)
# can be conjugated to                    VS,             AS,         AVC,          AVM,        AVN,        ASN
KW_Aa = '나ㅃ|바ㅃ'                     # 나ㅃ+ㅏ지다,    나ㅃ+ㅡ+다, 나ㅃ+ㅏ서,    나ㅃ+ㅡ+게, 나ㅃ+ㅡ+지, 나ㅃ+ㅡ+ㄴ
KW_Ab = '귀여|더|무서|쉬|차가|추|해로'  # 귀여+워지다,    귀여+ㅂ+다, 귀여+워서,    귀여+ㅂ+게, 귀여+ㅂ+지, 귀여+운
KW_Ac = '맑'                            # 맑+아지다,      맑+다,      맑+아서,      맑+게,      맑+지,      맑+은
KW_Ad = '다'            # sweet         # 다+ㄹ+아지다,   다+ㄹ+다,   다+ㄹ+아서,   다+ㄹ+게,   다+ㄹ+지,   다+ㄴ
KW_Ae = '예ㅃ'                          # 예ㅃ+ㅓ지다,    예ㅃ+ㅡ+다, 예ㅃ+ㅓ서,    예ㅃ+ㅡ+게, 예ㅃ+ㅡ+지, 예ㅃ+ㅡ+ㄴ
KW_Af = '다'            # different     # 다+ㄹ+라지다,   다+르+다,   다+ㄹ+라서,   다+르+게,   다+르+지,   다+른
KW_Ai = '붉'                            # 붉+어지다,      붉+다,      붉+어서,      붉+게,      붉+지,      붉+은
KW_Aj = '같|괜찮|낮|높|좋'              # 같+아지다,      같+다,      같+아서,      같+게,      같+지,      같+은
KW_Al = '섣부'                          # x,              섣부+르다,  섣부+ㄹ+러서, 섣부+르게,  섣부+르지,  섣부+른
KW_Am = '맛있'                          # 맛있+어지다,    맛있+다,    맛있+어서,    맛있+게,    맛있+지,    맛있+는
KW_An = '낯서|머'                       # 머+ㄹ+어지다,   머+ㄹ+다,   머+ㄹ+어서,   머+ㄹ+게,   머+ㄹ+지,   머+ㄴ
KW_Ao = '넓'                            # 넓+어지다,      넓+다,      넓+어서,      넓+게,      넓+지,      넓+은
KW_Ap = '희'                            # 희+어지다,      희+다,      희+어서,      희+게,      희+지,      희+ㄴ
KW_Ar = '이로|평화로'                   # 이로+와지다,    이로+ㅂ+다, 이로+와서,    이로+ㅂ+게, 이로+ㅂ+지, 이로+운
KW_As = '나'                            # 나+아지다,      나+ㅅ+다,   나+아서,      나+ㅅ+게,   나+ㅅ+지,   나+은 
KW_Aw = '고'                            # 고+와지다,      고+ㅂ+다,   고+와서,      고+ㅂ+게,   고+ㅂ+지,   고+은
KW_Ax = 'ㅆ|ㅋ'                         # ㅆ+ㅓ+지다,     ㅆ+ㅡ+다,   ㅆ+ㅓ+서,     ㅆ+ㅡ+게,   ㅆ+ㅡ+지,   ㅆ+ㅡ+ㄴ
KW_Ay = '못ㄷ'                          # 못ㄷ+ㅙ+지다,   못ㄷ+ㅚ+다, 못ㄷ+ㅙ+서,   못ㄷ+ㅚ+게, 못ㄷ+ㅚ+지, 못ㄷ+ㅚㄴ

# Adjective - Status
KW_AS = '|'.join(sorted(
        [kostr.concat(w, '해') for w in KW_Sh.split('|')]  # 착+해(지다)      
        + [kostr.concat(w, 'ㅏ') for w in KW_Aa.split('|')]  # 나ㅃ+ㅏ(지다) 
        + [kostr.concat(w, '워') for w in KW_Ab.split('|')]  # 귀여+워(지다)    
        + [kostr.concat(w, '아') for w in KW_Ac.split('|')]  # 맑+아(지다)   
        + [kostr.concat(w, 'ㄹ', '아') for w in KW_Ad.split('|')]  # 다+ㄹ+아(지다)   
        + [kostr.concat(w, 'ㅓ') for w in KW_Ae.split('|')]  # 예ㅃ+ㅓ(지다)    
        + [kostr.concat(w, 'ㄹ', '라') for w in KW_Af.split('|')]  # 다+ㄹ+라(지다)    
        + [kostr.concat(w, '어') for w in KW_Ai.split('|')]    # 붉+어(지다)      
        + [kostr.concat(w, '아') for w in KW_Aj.split('|')]    # 낮+아(지다)      
        + [kostr.concat(w, '어') for w in KW_Am.split('|')]  # 맛있+어(지다) 
        + [kostr.concat(w, 'ㄹ', '어') for w in KW_An.split('|')]  # 머+ㄹ+어(지다) 
        + [kostr.concat(w, '어') for w in KW_Ao.split('|')]  # 넓+어(지다) 
        + [kostr.concat(w, '어') for w in KW_Ap.split('|')]  # 희+어(지다) 
        + [kostr.concat(w, '와') for w in KW_Ar.split('|')]  # 이로+와(지다)      
        + [kostr.concat(w, '아') for w in KW_As.split('|')]  # 나+아(지다)      
        + [kostr.concat(w, '와') for w in KW_Aw.split('|')]  # 고+와(지다)      
        + [kostr.concat(w, 'ㅓ') for w in KW_Ax.split('|')]  # ㅆ+ㅓ+(지다)     
        + [kostr.concat(w, 'ㅙ') for w in KW_Ay.split('|')]  # 못ㄷ+ㅙ+(지다)   
        ))


# Adjective - Status - modifies Noun (형용사의 관형사형)
KW_ASN = '|'.join(
    sorted(
        [kostr.concat(w, '한') for w in KW_Sh.split('|')]
        + [kostr.concat(w, 'ㅡ', 'ㄴ') for w in KW_Aa.split('|')]
        + [kostr.concat(w, '운') for w in KW_Ab.split('|')]
        + [kostr.concat(w, '은') for w in KW_Ac.split('|')]  # 맑+은
        + [kostr.concat(w, 'ㄴ') for w in KW_Ad.split('|')]  # 다+ㄴ
        + [kostr.concat(w, 'ㅡ', 'ㄴ') for w in KW_Ae.split('|')]
        + [kostr.concat(w, '른') for w in KW_Af.split('|')]  # 다+른
        + [kostr.concat(w, '은') for w in KW_Ai.split('|')]
        + [kostr.concat(w, '은') for w in KW_Aj.split('|')]
        + [kostr.concat(w, '른') for w in KW_Al.split('|')]  # 섣부+른
        + [kostr.concat(w, '는') for w in KW_Am.split('|')]
        + [kostr.concat(w, 'ㄴ') for w in KW_An.split('|')]  # 머+ㄴ
        + [kostr.concat(w, '은') for w in KW_Ao.split('|')]
        + [kostr.concat(w, 'ㄴ') for w in KW_Ap.split('|')]
        + [kostr.concat(w, '운') for w in KW_Aw.split('|')]
        + [kostr.concat(w, '은') for w in KW_As.split('|')]
        + [kostr.concat(w, '은') for w in KW_Aw.split('|')]
        + [kostr.concat(w, 'ㅡ', 'ㄴ') for w in KW_Ax.split('|')]
        + [kostr.concat(w, 'ㅚ', 'ㄴ') for w in KW_Ay.split('|')]
    )
)

# AdVerb - Cause (이유를 나타내는 부사)
KW_AVC = '|'.join(sorted(
        [kostr.concat(w, '해서') for w in KW_Sh.split('|')]
        + [kostr.concat(w, 'ㅏ', '서') for w in KW_Aa.split('|')]
        + [kostr.concat(w, '워서') for w in KW_Ab.split('|')]
        + [kostr.concat(w, '아서') for w in KW_Ac.split('|')]  # 맑+아서
        + [kostr.concat(w, 'ㄹ', '아서') for w in KW_Ad.split('|')]  # 다+ㄹ+아서
        + [kostr.concat(w, 'ㅓ', '서') for w in KW_Ae.split('|')]
        + [kostr.concat(w, 'ㄹ', '라서') for w in KW_Af.split('|')]  # 다+ㄹ+라서
        + [kostr.concat(w, '어서') for w in KW_Ai.split('|')]
        + [kostr.concat(w, '아서') for w in KW_Aj.split('|')]
        + [kostr.concat(w, 'ㄹ', '러서') for w in KW_Al.split('|')]  # 섣부+ㄹ+러서
        + [kostr.concat(w, 'ㄹ', '어서') for w in KW_An.split('|')]  # 머+ㄹ+어서
        + [kostr.concat(w, '어서') for w in KW_Ao.split('|')]
        + [kostr.concat(w, '어서') for w in KW_Ap.split('|')]
        + [kostr.concat(w, '와서') for w in KW_Ar.split('|')]
        + [kostr.concat(w, '아서') for w in KW_As.split('|')]
        + [kostr.concat(w, '와서') for w in KW_Aw.split('|')]
        + [kostr.concat(w, 'ㅓ', '서') for w in KW_Ax.split('|')]
        + [kostr.concat(w, 'ㅙ', '서') for w in KW_Ay.split('|')]
        ))

# Adverb - Manner (태도, 방법을 나타내는 부사)
KW_AVM = '|'.join(
    sorted(
        ['함부로']
        + [kostr.concat(w, '하게') for w in KW_Sh.split('|')]
        + [kostr.concat(w, 'ㅡ', '게') for w in KW_Aa.split('|')]
        + [kostr.concat(w, 'ㅂ', '게') for w in KW_Ab.split('|')]
        + [kostr.concat(w, '게') for w in KW_Ac.split('|')]  # 맑+게
        + [kostr.concat(w, 'ㄹ', '게') for w in KW_Ad.split('|')]  # 다+ㄹ+게
        + [kostr.concat(w, 'ㅡ', '게') for w in KW_Ae.split('|')]
        + [kostr.concat(w, '르게') for w in KW_Af.split('|')]  # 다+르게
        + [kostr.concat(w, '게') for w in KW_Ai.split('|')]
        + [kostr.concat(w, '게') for w in KW_Aj.split('|')]
        + [kostr.concat(w, '르게') for w in KW_Al.split('|')]  # 섣부+르게
        + [kostr.concat(w, 'ㄹ', '게') for w in KW_An.split('|')]  # 머+ㄹ+게
        + [kostr.concat(w, '게') for w in KW_Ao.split('|')]
        + [kostr.concat(w, '게') for w in KW_Ap.split('|')]
        + [kostr.concat(w, 'ㅂ', '게') for w in KW_Ar.split('|')]
        + [kostr.concat(w, 'ㅅ', '게') for w in KW_As.split('|')]
        + [kostr.concat(w, 'ㅂ', '게') for w in KW_Aw.split('|')]
        + [kostr.concat(w, 'ㅡ', '게') for w in KW_Ax.split('|')]
        + [kostr.concat(w, 'ㅚ', '게') for w in KW_Ay.split('|')]
    )
)

# Adverb - Negative 
KW_AVN = '|'.join(
    sorted(
        [kostr.concat(w, '하지') for w in KW_Sh.split('|')]
        + [kostr.concat(w, 'ㅡ', '지') for w in KW_Aa.split('|')]
        + [kostr.concat(w, 'ㅂ', '지') for w in KW_Ab.split('|')]
        + [kostr.concat(w, '지') for w in KW_Ac.split('|')]  # 맑+지
        + [kostr.concat(w, 'ㄹ', '지') for w in KW_Ad.split('|')]  # 다+ㄹ+지
        + [kostr.concat(w, 'ㅡ', '지') for w in KW_Ae.split('|')]
        + [kostr.concat(w, '르지') for w in KW_Af.split('|')]  # 다+르지
        + [kostr.concat(w, '지') for w in KW_Ai.split('|')]
        + [kostr.concat(w, '지') for w in KW_Aj.split('|')]
        + [kostr.concat(w, '르지') for w in KW_Al.split('|')]  # 섣부+르지
        + [kostr.concat(w, 'ㄹ', '지') for w in KW_An.split('|')]  # 머+ㄹ+지
        + [kostr.concat(w, '지') for w in KW_Ao.split('|')]
        + [kostr.concat(w, '지') for w in KW_Ap.split('|')]
        + [kostr.concat(w, 'ㅂ', '지') for w in KW_Ar.split('|')]
        + [kostr.concat(w, 'ㅅ', '지') for w in KW_As.split('|')]
        + [kostr.concat(w, 'ㅂ', '지') for w in KW_Aw.split('|')]
        + [kostr.concat(w, 'ㅡ', '지') for w in KW_Ax.split('|')]
        + [kostr.concat(w, 'ㅚ', '지') for w in KW_Ay.split('|')]
    )
)
KW_AV = concat(KW_AVC, KW_AVM, KW_AVN)
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


### activity nouns (can be verb with '-하다/-되다' or used in form of '~을/를 하다')

# NAO: Nouns - Activity (Original Korean)
KW_NAOf = "생각|[가증]감|가공|곱|[건입]국|[연체]결|[총포]괄|가늠|[담배]당|가동|[노입출]력|[수제훈]련|[기수]록|[발변설연작제조증]명|함몰|고민|[개선]발|체벌|[손향]상|[개배연증해]설|[구생작완형]성|[연학]습|[예해]약|오염|[반운투]영|[사이적통포활]용|[교훈]육|[지]원|[도수]입|[수]?출입|시작|긴장|발전|[결설수측한]정|선언|선정|[도장부탈]착|제창|[수연인창]출|예측|[간선채]택|[동수실연]행|[면입]학|포함|[결취]합|[구실재표]현"  # f: has final consonant
KW_NAOv = "[인추참평]가|[제탈]거|[공소]개|[연촉]구|[상연제]기|이야기|시도|[고]려|치료|[관수처]리|연마|[공기]부|[반발조]사|[감축]소|[감준회]수|[기참]여|[긴소중필]요|[논합]의|폐지|대체|[성]취|[납배설]치|\\w+화|이해"  # v: ends with vowel (does not have final consonant)
KW_NAO = concat(KW_NAOf, KW_NAOv)

# NAF: Nouns - Activity - derived from Foreign language
KW_NAFf = "게임|다운로딩|로그아웃|로그인|로깅|모니터링|[업]?로딩|인덱싱|컴파일|필터링"
KW_NAFv = "다운로드|릴리스|마사지|[업]?로드|업데이트|트리거|플레이"
KW_NAF = concat(KW_NAFf, KW_NAFv)

# NA: Nouns - Activity
KW_NAf = concat(KW_NAOf, KW_NAFf)
KW_NAv = concat(KW_NAOv, KW_NAFv)
KW_NA = concat(KW_NAf, KW_NAv)

# NST: Nouns - STatus (can be adjective with '-하다')
KW_NSf = "가능|깔끔|건강|곤란|동일|둔감|부지런|민감|병약|[불]?성실|[부]?적절"
KW_NSv = "상이"
KW_NS = concat(KW_NSf, KW_NSv)

# NAS: Nouns - Activity + Status
#KW_NASf = concat(KW_NAf, KW_NSTf)
#KW_NASv = concat(KW_NAv, KW_NSTv)
#KW_NAS = concat(KW_NASf, KW_NASv)

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
KW_NPRf = "아들|동문|조상|자손|식솔|[처]?자식|[부장]인|동창|[일사삼오육칠팔]촌|남편"
KW_NPRv = "[식친]구|처남|자녀|아내|아주머니|[어할]머니|아줌마|엄마|[고대부이]모|동료|며느리|[대형]부|아빠|[제형]수|아저씨|애인|사위|저|[자처형]제|[할]아버지|제부|처형"

# NPA: nouns - person by Activity
KW_NPAf = "군인|경찰|동호인|애[견묘]인|[증행]인"
KW_NPAv = "감독자|감시자|강[연의]자|관[계련찰]자|글쓴이|당[사직]자|반[려역]자|발[제표]자|수집가|아마추어|엮은이|애호가|응시자|[원]작자|지은이|팬|프로|협력자"

# NPS: nouns - person
KW_NPf = concat(KW_NPEf, KW_NPNf, KW_NPJf, KW_NPRf, KW_NPAf)
KW_NPv = concat(KW_NPEv, KW_NPNv, KW_NPJv, KW_NPRv, KW_NPAv)
KW_NP = concat(KW_NPf, KW_NPv)

# NNC: Nouns - Number - derived from Chinese
#KW_NNCf = "일|삼|육|칠|팔"
#KW_NNCv = "이|사|오|구"
#KW_NNC = concat(KW_NNCf, KW_NNCv)
KW_NNC = "[일이삼사오육칠팔구십백천만]*[일이삼사오육칠팔구십백천만억조경]"

## NND: Nouns - Number - positional value in Decimal system
KW_NNDf = "십|백|천|만|억|경"
KW_NNDv = "조"
KW_NND = concat(KW_NNDf, KW_NNDv)

## NNA: Nouns - Number - Arabic
KW_NNA = "[1-9]?[0-9,]*"

## NNM: Nouns - Number - Mixed
KW_NNMf = KW_NNA + KW_NNDf
KW_NNMv = KW_NNA + KW_NNDv
KW_NNM = concat(KW_NNMf, KW_NNMv)

# NNK: nouns - Number - pure Korean
#KW_NNKf = '|'.join(
#    [
#        x + y
#        for x in [''] + "열|스물|서른|마흔|쉰|예순|일흔|여든|아흔".split('|')
#        for y in [''] + "한|둘|석|셋|넉|넷|다섯|댓|여섯|일곱|여덟|아홉".split('|')
#    ]
#).strip('|')
#
#KW_NNKv = '|'.join(
#    ["스무"] +
#    [
#        x + y
#        for x in [''] + "열|스물|서른|마흔|쉰|예순|일흔|여든|아흔".split('|')
#        for y in "하나|두|세|네".split('|')
#    ]
#).strip('|')
#
#KW_NNK = concat(KW_NNKf, KW_NNKv)

KW_NNK = "[열스서마쉰예일여아백]?[한두세네섯댓곱덟홉]"

KW_NN = concat(KW_NNC, KW_NND, KW_NNK)   

# NUC: Nouns - Units - Currency
KW_NUCf = "루블|엔|원|위안"
KW_NUCv = "달러|리라|유로|페소"
KW_NUC = concat(KW_NUCf, KW_NUCv)

# NUD: Nouns - Units - Distance
KW_NUDf = "광년"
KW_NUDv = "미터|리|킬로미터"
KW_NUD = concat(KW_NUDf, KW_NUDv)

# NUG: Nouns - Units - weiGht in symbol
KW_NUGf = "[mk]?g" 
KW_NUGv = "[k]?[LlMm]"
KW_NUG = concat(KW_NUGf, KW_NUGv)

# NUM: Nouns - Units - Multiplication
KW_NUM = "배"

# NU: Nouns - Units - aRea
KW_NURf = "평"
KW_NURv = "제곱미터|평방미터"
KW_NUR = concat(KW_NURf, KW_NURv)

# NUS: Nouns - Units - Stuff 
KW_NUSf = "그릇|달|명|방울|벌|쪽"
KW_NUSv = "가지|개|마리|박스|봉지|채|페이지|회"
KW_NUSd = "대" # should be handled carefully: '세 대(three device)' vs '3세대(third generation)' 
KW_NUS = concat(
    KW_NUSf, KW_NUSv#, KW_NUSd
)

# NUT: Nouns - Units - Time
KW_NUTf = "분|시간|일|달|개월|년"
KW_NUTv = "밀리초|세기|세대|초"
KW_NUT = concat(KW_NUTf, KW_NUTv)

# NUV: Nouns - Units - Volume
KW_NUVf = ""
KW_NUVv = "세제곱미터"
KW_NUV = concat(KW_NUVf, KW_NUVv)

# NU: nouns - Units - Weight
KW_NUWf = "그램|킬로그램|평"
KW_NUWv = "밀리리터|데시리터|리터|킬로리터|파운드"
KW_NUW = concat(KW_NUWf, KW_NUWv)

KW_NU = concat(KW_NUD, KW_NUG, KW_NUM, KW_NUR, KW_NUS, KW_NUT, KW_NUV, KW_NUW)

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

# Verb - from Adjective - status Change - idea
KW_VACi = [kostr.concat(s, '지') for s in KW_AS.split('|')]

# Verb - from Adjective - status Change - progress
KW_VACn = [kostr.concat(s, '진') for s in KW_AS.split('|')]

# Verb - from Adjective - status Changed - past
KW_VACp = [kostr.concat(s, '졌') for s in KW_AS.split('|')]

# verb: roots of verb -- these are not nouns
KW_VRB = "걸|갈|나누|넣|말|박|빼|졸|숨|재"

# verb: transive
KW_VTc = "[내망외]"  # ~치다(chida)
KW_VTd = "[받쳐]들|[내]밀|[박빨쪼찍]|허물" # ~다(da)
KW_VTg = "[당숨]"  # ~기다(gida)
KW_VTh = "가까이"  # ~하다(hada)
KW_VTi = "[드]높|[보죽죽]|되뇌" # ~이다(ida)
KW_VTl = "[되][돌살]|[쳐]올|[내때]"  # ~리다(lida)
KW_VTp = "[보]살피다"  # ~피다(pida)
KW_VTx = "[낮늦]"  # ~추다(chuda)
KW_VTw = "[치채]"  # ~우다(wuda)

KW_VT = concat(KW_VTc, KW_VTd, KW_VTg, KW_VTh, KW_VTi, KW_VTl, KW_VTp, KW_VTx, KW_VTw)

# verb: intransive
KW_VIe = "숨|죽"  # ~다, 었다, ~어서
KW_VIy = "숨죽ㅇ|생ㄱ|쓰러ㅈ|해ㅈ"  # ~ㅣ다, ㅕㅆ다, ~ㅕ서
KW_VIa = "살"  # ~다, ~았다
KW_VIs = "잘나"  # ~다, ~ㅆ다

# verb: passive
KW_VPl = "갈리다"  # ends with '~리다(lida)'
KW_VPi = "쓰이다"  # ends with '~이다(ida)'
KW_VPh = "먹|붙잡|잡"  # ends with '~히다(hida)'


