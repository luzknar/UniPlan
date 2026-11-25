from schedule import Schedule


class Exam(Schedule):
    def __init__(self, schedule_id, title, subject, deadline, exam_scope, exam_type, completed=False):
        super().__init__(schedule_id, title, subject, deadline, completed)
        self.exam_scope = exam_scope
        self.exam_type = exam_type

    def get_info(self):
        return f'[시험] {super().get_info()} | 범위: {self.exam_scope} | 유형: {self.exam_type}'
