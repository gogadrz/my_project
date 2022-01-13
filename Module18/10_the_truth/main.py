def decode_sym(symbol):
    if symbol.isspace():
        return symbol
    elif symbol == 'A':
        return 'Z'
    elif symbol == 'a':
        return 'z'
    else:
        return chr(ord(symbol) - 1)


def shift_word(word, shift):
    word_lst = list(word)
    for i_shift in range(shift):
        sym = word_lst[-1]
        word_lst.pop(-1)
        word_lst.insert(0, sym)
    return ''.join(word_lst)



message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
message2 = ''
message3 = []
tmp_msg = ''
shift = 3
start_range = 0
end_range = 0

# Преобразуем строку в "правильные" буквы.
for letter in message:
    message2 += ''.join(decode_sym(letter))

# Строку в список

while True:
    end_range = message2.find('.', start_range)
    end_range = message2.find(' ', end_range)
    if end_range != -1:
        message = message2[start_range: end_range]
    else:
        message = message2[start_range:]

    tmp_msg = list(message)
    message3.append(''.join(tmp_msg))
    start_range = end_range

    if end_range == -1:
        break

# Сдвигаем первую строку на 3,
# а каждую следующую на 3 + n.
# Сразу выводим на экран.
for string in message3:
    words = string.split()
    for word in words:
        print(shift_word(word, shift), end=' ')
    shift += 1
    print()
