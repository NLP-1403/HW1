from spacing import Spacing
import json

with open('crawling/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# refine all
i = 0
for item in data:
    sp = Spacing()
    i += 1
    item['content'] = sp.fix(item['content'])
    if i % 10 == 0:
        print(i)

with open('processed_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
