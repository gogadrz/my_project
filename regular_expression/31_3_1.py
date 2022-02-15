import re


def main() -> None:

    text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

    pattern = r'\b[AaEeIiOoUu]\w*'
    pattern2 = r'\b[^AaEeIiOoUu]\w*'

    result = re.findall(pattern, text)
    print(result)

    result2 = re.findall(pattern2, text)
    print(result2)


if __name__ == '__main__':
    main()
