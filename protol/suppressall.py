class SuppressAll:
    def __enter__(self) -> None:
        pass

    def __exit__(self, *args, **kwargs) -> bool:
        return True

