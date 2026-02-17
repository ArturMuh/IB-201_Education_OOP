class Document:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self._content = content
        self.__audit_log = []

    def read(self) -> str:
        return self._content

    def history(self) -> tuple[str, ...]:
        return tuple(self.__audit_log)

    def _log(self, event: str) -> None:
        self.__audit_log.append(event)

