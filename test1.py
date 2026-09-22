# 1. 打開 my_gene.fasta 檔案
with open('my_gene.fasta','r') as file:
    # 讀取第一行（這是 Header，例如 >seq1...）
    header = file.readline()

    # 讀取第二行（這才是真正的 DNA 序列）
    sequence = file.readline().strip()

# 2. 印出我們得到了什麼
print('讀取到的基因標頭:', header)
print('讀取到的序列內容:', sequence)

# 3. 計算長度
print('序列長度為:', len(sequence))

# 練習寫出GC含量
GC_percentage = (sequence.count('G') + sequence.count('C')) /len(sequence)
print('該基因的GC含量為:', GC_percentage*100, '%')
# 迴圈
