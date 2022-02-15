import re


def main() -> None:

    text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

    pattern = r'\b[AaEeIiOoUu]\w*'
    pattern2 = r'\b[^ AaEeIiOoUu]\S*'

    result = re.findall(pattern, text)
    print(result)

    result2 = re.findall(pattern2, text)
    print(result2)

    print('*' * 60)

    text_3 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
    result_3 = re.findall(r'\d{2}-\d{2}-\d{4}', text_3)
    print(result_3)


if __name__ == '__main__':
    main()
