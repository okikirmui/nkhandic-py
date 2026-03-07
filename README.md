# nkhandic-py — Python wrapper for the NK-HanDic MeCab dictionary

![PyPI - Version](https://img.shields.io/pypi/v/nkhandic)


👉 **NK-HanDic (dictionary) repository**: https://github.com/okikirmui/nkhandic

`nkhandic` is a **Python helper package** that makes it easy to use **NK-HanDic**, a MeCab dictionary for North Korean, **from Python code**.

> ⚠️ Important distinction  
> - **NK-HanDic** = the MeCab dictionary itself (linguistic resource)  
> - **nkhandic (this package)** = a Python interface / utility layer for HanDic  
>  
> The dictionary is developed and published separately;  
> this package focuses on *Python usability*.

If you need for a contemporary Korean, please check [HanDic](https://github.com/okikirmui/handic) (MeCab dictionary) and [handic](https://pypi.org/project/handic/) (Python wrapper).

---

# Overview

`nkhandic` provides a convenient Python interface for the **NK-HanDic North Korean morphological analysis dictionary**.

It allows researchers and developers to perform **North Korean morphological analysis from Python** without manually configuring dictionary paths or MeCab options.

The package:

- Bundles a snapshot of the NK-HanDic dictionary
- Provides **high-level Python APIs**
- Handles **Jamo-based input/output**
- Supports **Hanja-aware representations**
- Works across **Linux, macOS, and Windows environments**

---

## Relationship between NK-HanDic and this package

```
NK-HanDic (dictionary repository)
        ↓
   MeCab dictionary files
        ↓
  nkhandic (Python wrapper)
        ↓
  Your Python code
```

- The **linguistic design and dictionary entries** live in the NK-HanDic repository
- This package bundles a released snapshot of the dictionary **only to enable Python use**
- Updates to dictionary content are driven by the NK-HanDic project

---

## 🚀 Quick Start (Python)

### Installation

```bash
pip install nkhandic mecab-python3 jamotools
```

### Minimal example

```python
import nkhandic

text = "총비서동지께서 다음과 같이 말씀하시였다."

print(nkhandic.tokenize_hangul(text))
print(nkhandic.pos_tag(text))
print(nkhandic.convert_text_to_hanja_hangul(text))
```

**Example output**
```
[('총비서', 'NNG'), ('동지006', 'NNG'), ('께서', 'JKS'), ('다음01', 'NNG'), ('과12', 'JKB'), ('같이', 'MAG'), ('말씀', 'NNG'), ('하다02', 'XSV'), ('시', 'EP'), ('ㅆ', 'EP'), ('다06', 'EF'), ('.', 'SF')]
['총비서', '동지', '께서', '다음', '과', '같이', '말씀', '하', '시여', 'ㅆ', '다', '.']
總秘書同志께서 다음과 같이 말씀하시였다.
```

---

## High-level API (Python convenience layer)

### `tokenize_hangul(text)`

Return a list of tokens in Hangul base form(Unified Hangul Code).

- Internally uses NK-HanDic via MeCab
- Automatically restores Hangul syllables from Jamo
- Robust against unknown words

If you want to obtain tokens in surface form instead of base form, specify “surface” for the `mode` option.

example:

```python
text = "말씀하시였다."

nkhandic.tokenize_hangul(text, mode="surface")
# ['말씀', '하', '시여', 'ㅆ', '다', '.']

nkhandic.tokenize_hangul(text)
# ['말씀', '하다02', '시', 'ㅆ', '다06', '.']
```

---

### `tokenize(text)`

Return tokens in **Jamo surface form**.

- Low-level wrapper around MeCab

```python
text = "어쩌면 그리도 위대하신가."

nkhandic.tokenize(text)
# ['어쩌면', '그리도', '위대', '하', '시', 'ᆫ가', '.']
```

---

### `pos(text)` — lightweight POS

Return `(surface, coarse_pos)` pairs.

- Surface is returned in **Jamo surface form**
- POS corresponds to the first feature field

---

### `pos_tag(text)`
Return a list of `(token, POS)` tuples.

- Uses HanDic base forms(Unified Hangul Code) when available
- Falls back to surface forms for unknown words
- POS tags are based on the Sejong tag set(see https://docs.komoran.kr/firststep/postypes.html)

The following is an example for comparing `pos()` and `pos_tag()`.

```python
text = "말씀하시였다."

nkhandic.pos(text)
# [('말씀', 'Noun'), ('하', 'Suffix'), ('시여', 'Prefinal'), ('ᆻ', 'Prefinal'), ('다', 'Ending'), ('.', 'Symbol')]

nkhandic.pos_tag(text)
# [('말씀', 'NNG'), ('하다02', 'XSV'), ('시', 'EP'), ('ㅆ', 'EP'), ('다06', 'EF'), ('.', 'SF')]
```

---

### `parse(text)`

Return raw MeCab output string.

- Includes all feature fields
- Intended for advanced use

```python
print(nkhandic.parse("이제 우리앞에는 5개년계획기간이 2년 남아있다."))
```

output:

```Text
이제	Adverb,一般,*,*,*,이제01,이제,*,*,A,MAG
우리	Noun,代名詞,*,*,*,우리03,우리,*,*,A,NP
앞	Noun,普通,*,*,*,앞,앞,*,*,A,NNG
에	Ending,助詞,処格,*,*,에04,에,*,*,*,JKB
는	Ending,助詞,題目,*,*,는01,는,*,*,*,JX
5	Symbol,数字,*,*,*,*,*,*,*,*,SN
개년	Noun,依存名詞,助数詞,*,*,개년03,개년,個年,*,*,NNB
계획	Noun,普通,動作,*,*,계획01,계획,計劃,*,A,NNG
기간	Noun,普通,*,*,*,기간07,기간,期間,*,B,NNG
이	Ending,助詞,主格,*,*,이25,이,*,*,*,JKS
2	Symbol,数字,*,*,*,*,*,*,*,*,SN
년	Noun,依存名詞,助数詞,*,*,년02,년,年,*,A,NNB
남아	Verb,自立,*,語基3,*,남다01,남아,*,*,B,VV
있	Verb,非自立,*,語基1,3接続,있다01,있,*,*,A,VX
다	Ending,語尾,終止形,*,1接続,다06,다,*,*,*,EF
.	Symbol,ピリオド,*,*,*,.,.,*,*,*,SF
EOS
```

---

### `convert_text_to_hanja_hangul(text)`
Convert text into **mixed Hanja + Hangul** representation.

- Uses HanDic feature field (index 7)
- Preserves whitespace and punctuation
- Converts remaining Jamo into complete Hangul syllables

> ⚠️ **Caution**  
> 
> It may be possible to misidentifying homonyms. e.g. 자신: 自信/自身

---

## Platform compatibility (important update)

Recent versions of `nkhandic` include a **more robust MeCab initialization layer** to improve cross‑platform compatibility.

Earlier versions could fail on **Windows or Conda environments** due to platform-specific path handling issues.

Typical errors included:

```
[ifs] no such file or directory: /dev/null
```

or failures caused by Windows path escaping when dictionary paths contained spaces.

### Improvements

The initialization logic now:

- Uses **`os.devnull` instead of `/dev/null`**
- Automatically **quotes dictionary paths**
- Normalizes Windows paths to **forward-slash format**
- Improves MeCab argument handling

These changes make the package more reliable on:

- Windows 10 / 11
- Miniconda / Anaconda environments
- Python installations where the dictionary path contains spaces

Most users **do not need to change their code**.

---

## Low-level access (for compatibility)

```python
import handic

print(nkhandic.DICDIR)   # path to bundled NK-HanDic snapshot
print(nkhandic.VERSION)  # NK-HanDic dictionary version
```

These are provided mainly for **backward compatibility** and inspection.

---

## Typical use cases

- Using HanDic conveniently from Python
- North Korean corpus analysis and language education research
- Preprocessing North Korean text for NLP pipelines
- Exploring Hangul / Hanja correspondences in North Korean

---

## Features

Here is the list of features included in NK-HanDic. For more information, see the [HanDic 품사 정보](https://github.com/okikirmui/handic/blob/main/docs/pos_detail.md).

  - 품사1, 품사2, 품사3: part of speech(index: 0-2)
  - 활용형: conjugation "base"(ex. `語基1`, `語基2`, `語基3`)(index: 3)
  - 접속 정보: which "base" the ending is attached to(ex. `1接続`, `2接続`, etc.)(index: 4)
  - 사전 항목: base forms(index: 5)
  - 표층형: surface(index: 6)
  - 한자: for sino-words(index: 7)
  - 보충 정보: miscellaneous informations(index: 8)
  - 학습 수준: learning level(index: 9)
  - 세종계획 품사 태그: pos-tag(index: 10)
  - 조선어 표시: North Korean marker(index: 11)
  - 조선어 보충 정보: misc. informations about North Korean(index: 12)

---

## Citation

When citing **dictionary content**, please cite the NK-HanDic project:

```
NK-HanDic: morphological analysis dictionary for North Korean
https://github.com/okikirmui/nkhandic
```

When citing **this Python package**, please cite both the package and NK-HanDic.

---

## License

This code is licensed under the MIT license. NK-HanDic is copyright Yoshinori Sugai and distributed under the [BSD license](./LICENSE.nkhandic). 

---

## Acknowledgment

This repository is forked from [unidic-lite](https://github.com/polm/unidic-lite) with some modifications and file additions and deletions.
