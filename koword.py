# verb: roots of verb -- these are not nouns
KW_VRB = "걸|갈|나누|넣|말|박|빼|졸|숨|재"

# verb: transive
KW_VTG = "[당숨]기다"
KW_VTL = "[되][돌살]리다|[쳐]올리다|[내때]리다"
KW_VTI = "[드]높이다|[보죽]이다|되뇌이다"
KW_VTR = "낮추다|망치다|[보]살피다"
KW_VTD = "[내외]치다|[받쳐]들다|[내]밀다|[박빨쪼찍]다"
KW_VTW = "[치채]우다"

# verb: intransive
KW_VII = "숨죽이다"
KW_VID = "[살죽]다"

# verb: passive
KW_VPL = "갈리다"  # ends with '~리다(lida)'
KW_VPI = "쓰이다"  # ends with '~이다(ida)'
KW_VPH = "먹|붙잡|잡"  # ends with '~히다(hida)'


# noun: activity noun -- which can be followed by both '~하다(hada)' and '~을/를 하다'
KW_NAOF = "가감|건국|결정|곱|교육|기록|긴장|노력|담당|성취|운영|연습|입학|제련|제창|처리|출입|훈련|훈육|학습"
KW_NAOV = "고려|공부|논의|발사|연구|연마|제기|참가|참여|치료|합의"

# noun: activity noun derived from foreign language
KW_NAFF = "게임|로깅|모니터링"
KW_NAFV = "마사지"

# noun: activity 
KW_NATF = "|".join([KW_NAOF, KW_NAFF])
KW_NATV = "|".join([KW_NAOV, KW_NAFV])
KW_NATA = "|".join([KW_NATF, KW_NATV])

# noun: status
KW_NSTF = "건강|동일|둔감|민감|병약|불성실|성실"
KW_NSTV = "상이"

# noun: activity nouns + status nouns
KW_NASF = "|".join([KW_NATF, KW_NSTF])
KW_NASV = "|".join([KW_NATV, KW_NSTV])
KW_NASA = "|".join([KW_NASF, KW_NASV])


# noun: person by existance
KW_NPEF = "사람|인[간물]"  # has final consonant
KW_NPEV = "인류"  # ends with vowel (does not have final consonant)

# noun: person by biological or phisical condition
KW_NPNF = "[비]?장애인|어른"
KW_NPNV = "감염자|[고남여병환]자|[동양이]성애자|바보|아기"

# noun: person by job title or membership
KW_NPJF = "감독[관]?[님]?|강사님|과장[님]?|교수님|[국군도동시]민|기업인|대[리표]님|대통령[님]?|사원|[사소의회]장[님]?|시인|작[곡사]?가님|직장인|학생|[수해]병|초대 회장|회사원"
KW_NPJV = "강사|교[사수]|대[리표]|작[곡사]?가"
KW_NPJA = "|".join([KW_NPJF, KW_NPJV])

# noun: person by rank
NW_NPKF = "[경병부차]장[님]?|[상이일]병|[대중소준][령장]|사령관|통수권자"
NW_NPKV = "경[사위]|[대중소준][위좌]|[상중하]사"

# noun: person by social relation
KW_NPRF = "남편|며느리|[부장]인|사위|[일사삼오육칠팔]촌|식솔|아내|자[손식제]"
KW_NPRV = "[고대이]모|동[기료문창]|대부|부모|식구|아버지|아빠|아저씨|아줌마|애인|어머니|엄마|자녀|저|제[부수]|조상|처[남자제형]|처자식|친구|할머니|할아버지|형[부수제]"

# noun: person by activity
KW_NPAF = "군인|경찰|동호인|애[견묘]인|[증행]인"
KW_NPAV = "감독자|감시자|강[연의]자|관[계련찰]자|글쓴이|당[사직]자|반[려역]자|발[제표]자|수집가|아마추어|엮은이|애호가|응시자|[원]작자|지은이|프로|협력자"

# noun: person
KW_NPSF = "|".join([KW_NPEF, KW_NPNF, KW_NPJF, KW_NPRF, KW_NPAF])
KW_NPSV = "|".join([KW_NPEV, KW_NPNV, KW_NPJV, KW_NPRV, KW_NPAV])
KW_NPSN = "|".join([KW_NPSF, KW_NPSV])

# noun: measure in Korean
KW_NMK = "그램|미터|킬로그램|킬로미터"

# noun: measure in symbol
KW_NMS = "g|m|kg|km"

# noun: measure
KW_NM = "|".join([KW_NMK, KW_NMS])

# adjective
KW_ADP = "너희|내|우리|저희"
KW_ADS = "나쁜|작은|좋은|큰"
KW_ADJ = "|".join([KW_ADP, KW_ADS])
