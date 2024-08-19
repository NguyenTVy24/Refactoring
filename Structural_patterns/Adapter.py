class Target:
    """
    Target định nghĩa giao diện để trả về nhiệt độ theo độ C.
    """

    def request(self) -> str:
        return "Target: Nhiệt độ hiện tại theo độ C."


class Adaptee:
    """
    Adaptee sử dụng nhiệt độ theo độ F.
    """

    def specific_request(self) -> str:
        return "Nhiệt độ hiện tại là 77°F"


class Adapter(Target, Adaptee):
    """
    Adapter chuyển đổi nhiệt độ từ độ F sang độ C.
    """

    def request(self) -> str:
        fahrenheit = float(self.specific_request().split()[5][:-2])
        celsius = (fahrenheit - 32) * 5.0/9.0
        return f"Adapter: Nhiệt độ hiện tại là {celsius:.2f}°C"


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Adaptee: ", adaptee.specific_request(), end="\n\n")

    adapter = Adapter()
    client_code(adapter)
