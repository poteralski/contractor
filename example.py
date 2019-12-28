import ricky
from dataclasses import dataclass


@dataclass
class AirlineUpdate:
    name: str


def handler(message: AirlineUpdate):
    print(f"Airline updated: {message.name}")


if __name__ == '__main__':
    app = ricky.FakeServer(__name__, specification_dir='spec/')
    app.add_server('server.yaml')
    app.run()
