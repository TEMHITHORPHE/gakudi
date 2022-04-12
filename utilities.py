import base64
from typing import IO


def convertImageToBase64Blob(imageBlob:IO[bytes]):
    enc = base64.b64encode(imageBlob.read());
    enc = enc.decode('utf8')
    return enc;