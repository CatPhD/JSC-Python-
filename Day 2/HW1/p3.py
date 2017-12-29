Bits = int(input("사운드의 비트(Bits)를 입력하세요: "))
Hz = int(input("사운드의 Sampling Rates(Hz)를 입력하세요: "))
Length = float(input("사운드의 길이(Min)를 입력하세요: "))
Type = int(input("사운드의 종류를 입력하세요(Mono:1, Stereo:2): "))
B = Bits*Hz*Length*60*Type/8
KB = B//2**10
MB = KB//2**10

print(Bits, "bit, ",Hz, "Hz, ",Length, "분, ",Type, "채널 무압축 사운드의 용량은", sep='')
print("{:,.0f} B, {:,.0f} KB, {:,.0f} MB 입니다.".format(B, KB, MB))
