import flet as ft

# منوی کافه با قیمت‌ها
menu = {
    'قهوه': {
        'اسپرسو': 20000,
        'کاپوچینو': 25000,
        'موکا': 30000
    },
    'چای': {
        'چای سیاه': 15000,
        'چای سبز': 18000,
        'چای نعنا': 17000
    },
    'شیرینی': {
        'کیک شکلاتی': 30000,
        'کیک وانیلی': 25000,
        'ماکارون': 20000
    }
}

def main(page: ft.Page):
    page.title = "کافه"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # ایجاد Dropdown برای انتخاب منو
    dropdown = ft.Dropdown(
        label="انتخاب کنید:",
        options=[ft.dropdown.Option(f"{category}: {item} - {price} تومان") 
                 for category, items in menu.items() 
                 for item, price in items.items()],
        on_change=lambda e: update_label(dropdown.value)
    )

    # لیبل برای نمایش انتخاب
    selected_label = ft.Text("شما انتخاب نکرده‌اید.", size=20)
    price_label = ft.Text("", size=20)

    # تابع برای به‌روزرسانی لیبل
    def update_label(selected_item):
        if selected_item:
            item_details = selected_item.split(" - ")
            item_name = item_details[0]
            price = item_details[1]

            selected_label.value = f"شما انتخاب کردید: {item_name}"
            price_label.value = f"قیمت: {price}"
        else:
            selected_label.value = "شما انتخاب نکرده‌اید."
            price_label.value = ""
        page.update()

    # دکمه تأیید سفارش
    confirm_button = ft.ElevatedButton(
        text="تأیید سفارش",
        on_click=lambda e: confirm_order(dropdown.value)
    )

    # تابع برای تأیید سفارش
    def confirm_order(selected_item):
        if selected_item:
            page.add(ft.Text(f"سفارش شما با موفقیت ثبت شد: {selected_item}"))
        else:
            page.add(ft.Text("لطفاً یک گزینه انتخاب کنید."))

    # افزودن عناصر به صفحه
    page.add(dropdown, selected_label, price_label, confirm_button)

# اجرای برنامه
ft.app(target=main)

    