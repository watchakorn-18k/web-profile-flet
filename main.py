import flet
from flet import (
    AppBar,
    Icon,
    IconButton,
    Page,
    Text,
    colors,
    icons,
    Container,
    alignment,
    Row,
    Column,
    Image,
    TextButton,
    TextField,
    ListView,
    ElevatedButton,
)

import webbrowser


def homepage(page: Page):
    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    container_1 = Container(
        content=Image(
            src=f"https://avatars.githubusercontent.com/u/74919942?v=4",
            fit="cover",
        ),
        alignment=alignment.center,
        height=250,
        margin=-50
    )
    container_2 = Container(
        content=Text("Hi I'm Watchakorn", size=30),
        alignment=alignment.center,
    )
    container_3 = Container(
        content=Text("สวัสดี ผม ชื่อ วัชกร", size=15),
        alignment=alignment.center,
    )
    container_4 = Container(
        content=Row(
            [TextButton(content=Image(
                src=f"https://media.discordapp.net/attachments/585069498986397707/1030030399201615932/unknown.png?width=428&height=428",
                fit="cover",
                height=40, width=40
            ), on_click=lambda e:webbrowser.open('https://github.com/watchakorn-18k')),
                TextButton(content=Image(
                    src=f"https://media.discordapp.net/attachments/585069498986397707/1030031467050455090/unknown.png",
                    fit="cover",
                    height=40, width=40
                ), on_click=lambda e:webbrowser.open('https://dev.to/watchakorn18k'))], alignment="center"),
    )
    image_1 = Container(content=Image(
        src=f"https://media.discordapp.net/attachments/585069498986397707/1030043412516323388/unknown.png?width=428&height=428",
        fit="cover",
        height=300,
        border_radius=20
    ), alignment=alignment.center)

    def Change_Text(e):
        if input_name.value != "":
            t_wel.value = f"Welcome {input_name.value}"
            t_wel.color = colors.GREEN
            input_name.disabled = True
            btn_con.disabled = True
            page.update()
        else:
            input_name.error_text = "Please enter your name !"
            page.update()
    t_wel = Text(value="Welcome to my page", text_align="center", size=30)
    input_name = TextField(
        label="What your name ?", hint_text="Your name", prefix_icon=icons.PERSON
    )
    btn_con = ElevatedButton("Confirm", on_click=Change_Text)

    form_1 = Container(content=Column([
        t_wel, input_name, btn_con
    ], horizontal_alignment="center"), padding=100)
    content_all = [container_1, container_2,
                   container_3, container_4, image_1, form_1]
    for i in content_all:
        lv.controls.append(i)
    page.add(lv)


def main(page: Page):
    page.title = "หน้าแรก"
    page.horizontal_alignment = "center"

    def theme_changed(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

    page.appbar = AppBar(
        leading=Icon(icons.HOME),
        leading_width=40,
        title=Text("หน้าแรก"),
        center_title=False,
        bgcolor=colors.BLACK54,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED, on_click=theme_changed)
        ],
    )
    homepage(page)


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
