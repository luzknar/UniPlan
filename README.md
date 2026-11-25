# UniPlan
대학생 통합 일정 관리 프로그램 (대학SW·AI입문 팀 프로젝트)

## 실행
Python 3.8 이상에서 `python main.py` 실행. 외부 라이브러리 불필요.

## 클래스 구성
- Schedule: 공통 정보, D-day, 완료 처리
- Assignment, Exam, PersonalSchedule: Schedule 상속 및 get_info 오버라이딩
- Subject: 과목별 일정 객체 관리
- ScheduleManager: 등록, 조회, 수정(제목과 날짜), 삭제, 검색, 정렬, 필터, 통계
- FileManager: JSON 저장 및 유형별 객체 복원
- main.py: 콘솔 메뉴와 입력 처리

과목은 일정 등록 시 자동 등록하거나 별도로 등록할 수 있다. 개인 일정은 과목이 없다. 변경 사항은 메뉴 처리 후 자동 저장된다. 데이터 파일은 개인 일정 공개 방지를 위해 Git에서 제외한다. 파일이 없으면 빈 상태로 시작한다.

## 테스트
`python -m unittest discover -s tests` 실행.
