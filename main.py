from pathlib import Path
from datetime import date
from assignment import Assignment
from exam import Exam
from personal_schedule import PersonalSchedule
from file_manager import FileManager


def required(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError('빈 값은 입력할 수 없습니다.')
    return value


def show(schedules):
    if not schedules:
        print('등록된 일정이 없습니다.')
    for schedule in schedules:
        print(schedule.get_info())


def register(manager):
    kind = input('1. 과제  2. 시험  3. 개인 일정: ').strip()
    if kind not in ('1', '2', '3'):
        raise ValueError('잘못된 일정 유형입니다.')
    title = required('제목: ')
    subject = required('과목명: ') if kind != '3' else None
    deadline = date.fromisoformat(required('날짜 (YYYY-MM-DD): ')).isoformat()
    args = (manager.next_id(), title, subject, deadline)
    if kind == '1':
        submission = required('제출 형식: ')
        priority = required('우선순위 (상/중/하): ')
        if priority not in ('상', '중', '하'):
            raise ValueError('상, 중, 하 중 하나를 입력하세요.')
        schedule = Assignment(*args, submission, priority)
    elif kind == '2':
        schedule = Exam(*args, required('시험 범위: '), required('시험 유형: '))
    else:
        schedule = PersonalSchedule(*args, required('장소: '), required('일정 유형: '))
    manager.add_schedule(schedule)
    print('일정을 등록했습니다.')


def main():
    storage = FileManager(Path(__file__).resolve().parent / 'data' / 'schedules.json')
    try:
        manager = storage.load()
    except (OSError, ValueError, KeyError, TypeError) as error:
        print('데이터를 불러올 수 없습니다. 원본 파일을 확인하세요:', error)
        return
    while True:
        print('\n========== UniPlan ==========')
        print('1. 일정 등록     2. 전체 일정 조회')
        print('3. 일정 수정     4. 일정 삭제')
        print('5. 완료 처리     6. 일정 검색')
        print('7. 유형별 조회   8. 과목 관리')
        print('9. 일정 통계     0. 저장 및 종료')
        try:
            choice = input('메뉴 선택: ').strip()
            if choice == '1':
                register(manager)
            elif choice == '2':
                show(manager.sort_schedules())
            elif choice == '3':
                show(manager.schedules)
                number = int(input('수정할 일정 번호: '))
                schedule = manager.find(number)
                title = input(f'새 제목 ({schedule.title}): ').strip() or schedule.title
                deadline = input(f'새 날짜 ({schedule.deadline}): ').strip() or schedule.deadline
                manager.update_schedule(number, title, deadline)
                print('수정했습니다.')
            elif choice == '4':
                show(manager.schedules)
                manager.delete_schedule(int(input('삭제할 일정 번호: ')))
                print('삭제했습니다.')
            elif choice == '5':
                show(manager.schedules)
                manager.find(int(input('완료할 일정 번호: '))).complete()
                print('완료 처리했습니다.')
            elif choice == '6':
                show(manager.search_schedule(required('검색어: ')))
            elif choice == '7':
                kinds = {'1': 'Assignment', '2': 'Exam', '3': 'PersonalSchedule'}
                kind = input('1. 과제  2. 시험  3. 개인 일정: ')
                if kind not in kinds:
                    raise ValueError('잘못된 유형입니다.')
                show(manager.filter_schedules(kinds[kind]))
            elif choice == '8':
                print('과목 목록:', ', '.join(s.name for s in manager.subjects) or '없음')
                action = input('1. 과목 등록  2. 과목별 조회: ')
                if action == '1':
                    manager.add_subject(required('과목명: '))
                elif action == '2':
                    name = required('과목명: ')
                    show([s for s in manager.schedules if s.subject == name])
                else:
                    raise ValueError('잘못된 메뉴입니다.')
            elif choice == '9':
                print(f'전체 일정: {len(manager.schedules)}개')
                for label, kind in [('과제', 'Assignment'), ('시험', 'Exam'), ('개인', 'PersonalSchedule')]:
                    print(f'{label}: {len(manager.filter_schedules(kind))}개')
                print(f'완료율: {manager.get_completion_rate():.1f}%')
            elif choice == '0':
                storage.save(manager)
                print('저장 후 종료합니다.')
                break
            else:
                print('0~9 사이의 메뉴를 선택하세요.')
                continue
            storage.save(manager)
        except (ValueError, OSError) as error:
            print('오류:', error)
        except (EOFError, KeyboardInterrupt):
            print('\n프로그램을 종료합니다.')
            break


if __name__ == '__main__':
    main()
