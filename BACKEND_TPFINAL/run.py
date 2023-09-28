from app import init_app
from config import Config

if __name__ == "__main__":
    app = init_app()
    app.config.from_object(Config)
    app.run()