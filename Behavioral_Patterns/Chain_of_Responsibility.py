from abc import ABC, abstractmethod


# Interface cho các bộ xử lý (handlers)
class Handler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, _request):
        if self._next_handler:
            return self._next_handler.handle(_request)
        return None


# Bộ xử lý kiểm tra xác thực người dùng
class AuthHandler(Handler):
    def handle(self, _request):
        if not _request.get("authenticated", False):
            print("Người dùng chưa xác thực.")
            return "Yêu cầu bị từ chối: chưa xác thực"
        print("Người dùng đã xác thực.")
        return super().handle(_request)


# Bộ xử lý kiểm tra quyền admin
class AdminHandler(Handler):
    def handle(self, _request):
        if not _request.get("is_admin", False):
            print("Người dùng không có quyền admin.")
            return "Yêu cầu bị từ chối: không có quyền admin"
        print("Người dùng có quyền admin.")
        return super().handle(_request)


# Bộ xử lý kiểm tra dữ liệu hợp lệ
class DataValidationHandler(Handler):
    def handle(self, _request):
        if not _request.get("valid_data", False):
            print("Dữ liệu không hợp lệ.")
            return "Yêu cầu bị từ chối: dữ liệu không hợp lệ"
        print("Dữ liệu hợp lệ.")
        return super().handle(_request)


if __name__ == "__main__":

    # Khởi tạo các bộ xử lý và xâu chuỗi chúng
    auth_handler = AuthHandler()
    admin_handler = AdminHandler()
    data_handler = DataValidationHandler()

    auth_handler.set_next(admin_handler).set_next(data_handler)

    # Tạo yêu cầu và xử lý nó
    request = {
        "authenticated": True,
        "is_admin": True,
        "valid_data": True
    }

    response = auth_handler.handle(request)
    if response:
        print(response)
    else:
        print("Yêu cầu đã được xử lý thành công.")
