import ssl
import OpenSSL

def get_SSL_Expiry_Date(host, port):
    cert = ssl.get_server_certificate((host, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    print(x509.get_notAfter())

lista = (
 "wwwt.connectmed.com.br",
 "wwwt.connectmed.com.br",
 "sispasa.planopasa.com.br",
 "tfd.planopasa.com.br",
 "viacep.com.br",
 "cobranca.planopasa.com.br",
 "intranet.planopasa.com.br",
 "wwwt.connectmed.com.br",
 "smtp.planopasa.com.br",
 "www.saudepasa.com.br",
 )


for item in lista:
    print(item)
    get_SSL_Expiry_Date(item, 443)
