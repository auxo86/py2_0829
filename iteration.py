# encoding=UTF-8
import itertools

result = itertools.chain('abc', '123', u'甲乙丙')
print [item for item in result]
# permutations是順序有關的
result2 = itertools.permutations('AKQJ',2)
list3 = [item for item in result2]
print len(list3), list3
# combinations是順序無關
result3 = itertools.combinations('abcde', 3)
list4 = [item for item in result3]
print len(list4), list4