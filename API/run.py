import os

config_var = os.getenv('APP_SETTINGS')

from app import create_app
app = create_app(config_var)

if __name__ == "__main__":
    app.run(debug=True)