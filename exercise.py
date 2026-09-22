# 定義一條 DNA 序列
dna_sequence = "ATGCGTACGTTAGC"

# 計算這條 DNA 的長度
length = len(dna_sequence)

# 印出結果
print("我的第一條 DNA 序列：", dna_sequence)
print("這條序列的長度是：", length)
A_number = dna_sequence.count('A')
print(A_number)

G_number = dna_sequence.count('G')
C_number = dna_sequence.count('C')
GC_percentage = ((C_number + G_number)/length)*100
print('GC 含量百分比為:', GC_percentage, '%')