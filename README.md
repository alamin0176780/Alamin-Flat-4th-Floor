# Alamin-Flat-4th-Floor
Flat rent info app
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class RentApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # ভাড়াটিয়াদের ডাটা (নাম : বাকি টাকা)
        tenants = {
            "লিটন/মিদুল ভাই": 3670,
            "জুবায়ের ভাই": 2817,
            "জয় ভাই": 6517,
            "তানভীর ভাই": 5134,
        }

        # টাইটেল
        layout.add_widget(Label(text="🏠 Flat Rent Info", font_size=24))

        total_due = 0

        # প্রত্যেক ভাড়াটিয়ার বাকি ভাড়া দেখানো
        for name, due in tenants.items():
            total_due += due
            if due > 0:
                text = f"{name} → {due} টাকা বাকি"
            else:
                text = f"{name} → সব ভাড়া পরিশোধ করা হয়েছে ✅"
            layout.add_widget(Label(text=text, font_size=18))

        # মোট যোগফল দেখানো
        layout.add_widget(Label(text=f"\nমোট বাকি ভাড়া: {total_due} টাকা", font_size=20, bold=True))

        return layout


if __name__ == "__main__":
    RentApp().run()
