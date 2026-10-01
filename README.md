# Baekjoon Problem Solving Archive

백준 알고리즘 문제 풀이를 기록하는 저장소입니다.  
단순 정답 제출이 아니라 문제 해결 과정과 사고 흐름을 정리하는 것을 목표로 합니다.

백준을 중심으로 SWEA 풀이도 함께 보관합니다. 서비스 프로젝트와 구분되는 Python 알고리즘 학습 기록입니다.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Purpose: Learning](https://img.shields.io/badge/Purpose-Learning-374151?style=flat)

[풀이 탐색](#풀이-둘러보기) · [실행과 기록](#실행과-기록) · [복습 기준](#학습-목표와-복습-기준)

## 풀이 둘러보기

| 문제 플랫폼 | 학습 기록 |
|---|---|
| 백준 | [Python 풀이 · 원문 링크](Python/백준) |
| SWEA | [Python 풀이 · 제출 기록](Python/SWEA) |

**자료구조 선택 예시**

- [집합으로 출입 상태 관리](Python/%EB%B0%B1%EC%A4%80/Silver/7785.%E2%80%85%ED%9A%8C%EC%82%AC%EC%97%90%E2%80%85%EC%9E%88%EB%8A%94%E2%80%85%EC%82%AC%EB%9E%8C/%ED%9A%8C%EC%82%AC%EC%97%90%E2%80%85%EC%9E%88%EB%8A%94%E2%80%85%EC%82%AC%EB%9E%8C.py): 입·퇴장 이벤트를 `set`에 반영하고 남은 이름을 역순 정렬합니다.
- [스택으로 괄호 검증](Python/%EB%B0%B1%EC%A4%80/Silver/9012.%E2%80%85%EA%B4%84%ED%98%B8/%EA%B4%84%ED%98%B8.py): 닫는 괄호를 만났을 때의 짝과 마지막 스택 상태를 확인합니다.

## 실행과 기록

각 풀이는 표준 입력을 받는 독립 Python 프로그램입니다. 원문 문제의 입력 예제를 준비해 실행할 수 있습니다.

```bash
python3 "문제 폴더/풀이.py" < input.txt
```

문제별 README의 시간·메모리·제출일은 저장된 제출 기록입니다. 전체 풀이의 재채점이나 동일 환경에서의 성능 비교 결과를 의미하지 않습니다.

2026-10-01 문서 정리에서는 링크와 소개한 코드의 대응만 확인했으며 **실행 검증 미수행**입니다.

문제 원문은 [백준 온라인 저지](https://www.acmicpc.net/)에 있으며, [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)로 기록한 문제 링크와 채점 메타데이터를 보존합니다. 풀이 코드와 플랫폼 문제 설명의 출처를 구분합니다.

SWEA 문제는 [SW Expert Academy](https://swexpertacademy.com/)의 자료이며 개별 문제 README의 출처를 따릅니다.

## 학습 목표와 복습 기준

<details>
<summary>학습 목표와 복습 기준</summary>

## Purpose

- 문제 해결 능력 향상
- 시간복잡도 기반 사고
- 자료구조 선택 능력 강화
- 실패 원인 분석 및 개선

---

## Goal

- 풀이를 설명할 수 있는 수준까지 이해
- 유형별 접근 방식 정리
- 실전 개발에 적용 가능한 사고력 확보

---

## Language

- Python

---

## Directory Structure

```text
Python/
├─ 백준/
│  ├─ Bronze/
│  ├─ Silver/
│  └─ Gold/
└─ SWEA/
```

---

## How I Approach Problems

- 완전탐색 가능 여부 판단
- 입력 크기 기반 시간복잡도 검토
- 자료구조 선택
- 중복 연산 제거
- 알고리즘 패턴 분류 (BFS, DFS, DP 등)

---

## Review 기준

각 문제를 풀고 아래 내용을 점검합니다.

- 접근 방식
- 실패 원인
- 해결 방법
- 개선 포인트
- 재사용 가능한 인사이트

---

## Retrospective

- 처음 풀이가 최적해가 아닌 경우가 많았다
- 시간복잡도 판단이 틀리면 대부분 실패했다
- 자료구조 선택이 성능에 큰 영향을 줬다
- 정답보다 "이유 설명"이 더 중요했다

---

## Improvement Plan

- 유형별 문제 정리
- 반복 실패 패턴 기록
- 재풀이 및 리팩토링

</details>
