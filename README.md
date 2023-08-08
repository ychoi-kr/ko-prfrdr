한국어 문장을 교정합니다.

   * [spellchk.py](#spellchkpy) : 맞춤법(띄어쓰기 포함) 검사
   * [grmchk.py](#grmchkpy) : 문법 검사
   * [stylechk.py](#stylechkpy) : 문체 검사
   * [suggest.py](#suggestpy) : 쉬운 말, 차별적이지 않은 표현 추천
   * [proofread.py](#proofreadpy) : 모든 검사
   * [proof-gpt.py](#proof-gptpy) : OpenAI API를 사용해 검사
   * [test_proofread.py](#test_proofreadpy) : 검사 규칙에 대한 단위 테스트

<a name="requirements"></a>
## 공통 요구사항

1. Python3가 설치되어 있어야 합니다.
2. 다음 명령을 실행해 필요한 패키지를 설치합니다.

    `pip install -r requirements.txt`

팁:
- [파이썬 3 설치](https://wikidocs.net/44)
- [윈도우 CMD에서 파이썬 활용 팁](https://wikidocs.net/124333)


## correct.py

([proofread.py](#proofreadpy)로 이름 변경됨)


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


## proofread.py

원고(docx 파일)에서 규칙을 준수하는지 검사합니다.

관련 파일:

- 맞춤법
    - [dic.txt](dic.txt) : 사전
    - [en_spelling_rules.json](en_spelling_rules.json) : 영어 철자
    - [ko_foreign_word.json](ko_foreign_word.json) : 외래어 표기법
    - [ko_spacing_rules.json](ko_spacing_rules.json) : 띄어쓰기
    - [ko_spelling_rules.json](ko_spelling_rules.json) : 맞춤법 
    - [ko_terms_error.json](ko_terms_error.json) : 용어 오탈자
- 문체
    - [en_ko_style_correction.json](en_ko_style_correction.json) : 영어 번역 투
    - [ja_ko_style_correction.json](ja_ko_style_correction.json) : 일어 번역 투
    - [ko_grammar.json](ko_grammar.json) : 국문법 
    - [concise_writing.json](concise_writing.json) : 간결한 글쓰기
    - [wikibook_style_guide.json](wikibook_style_guide.json) : 위키북스 글쓰기 지침
- 제안
    - [ko_electric_terms.json](ko_electric_terms.json) : 전력용어 순화
    - [ko_forest_terms.json](ko_forest_terms.json) : 산림용어 순화
    - [ko_gov_terms_2012.json](ko_gov_terms_2012.json) : 행정 용어 순화(2012년)
    - [ko_norm_2002.json](ko_norm_2002.json) : 어문 규범(2002)
    - [ko_plain.json](ko_plain.json) : 쉬운 말
    - [ko_standard_terms.json](ko_standard_terms.json) : 표준 전문용어
    - [ko_unbiased.json](ko_unbiased.json) : 차별적 표현

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

특정 규칙만 검사할 수 있습니다.

예: ‘그중’을 ‘그 중’으로 잘못 쓴 곳(규칙 [109302b](https://wikidocs.net/109302#b))을 검사

```
$ prf 알고리즘수학_1교_20221110.docx --rule 109302b

그리고 그 중에서 양의 정수인 것도 표시해주세요.
       ^
   => 그 중에서 →  그중에서	 (0109302b_그중 : https://wikidocs.net/109302#b)

1 이상 3 이하의 정수를 적는 방법은 모두 9가지이지만, 그 중에서 합계 4 이하가 되는 방법은 6가지이기 때문입니다.
                                                    ^
   => 그 중에서 →  그중에서	 (0109302b_그중 : https://wikidocs.net/109302#b)

=== Summary ===
0109302b_그중 ==> count: 2
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


## proof-gpt.py

입력한 텍스트가 규칙에 맞는지를 OpenAI API로 검사합니다.

### 준비

사용하려면 [OpenAI API 키를 발급받고](https://wikidocs.net/196075) `.env` 파일을 만듭니다.

```
$ cat > .env
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
^D⏎
```

### 사용법

규칙 번호는 [⟪IT 글쓰기와 번역 노트⟫](https://wikidocs.net/book/4103)의 페이지 ID입니다.

사용 예:

```
$ python proof-gpt.py "그 책을 다 읽는데 이틀 걸렸다." -r 67215
{
  "input_text": "그 책을 다 읽는데 이틀 걸렸다.",
  "checked_rule": "https://wikidocs.net/67215",
  "corrections":
    [
      {"pos": "8", "bad": "는데", "good": "는 데", "description": "'데'가 의존 명사로 쓰일 때에는 앞말과 띄어서 씁니다."}
    ]
}
$ python proof-gpt.py "프로그램 오류시 업데이트하세요." -r 94354
{
  "input_text": "프로그램 오류시 업데이트하세요.",
  "checked_rule": "https://wikidocs.net/94354",
  "corrections":
    [
      {"pos": "7", "bad": "오류시", "good": "오류 시", "description": "'시(時)'는 앞말과 띄어 쓴다."}
    ]
}
$ python proof-gpt.py "결혼 유/무" -r 187342
{
  "input_text": "결혼 유/무",
  "checked_rule": "https://wikidocs.net/187342",
  "corrections":
    [
      {"pos": "0~7", "bad": "결혼 유/무", "good": "결혼 여부", "description": "'유/무'는 '있음과 없음'을 뜻하고, '여부'는 '그러함과 그러하지 아니함'을 뜻한다. '결혼'의 경우 '여부'를 사용하는 것이 적절하다."}
    ]
}
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

