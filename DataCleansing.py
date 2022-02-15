import re
from unittest import result
pattern = r'[\d,]+'
text = '$54,321,210'

result = re.search(pattern, text)
print(result)


if result:
    print('清洗成功')
else:
    print('清洗失敗')