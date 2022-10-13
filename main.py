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
    PopupMenuItem,
    PopupMenuButton
)
import i18n as lang


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
        content=Text(lang.t('app.introduce'), size=30),
        alignment=alignment.center,
    )
    container_3 = Container(
        content=Text("porton555@gmail.com", size=15),
        alignment=alignment.center,
    )
    container_4 = Container(
        content=Row(
            [TextButton(content=Image(
                src=f"https://media.discordapp.net/attachments/585069498986397707/1030030399201615932/unknown.png?width=428&height=428",
                fit="cover",
                height=40, width=40
            ), on_click=lambda e:page.launch_url('https://github.com/watchakorn-18k')),
                TextButton(content=Image(
                    src=f"https://media.discordapp.net/attachments/585069498986397707/1030031467050455090/unknown.png",
                    fit="cover",
                    height=40, width=40
                ), on_click=lambda e:page.launch_url('https://dev.to/watchakorn18k'))], alignment="center"),
    )
    image_1 = Container(content=Image(
        src=f"https://media.discordapp.net/attachments/585069498986397707/1030043412516323388/unknown.png?width=428&height=428",
        fit="cover",
        height=300,
        border_radius=20
    ), alignment=alignment.center)

    def Change_Text(e):
        if input_name.value != "":
            t_wel.value = f"{lang.t('app.welcome')} {input_name.value}"
            t_wel.color = colors.GREEN
            input_name.disabled = True
            btn_con.disabled = True
            page.update()
        else:
            input_name.error_text = lang.t('app.error_1')
            page.update()
    t_wel = Text(value=lang.t('app.Welcome_to_my_page'), text_align="center", size=30)
    input_name = TextField(
        label=lang.t('app.ask_1'), hint_text=lang.t('app.hint_1'), prefix_icon=icons.PERSON
    )
    btn_con = ElevatedButton(lang.t('app.confirm'), on_click=Change_Text)

    form_1 = Container(content=Column([
        t_wel, input_name, btn_con
    ], horizontal_alignment="center"), padding=100)
    content_all = [container_1, container_2,
                   container_3, container_4, image_1, form_1]
    for i in content_all:
        lv.controls.append(i)
    page.add(lv)


def main(page: Page):
    lang.load_path.append('i18n')
    lang.set('enable_memoization', True)
    def lang_th(e):
        lang.set('locale', 'th')
        page.controls.pop()
        homepage(page)
        page.appbar.title = Text(lang.t('app.home'))
        page.update()
    def lang_en(e):
        lang.set('locale', 'en')
        page.controls.pop()
        homepage(page)
        page.appbar.title = Text(lang.t('app.home'))
        page.update()

    page.title = lang.t('app.home')
    page.horizontal_alignment = "center"
    

    def theme_changed(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

    page.appbar = AppBar(
        leading=Icon(icons.HOME),
        leading_width=40,
        title=Text(lang.t('app.home')),
        center_title=False,
        bgcolor=colors.BLACK54,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED, on_click=theme_changed),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="ภาษาไทย",on_click=lang_th),
                    PopupMenuItem(text="English",on_click=lang_en)
                ]
            )
            
        ],
    )
    homepage(page)


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
