from utils import joinseq

##############
# Korean Roots

## A: Adjective (removed final consonant which will be dropped during conjugatation)
# can be conjugated to                  # VS          AS       ASN     AVC       AVM     AVN   
KR_Aa = '나ㅃ|바ㅃ'                     # +ㅏ지다     +ㅡ+다   +ㅡ+ㄴ  +ㅏ서     +ㅡ+게  +ㅡ+지 
KR_Ab = '귀여|더|무서|쉬|차가|추|해로'  # +워지다     +ㅂ+다   +운     +워서     +ㅂ+게  +ㅂ+지 
KR_Ac = '맑'                            # +아지다     +다      +은     +아서     +게     +지    
KR_Ad = '다'            # sweet         # +ㄹ+아지다  +ㄹ+다   +ㄴ     +ㄹ+아서  +ㄹ+게  +ㄹ+지 
KR_Ae = '예ㅃ'                          # +ㅓ지다     +ㅡ+다   +ㅡ+ㄴ  +ㅓ서     +ㅡ+게  +ㅡ+지 
KR_Af = '다'            # different     # +ㄹ+라지다  +르+다   +른     +ㄹ+라서  +르+게  +르+지 
KR_Ah = '깔끔|긴요|매끈|복잡|비슷|섬세|장대|장렬|졸렬|중요|지저분|진부|착|참신'
                                        # +해지다     +하다    +한     +해서     +하게   +하지
KR_Ai = '붉'                            # +어지다     +다      +은     +어서     +게     +지    
KR_Aj = '같|괜찮|낮|높|좋'              # +아지다     +다      +은     +아서     +게     +지    
KR_Al = '섣부'                          # x           +르다    +른     +ㄹ+러서  +르게   +르지  
KR_Am = '맛있'                          # +어지다     +다      +는     +어서     +게     +지    
KR_An = '낯서|머'                       # +ㄹ+어지다  +ㄹ+다   +ㄴ     +ㄹ+어서  +ㄹ+게  +ㄹ+지 
KR_Ao = '넓'                            # +어지다     +다      +은     +어서     +게     +지    
KR_Ap = '희'                            # +어지다     +다      +ㄴ     +어서     +게     +지    
KR_Ar = '이로|평화로'                   # +와지다     +ㅂ+다   +운     +와서     +ㅂ+게  +ㅂ+지 
KR_As = '나'                            # +아지다     +ㅅ+다   +은     +아서     +ㅅ+게  +ㅅ+지 
KR_Aw = '고'                            # +와지다     +ㅂ+다   +운     +와서     +ㅂ+게  +ㅂ+지 

# '쓰다(bitter)' is not included because it is ambiguous with '쓰다(write)'

KR_Ax = 'ㅋ'                            # +ㅓ+지다,   +ㅡ+다,  +ㅓ+서,  +ㅡ+게,  +ㅡ+지,  +ㅡ+ㄴ
KR_Ay = '못ㄷ'                          # +ㅙ+지다,   +ㅚ+다,  +ㅙ+서,  +ㅚ+게,  +ㅚ+지,  +ㅚㄴ


## roots of verb

### Both(intransives can conjugate to transive)
#                                   # intransive                    transive
#                                   # no-tense  past      present   no-tense     past         intension
KR_VCg = "숨"                       # 숨+다     숨+었+다  숨+는+다  숨+ㄱ+ㅣ+다  숨+ㄱ+였+다  숨+ㄱ+ㅣ+ㄹ
KR_VCi = "먹|죽"                    # 먹+다     먹+었+다  먹+는+다  먹+이+다     먹+여+ㅆ+다  먹+일
KR_VCl = "살"                       # 살+다     살+았+다  산+다     살+리+다     살+렸+다     살+릴

### Intransive
#                                   # no-tense    past           present
KR_VIa = "가"                       # 가+다       가+ㅆ+다       가+ㄴ+다
KR_VIe = "야물|여물"                # 여무+ㄹ+다  여무+ㄹ+었+다  여무+ㄴ+다
KR_VIy = "숨죽ㅇ|생ㄱ|쓰러ㅈ|해ㅈ"  # 생ㄱ+ㅣ+다  생ㄱ+ㅕ+ㅆ+다  생ㄱ+ㅣ+ㄴ+다
KR_VIl = "조"                       # 조+ㄹ+다    조+ㄹ+았+다    조+ㄴ+다
KR_VIs = "잘나"                     # 잘나+다     잘나+ㅆ+다

### Transive
#                                   # active                            passive
#                                   # no-tense   present    past        no-tense      present          past            
KR_VTg = "박|붙잡|잡"               # +다        +는+다     +았+다      +히+다        +힌+다           +혔+다        
KR_VTh = "먹|읽"                    # +다        +는+다     +었+다      +ㅎ+ㅣ+다     +ㅎ+ㅣ+ㄴ+다     +ㅎ+ㅕ+ㅆ+다
KR_VTi = "보"                       # +다        +ㄴ+다     +았+다      +ㅇ+ㅣ+다     +ㅇ+ㅣ+ㄴ+다     +ㅇ+ㅕ+ㅆ+다
KR_VTl = "가" # grind               # +ㄹ+다     +ㄴ+다     +ㄹ+았+다   +ㄹ+ㄹ+ㅣ+다  +ㄹ+ㄹ+ㅣ+ㄴ+다  +ㄹ+ㄹ+ㅕ+ㅆ+다 
KR_VTm = "거|드|미"                 # +ㄹ+다     +ㄴ+다     +ㄹ+었+다   +ㄹ+ㄹ+ㅣ+다  +ㄹ+ㄹ+ㅣ+ㄴ+다  +ㄹ+ㄹ+ㅕ+ㅆ+다  
KR_VTn = "빠" # wash                # +ㄹ+다     +ㄴ+다     +ㄹ+았+다   +ㄹ+ㄹ+ㅣ+다  +ㄹ+ㄹ+ㅣ+ㄴ+다  +ㄹ+ㄹ+ㅕ+ㅆ+다  
KR_VTy = "나ㄴ"                     # +ㅜ+다     +ㅜ+ㄴ+다  +ㅝ+ㅆ+다   +ㅟ+다        +ㅟ+ㄴ+다        +ㅟ+었+다      

### Active
KR_VAd = "내밀|넣|말|받들|빼|재|쳐들|쪼|찍|허물"  # ~다(da)
KR_VAh = "가까이"                   # 가까이+하+다  가까이+했+다  가까이+한+다 x
KR_VAi = "내ㅊ|당ㄱ|[되]?[돌살]ㄹ|망ㅊ|숨ㄱ|외ㅊ|[드]높|되뇌|죽|[보]살ㅍ" # ~ㅣ다(ida)
KR_VAl = "[되][돌살]|[쳐]올|[내때]"  # ~리다(lida)
KR_VAu = "ㅊ|낮ㅊ|늦ㅊ"             # +ㅜ+다     +ㅜ+ㄴ+다  +ㅝ+ㅆ+다        
KR_VAw = "[치채]"  # ~우다(wuda)

