#!/usr/bin/env python

import unittest
import re


def urlBatata(url):
    url_elements = url[8:].split('/')

    if url[0:7] =='http://' and url_elements[0][-4:] == ".com":
        return True
    return False
    #check = re.search('http:\/\/.*\.com[\.|\/| ]?', url)
    #if check:
    #    return True
    #else:
    #    return False  

def dataFromUrl(url):
    try:
        protocolo, resto = url.split('://')
    except ValueError:
        return None
    restos = resto.split('/')
    host = ""
    dominio = ""
    path = ""
    parametros = ""

    if 'www'in restos[0]:
        host = 'www'
        dominio = restos[0][4:]
    else:
        dominio = restos[0]
    restos = restos[1:]

    if len(restos) > 0 and "=" in restos[-1]:
        parametros = restos[-1]
        restos = restos[:-1]

    path = "/".join(restos)

    return  {"protocolo": protocolo, "host": host, "domínio":dominio, "path": path,"parametros": parametros}

class DojoTestCase(unittest.TestCase):
    def test_http_potato(self):
        self.assertIsNone(dataFromUrl('http:/sssas.sasa'))

    def test_http_real(self):
        self.assertEqual(dataFromUrl('http://gmail.com'), 
            {"protocolo": "http", "host": "", "domínio":"gmail.com", "path": "","parametros": "" }
        )

    def test_http_real_with_path(self):
        self.assertTrue(urlBatata('http://gmail.com/dojo'))

    def test_http_real_realissimo(self):
        self.assertFalse(urlBatata('http://gmail'))

    def test_http_real_ponto_coms(self):
        self.assertFalse(urlBatata('http://gmail.coms'))

    def test_data_shape(self):
        self.assertEqual(
            dataFromUrl('http://gmail.com/dojo'),
            {"protocolo": "http", "host": "", "domínio":"gmail.com", "path": "dojo","parametros": "" }
        )

    def test_url_completa(self):
        self.assertEqual(
            dataFromUrl("http://www.google.com/mail/test/user=fulano"),
            {"protocolo": "http", "host": "www", "domínio":"google.com", "path": "mail/test","parametros": "user=fulano" }
        )

if __name__ == "__main__":
    unittest.main()
