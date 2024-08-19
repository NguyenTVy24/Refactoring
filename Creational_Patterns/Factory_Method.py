from abc import ABC, abstractmethod


class People(ABC):
    """
        Tạo ra một class AbstractClass sở hưu những các hành động chung là say và get_product
        là những Abstractmethod sẽ được định nghĩa ở những class kế thừa.
    """

    @abstractmethod
    def say(self):
        pass

    @property
    @abstractmethod
    def get_product(self):
        pass


class Product(ABC):
    """
        Cũng là một class AbstractClass và có một phương thức get_is_have_product sẽ được định nghĩa
        ở lớp kế thừa.
    """
    @abstractmethod
    def get_is_have_product(self):
        pass


class ManagerProduct(Product):
    """
        Đối với Manager thì sẽ không có Product vì không trực tiếp tham gia sản xuất.
    """
    def get_is_have_product(self):
        print('I am a manager and I don\'t have product')


class EmployeeProduct(Product):
    """
        Đối với Employee thì sẽ có Product vì trực tiếp tham gia sản xuất.
    """
    def get_is_have_product(self):
        print('I am an employee and I have product')


class Manager(People):
    """
        Manager kế thừa Class People, định nghĩa các phương thức đã được khởi tạo trước đó
    """
    def say(self):
        # Vì là manager nên phương thức say sẽ có dạng như sau
        print('I am a manager')

    @property
    def get_product(self) -> Product:
        return ManagerProduct()


class Employee(People):
    """
        Employee kế thừa Class People, định nghĩa các phương thức đã được khởi tạo trước đó
    """
    def say(self):
        print('I am an employee')

    @property
    def get_product(self) -> Product:
        return EmployeeProduct()


if __name__ == '__main__':
    manager = Manager()
    manager.say()
    manager.get_product.get_is_have_product()

    employee = Employee()
    employee.say()
    employee.get_product.get_is_have_product()
