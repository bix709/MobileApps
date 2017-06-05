import os
import sys
from kivy.app import App

loginscreen_properties = {
    'background_image': "adventureskiing/graphics/loginscreen.jpg"
}

loginbutton_properties = {
    'background_normal': "adventureskiing/graphics/blue_snow.png",
    'text': "Zaloguj",
    'color': (0, 0, 0, 0.4),
    'size_hint_y': 0.30,
    'font_size': 25
}
credential_label_properties = {
    'color': (0, 0, 0, 1),
    'size_hint_y': 0.30,
    'font_size': 30
}

action_button_properties = {
    'background_down': 'adventureskiing/graphics/red_down.png',
    'color': (1, 1, 1, 1)
}
action_prev_properties = {
    'app_icon': 'adventureskiing/graphics/red_normal.png',
    'app_icon_width': 0.1,
    'size_hint_x': None,
    'width': 0,
    'with_previous': False

}

action_bar_properties = {
    'action_prev_properties': action_prev_properties,
    'background_image': 'adventureskiing/graphics/red_normal.png',
    'pos_hint': {'x': 0, 'y': 0.9},
    'size_hint_y': 0.1
}

todayscreen_properties = {
    'background_image': 'adventureskiing/graphics/bg.jpg',
    'name': 'Dzis',
    'buttons_properties': {'background_normal': 'adventureskiing/graphics/blue_snow.png'},
    'dropdown_buttons_properties': {'background_normal': 'adventureskiing/graphics/yellow_snow.png'}
}

calendarscreen_properties = {
    'background_image': 'adventureskiing/graphics/bg.jpg',
    'name': 'Kalendarz',
    'calendar_properties': {'month_header_font_color': (0, 0, 0, 1),
                            'days_header_font_color': (0, 0, 0, 1),
                            'days_button_color': (1, 1, 1, 1)}
}

dailyscreen_properties = {
    'background_image': 'adventureskiing/graphics/bg.jpg',
    'name': 'Grafik',
    'header_font_color': (0, 0, 0, 1),
    'busy_buttons_properties': {'background_normal': 'adventureskiing/graphics/red_snow.png'},
    'configuration_buttons_properties': {'background_normal': 'adventureskiing/graphics/yellow_snow.png'}
}

maintenancescreen_properties = {
    'background_image': 'adventureskiing/graphics/bg.jpg',
    'name': 'Opcje',
    'buttons_properties': {'background_normal': 'adventureskiing/graphics/yellow_snow.png'}
}

earningscreen_properties = {
    'background_image': 'adventureskiing/graphics/loginscreen.jpg',
    'name': 'Zarobki',
    'header_font_color': (0, 0, 0, 1),
    'buttons_properties': {'background_normal': 'adventureskiing/graphics/yellow_snow.png'},
    'dropdown_buttons_properties': {'background_normal': 'adventureskiing/graphics/blue_snow.png'}
}
carousel_with_actionbar_properties = {
    'action_button_properties': action_button_properties,
    'action_bar_properties': action_bar_properties
}
