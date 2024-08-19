from abc import ABC, abstractmethod


# Định nghĩa giao diện Builder
class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_cpu(self, cpu: str) -> None:
        pass

    @abstractmethod
    def set_ram(self, ram: str) -> None:
        pass

    @abstractmethod
    def set_storage(self, storage: str) -> None:
        pass

    @abstractmethod
    def set_gpu(self, gpu: str) -> None:
        pass

    @abstractmethod
    def set_display(self, display: str) -> None:
        pass


# Định nghĩa lớp sản phẩm (Computer)
class Computer:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Computer parts: {', '.join(self.parts)}", end="")


class ComputerBuilder(Builder):
    def __init__(self) -> None:
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = Computer()

    @property
    def product(self) -> Computer:
        product = self._product
        self.reset()
        return product

    def set_cpu(self, cpu: str) -> None:
        self._product.add(f"CPU: {cpu}")

    def set_ram(self, ram: str) -> None:
        self._product.add(f"RAM: {ram}")

    def set_storage(self, storage: str) -> None:
        self._product.add(f"Storage: {storage}")

    def set_gpu(self, gpu: str) -> None:
        self._product.add(f"GPU: {gpu}")

    def set_display(self, display: str) -> None:
        self._product.add(f"Display: {display}")


# Định nghĩa lớp Director
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, _builder: Builder) -> None:
        self._builder = _builder

    def build_basic_computer(self) -> None:
        self.builder.set_cpu("Intel i3")
        self.builder.set_ram("8GB")
        self.builder.set_storage("256GB SSD")

    def build_gaming_computer(self) -> None:
        self.builder.set_cpu("Intel i9")
        self.builder.set_ram("32GB")
        self.builder.set_storage("1TB SSD")
        self.builder.set_gpu("NVIDIA RTX 3080")
        self.builder.set_display("27-inch 144Hz")

    def build_workstation_computer(self) -> None:
        self.builder.set_cpu("AMD Ryzen 9")
        self.builder.set_ram("64GB")
        self.builder.set_storage("2TB NVMe SSD")
        self.builder.set_gpu("NVIDIA Quadro RTX 5000")
        self.builder.set_display("32-inch 4K")


# Sử dụng mẫu thiết kế Builder
if __name__ == "__main__":
    director = Director()
    builder = ComputerBuilder()
    director.builder = builder

    print("Basic Computer: ")
    director.build_basic_computer()
    builder.product.list_parts()

    print("\n")

    print("Gaming Computer: ")
    director.build_gaming_computer()
    builder.product.list_parts()

    print("\n")

    print("Workstation Computer: ")
    director.build_workstation_computer()
    builder.product.list_parts()

    print("\n")

    # Sử dụng Builder mà không cần Director
    print("Custom Computer: ")
    builder.set_cpu("Intel i7")
    builder.set_ram("16GB")
    builder.set_storage("512GB SSD")
    builder.set_display("24-inch")
    builder.product.list_parts()
