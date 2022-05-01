출판물 제작 업무를 돕는 명령행 스크립트들입니다.

* [공통 요구사항](#공통)

* 한국어 원고 교정
   * [correct.py](#correctpy) : 맞춤법과 문체 검사
   * [spellchk.py](#spellchkpy) : 맞춤법 검사
   * [stylechk.py](#stylechkpy) : 문체 검사

* 한국어 높임법
   * [hae.py](#haepy) : 해체로 변환
   * [haera.py](#haerapy) : 해라체로 변환
   * [haeyo.py](#haeyopy) : 해요체로 변환
   * [hasipsio.py](#hasipsiopy) : 하십시오체로 변환

* 외래어/외국어
   * [pyko.py](#pykopy) : 중국어 병음을 한국어로 표기
   * [p2a.py](#p2apy) : 영어 수동태를 능동태로 변환
   * indian.py, indiantree.py : 영문으로 표기된 인도어를 한국어로 표기

* 마이크로소프트 워드
   * [doc2docx.py](#doc2docxpy) : doc 파일을 docx 파일로 일괄 변환 (Windows 전용)
   * [exfigs.py](#exfigspy) : docx 파일에서 이미지 파일을 일괄 추출
   * [openall.py](#openallpy) : 현재 경로의 모든 docx 파일을 열기 (Windows 전용)
   * [pgcnt.py](#pgcntpy): docx 파일의 페이지 수 세기
   * [termlist.py](#termlistpy) : docx 파일에 국영문 병기된 용어의 목록을 출력

* 파일 관리
   * [mvfig.py](#mvfigpy) : 그림 파일명 일괄 변경

* PDF
   * [pdf_merge.py](#pdf_mergepy) : PDF 파일 병합
   * [pdf2docx.py](#pdf2docxpy) : PDF 파일을 docx 파일로 변환
   * [pdftotext.py](#pdftotextpy) : PDF 파일을 txt 파일로 변환
   * [searchable.py](#searchablepy) : 검색 가능한 PDF 파일을 생성

* 웹
   * [yes24.py](#yes24py) : 예스24 도서 검색
   * wikidocs_toc.py : 위키독스 책의 목차 추출

* 번역
   * [fakemt.py](#fakemtpy) : OmegaT용 MT

* 기타
   * [sort.py](#sortpy) : 입력받은 행들을 오름차순으로 정렬하여 출력


## 공통

<a name="common_requirements"></a>
요구사항:

- [파이썬 3 설치](https://wikidocs.net/44)

팁:

- [윈도우 CMD에서 파이썬 활용 팁](https://wikidocs.net/124333)


## correct.py

원고(docx 파일)에서 규칙을 준수하는지 검사합니다.

관련 파일:

- 맞춤법: [ko_spelling_rules.json](ko_spelling_rules.json)
- 띄어쓰기: [ko_spacing_rules.json](ko_spacing_rules.json)
- 외래어 표기법: [foreign_sound_rules.json](foreign_sound_rules.json)
- 영한 번역투: [en_ko_style_correction.json](en_ko_style_correction.json)
- 일한 번역투: [ja_ko_style_correction.json](ja_ko_style_correction.json)
- 위키북스 글쓰기 지침: [wikibook_style_guide.json](wikibook_style_guide.json)
- 간결한 글쓰기: [simple_style.json](simple_style.json)
- 사전: [dic.txt](dic.txt)

요구사항:

- `pip3 install docx2txt`
- PDF 파일을 검사하려면 [Xpdf](http://www.xpdfreader.com/about.html) 명령행 도구를 [설치](https://wikidocs.net/154110)
- HWP 파일을 검사하려면
    - `pip3 install pyhwp`
    - `hwp5txt`를 실행할 수 있게 PATH 환경변수에 경로를 등록
        - 맥 환경은 https://blog.naver.com/yoonsweety/221451960610 참고
- 품사 검사 기능을 이용하려면
    - `pip3 install --force-reinstall git+git://github.com/ychoi-kr/konlpy.git`

사용법:

아래처럼 해도 되고,

```
cd <원고가 있는 폴더>
python3 correct.py "Mastering_PyTorch_편집본_20211104.docx"
```

파이썬 스크립트가 자동 실행 가능한 환경에서는 다음과 같이 할 수 있고,

```
correct "Mastering_PyTorch_편집본_20211104.docx"
```

파일명을 생략하면 최신 파일을 찾습니다. 따라서 다음과 같이 실행하면 됩니다.

```
correct
```

파일이 열려 있으면 안 되므로 워드 파일을 닫거나 읽기 전용으로 바꾼 후 실행해야 합니다.

실행 결과는 다음과 비슷하게 나옵니다.

```
* 초보자가 전문가로 성장하기 위해 활용할 수 있는 자원은 무한히 많다.
                        ^
  => ~기 위해 활용할 → ~는 데 활용할    (rule204_-위해)


* 시그모이드와는 다르게 TanH 활성화 함수의 경우 출력값 는 -1과 1 사이의 값을 갖는다.
                                                                          ^
  => ~을 갖는다 → ~이 있다      (rule213_영어의 have에서 비롯된 '가지다')

(생략)

* 여기서도 필기체 숫자 분류기를 훈련시키는 비슷한 실습을 했다.
                                                      ^
  => ~을 했다    (rule105_불필요한 조사를 뺀다 : 실행을 한다 → 실행한다, 도입을 했다 → 도입했다, 컴파일이 되지만 → 컴파일되지만)


=== Summary ===
rule002_다운로드하다 ==> count: 1
rule101_간결하게 쓴다 ==> count: 1
rule102_되도록 수동태 표현이나 사역형 표현은 쓰지 않는다 ==> count: 9
rule103_가급적 쉬운 표현을 쓴다 ==> count: 51
rule105_불필요한 조사를 뺀다 ==> count: 10
rule108_자주 쓰는 표현은 가급적 한글로 표기한다 ==> count: 1
rule204_-위해 ==> count: 4
rule206_때문에 ==> count: 31
rule207_-도록 ==> count: 1
rule208_의미가 모호한 '제공하다'의 남발 ==> count: 1
rule212_~되다 ==> count: 4
rule213_영어의 have에서 비롯된 '가지다' ==> count: 24
rule222_각각의 ==> count: 4
rule224_생략해야 하는 표현 ==> count: 17
```

팁:

- 실행 결과를 파일로 저장하려면 리다이렉션을 이용하면 됩니다. 예를 들어, `python3 correct.py > report`를 실행하면 `report` 파일에 텍스트로 저장되고, 메모장으로 열 수 있습니다.
- 워드 파일을 편집 중일 때 다른 프로그램에서 동시에 열 수 없지만, 다른 컴퓨터에서 OneDrive로 동기화된 파일을 열 수는 있습니다. 따라서 컴퓨터가 두 대 있다면 한 대로는 `python3 correct.py | more`로 확인하면서 다른 컴퓨터로 워드 파일을 편집하는 식으로 작업할 수 있습니다.
- `correct.py`로 모든 검사를 한 번에 해도 되지만, `spellchk.py`로 맞춤법을 검사해서 수정한 후 `stylechk.py`로 문체를 검사하면 더 좋습니다.
- [find 명령으로 여러 개의 파일을 검사](https://wikidocs.net/162133)

## doc2docx.py

현재 작업 디렉터리에 있는 모든 doc 파일에 대하여 docx 포맷의 사본을 만듭니다.

사용법:

```
python doc2docx.py
```

## exfigs.py

`.docx` 파일에 삽입된 그림 파일을 추출합니다. 아래 문서에 설명한 작업을 자동화한 것입니다.

- [Word(.docx) 파일에 삽입된 그림을 일괄 추출하는 방법](https://wikidocs.net/160542)


## fakemt.py

[OmegaT FakeMT Plugin](https://github.com/briacp/omegat-plugin-fake-mt) 서버입니다.
요청 받은 텍스트를 구글 번역으로 보낸 후 결과를 받아서 해라체로 바꿔 응답합니다.
[OmegaT가 설치](https://wikidocs.net/67103)되어 있어야 하고 [OmegaT FakeMT 플러그인도 설치 및 설정](https://wikidocs.net/157584)해야 합니다.

실행:

```
python3 fakemt.py
```

## hae.py

텍스트를 입력받아서 해체로 바꿔줍니다.


## haera.py

텍스트를 입력받아서 해라체로 바꿔줍니다.

`haera`를 실행한 뒤 텍스트를 입력하고 엔터 키를 누르면 변환 결과가 출력됩니다.

예:

```
$ haera
ROC 곡선은 이상적인 모델에서는 이처럼 원점에서 수직으로 높아지고 재현율이 1에 도달한 후에 수평으로 변화합니다. 그러나 정답률이 100%가 아닌 (일반적인) 모델에서는 곡선이 오른쪽 아래 방향으로 이동합니다. 이렇게 이동하는 정도를 정량화하기 위해 곡선 아래쪽 면적을 계산해서 그 결과를 모델의 평가지표로 이용합니다. 이것을 AUC(area under the curve)라고 말합니다. - 《데이터 분석을 위한 수리 모델 입문》

ROC 곡선은 이상적인 모델에서는 이처럼 원점에서 수직으로 높아지고 재현율이 1에 도달한 후에 수평으로 변화한다. 그러나 정답률이 100%가 아닌 (일반적인) 모델에서는 곡선이 오른쪽 아래 방향으로 이동한다. 이렇게 이동하는 정도를 정량화하기 위해 곡선 아래쪽 면적을 계산해서 그 결과를 모델의 평가지표로 이용한다. 이것을 AUC(area under the curve)라고 말한다. - 《데이터 분석을 위한 수리 모델 입문》
```

## haeyo.py

텍스트를 입력받아서 해요체로 바꿔줍니다.


## hasipsio.py

텍스트를 입력받아서 하십시오체로 바꿔줍니다.


## mvfig.py

그림 파일들의 파일명을 일괄 변경합니다.

변경 전 파일명과 변경 후 파일명을 나열하는 Tab-Separated Values 파일인 `fig_list.tsv`를 작성해야 합니다.

예:

```
$ cat fig_list.tsv
image1	그림 1.1 개인, 기관, 외국인 주식투자 수익률 비교
image2	그림 1.2 개인투자자 1인당 보유 종목 수
```

`fig_list.tsv`의 각 행에 대하여, 첫 번째 열의 이름을 두 번째 열의 이름으로 바꿉니다. 확장자는 기존 파일의 것이 유지됩니다.

실행 예:

```
$ ls 
fig_list.tsv    image1.png    image2.jpg    mvfig.py

$ python mvfig.py

$ ls
fig_list.tsv    '그림 1.1 개인, 기관, 외국인 주식투자 수익률 비교.png'    '그림 1.2 개인투자자 1인당 보유 종목 수.jpg'    mvfig.py
```


## openall.py

현재 위치의 `docx` 파일을 모두 엽니다. Windows 전용입니다.

요구사항:

```
pip install pywin32
```

사용법:

- `py openall.py` : 현재 작업 폴더의 `docx` 파일을 모두 엽니다.
- `py openall.py -R` : 현재 작업 폴더 및 하위 폴더의 `docx` 파일을 모두 엽니다.


## p2a.py

영어 수동태 문장을 능동태로 변환합니다.

아래 저장소에서 코드를 가져온 뒤 오류가 발생하는 부분만 수정했습니다.
- https://github.com/DanManN/pass2act
- https://github.com/clips/pattern

요구사항:

사용하려면 [spacy](https://pypi.org/project/spacy/)를 설치해야 합니다.

`pip install spacy`

사용법:

`p2a`를 실행한 뒤 수동태 문장을 입력하면 능동태 문장이 출력되며, `q`를 입력하면 종료합니다.

```
$ p2a

The book is written by myself.
Myself wrote the book.

A policy of whitewashing and cover-up has been pursed by the CIA director and his close advisors.
The CIA director and his close advisors has pursed a policy of whitewashing and cover-up.

q
```

능동태의 주어에 해당하는 절이 있어야 변환 가능합니다.

```
Mistakes were made.
Mistakes were made.

Mistakes were made by us.
We made mistakes.
```


## pdf_merge.py

같은 이름으로 시작하는 PDF 파일들을 하나로 합칩니다.

요구사항:

`pip install PyPDF2`

사용법:

```
python pdf_merge.py [directory] bookname`
```

`directory` 인자로 지정한 이름(기본값: `merged`)의 서브디렉터리가 만들어지고 그곳에 병합된 PDF 파일이 만들어집니다.

예:

```
python d:\GitHub\sk8erchoi\ko-prfrdr\pdf_merge.py "Mastering PyTorch_최종인쇄용_0125"
```

## pdf2docx.py

PDF 문서를 docx로 변환하는 [pdf2docx](https://github.com/dothinking/pdf2docx)를 호출합니다.

요구사항:

`pip install pdf2docx`

사용법:

`pdf2docx <파일명>`


## pdftotext.py

PDF에서 텍스트를 추출하는 [pdftotext](https://www.xpdfreader.com/about.html)를 좀 더 편리하게 사용할 수 있게 해주는 스크립트입니다.

주요 기능:

- 페이지 번호 부분을 제외한 본문 영역의 텍스트를 추출
- 줄바꿈과 하이픈 삭제(영어만 됨)
- 암호화된 파일 열기(사용자 암호를 입력해야 함)
- 페이지별 사이즈가 다르거나 양면으로 된 파일에서도 내용 추출

요구 사항:

- [공통 요구사항](#common_requirements)을 충족
- Xpdf 명령행 도구를 [설치](https://wikidocs.net/154110)
- [pikepdf](https://github.com/pikepdf/pikepdf)를 설치

사용법:

아래 명령을 실행하면 PDF와 같은 이름의 txt 파일이 생성됩니다.

```
python pdftotext.py [옵션] "<PDF 파일명>"
```

- `--password "<패스워드>"`: 사용자 패스워드가 걸린 파일을 풀 때 이 옵션을 사용합니다.
- `--header <숫자>`: 머리말 여백의 높이를 지정합니다(기본값은 50). 본문 위쪽이 잘리거나 머리말이 제외되지 않은 경우 이 옵션을 조정합니다.
- `--footer <숫자>`: 꼬리말 여백의 높이를 지정합니다(기본값은 60). 본문 아래쪽이 잘리거나 꼬리말이 제외되지 않은 경우 이 옵션을 조정합니다.

이슈:

- 국어 문장의 줄바꿈을 삭제할 때 무조건 공백을 추가하게 되어 있음
- 페이지 번호가 옆쪽에 있는 것
- 페이지 내에 다단으로 편집된 것을 인식하지 못함

팁:

- 잘 안 될 경우 영문자만으로 이뤄진 간단한 파일명으로 PDF 파일을 복사해서 시도해보시기 바랍니다.
- 이 스크립트 없이 `pdftotext.exe`만으로도 텍스트를 추출할 수 있습니다.


## pgcnt.py

현재 디렉터리에 있는 docx 문서들의 페이지 수를 셉니다. (Windows 전용)

요구사항:

```
pip install natsort
```

사용법:

```
$ python pgcnt.py "워드 파일명" # 특정 파일의 페이지 수 출력
$ python pgcnt.py # 현재 폴더 내 모든 워드 파일의 페이지 수 출력
```

예:

```
> python pgcnt.py
1~2장.doc          63      63
3장.doc    44     107
4장.doc    32     139
5장.doc    54     193
6장.doc    79     272
7장.doc    35     307
8장.doc    53     360
9장.doc    83     443
10장.doc           77     520
```


## pyko.py

중국어 병음(Pinyin)을 입력하면 [한국어 표기](https://ko.wikipedia.org/wiki/중국어의_한글_표기)로 바꿔줍니다.

사용법:

```
$ python pyko.py
Zhōngguó
중궈
```

## searchable.py

스캔해서 만들어진 PDF 파일로부터 검색 가능한 PDF 파일을 생성합니다. 한글 인식이 잘 안 됩니다.

요구사항:


1. [Xpdf 명령행 도구 설치](https://wikidocs.net/154110)
2. [Tesseract 셋업](https://wikidocs.net/162293)
3. `pip install pytesseract numpy opencv-python PyPDF2 pdf2image`

이슈:

- 글자 사이에 불필요한 공백이 들어가서 검색 기능을 활용하는 데 지장 있음.


## sort.py

텍스트 파일의 행을 오름차순으로 정렬합니다.

```
>type glossary.txt
banana  바나나
orange  오렌지
apple   사과

>sort.py glossary.txt

>type glossary.txt
apple   사과
banana  바나나
orange  오렌지

>
```


## spellchk.py

원고의 맞춤법, 띄어쓰기, 외래어 표기법을 검사합니다.


## stylechk.py

원고의 영한 번역투, 일한 번역투, 위키북스 글쓰기 지침 준수 여부를 검사합니다.


## termlist.py

원고에서 `국문(영문)` 형식으로 병기한 부분을 찾아서 영문 용어 목록을 출력합니다.

요구사항:

`pip install docx2txt`

사용법:

```
$termchk
TERM                                               COUNT
Atari                                              1
atomic                                             1
Automated Machine Learning                         1
AutoML                                             1
auxiliary classifier                               1
Azure                                              2
Azure Machine Learnin Service, AMLS                1
b                                                  1
batch_size                                         1
Beam Search                                        1
Bernd Krueger                                      1
bias correction                                    1
Bibhuti Bhushan Jha                                1
budget                                             1
CNN                                                2
```


## yes24.py

예스24에서 국내 도서 목록을 검색합니다(e북 제외).

요구사항:

```
pip install beautifulsoup4
````

사용법:

```
yes24.py [-h] [--order {인기도순,정확도순,신상품순,최저가순,최고가순,평점순,리뷰순}] keyword [keyword ...]
```

예 1:

```
$ python yes24.py 파이썬 위키북스
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%9C%84%ED%82%A4%EB%B6%81%EC%8A%A4 ...

파이썬을 이용한 딥러닝/강화학습 주식투자
http://www.yes24.com/Product/Goods/108251432
퀀티랩 저 | 위키북스 | 2022년 03월
판매지수 1,776

파이썬 텍스트 마이닝 완벽 가이드
http://www.yes24.com/Product/Goods/107008224
박상언, 강주영, 정석찬 저 | 위키북스 | 2022년 02월
판매지수 2,517

손에 잡히는 퀀트 투자 with 파이썬
http://www.yes24.com/Product/Goods/107036607
GIL′s LAB 저 | 위키북스 | 2022년 02월
판매지수 1,782

일 잘하는 직장인을 위한 엑셀 자동화 with 파이썬
http://www.yes24.com/Product/Goods/94483920
최은석 저 | 위키북스 | 2020년 11월
판매지수 4,113

...
```

예 2:

```
$ yes24 C++
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=C%2B%2B&order=SINDEX_ONLY ...

Clean Code 클린 코드
http://www.yes24.com/Product/Goods/11681152
로버트 C. 마틴 저/박재호, 이해영 역 | 인사이트(insight) | 2013년 12월
판매지수 61,812

전지적 독자 시점 4
http://www.yes24.com/Product/Goods/107874372
싱숑 원저/슬리피-C 글그림 | 에이템포미디어 | 2022년 02월
판매지수 24,849

역시 내 청춘 러브코메디는 잘못됐다. 결 1
http://www.yes24.com/Product/Goods/107847414
와타리 와타루 저/퐁칸 ⑧ 그림/김장준 역 | 디앤씨미디어(D&C미디어) | 2022년 03월
판매지수 18,843

혼자 공부하는 C 언어
http://www.yes24.com/Product/Goods/74269921
서현우 저 | 한빛미디어 | 2019년 06월
판매지수 41,073

...

$ yes24 --order 정확도순 C++
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=C%2B%2B&order=RELATION ...

독하게 시작하는 C 프로그래밍
http://www.yes24.com/Product/Goods/18732021
최호성 저 | 루비페이퍼 | 2015년 06월
판매지수 1,440

코믹 흔해빠진 직업으로 세계최강 8
http://www.yes24.com/Product/Goods/108603876
시라코메 료 원저/RoGa 글그림/김장준 역 | 디앤씨미디어(D&C미디어) | 2022년 04월
판매지수 1,710

방과 후, 이세계 카페에서 커피를 4
http://www.yes24.com/Product/Goods/108603698
카자미 도리 저/U스케 그림/이진주 역 | 디앤씨미디어(D&C미디어) | 2022년 04월
판매지수 1,200

Game Programming in C++
http://www.yes24.com/Product/Goods/78898401
산자이 마드하브 저/박주항 역 | 에이콘출판사 | 2019년 09월
판매지수 1,044

...
```
