# def find_food(*args, regularize=None, reduce=None):
#     list_res = []
#
#     for i in args:
#         sep = list(map(int, i.split()))
#         sep_len = len(sep)
#         cr_zn = sum(sep) / sep_len
#         min_s = min(list(filter(lambda x: x > cr_zn, sep)))
#
#         if reduce:
#             list_res.append((sep_len, min_s // reduce))
#         else:
#             list_res.append((sep_len, min_s))
#
#     if regularize is True:
#         list_res = sorted(list_res)
#
#     elif regularize is False:
#         list_res = sorted(list_res, reverse=True)
#
#     return list_res

# def fast_and_high(*args, key_sort=None, words_number=None):
#
#     res_list = []
#     max_string = []
#     for i in args:
#
#         kmax = 0
#         if words_number and len(i) > words_number:
#             for j in i:
#                 adict = {}
#                 #adict[j] = []
#                 for x in j.split():
#
#                     adict[x] = []
#                     if j not in adict[x]:
#                         adict[x] += x
#                     kmax = max(kmax, len(adict[x]))
#                     max_string.append(adict[x])
#                 res_list.append((len(j.split()), kmax))
#         else:
#             for j in i:
#                 adict = {}
#                 #adict[j] = []
#                 for x in j.split():
#                     adict[x] = []
#                     if j not in adict[x]:
#                         adict[x] += x
#
#                     kmax = max(kmax, len(adict[x]))
#                     max_string.append(adict[x])
#                 res_list.append((len(j.split()), kmax))
#     return adict
def fast_and_high(*args, key_sort=None, words_number=None):
    result = []
    for arg in args:
        words = arg.split()
        if words_number is not None and len(words) < words_number:
            continue

        max_letters = 0
        max_word = ''
        for word in words:
            unique_letters = set(word)
            if len(unique_letters) > max_letters:
                max_letters = len(unique_letters)
                max_word = word
        result.append((len(words), max_word))
    if key_sort is True:
        result.sort()
    elif key_sort is False:
        result.sort(reverse=True)
    return result

#data = ['He should know that flying fast is easier than flying slow', 'He should know that flying high is easier than flying low', 'A white man can not fly that high', 'White is lagging behind']

data = ['All day long the white goose Martin flew level with the whole flock', 'as if he had never been a domestic goose', 'it was as if he had been flying all his life', 'And where did he get such a rush']
print(*fast_and_high(*data, key_sort=False, words_number=9))


