from abc import ABC, abstractmethod


# Interface chung cho các tài liệu. Các lớp thực tế và Proxy đều kế thừa từ đây.
class Document(ABC):
    """
    Giao diện Document khai báo các phương thức chung cho cả RealDocument và Proxy.
    Miễn là client làm việc với Document thông qua giao diện này, bạn có thể truyền vào
    một proxy thay vì đối tượng thực.
    """

    @abstractmethod
    def display_content(self) -> None:
        pass


# Lớp chứa logic thực tế của tài liệu.
class RealDocument(Document):
    """
    RealDocument chứa logic cốt lõi để hiển thị nội dung tài liệu.
    Trong ví dụ thực tế, lớp này có thể thực hiện các tác vụ tốn thời gian như tải tài liệu
    từ cơ sở dữ liệu hoặc từ hệ thống file.
    """

    def __init__(self, file_name: str) -> None:
        self._file_name = file_name
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        # Giả lập quá trình tải tài liệu từ đĩa.
        print(f"RealDocument: Tải tài liệu '{self._file_name}' từ đĩa...")

    def display_content(self) -> None:
        print(f"RealDocument: Hiển thị nội dung của tài liệu '{self._file_name}'.")


# Proxy cho tài liệu, kiểm tra quyền truy cập trước khi hiển thị nội dung.
class DocumentProxy(Document):
    """
    Proxy có cùng giao diện với RealDocument và kiểm tra quyền truy cập trước khi cho phép
    thực hiện phương thức của RealDocument.
    """

    def __init__(self, file_name: str, user_role: str) -> None:
        self._real_document = None
        self._file_name = file_name
        self._user_role = user_role

    def display_content(self) -> None:
        """
        Phương thức chính để kiểm tra quyền truy cập trước khi tải và hiển thị nội dung tài liệu.
        """

        if self._check_access():
            if not self._real_document:
                self._real_document = RealDocument(self._file_name)
            self._real_document.display_content()
        else:
            print(f"Proxy: Quyền truy cập bị từ chối cho tài liệu '{self._file_name}'.")

    def _check_access(self) -> bool:
        """
        Kiểm tra xem người dùng có quyền truy cập tài liệu hay không.
        """

        print("Proxy: Kiểm tra quyền truy cập...")
        # Giả lập việc kiểm tra quyền dựa trên vai trò người dùng.
        if self._user_role == "Admin":
            return True
        else:
            return False


# Mã khách hàng để sử dụng lớp Document thông qua giao diện chung.
def client_code(document: Document) -> None:
    """
    Mã khách hàng làm việc với tất cả các đối tượng (cả đối tượng thực và proxy) thông qua giao diện Document.
    """

    document.display_content()


# Ví dụ sử dụng
if __name__ == "__main__":
    print("Client: Sử dụng RealDocument với quyền Admin:")
    real_document = RealDocument("SecretDocument.pdf")
    client_code(real_document)

    print("")

    print("Client: Sử dụng DocumentProxy với quyền User:")
    proxy_document_user = DocumentProxy("SecretDocument.pdf", "User")
    client_code(proxy_document_user)

    print("")

    print("Client: Sử dụng DocumentProxy với quyền Admin:")
    proxy_document_admin = DocumentProxy("SecretDocument.pdf", "Admin")
    client_code(proxy_document_admin)
