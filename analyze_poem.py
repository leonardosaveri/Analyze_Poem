import time
import unidecode
import re

start_time = time.time()


def clean_list(lines):
    lines = [re.sub(r'[^A-Za-zÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖØÙÚÛÜÝŸàáâãäåèéêëìíîïòóôõöøùúûüýÿ]', '', file) for file in lines]
    for i in range(len(lines)):
        lines[i] = unidecode.unidecode(lines[i])
    return list(map(lambda s: s.lower(), lines))



def find_se(lines):
    se = ""
    final_se = []
    cnt = []
    for i in range(len(lines)):
        line = lines[i]
        c = 0
        count = 0
        for letter in line:
            if c + 2 > len(line):
                se += letter
                final_se.append(se)
                count += 1
                break
            if letter not in ['a', 'e', 'i', 'o', 'u', 'j', 'y']:
                se += letter
            else:
                if line[c+1] not in ['a', 'e', 'i', 'o', 'u', 'j', 'y']:
                    se += letter
                    se = ''
                    count += 1
                else:
                    se += letter
            c += 1
        cnt.append(count)
        se = ''
    return final_se, cnt


def prosodic_structure(final_se):
    l = final_se
    structure = [None] * len(l)
    c = 1
    for i in range(len(structure)):
        if None not in structure:
            break
        if isinstance(structure[i], int):
            continue
        for d in range(i):
            if l[i] == l[d]:
                structure[i] = structure[d]
        for h in range(len(structure)):
            if structure[h] is None:
                structure[h] = c
                c += 1
                break
    return structure


def check_pattern(cnt):
    # return [len(cnt[:i]) for i in range(3, len(cnt) // 2) if len(cnt) % i == 0 and cnt[:i] * (len(cnt) // i) == cnt]
    for i in range(3, len(cnt) // 2):
            if len(cnt) % i == 0 and cnt[:i] * (len(cnt) // i) == cnt:
                return len(cnt[:i])

filename = "poem.txt"

lines = open(filename).read().splitlines()
final_se, cnt = find_se(clean_list(lines))
print(f"prosody: {prosodic_structure(cnt)}\n module: {check_pattern(cnt)}\n lengths: {cnt}\n finals: {final_se}")

print("My program took", time.time() - start_time, "to run")
