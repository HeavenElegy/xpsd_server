from Crypto.Cipher import AES
from Crypto.Cipher import AES
from passlib.utils import pbkdf2
from passlib.hash import pbkdf2_sha1
import array
import base64
import codecs


# 原始明文密钥
DEFAULT_REW_KEY = 'com.xiaopao.zhongrong.workassistant.develop' # TODO 需要转移到更安全的地方
# 加密盐
SALT = 'MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAJ0lH07sM7+yGiuJUQ4sjpftsdpyQ6G4LqYANiViMMlrAgMBAAE='    # TODO 需要转移到更安全的地方

def encrypt(plaintext):
    """
    AES加密

    :param plaintext:   明文字符串

    :return:    Base64密文字符串

    """
    # 获取key
    key = getKeyBytes()
    # print("密钥=>", array.array('b',key))

    # 重构输入值。CBC模式下，明文长度必须是16的倍数
    # btyes = plaintext.encode("UTF-8")
    bytes = bytearray(plaintext, "UTF-8")
    length = 16
    count = len(bytes)
    y = count % length
    if y!=0:
        for i in range(0, 16 - y):
            bytes.append(0)
    # print("明文=>", array.array('b', bytes))

    # 构造向量
    vi = key[:16]
    # print("向量:", array.array('b', vi))

    # 创建加密实例
    aes = AES.new(key,AES.MODE_CBC, vi)

    # 进行加密
    e = aes.encrypt(bytes)
    # print("密文=>", array.array('b', e))
    # print("密文=>", base64Encode(e))

    # 返回Base64编码密文
    return base64Encode(e)


def decrypt(ciphertext):
    """
    AES解密

    :param ciphertext:  base64加密的密文

    :return:    解密后的字节。自行解析
    """
    # 解除Base64
    btyes = base64Decode(ciphertext)
    # 获取Key
    key = getKeyBytes()

    # 构造向量
    vi = key[:16]

    # 获取操作实例
    aes = AES.new(key, AES.MODE_CBC, vi)

    # 调用返回bytes
    result = aes.decrypt(btyes)
    for i in range(len(result), 0, -1):
        if result[i-1] != 0:
            result = result[0:i]
            break
    return result



def decryptToString(ciphertext):
    """
    AES解密

    :param ciphertext:  base64加密的密文

    :return:    明文字符串
    """

    # 调用实现方法
    btyes = decrypt(ciphertext)

    # 返回字符串
    return btyes.decode("UTF-8")





def getKeyBytes():
    """
    获取key的方法

    :return:    key
    """

    global DEFAULT_REW_KEY
    global SALT

    # 这是明文密钥
    a = DEFAULT_REW_KEY.encode("utf-8")
    # 盐
    b = base64Decode(SALT)

    # 制作pbkdf2_hmaxsha1密钥
    bytes = pbkdf2.pbkdf2_hmac('SHA1', a, b, 1000, 32)
    return bytes;


def base64Decode(src):
    """
    Base64解码
    :param src: base64字符串。NO_PADDING|NO_WRAP
    :return:    types
    """

    # lens = len(src)
    # lenx = lens - (lens % 4 if lens % 4 else 4)
    return base64.decodebytes(src.encode("UTF-8"))


def base64Encode(src):
    """
    Base4编码
    :param src: 字符串
    :return:    base64字符串
    """
    if type(src)==bytes:
        a = base64.encodebytes(src)
    else:
        a = base64.encodebytes(src.encode("UTF-8"))
    return str(a, "UTF-8")
