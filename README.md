## chk_manuscript.py

원고(docx 파일)에서 규칙을 준수하는지 자동으로 검사합니다.

규칙:

- 맞춤법: [ko_spelling_rules.json](ko_spelling_rules.json)
- 띄어쓰기: [ko_spacing_rules.json](ko_spacing_rules.json)
- 외래어 표기법: [foreign_sound_rules.json](foreign_sound_rules.json)
- 영한 번역투: [en_ko_style_correction.json](en_ko_style_correction.json)
- 일한 번역투: [jp_ko_style_correction.json](jp_ko_style_correction.json)
- 위키북스 글쓰기 지침: [wikibook_style_guide.json](wikibook_style_guide.json)

사용법은 아래처럼 해도 되고,

```
cd <원고가 있는 폴더>
python c:\utils\chk_manuscript.py -f "Mastering_PyTorch_편집본_20211104.docx"
```

파이썬 스크립트가 자동 실행 가능한 환경에서는 다음과 같이 할 수 있고,

```
chk_manuscript -f Mastering_PyTorch_편집본_20211104.docx
```

`-f` 옵션을 생략하면 최신 파일을 찾습니다. 따라서 다음과 같이 실행하면 됩니다.

```
chk_manuscript
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

실행 결과를 파일로 저장하려면 리다이렉션을 이용하면 됩니다.

```
spellchk > report
```

위와 같이 하면 `report` 파일에 텍스트로 저장되고, 메모장으로 열 수 있습니다.


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


## spellchk.py

원고의 맞춤법, 띄어쓰기, 외래어 표기법을 검사합니다.


## stylechk.py

원고의 영한 번역투, 일한 번역투, 위키북스 글쓰기 지침 준수 여부를 검사합니다.


## termlist.py

원고에서 `국문(영문)` 형식으로 병기한 부분을 찾아서 영문 용어 목록을 출력합니다.

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
