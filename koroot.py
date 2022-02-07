from utils import joinseq

##############
# Korean Roots

## A: Adjective (removed final consonant which will be dropped during conjugatation)
# can be conjugated to                  # VS             AS          ASN        AVC           AVM         AVN         #
KR_Aa = '나ㅃ|바ㅃ'                     # 나ㅃ+ㅏ지다    나ㅃ+ㅡ+다  나ㅃ+ㅡ+ㄴ 나ㅃ+ㅏ서     나ㅃ+ㅡ+게  나ㅃ+ㅡ+지  #
KR_Ab = '귀여|더|무서|쉬|차가|추|해로'  # 귀여+워지다    귀여+ㅂ+다  귀여+운    귀여+워서     귀여+ㅂ+게  귀여+ㅂ+지  #
KR_Ac = '맑'                            # 맑+아지다      맑+다       맑+은      맑+아서       맑+게       맑+지       #
KR_Ad = '다'            # sweet         # 다+ㄹ+아지다   다+ㄹ+다    다+ㄴ      다+ㄹ+아서    다+ㄹ+게    다+ㄹ+지    #
KR_Ae = '예ㅃ'                          # 예ㅃ+ㅓ지다    예ㅃ+ㅡ+다  예ㅃ+ㅡ+ㄴ 예ㅃ+ㅓ서     예ㅃ+ㅡ+게  예ㅃ+ㅡ+지  #
KR_Af = '다'            # different     # 다+ㄹ+라지다   다+르+다    다+른      다+ㄹ+라서    다+르+게    다+르+지    #
KR_Ah = '깔끔|매끈|복잡|비슷|착|지저분' # 착+해지다      착+하다     착+한      착+해서       착하게      착하지      #
KR_Ai = '붉'                            # 붉+어지다      붉+다       붉+은      붉+어서       붉+게       붉+지       #
KR_Aj = '같|괜찮|낮|높|좋'              # 같+아지다      같+다       같+은      같+아서       같+게       같+지       #
KR_Al = '섣부'                          # x              섣부+르다   섣부+른    섣부+ㄹ+러서  섣부+르게   섣부+르지   #
KR_Am = '맛있'                          # 맛있+어지다    맛있+다     맛있+는    맛있+어서     맛있+게     맛있+지     #
KR_An = '낯서|머'                       # 머+ㄹ+어지다   머+ㄹ+다    머+ㄴ      머+ㄹ+어서    머+ㄹ+게    머+ㄹ+지    #
KR_Ao = '넓'                            # 넓+어지다      넓+다       넓+은      넓+어서       넓+게       넓+지       #
KR_Ap = '희'                            # 희+어지다      희+다       희+ㄴ      희+어서       희+게       희+지       #
KR_Ar = '이로|평화로'                   # 이로+와지다    이로+ㅂ+다  이로+운    이로+와서     이로+ㅂ+게  이로+ㅂ+지  #
KR_As = '나'                            # 나+아지다      나+ㅅ+다    나+은      나+아서       나+ㅅ+게    나+ㅅ+지    #
KR_Aw = '고'                            # 고+와지다      고+ㅂ+다    고+운      고+와서       고+ㅂ+게    고+ㅂ+지    #

# '쓰다(bitter)' is not included because it is ambiguous with '쓰다(write)'
KR_Ax = 'ㅋ'                            # ㅋ+ㅓ+지다,     ㅋ+ㅡ+다,   ㅋ+ㅓ+서,     ㅋ+ㅡ+게,   ㅋ+ㅡ+지,   ㅋ+ㅡ+ㄴ

KR_Ay = '못ㄷ'                          # 못ㄷ+ㅙ+지다,   못ㄷ+ㅚ+다, 못ㄷ+ㅙ+서,   못ㄷ+ㅚ+게, 못ㄷ+ㅚ+지, 못ㄷ+ㅚㄴ


## roots of verb

### Transive
KR_VTc = "[내망외]"  # ~치다(chida)
KR_VTd = "걸|갈|나누|내밀|넣|들|말|밀|박|빨|받들|빼|재|쳐들|쪼|찍|허물"  # ~다(da)
KR_VTg = "[당숨]"  # ~기다(gida)
KR_VTh = "가까이"  # ~하다(hada)
KR_VTi = "[드]높|보|되뇌|죽" # ~이다(ida)
KR_VTl = "[되][돌살]|[쳐]올|[내때]"  # ~리다(lida)
KR_VTp = "[보]살"  # ~피다(pida)
KR_VTx = "[낮늦]"  # ~추다(chuda)
KR_VTw = "[치채]"  # ~우다(wuda)
KR_VT = joinseq(KR_VTc, KR_VTd, KR_VTg, KR_VTh, KR_VTi, KR_VTl, KR_VTp, KR_VTx, KR_VTw)

### Intransive
KR_VIe = "숨|야물|여물|죽"  # ~다, 었다, ~어서
KR_VIy = "숨죽ㅇ|생ㄱ|쓰러ㅈ|해ㅈ"  # ~ㅣ다, ㅕㅆ다, ~ㅕ서
KR_VIa = "살|졸"  # ~다, ~았다
KR_VIs = "잘나"  # ~다, ~ㅆ다
KR_VPh = "먹|붙잡|잡"  # ends with '~히다(hida)'
