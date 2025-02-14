from kivy.app import app
from frontend.homescreen import MainScreen

class NametagApp(app):
    def build(self):
        print("Application started successfully!")
        
        # Create some logic for initiating the frontend display.
        return MainScreen()

if __name__ == "__main__":
    NametagApp().run()