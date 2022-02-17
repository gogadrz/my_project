import requests
import json
import re


def main() -> None:

    url: str = 'http://www.columbia.edu/~fdc/sample.html'

    my_req = requests.get(url)
    data = my_req.text

    result = re.findall(r'<h3.*>(.*)</h3>', data)

    print(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
