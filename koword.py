
def concat(*s):
    return "|".join(s)

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


### activity nouns (which can be followed by both '~하다(hada)' and '~을/를 하다')

# NAO: activity nouns (original Korean)
KW_NAOF = "[가증]감|곱|[건입]국|[연체]결|[총포]괄|[담배]당|[노입출]력|[수제훈]련|[기수]록|[개선]발|[구작형]성|[연학]습|[지]원|[반운투]영|[이적포활]용|[교훈]육|수[출]?입|[결설수한]정|선언|선정|제창|수출|선택|[동수실연]행|[면입]학|포함|[결취]합|[구실재]현|"  # F: has final consonant
KW_NAOV = "참가|[연]구|제기|[고]려|치료|처리|연마|[공기]부|[반발조]사|[개배증해]설|[기참]여|[논합]의|[성]취|[배설]치"  # V: ends with vowel (does not have final consonant)
KW_NAOA = concat(KW_NAOF, KW_NAOV)

# NAF: activity noun derived from foreign language
KW_NAFF = "게임|로깅|모니터링"
KW_NAFV = "마사지"
KW_NAFA = concat(KW_NAFF, KW_NAFV)

# NAT: all activity nouns
KW_NATF = concat(KW_NAOF, KW_NAFF)
KW_NATV = concat(KW_NAOV, KW_NAFV)
KW_NATA = concat(KW_NATF, KW_NATV)

# NST: status nouns
KW_NSTF = "건강|긴장|동일|둔감|민감|병약|불성실|성실|함몰"
KW_NSTV = "상이"
KW_NSTA = concat(KW_NSTF, KW_NSTV)

# NAS: activity nouns + status nouns
KW_NASF = concat(KW_NATF, KW_NSTF)
KW_NASV = concat(KW_NATV, KW_NSTV)
KW_NASA = concat(KW_NASF, KW_NASV)

# NPE: nouns - person by Existance
KW_NPEF = "사람|인[간물]"
KW_NPEV = "인류"

#  NPN: nouns - person by biological or phisical conditioN
KW_NPNF = "[비]?장애인|어른"
KW_NPNV = "감염자|[고남여병환]자|[동양이]성애자|바보|아기"

# NPJ: nouns - person by Job title or membership
KW_NPJF = "감독[관]?[님]?|강사님|과장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|사원|[사소의회]장[님]?|시인|작[곡사]?가님|직장인|학생|[수해]병|초대 회장|회사원"
KW_NPJV = "강사|교[사수]|대[리표]|작[곡사]?가"
KW_NPJA = concat(KW_NPJF, KW_NPJV)

# NPK: nouns - person by ranK
NW_NPKF = "[경병부차]장[님]?|[상이일]병|[대중소준][령장]|사령관|통수권자"
NW_NPKV = "경[사위]|[대중소준][위좌]|[상중하]사"

# NPR: nouns - person by social Relation
KW_NPRF = "아들|동문|조상|자손|식솔|[처]자식|[부장]인|자제|동창|[일사삼오육칠팔]촌|남편"
KW_NPRV = "[식친]구|처남|자녀|아내|아주머니|[어할]머니|아줌마|엄마|[고대부이]모|동료|며느리|[대형]부|아빠|[제형]수|아저씨|애인|사위|저|[처형]제|[할]아버지|제부|처형"

# NPA: nouns - person by Activity
KW_NPAF = "군인|경찰|동호인|애[견묘]인|[증행]인"
KW_NPAV = "감독자|감시자|강[연의]자|관[계련찰]자|글쓴이|당[사직]자|반[려역]자|발[제표]자|수집가|아마추어|엮은이|애호가|응시자|[원]작자|지은이|프로|협력자"

# NPS: nouns - person
KW_NPSF = concat(KW_NPEF, KW_NPNF, KW_NPJF, KW_NPRF, KW_NPAF)
KW_NPSV = concat(KW_NPEV, KW_NPNV, KW_NPJV, KW_NPRV, KW_NPAV)
KW_NPSA = concat(KW_NPSF, KW_NPSV)

# NNC: Nouns - Number - derived from Chinese
KW_NNCF = "일삼육칠팔"
KW_NNCV = "이사오구"
KW_NNCA = concat(KW_NNCF, KW_NNCV)

## NND: Nouns - Number - positional value in Decimal system
KW_NNDF = "십백천만억경"
KW_NNDV = "조"
KW_NNDA = concat(KW_NNDF, KW_NNDV)

# NNK: nouns - Number - pure Korean
KW_NNKF = "\\w+[한두둘석세셋넉네넷섯곱덟홉열]"
KW_NNKV = "하나"
KW_NNKA = concat(KW_NNKF, KW_NNKV)

KW_NNA = concat(KW_NNCA, KW_NNDA, KW_NNKA)   

# NUS: Nouns - Units - Stuff 
KW_NUSF = "그릇|달|명|방울|벌|시간|쪽"
KW_NUSV = "가지|마리|채|페이지|회"
KW_NUSA = concat(KW_NUSF, KW_NUSV)

# NUT: Nouns - Units - Time
KW_NUTF = "분|시간|일|달|개월|년|세기"
KW_NUTV = "밀리초|초"
KW_NUTA = concat(KW_NUTF, KW_NUTV)

# NUD: Nouns - Units - Distance
KW_NUDF = "광년"
KW_NUDV = "미터|킬로미터"
KW_NUDA = concat(KW_NUDF, KW_NUDV)

# NU: nouns - Units - Weight
KW_NUWF = "그램|킬로그램|평"
KW_NUWV = "밀리리터|데시리터|리터|킬로리터|파운드"
KW_NUWA = concat(KW_NUWF, KW_NUWV)

# NUG: Nouns - Units - weiGht in symbol
KW_NUGF = "[mk]?g" 
KW_NUGV = "[k]?[LlMm]"
KW_NUGA = concat(KW_NUGF, KW_NUGV)

# NU: Nouns - Units - aRea
KW_NURF = "평"
KW_NURV = "제곱미터|평방미터"
KW_NURA = concat(KW_NURF, KW_NURV)

# NUV: Nouns - Units - Volume
KW_NUVF = ""
KW_NUVV = "세제곱미터"
KW_NUVA = concat(KW_NUVF, KW_NUVV)

KW_NUA = concat(KW_NUSA, KW_NUTA, KW_NUDA, KW_NUWA, KW_NUGA, KW_NURA, KW_NUVA)

# NL: nouns - animaL - Domestic
KW_NLDF = "말" 
KW_NLDV = "개|고양이|돼지|소|오리" 
KW_NLDA = concat(KW_NLDF, KW_NLDV)

# NL: nouns - animaL - Insects
KW_NLIF = "개미|딱정벌레|지네"
KW_NLIV = "[꿀]벌|[여]왕벌"
KW_NLIA = concat(KW_NLIF, KW_NLIV)

# AD: adjectives
KW_ADP = "너희|내|우리|저희"  # possesive
KW_ADS = "나쁜|작은|좋은|큰"  # status
KW_ADJ = concat(KW_ADP, KW_ADS)
