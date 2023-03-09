data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:  #每讀取一千則才印一次，知道讀取進度
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:                  #現在d為一個字串
    sum_len = sum_len + len(d)  #ex:讀第一筆資料sum_len總數100 = 0 + 100，回去for讀第二筆資料sum_len250 = 100 + 150
                 #每加總一次就印出長度一次
print('平均每筆留言長度是', sum_len/len(data))  #平均每筆留言的字數長度






