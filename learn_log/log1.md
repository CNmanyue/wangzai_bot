x=10//3         # x 是商的整数部分
x=10%3         # x 是余数

DES算法的入口参数有三个：Key、Data、Mode  
- Key为7个字节共56位，是DES算法的工作密钥；  
- Data为8个字节64位，是要被加密或被解密的数据；  
- Mode为DES的工作方式,有两种:加密或解密  

填充算法(Pkcs5、Pkcs7)
PKCS5Padding与PKCS7Padding基本上是可以通用的。在PKCS5Padding中，明确定义Block的大小是8位，而在PKCS7Padding定义中，对于块的大小是不确定的，可以在1-255之间（块长度超出255的尚待研究），填充值的算法都是一样的：

```python
pad = k - (l mod k) #k=块大小，l=数据长度，如果k=8， l=9，则需要填充额外的7个byte的7
```

因为DES算法的Data为64位，所以填充时，数据块大小应该设置为64

```python

# 字节转十六进制
binascii.a2b_hex(hexlify)
# 十六进制转字节
binascii.b2a_hex(data)
# 十六进制转字符
b''.hex()

```

 

