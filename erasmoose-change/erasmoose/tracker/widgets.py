import re
from django import forms
from django.template.loader import render_to_string


class GoogleMapPointWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        lat, lng = "60.170771", "24.938469"
        if value:
            lat, lng = value.replace(" ", "").split(',')

        html = render_to_string('tracker/google_map_point_widget.html', {
            'id': attrs['id'],
            'base_lat': lat,
            'base_lng': lng,
        })

        return super(GoogleMapPointWidget, self) \
            .render(name, value, attrs) + html
