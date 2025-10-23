class DSstudent:
    def __init__(self, stu_id,name):
        self.name=name
        self.stu_id=stu_id

    def show_info(self):
        print(f"{self.stu_id},이름: {self.name}")

student1=DSstudent(20251247,"김유림")

student1.show_info()