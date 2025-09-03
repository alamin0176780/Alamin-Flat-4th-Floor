# Kivy থেকে প্রয়োজনীয় জিনিসগুলো ইমপোর্ট করছি
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# আমাদের মূল অ্যাপ ক্লাস
class RentApp(App):
    def build(self):
        # ভিউ (UI) এর জন্য BoxLayout (উপর নিচে সাজানো)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # ভাড়াটিয়াদের ডাটা (নাম : কত টাকা বাকি)
        tenants = {
            "লিটন/মিদুল ভাই": 3670,
            "জুবায়ের ভাই": 2817,
            "জয় ভাই": 6517,
            "তানভীর ভাই": 5134
        }

        # প্রত্যেক ভাড়াটিয়ার জন্য লেবেল তৈরি করা
        for name, due in tenants.items():
            info = f"{name} - {due}৳ বাকি"
            layout.add_widget(Label(text=info, font_size=20))

        return layout

# প্রোগ্রাম রান করার জন্য
if __name__ == "__main__":
    RentApp().run()
