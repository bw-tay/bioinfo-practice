# 1. 準備一個空字串，用來收集所有的 DNA 字母
full_sequence = ''

# 2. 打開檔案
with open('test_gene2.fasta', 'r') as file:
    # 用 for 迴圈逐行讀取檔案
    for line in file:
        # 先剃除每一行結尾的換行符號
        clean_line = line.strip()

        #判斷:如果這一行不是以 > 開頭，代表他是序列!
        if not clean_line.startswith('>'):
            full_sequence = full_sequence = full_sequence + clean_line

# 3. 檢查組裝成果
print('完整合併後的 DNA 序列:')
print(full_sequence)
print('總長度為:', len(full_sequence))