# Для определения формата мы можем использовать один из следующих кодов форматирования:
#
#     %a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются английские наименования)
#     %A: день недели полностью, например, Wednesday
#     %b: аббревиатура названия месяца. Например, Oct (сокращение от October)
#     %B: название месяца полностью, например, October
#     %d: день месяца, дополненный нулем, например, 01
#     %m: номер месяца, дополненный нулем, например, 05
#     %y: год в виде 2-х чисел
#     %Y: год в виде 4-х чисел
#     %H: час в 24-х часовом формате, например, 13
#     %I: час в 12-ти часовом формате, например, 01
#     %M: минута
#     %S: секунда
#     %f: микросекунда
#     %p: указатель AM/PM
#     %c: дата и время, отформатированные под текущую локаль
#     %x: дата, отформатированная под текущую локаль
#     %X: время, форматированное под текущую локаль
#
# Используем различные форматы:
#
# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))             # 2017-05-03
# print(now.strftime("%d/%m/%Y"))             # 03/05/2017
# print(now.strftime("%d/%m/%y"))             # 03/05/17
# print(now.strftime("%d %B %Y (%A)"))        # 03 May 2017 (Wednesday)
# print(now.strftime("%d/%m/%y %I:%M"))       # 03/05/17 01:36

from datetime import datetime

now = datetime.now()
print(now.strftime("%d.%b.%Y %H:%M:%S"))
