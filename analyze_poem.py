import time
start_time = time.time()


def ex1(poem_filename):
    with open(poem_filename, encoding='utf-8') as f:
        only_one_string = []
        s_e = []
        tot_s_e = []
        last_s_e = []
        for word in f.readlines():
            only_one_string.append(word.lower())
        right_string = clean_list(only_one_string)
        for index in range(len(right_string)):
            s_e.append(sound_element(right_string[index]))
            tot_s_e.append(len(s_e[index]))
            last_s_e.append(s_e[index][-1])
        return scheme(last_s_e, tot_s_e), pattern(tot_s_e), tot_s_e, last_s_e


def clean_list(only_one_string):
    i = 0
    only_char = ""
    right_string = []
    no_accent = {224: 97,
                 225: 97,
                 226: 97,
                 227: 97,
                 228: 97,
                 229: 97,
                 232: 101,
                 233: 101,
                 234: 101,
                 235: 101,
                 236: 105,
                 237: 105,
                 238: 105,
                 239: 105,
                 242: 111,
                 243: 111,
                 244: 111,
                 245: 111,
                 246: 111,
                 247: 111,
                 248: 111,
                 249: 117,
                 250: 117,
                 251: 117,
                 252: 117,
                 253: 121,
                 255: 121}
    while i < len(only_one_string):
        for char in only_one_string[i]:
            if char.isalpha():
                only_char += char
            only_one_string[i] = only_char
        right_string.append(only_one_string[i].translate(no_accent))
        only_char = ""
        i += 1
    return right_string


def sound_element(right_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'j', 'y']
    o = 0
    s_e = []
    p = ""
    while o < len(right_string):
        p += right_string[o]
        if right_string[o] in vowels:
            o += 1
            if right_string[o] not in vowels:
                s_e.append(p)
                p = ""
        else:
            o += 1
            if right_string[o - 1] in vowels:
                s_e.append(p)
                p = ""
        if o == len(right_string) - 1:
            s_e.append(p + right_string[o])
            break
    return s_e


def scheme(last_s_e, tot_s_e):
    frequency = {}
    i = 0
    scheme_list = []
    for index in range(len(last_s_e)):
        if (last_s_e[index], tot_s_e[index]) not in frequency:
            scheme_list.append(i)
            frequency[last_s_e[index], tot_s_e[index]] = i
            i += 1
        else:
            scheme_list.append(frequency[last_s_e[index], tot_s_e[index]])
    return scheme_list


def pattern(tot_s_e):
    div = 3
    div_list = []
    while div < len(tot_s_e):
        if len(tot_s_e) % div == 0:
            div_list.append(div)
        div += 1
    a = 0
    index = 0
    while div_list[index] <= len(tot_s_e):
        if tot_s_e[a:div_list[index]] == tot_s_e[div_list[index]:div_list[index] * 2]:
            return div_list[index]
        index += 1

# Inseet here the filename
filename = ""

print(ex1(filename))

print("My program took", time.time() - start_time, "to run")
