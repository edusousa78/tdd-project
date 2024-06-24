
from fastapi import FastAPI
from store1.core.config import settings




class App(FastAPI):
    def __init__(self, *args, **Kwargs) -> None:
        super().__init__(
            *args, 
            **Kwargs, 
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH

        )



app = App()
