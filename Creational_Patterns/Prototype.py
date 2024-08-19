import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Book:
    """
    Lớp `Book` mô phỏng một quyển sách với các thuộc tính như tiêu đề, nội dung
    và một đối tượng tham chiếu tự thân.
    """

    def __init__(self, title, content, circular_ref):
        self.title = title
        self.content = content
        self.circular_ref = circular_ref

    def __copy__(self):
        """
        Tạo một bản sao nông. Phương thức này sẽ được gọi khi gọi `copy.copy`
        và trả về bản sao nông của đối tượng hiện tại.
        """
        circular_ref_copy = copy.copy(self.circular_ref)
        new = self.__class__(
            self.title, self.content, circular_ref_copy
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        """
        Tạo một bản sao sâu. Phương thức này sẽ được gọi khi gọi `copy.deepcopy`
        và trả về bản sao sâu của đối tượng hiện tại.

        Tham số `memo` là từ điển được sử dụng để ngăn chặn việc sao chép lặp lại
        vô tận trong trường hợp có tham chiếu vòng.
        """
        if memo is None:
            memo = {}

        circular_ref_copy = copy.deepcopy(self.circular_ref, memo)
        new = self.__class__(
            self.title, copy.deepcopy(self.content, memo), circular_ref_copy
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


class Library:
    """
    Lớp `Library` mô phỏng một thư viện chứa danh sách các quyển sách.
    """

    def __init__(self, books):
        self.books = books

    def __copy__(self):
        """
        Tạo một bản sao nông của thư viện. Chỉ tạo bản sao nông của danh sách sách.
        """
        books_copy = copy.copy(self.books)
        return Library(books_copy)

    def __deepcopy__(self, memo=None):
        """
        Tạo một bản sao sâu của thư viện. Tạo bản sao sâu của từng quyển sách trong danh sách.
        """
        if memo is None:
            memo = {}
        books_copy = copy.deepcopy(self.books, memo)
        return Library(books_copy)


if __name__ == "__main__":
    # Khởi tạo danh sách sách với một đối tượng tự tham chiếu
    circular_ref = SelfReferencingEntity()
    book1 = Book("Book One", "Content of Book One", circular_ref)
    book2 = Book("Book Two", "Content of Book Two", circular_ref)
    circular_ref.set_parent(book1)
    original_library = Library([book1, book2])

    # Sao chép nông thư viện
    shallow_copied_library = copy.copy(original_library)
    shallow_copied_library.books[0].content = "Modified Content of Book One"

    # Sao chép sâu thư viện
    deep_copied_library = copy.deepcopy(original_library)
    deep_copied_library.books[1].content = "Modified Content of Book Two"

    # Kiểm tra kết quả
    print("Original library book contents:")
    for book in original_library.books:
        print(f"- {book.title}: {book.content}")

    print("\nShallow copied library book contents:")
    for book in shallow_copied_library.books:
        print(f"- {book.title}: {book.content}")

    print("\nDeep copied library book contents:")
    for book in deep_copied_library.books:
        print(f"- {book.title}: {book.content}")

    # Kiểm tra tham chiếu tự thân sau khi sao chép sâu
    print(
        f"\nid(deep_copied_library.books[0].circular_ref.parent): "
        f"{id(deep_copied_library.books[0].circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_library.books[1].circular_ref.parent): "
        f"{id(deep_copied_library.books[1].circular_ref.parent)}"
    )
    print(
        "^^ Điều này cho thấy rằng các đối tượng đã được sao chép sâu có cùng một tham chiếu."
    )
