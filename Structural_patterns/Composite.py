from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class EmployeeComponent(ABC):
    """
    Lớp cơ sở trừu tượng cho tất cả các thành phần trong hệ thống tổ chức.
    """

    @property
    def parent(self) -> EmployeeComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: EmployeeComponent):
        self._parent = parent

    def add(self, component: EmployeeComponent) -> None:
        pass

    def remove(self, component: EmployeeComponent) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def show_details(self) -> str:
        pass


class Employee(EmployeeComponent):
    """
    Lớp nhân viên, đại diện cho các phần tử cuối cùng trong hệ thống tổ chức.
    """

    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position

    def show_details(self) -> str:
        return f"Employee: {self.name}, Position: {self.position}"


class Department(EmployeeComponent):
    """
    Lớp phòng ban, có thể chứa các nhân viên và các phòng ban khác.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._employees: List[EmployeeComponent] = []

    def add(self, component: EmployeeComponent) -> None:
        self._employees.append(component)
        component.parent = self

    def remove(self, component: EmployeeComponent) -> None:
        self._employees.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def show_details(self) -> str:
        details = [f"Department: {self.name}"]
        for employee in self._employees:
            details.append(f"  {employee.show_details()}")
        return "\n".join(details)


def client_code(component: EmployeeComponent) -> None:
    """
    Client code làm việc với tất cả các thành phần thông qua giao diện chung.
    """
    print(component.show_details(), end="")


def client_code2(component1: EmployeeComponent, component2: EmployeeComponent) -> None:
    """
    Client code quản lý việc thêm các thành phần vào một phòng ban.
    """
    if component1.is_composite():
        component1.add(component2)

    print(component1.show_details(), end="")


if __name__ == "__main__":
    # Tạo một nhân viên đơn lẻ
    emp1 = Employee("John Doe", "Developer")
    print("Client: Tôi có một nhân viên đơn lẻ:")
    client_code(emp1)
    print("\n")

    # Tạo một phòng ban và thêm nhân viên vào phòng ban đó
    dev_department = Department("Development")

    emp2 = Employee("Jane Smith", "Senior Developer")
    emp3 = Employee("Emily Davis", "QA Engineer")

    dev_department.add(emp2)
    dev_department.add(emp3)

    print("Client: Tôi có một phòng ban với một số nhân viên:")
    client_code(dev_department)
    print("\n")

    # Tạo một công ty với các phòng ban
    company = Department("Headquarters")

    hr_department = Department("Human Resources")
    hr_department.add(Employee("Alice Brown", "HR Manager"))
    hr_department.add(Employee("Bob Johnson", "Recruiter"))

    company.add(hr_department)
    company.add(dev_department)

    print("Client: Tôi có một công ty với nhiều phòng ban và nhân viên:")
    client_code(company)
    print("\n")

    # Quản lý các thành phần mà không cần quan tâm đến lớp cụ thể của chúng
    print("Client: Tôi có thể thêm một nhân viên vào phòng ban mà không cần biết cụ thể lớp của chúng:")
    client_code2(company, emp1)
