# Health GO

---

## 개요

- Fleek 클론코딩
- DRF View 및 Serializer에대한 공부와 Front 공부의 목적으로 진행
- 운동기록, 소셜 기능까지 목표


---

## 서버 구조

> Back : Django Rest Framework
> Python Version : 3.11

> 사용 기술 및 스택
> 1. Djang-jwt를 사용한 사용자 보안인증
> 2. AWS - EC2, S3 
> 3. CICD

> Front : React / typeScript



---

## 기능 구상

  >1. 루틴
  >   - 커스텀 루틴
  >    - 날자 선택해서 하루 운동기록 (완료)
  >    - 운동 종목별로 방법, 자세 등 영상등록
  >2. 트레이너 회원관리 시스템
  >   - 트레이너들이 회원들의 루틴을 수정해 PT내용에 도움을 줌
  >3. 커뮤 게시판
  >   - 게시글에 본인 루틴을 공유할 수 있는 커뮤 게시판
  >   - 일반적인 커뮤 게시판 
  >4. AI 루틴 (나중 나중 나중에 AI 공부할 때 추가하고자 함)
  >   - 본인 신체스펙에 맞게 AI 루틴 추천


## info
RotuineInfo -> info_json 예시
```JSON
[{"set":1,"kg":80,"labs":8},{"set":2,"kg":90,"labs":5},{"set":3,"kg":100,"labs":3}]
```
