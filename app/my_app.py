import datetime
import httpx
from rich.text import Text
from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Static, Button
from textual.containers import VerticalScroll, Horizontal, Vertical
from textual import log

miasta = ["Lublin", "Warsaw", "Sacramento", "Tokyo"]


def on_mount(self) -> None:
    log("Data: ",datetime.date)
    log("Bartosz Brudkowski")
    log("Port: 8090")


class WeatherApp(App):
    CSS_PATH = "weather.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Input(placeholder="Enter a City")
                with VerticalScroll(id="button-list"):
                    for miasto in miasta:
                        yield Button(miasto, id=miasto, variant='primary')
            
            with VerticalScroll(id="weather-container"):
                yield Static(id="weather")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.run_worker(self.update_weather(event.button.id), exclusive=True)

    async def on_input_changed(self, message: Input.Changed) -> None:
        self.run_worker(self.update_weather(message.value), exclusive=True)

    async def update_weather(self, city: str) -> None:
        weather_widget = self.query_one("#weather", Static)
        if city:
            # Query the network API
            url = f"https://wttr.in/{city}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                weather = Text.from_ansi(response.text)
                weather_widget.update(weather)
        else:
            weather_widget.update("")



if __name__ == "__main__":
    app = WeatherApp()
    app.run()




