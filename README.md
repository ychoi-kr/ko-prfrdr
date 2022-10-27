출판물 제작 업무를 돕는 명령행 스크립트들입니다.

* [공통 요구사항](#requirements)

* 한국어 문장 교정
   * [spellchk.py](#spellchkpy) : 맞춤법(띄어쓰기 포함) 검사
   * [grmchk.py](#grmchkpy) : 문법 검사
   * [stylechk.py](#stylechkpy) : 문체 검사
   * [suggest.py](#suggestpy) : 쉬운 말, 차별적이지 않은 표현 추천
   * [proofread.py](#proofreadpy) : 모든 검사
   * [test_proofread.py](#test_proofreadpy) : 검사 규칙에 대한 단위 테스트

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
   * [comments.py](#commentspy) : doc 파일의 메모 목록을 엑셀 시트에 작성 (Windows 전용)
   * [doc2docx.py](#doc2docxpy) : doc 파일을 docx 파일로 일괄 변환 (Windows 전용)
   * [exfigs.py](#exfigspy) : docx 파일에서 이미지 파일을 일괄 추출
   * [openall.py](#openallpy) : 현재 경로의 모든 docx 파일을 열기 (Windows 전용)
   * [pgcnt.py](#pgcntpy): docx 파일의 페이지 수 세기
   * [termlist.py](#termlistpy) : docx 파일에 국영문 병기된 용어의 목록을 출력

* 파일 관리
   * [mvfig.py](#mvfigpy) : 그림 파일명 일괄 변경
   * [today.py](#todaypy) : 파일명의 날짜를 일괄 변경

* PDF
   * [pdf_merge.py](#pdf_mergepy) : PDF 파일 병합
   * [pdf2docx.py](#pdf2docxpy) : PDF 파일을 docx 파일로 변환
   * [pdftotext.py](#pdftotextpy) : PDF 파일을 txt 파일로 변환
   * [searchable.py](#searchablepy) : 검색 가능한 PDF 파일을 생성

* 웹
   * [yes24.py](#yes24py) : 예스24 도서 검색
   * [yes24_review.py](#yes24_reviewpy) : 예스24 상품평 조회
   * yesblog.py : YES 블로그 본문 추출
   * wikidocs.py : 위키독스 책의 목차 및 본문 추출
   * wikipedia.py : 위키백과의 본문 추출

* 번역
   * [fakemt.py](#fakemtpy) : OmegaT용 MT

* 기타
   * [sort.py](#sortpy) : 입력받은 행들을 오름차순으로 정렬하여 출력


<a name="requirements"></a>
## 공통 요구사항

1. Python3가 설치되어 있어햐 합니다.
2. 다음 명령을 실행해 필요한 패키지를 설치합니다.

    `pip install -r requirements.txt`

팁:
- [파이썬 3 설치](https://wikidocs.net/44)
- [윈도우 CMD에서 파이썬 활용 팁](https://wikidocs.net/124333)


## comments.py

현재 디렉터리의 모든 `.docx` 파일의 메모를 엑셀 시트에 작성합니다. (Windows 전용)


## correct.py

([proofread.py](proofreadpy)로 이름 변경됨)

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


## grmchk.py

문장의 문법을 검사합니다.

사용 예:

```
$ echo "양자 알고리즘의 제시되었다." | grmchk.py
Trying to import KoNLPy...
Loading rule file: ko_grammar.json...
양자 알고리즘의 제시되었다.

     ^
   => 알고리즘의 제시되었다 →  알고리즘이 제시되었다	 (0167020a_주어-술어 호응 : https://wikidocs.net/167020#a)

=== Summary ===
0167020a_주어-술어 호응 ==> count: 1
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


## proofread.py

원고(docx 파일)에서 규칙을 준수하는지 검사합니다.

관련 파일:

- [concise_writing.json](concise_writing.json) : 간결한 글쓰기
- [dic.txt](dic.txt) : 사전
- [en_ko_style_correction.json](en_ko_style_correction.json) : 영어 번역 투
- [en_spelling_rules.json](en_spelling_rules.json) : 영어 철자
- [ja_ko_style_correction.json](ja_ko_style_correction.json) : 일어 번역 투
- [ko_foreign_word.json](ko_foreign_word.json) : 외래어 표기법
- [ko_gov_terms_2012.json](ko_gov_terms_2012.json) : 행정 용어 순화(2012년)
- [ko_grammar.json](ko_grammar.json) : 국문법 
- [ko_norm_2002.json](ko_norm_2022.json) : 어문 규범(2002)
- [ko_plain.json](ko_plain.json) : 쉬운 말
- [ko_spacing_rules.json](ko_spacing_rules.json) : 띄어쓰기
- [ko_spelling_rules.json](ko_spelling_rules.json) : 맞춤법 
- [ko_terms_error.json](ko_terms_error.json) : 용어 오탈자
- [ko_unbiased.json](ko_unbiased.json) : 차별적 표현
- [wikibook_style_guide.json](wikibook_style_guide.json) : 위키북스 글쓰기 지침

요구사항:

- docx 파일을 검사하려면 docx2txt를 설치(`pip install docx2txt`)
- PDF 파일을 검사하려면 [Xpdf](http://www.xpdfreader.com/about.html) 명령행 도구를 [설치](https://wikidocs.net/154110)
- HWP 파일을 검사하려면
    - `pip3 install pyhwp`
    - `hwp5txt`를 실행할 수 있게 PATH 환경변수에 경로를 등록
        - 맥 환경은 https://blog.naver.com/yoonsweety/221451960610 참고
- 품사 검사 기능을 이용하려면
    - `pip3 install git+https://github.com/konlpy/konlpy.git`

사용법:

아래처럼 해도 되고,

```
cd <원고가 있는 폴더>
python3 proofread.py "Mastering_PyTorch_편집본_20211104.docx"
```

파이썬 스크립트가 자동 실행 가능한 환경에서는 다음과 같이 할 수 있습니다.

```
proofread "Mastering_PyTorch_편집본_20211104.docx"
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
...
rule222_각각의 ==> count: 4
rule224_생략해야 하는 표현 ==> count: 17
```

표준 입력을 받아서 교정할 수 있습니다.

```
$ echo "프로그래밍이 뭐냐구요? 소프트웨어를 만드는 것이 프로그래밍입니다. 그리고, 컴퓨터가 알아듣는 말을 프로그래밍 언어라고 하지요." | correct.py
프로그래밍이 뭐냐구요?

             ^
   => 뭐냐구요? →  뭐냐고요?	 (spel2000_국어의 오용 사례 모음 - 어문 규범 준수 실태 조사(아동도서), 2001 : https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=52&pageIndex=50)

그리고, 컴퓨터가 알아듣는 말을 프로그래밍 언어라고 하지요.

^
   => 그리고, →  그리고	 (0079918_쉼표, 반점 : https://wikidocs.net/79918)

```

팁:

- 실행 결과를 파일로 저장하려면 리다이렉션을 이용하면 됩니다. 예를 들어, `python3 proofread.py > report`를 실행하면 `report` 파일에 텍스트로 저장되고, 메모장으로 열 수 있습니다.
- 워드 파일을 편집 중일 때 다른 프로그램에서 동시에 열 수 없지만, 다른 컴퓨터에서 OneDrive로 동기화된 파일을 열 수는 있습니다. 따라서 컴퓨터가 두 대 있다면 한 대로는 `python3 proofread.py | more`로 확인하면서 다른 컴퓨터로 워드 파일을 편집하는 식으로 작업할 수 있습니다.
- `proofread.py`로 모든 검사를 한 번에 해도 되지만, [spellchk.py](#spellchkpy)로 맞춤법을 검사해서 수정한 후 [stylechk.py](#stylechkpy)로 문체를 검사하면 더 좋습니다.
- [find 명령으로 여러 개의 파일을 검사](https://wikidocs.net/162133)


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

원고의 맞춤법, 띄어쓰기, 외래어 표기법 등을 검사합니다.

사용 예:

```
$ spellchk.py sample.txt
Trying to import KoNLPy...
Loading rule file: ko_spelling_rules.json...
Loading rule file: ko_spacing_rules.json...
Loading rule file: ko_foreign_word.json...
다만 로고에는 뱀 두마리가 형상화 되어 있다.

                         ^
   => 형상화 되어 →  형상화되어	 (0067208a_-되다(접미사) : https://wikidocs.net/67208#a)

                 ^
   => 두마리가 →  두 마리가	 (0100750a2_단위를 나타내는 명사 : https://wikidocs.net/100750#a)

객체 지향 프로그래밍과 구조적 프로그래밍을 완벽하게 지원하며 함수형 프로그래밍, 관점 지향 프로그래밍 등도 주요 기능에서 지원 된다.

                                                                                                                        ^
   => 지원 된다 →  지원된다	 (0067208a_-되다(접미사) : https://wikidocs.net/67208#a)

파이썬의 이러한 엄격한 스타일 제한은 쓰는 사람에 관계 없이 통일성을 유지하게 하며, 그 결과 가독성이 향상될 수 있는 장점이 있지만, 다른 한편으로는 프로그램을 쓰는 스타일을 선택할 자유를 제약하는 것이란 의견도 있다.

                                          ^
   => 사람에 관계 없이 →  사람에 관계없이	 (0164399b_관계 없다 / 관계없다, 관계 있다 / 관계있다, 상관 없다 / 상관없다, 상관 있다 / 상관있다 : https://wikidocs.net/0164399#b)

다음과 같이 한줄로 작성하여 표현하는 것을 'pythonic 하다'라고 말할 수 있다.

            ^
   => 한줄로 →  한 줄로	 (0100750a2_단위를 나타내는 명사 : https://wikidocs.net/100750#a)

이뮤터블(immutable) 방식의 진리값.

                           ^
   => 진리값 →  진릿값	 (0080784d_값 : https://wikidocs.net/80784#d)

Visual Studio Code : 파이썬 뿐이 아니라 대부분의 언어를 지원한다.
                     ^
   => 파이썬 뿐이 →  파이썬뿐이	 (0079973a_-뿐(조사) : https://wikidocs.net/79973#a)

위키미디어 공용에 관련된미디어 분류가 있습니다.파이썬

                                     ^
   => 있습니다.파이썬 →  있습니다. 파이썬	 (0075024e_마침표의 띄어쓰기 : https://wikidocs.net/75024#e)

=== Summary ===
0067208a_-되다(접미사) ==> count: 2
0075024e_마침표의 띄어쓰기 ==> count: 1
0079973a_-뿐(조사) ==> count: 1
0080784d_값 ==> count: 1
0100750a2_단위를 나타내는 명사 ==> count: 2
0164399b_관계 없다 / 관계없다, 관계 있다 / 관계있다, 상관 없다 / 상관없다, 상관 있다 / 상관있다 ==> count: 1
```


## stylechk.py

원고의 영한 번역투, 일한 번역투, 위키북스 글쓰기 지침 준수 여부를 검사합니다.

## suggest.py

쉬운 말, 차별적이지 않은 표현을 제안합니다.

사용 예:

```
$ echo "프로세스의 실행이 감지되면 블랙 리스트와 비교하여" | suggest.py 
Trying to import KoNLPy...
Loading rule file: ko_norm_2002.json...
Loading rule file: ko_gov_terms_2012.json...
Loading rule file: ko_plain.json...
Loading rule file: ko_unbiased.json...
프로세스의 실행이 감지되면 블랙 리스트와 비교하여

^
   => 프로세스의 실행이 감지되면 블랙 리스트와 비교하여
   →  프로세스의 실행이 감지되면 거부 목록과 비교하여	 (0177252_인종차별적 용어 : https://wikidocs.net/177252)

=== Summary ===
0177252_인종차별적 용어 ==> count: 1
```

## termlist.py

원고에서 `국문(영문)` 형식으로 병기한 부분을 찾아서 영문 용어 목록을 출력합니다.

요구사항:

`pip install docx2txt`

사용법:

```
$ ./termlist.py sample.txt
TERM                                               COUNT
Anaconda                                           1
Beautiful Soup                                     1
BitTorrent                                         1
boolean                                            1
Byte code                                          1
Cython                                             1
Dropbox                                            1
dynamic typing                                     2
dynamically typed                                  1
en                                                 1
GC, Garbage Collector                              1
ILM                                                1
immutable                                          7
Inkscape                                           1
JPython                                            1
JS                                                 1
long integer                                       1
MailMan                                            1
MoinMoin Wiki                                      1
mutable                                            3
NASA                                               1
NOAA                                               1
NumPy                                              1
Paint Shop Pro                                     1
Pillow                                             1
Plucker                                            1
Portage                                            1
PyGame                                             1
PySol                                              1
repository                                         1
Shade                                              1
tuple                                              1
VB.NET                                             1
```


## today.py

현재 디렉터리의 모든 `.docx` 파일의 파일명에서 YYYYMMDD 형식으로 된 부분을 오늘 날짜로 바꿉니다. (Windows 전용)


## yes24.py

예스24에서 국내 도서 목록을 검색합니다(e북 제외).

요구사항:

```
pip install beautifulsoup4
````

사용법:

```
yes24.py [-h] [--order {인기도순,정확도순,신상품순,최저가순,최고가순,평점순,리뷰순}] [--category CATEGORY] keyword
```

두 개 이상의 키워드로 찾고 싶을 때는 따옴표로 감싸면 됩니다.

```
$ yes24.py "파이썬 위키북스"
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%9C%84%ED%82%A4%EB%B6%81%EC%8A%A4&order=SINDEX_ONLY&dispno2=001001003 ...

파이썬 머신러닝 완벽 가이드: 다양한 캐글 예제와 함께 기초 알고리즘부터 최신 기법까지 배우는
http://www.yes24.com/Product/Goods/108824557
권철민 저 | 위키북스 | 2022년 04월
판매지수 4,401

손가락 하나 까딱하지 않는 주식 거래 시스템 구축: 파이썬을 이용한 데이터 수집과 차트 분석, 매매 자동화까지
http://www.yes24.com/Product/Goods/89999945
장용준 저 | 위키북스 | 2020년 04월
판매지수 3,900

일 잘하는 직장인을 위한 엑셀 자동화 with 파이썬: 복잡하고 지루한 반복 업무를 쉽고 빠르게 해치우는 방법
http://www.yes24.com/Product/Goods/94483920
최은석 저 | 위키북스 | 2020년 11월
판매지수 3,654

...
```

검색어에서 제외하고 싶은 키워드는 마이너스를 붙이면 됩니다.

```
$ yes24.py "Rust -일러스트 -애니 -웹툰"
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=Rust&order=SINDEX_ONLY&dispno2=001001003 ...

15단계로 배우는 도커와 쿠버네티스
http://www.yes24.com/Product/Goods/93317828
타카라 마호 저/이동규 역 | 제이펍 | 2020년 10월
판매지수 3,990

쿠버네티스 모범 사례: 쿠버네티스 창시자가 알려주는 최신 쿠버네티스 개발 및 배포 기법 
http://www.yes24.com/Product/Goods/95560470
브렌던 번스, 에디 비얄바, 데이브 스트레벨, 라클런 이븐슨 저/장정호 역 | 한빛미디어 | 2020년 12월
판매지수 2,622

동시성 프로그래밍: Rust, C, 어셈블리어로 구현하며 배우는 동시성 프로그래밍 A to Z
http://www.yes24.com/Product/Goods/108570426
다카노 유키 저/김모세 역 | 한빛미디어 | 2022년 04월
판매지수 2,310
```

정렬 순서를 지정할 수 있습니다.

```
$ yes24.py --order 신상품순 AWS | head -16
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=AWS&order=RECENT&dispno2=001001003 ...

Must Have 코로나보드로 배우는 실전 웹 서비스 개발: Node.js와 AWS를 활용한 설계부터 크롤링, 개발, 운영, 수익화까지
http://www.yes24.com/Product/Goods/108903274
권영재, 주은진 저 | 골든래빗 | 2022년 05월
판매지수 2,673

쉽게 배우는 AWS AI 서비스: 챗봇, 음성비서, 크롤러 프로젝트를 구현하며 만나는 서비스형 AI
http://www.yes24.com/Product/Goods/108685145
피터 엘거, 오언 셔너히 저/맹윤호, 임지순 역/곽근봉 감수 | 한빛미디어 | 2022년 04월
판매지수 576

MLFlow를 활용한 MLOps: AWS, Azure, GCP에서 MLOps 시작하기
http://www.yes24.com/Product/Goods/106709982
스리다르 알라, 수만 칼리안 아다리 저/정이현 역 | 에이콘출판사 | 2022년 02월
판매지수 1,938
```

검색 카테고리를 지정할 수 있습니다.

```
$ yes24.py --category 대학교재 통계 | head -16
Opening http://www.yes24.com/Product/Search?domain=BOOK&query=%ED%86%B5%EA%B3%84&order=SINDEX_ONLY&dispno2=001001014 ...

제대로 알고 쓰는 논문 통계분석: SPSS & AMOS
http://www.yes24.com/Product/Goods/70748357
노경섭 저 | 한빛아카데미 | 2019년 02월
판매지수 12,564

SPSS 결과표 작성과 해석 방법: 한번에 통과하는 논문
http://www.yes24.com/Product/Goods/59577796
히든그레이스 논문통계팀, 김성은, 정규형, 우종훈, 허영회 저 | 한빛아카데미 | 2018년 03월
판매지수 9,768

정신질환의 진단 및 통계편람: DSM-5
http://www.yes24.com/Product/Goods/17843603
APA 저/권준수, 김재진, 남궁기, 박원명 역 | 학지사 | 2015년 04월
판매지수 8,274
```

카테고리는 URL의 `dispno2` 값을 넣어도 되고, 한글로 지정할 수도 있습니다. 사용 가능한 카테고리 이름을 확인하려면 다음과 같이 하면 됩니다(제가 임의로 정한 것이므로 예스24의 카테고리명과는 차이가 있습니다).

```
$ python -c "import yes24; print(yes24.categorymap)"
{'art': '001001007', 'biz': '001001025', 'elementary': '001001044', 'exam': '001001015', 'humanity': '001001019', 'it': '001001003', 'kid': '001001016', 'kids': '001001016', 'literature': '001001046', 'middle': '001001013', 'sci': '001001002', 'self': '001001026', 'teen': '001001005', 'test': '001001015', 'univ': '001001014', '경영': '001001025', '경제': '001001025', '과학': '001001002', '대학교재': '001001014', '문학': '001001046', '수험서': '001001015', '어린이': '001001016', '예술': '001001007', '인문': '001001019', '자격증': '001001015', '자기개발': '001001026', '자기계발': '001001026', '자연과학': '001001002', '중고등': '001001013', '중고등참고서': '001001013', '청소년': '001001005', '초등': '001001044', '초등참고서': '001001044'}
``` 

기능 제한:

- 페이징 기능이 없어 상품 목록의 첫 번째 페이지만 조회합니다.

## yes24_review.py

예스24의 상품 번호를 입력해 리뷰를 조회할 수 있습니다.

```
$ echo -e "97315227\n90322497" | yes24_review.py
2021-03-22 밍*이 
내용 평점5점  편집/디자인 평점5점
어렸을때 준비했던 정보보안전문가가 다시 기억나는 책요즘 들어, 웹 개발, 반응형을 포함한 모바일 웹앱까지 개발하다 보니 웹 보안에 대해 더 신경을 많이 쓰게 되었는데 마침 좋은 기회가 있어                    더보기찰, 공격, 방어 세 단계로 배우는 웹 애플리케이션 보안의 모든 것'이 문장만 들어도 나로선, 어렸을 때부터 정보보안에 관심이 많았던...

2021-03-22 z****n 
내용 평점5점  편집/디자인 평점5점
2021년 올해의 책리뷰 / 웹 애플리케이션 보안 / 한빛미디어드디어 출시된 웹 애플리케이션 보안!!이 책은 정말 해킹과 보안에 관심있는 사람들에게는 필독인 책이다. 해커로부터 웹 애플리케이션                    더보기웹 애플리케이션을 조사하고 침입하는 방법을 다루는 책이다. 취약점을 식별하며 애플리케이션 데이터를 공격에 악용하는 페이로드를...

...

2020-10-13 출*****4 구매
평점5점
칼리,네트워크 설정 및 서버 구축에 있어서 어느정도에 지식이 있는 사람이 읽어야 한다.
```

CSV 형식으로 출력할 수 있습니다.

```
$ echo -e "97315227\n90322497" | yes24_review.py --csv
"책 제목","URL","저자/역자","발행일","작성일","작성자","구매","평점","리뷰"
"웹 애플리케이션 보안","http://www.yes24.com/Product/Goods/97315227","앤드루 호프먼 저/최용 역","2021년 02월 19일","2021-03-22","밍*이","","내용 평점5점  편집/디자인 평점5점","어렸을때 준비했던 정보보안전문가가 다시 기억나는 책요즘 들어, 웹 개발, 반응형을 포함한 모바일 웹앱까지 개발하다 보니 웹 보안에 대해 더 신경을 많이 쓰게 되었는데 마침 좋은 기회가 있어서 이                     더보기" , 방어 세 단계로 배우는 웹 애플리케이션 보안의 모든 것'이 문장만 들어도 나로선, 어렸을 때부터 정보보안에 관심이 많았던...
"웹 애플리케이션 보안","http://www.yes24.com/Product/Goods/97315227","앤드루 호프먼 저/최용 역","2021년 02월 19일","2021-03-22","z****n","","내용 평점5점  편집/디자인 평점5점","2021년 올해의 책리뷰 / 웹 애플리케이션 보안 / 한빛미디어드디어 출시된 웹 애플리케이션 보안!!이 책은 정말 해킹과 보안에 관심있는 사람들에게는 필독인 책이다. 해커로부터 웹 애플리케이션을 보호                    더보기" 케이션을 조사하고 침입하는 방법을 다루는 책이다. 취약점을 식별하며 애플리케이션 데이터를 공격에 악용하는 페이로드를...

...

"침투 본능, 해커의 기술","http://www.yes24.com/Product/Goods/90322497","아드리안 프루티아누 저/최용 역","2020년 05월 28일","2020-10-13","출*****4","구매","평점5점","칼리,네트워크 설정 및 서버 구축에 있어서 어느정도에 지식이 있는 사람이 읽어야 한다."
```

`yes24.py`로 조회한 상품 ID 목록을 파이프로 넘겨받아 리뷰를 수집하고 CSV 파일로 저장할 수 있습니다.

```
$ yes24.py --order 신상품순 --id_only 위키북스 | yes24_review.py --csv > 리뷰.csv
```

기능 제한:

- 페이징 기능이 없어 최근 리뷰만 조회됩니다.

팁:

- Excel에서 글자가 깨져 보이는 경우, 리본 메뉴에서 ‘데이터’ - ‘텍스트/CSV에서’를 선택해 CSV 파일을 열어 보세요.
