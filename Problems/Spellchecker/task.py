dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = [word for word in input().split() if not dictionary.count(word)]

print("\n".join(words) if len(words) != 0 else "OK")
