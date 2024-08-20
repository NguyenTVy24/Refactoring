from typing import Dict


class Character:
    """
    Lớp Character đại diện cho một ký tự cụ thể trong văn bản. Lớp này sử dụng
    Flyweight để chia sẻ dữ liệu chung giữa các ký tự giống nhau.
    """

    def __init__(self, symbol: str) -> None:
        # Ký tự được chia sẻ giữa các đối tượng Character.
        self._symbol = symbol

    def display(self, font_size: int) -> None:
        """
        Phương thức hiển thị ký tự với kích thước phông chữ cụ thể (trạng thái ngoại lai).
        """
        print(f"Character: {self._symbol} displayed in font size {font_size}.")


class CharacterFactory:
    """
    Nhà máy Character quản lý các đối tượng Character. Nó đảm bảo rằng mỗi ký tự
    chỉ được tạo một lần và được chia sẻ giữa các đối tượng khi cần.
    """

    _characters: Dict[str, Character] = {}

    def get_character(self, symbol: str) -> Character:
        """
        Trả về đối tượng Character với ký tự cho trước. Nếu chưa tồn tại, tạo mới.
        """
        if symbol not in self._characters:
            print(f"CharacterFactory: Creating new character for symbol '{symbol}'.")
            self._characters[symbol] = Character(symbol)
        else:
            print(f"CharacterFactory: Reusing existing character for symbol '{symbol}'.")

        return self._characters[symbol]

    def list_characters(self) -> None:
        """
        Hiển thị danh sách các ký tự hiện đang được quản lý bởi nhà máy.
        """
        count = len(self._characters)
        print(f"CharacterFactory: Currently managing {count} characters:")
        print(", ".join(self._characters.keys()))


class Document:
    """
    Lớp Document đại diện cho một tài liệu văn bản chứa nhiều ký tự. Nó sử dụng
    CharacterFactory để quản lý và hiển thị các ký tự trong tài liệu.
    """

    def __init__(self) -> None:
        self._characters = []
        self._factory = CharacterFactory()

    def add_character(self, symbol: str, font_size: int) -> None:
        """
        Thêm một ký tự vào tài liệu với kích thước phông chữ cụ thể.
        """
        character = self._factory.get_character(symbol)
        self._characters.append((character, font_size))

    def display(self) -> None:
        """
        Hiển thị toàn bộ tài liệu với các ký tự và kích thước phông chữ tương ứng.
        """
        for character, font_size in self._characters:
            character.display(font_size)

    @property
    def factory(self):
        return self._factory


if __name__ == "__main__":
    # Tạo một tài liệu văn bản mới.
    document = Document()

    # Thêm các ký tự vào tài liệu với kích thước phông chữ khác nhau.
    document.add_character('H', 12)
    document.add_character('e', 12)
    document.add_character('l', 12)
    document.add_character('l', 14)  # Chữ 'l' được tái sử dụng nhưng với kích thước khác.
    document.add_character('o', 12)

    # Hiển thị tài liệu.
    document.display()

    # Hiển thị danh sách các ký tự hiện đang được quản lý bởi nhà máy.
    document.factory.list_characters()
