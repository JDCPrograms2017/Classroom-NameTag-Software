from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        # initialize other stuff like the backend logic controller.

        # Creating a label in the MainScreen object to display the user's credentials.
        self.label = Label(text="No Student Logged In", font_size=40)
        self.add_widget(self.label)

        # Creating the button to allow the user to log in.
        self.button = Button(text="Log In", font_size=30, size_hint=(1, 0.3))
        self.button.bind(on_press=self.on_establish_user_login_press)
        self.add_widget(self.button)

    def on_establish_user_login_press(self, instance):
        self.label.text = "LOGGING IN!"
