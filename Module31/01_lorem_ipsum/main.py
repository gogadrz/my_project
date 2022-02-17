from typing import List, ClassVar
import re


def main() -> None:
    text: str = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
    nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
    Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
    """

    pattern: ClassVar = re.compile(r'\b\w{4}\b')
    result: List[str] = re.findall(pattern, text)

    print('Все совпадения по шаблону:', result)


if __name__ == '__main__':
    main()
