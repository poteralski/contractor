import yaml
import importlib


class FakeServer:
    def __init__(self, app_name, specification_dir):
        self.specification_dir = specification_dir
        self.app_name = app_name

    def add_server(self, spec_file):
        with open(f"{self.specification_dir}/{spec_file}", "r") as f:
            self.y = yaml.load(f)

    def run(self):

        print(self.y)

        for queue, details in self.y['channels'].items():
            print(f"subscribing into queue: {queue}")
            location = details['subscribe']['operationId']

            module_name, method_name = location.split(".")
            module = importlib.import_module(module_name)
            method = getattr(module, method_name)
            message = method.__annotations__["message"]
            message_spec = details['subscribe']['message']

            for expected_key, data in message_spec.items():
                has = message.__annotations__.get(expected_key)
                if not has:
                    print(f"missing {expected_key}")
            print(message)
