from Crypto.Cipher import AES
from passlib.utils import pbkdf2
from passlib.hash import pbkdf2_sha1
import array
import base64


p = 'MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAO9hLfwp0hmlWudY2AUucaH6SSYxF4brLhAysky2rgVnAgMBAAE'
r = 'MIHCAgEAMA0GCSqGSIb3DQEBAQUABIGtMIGqAgEAAiEA72Et/CnSGaVa51jYBS5xofpJJjEXhusuEDKyTLauBWcCAwEAAQIgFPJNSoQp6qBh0kRscEhuaefaFsbTm5KSwh8qMYY72mECEQD45WVk/JfOY3r8MIYKSnjhAhEA9jY/7/BY1eDk+Jpud4tfRwIRAOTpfjbCBhCg9/TH4A/I7KECECBs3pjD538rYhxXgkreIQsCEDi0lNGxKunBb6Qcx3xMue0'

def encrypt():
    # e = pbkdf2_sha1.hash('999')
    # print(type(e))
    # handlers.
    # a = 'aa'.encode("utf-8")
    # b = '00'.encode("utf-8")
    # print(array.array('B', a))
    # print(array.array('B', b))
    # p = pbkdf2.pbkdf2_hmac('SHA1', a, b, 1, 32)
    # print(base64.b64decode(p))
    # print(array.array('B', p))

    # e = pbkdf2_sha1.hash(a, salt = b, rounds = 1)
    # print(e)
    # print(array.array('B','JghjxQzhI.gwagK8ISASRd748uA'.encode("utf-8")))

    print(array.array('B',p.encode("utf-8")))
    aes = AES.new(p.encode("utf-8"), AES.MODE_CBC)
    decrypt = aes.decrypt('gVIZERpAKxJ36mPqPnyJ1TmX1WvxWfy8DthKDrfQUoU')
    print(decrypt)

def base64Decode(src):
    """

    :param src: base64字符串。NO_PADDING|NO_WRAP
    :return:    types
    """

    lens = len(src)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    return base64.decodestring(src[:lenx].encode("utf-8"))


def base64Encode(src):
    """

    :param src: 字符串
    :return:    base64字符串
    """

    a = base64.encodebytes(src.encode("UTF-8"))
    return str(a, "UTF-8")

encrypt()