## 공공데이터 및 웹 크롤링 활용하여 병원(의료)정보 데이터 시각화 대시보드 제작 - 케어브릿지
* **시연 영상은 필요하실때 연락주시면 보내드립니다**
* [문서 다운로드](https://drive.google.com/file/d/1gXqq6W6XWE7XqcNARcffWmU5jGFes81M/view?usp=drive_link)

### 개요
* 기존 서비스들은 응급실 현황이나 감염병 정보처럼 의사결정에 중요한 정보가 없거나 제한적으로 제공되는 한계가 있었습니다. 이러한 한계를 프로젝트 주제로 다룰 가치가 있다고 판단해 본 프로젝트를 선정했습니다.
* 응급실 정보와 병원 예약 기능을 하나의 플랫폼으로 통합해** 사용자가 여러 서비스를 오가지 않도록 했습니다.
* 단순 병상 정보 나열이 아닌, 필터 기능과 종합점수를 활용해 사용자가 자신의 상황에 맞는 응급실을 빠르게 선별할 수 있도록 설계했습니다
* 의료 정보라는 다소 복잡한 데이터를 누구나 빠르고 쉽게 이해할 수 있도록 직관적인 UI/UX로 제공하는 것을 기획의 핵심 목표로 삼았습니다.

### 프로젝트 참여도 및 기술 스택
* 참여도 : 20%
* 프론트 : HTML, CSS, JavaScript(AJAX), Jquery, WebSocket
* 벡엔드 : Django, redis Channel Layer
* DB : MySQL, Django ORM
* 서버 : AWS EC2
* API : Kakao Map API, 공공데이터포털 API(XML)
* 형상관리 : GitHub, gitFlow방식 관리
* 개발툴 : VS Code

### 의사대시보드
* 의사가 한눈에 진료받을 환자의 정보나 7일간 환자 통계 등 볼수있는 의사 대시보드 구현
![Image](https://github.com/user-attachments/assets/5b09a447-7c35-4d40-8809-74978e456951)

### 의료진대시보드
* 의료진이 빠르게 환자의 오더를 처리할수 있도록 실시간 데이터 통신인 웹소켓을 이용한 의료진 대시보드 구현
![의료진대시보드](https://github.com/user-attachments/assets/ac4f2702-682f-4325-b5b8-eb0271764adc)

### 검사기록 작성 및 치료기록 작성
* 의료진이 오더를 처리하기 위한 치료기록 작성 및 검사기록 작성 페이지 구현
* 치료기록의 치료 데이터는 공공 데이터 포털 사용
<img width="2226" height="1211" alt="스크린샷 2025-12-31 100701" src="https://github.com/user-attachments/assets/8b7949ee-d760-4a64-a014-6b5af48b44c9" />

![검사기록 작성](https://github.com/user-attachments/assets/04362829-ffb2-4567-bae5-7309a9879bb5)

### DB 구조
<img width="1579" height="1264" alt="스크린샷 2025-12-30 172025" src="https://github.com/user-attachments/assets/77a17f05-da4c-423b-81b1-4ac9673a783e" />

