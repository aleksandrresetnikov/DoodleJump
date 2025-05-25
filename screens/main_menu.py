from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from screens.screen_base import ScreenBase
from settings_manager import settings_instance


class MainMenu(ScreenBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = None
        self.init_components()

    def init_components(self):
        self.clear_widgets()

        layout = self.create_layout()
        self.add_widget(layout)

    def create_layout(self):
        layout = FloatLayout()

        self.background = Image(source='assets/background/Default.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        play_button = Button(
            text="Играть",
            color=(255, 255, 255),
            on_press=self.start_game,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.28, 'y': 0.58},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )
        market_button = Button(
            text="Скины",
            color=(255, 255, 255),
            on_press=self.open_market,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.28, 'y': 0.50},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )
        stats_button = Button(
            text="Статистика",
            color=(255, 255, 255),
            on_press=self.open_rating,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.28, 'y': 0.42},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )
        exit_button = Button(
            text="Выход",
            color=(255, 255, 255),
            on_press=self.exit_game,
            size_hint=(0.28, 0.053),
            pos_hint={'center_x': 0.28, 'y': 0.34},
            background_normal='assets/buttons/button_common.png',
            background_down='assets/buttons/button_common_press.png'
        )

        logo = Image(
            source='assets/promo/logo_main.png',
            keep_ratio=False,
            x=-65,
            y=260
        )

        layout.add_widget(logo)
        layout.add_widget(play_button)
        layout.add_widget(market_button)
        layout.add_widget(stats_button)
        layout.add_widget(exit_button)
        return layout

    def on_enter(self):
        skin_name = settings_instance.get_select_theme()
        self.background.source=f'assets/background/{skin_name}.png'
        self.background.reload()

    def start_game(self, instance):
        self.manager.current = "game"  # Переключение на игру

    def open_market(self, instance):
        self.manager.current = "market"  # Переключение на игру

    def open_rating(self, instance):
        self.manager.current = "rating_menu" # Переключение на меню списка лидеров

    def exit_game(self, instance):
        exit(0)
