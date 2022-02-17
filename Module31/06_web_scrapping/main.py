import requests
import json
import re
from typing import ClassVar


def main() -> None:

    url: str = 'http://www.columbia.edu/~fdc/sample.html'

    my_req: ClassVar = requests.get(url)
    data: str = my_req.text

    result: list = re.findall(r'<h3.*>(.*)</h3>', data)

    print(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
