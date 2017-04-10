from __future__ import absolute_import

import json
import os
from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1024, 768)
        self.browser.implicitly_wait(5000)

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_2_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(os.path.abspath('persona.jpg'))

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_3_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_4_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(10)

        login_usuario = self.browser.find_element_by_id('id_username_login')
        login_usuario.send_keys('juan645')

        login_clave = self.browser.find_element_by_id('id_password_login')
        login_clave.send_keys('clave123')

        botonIngresar = self.browser.find_element_by_id('btn_login')
        botonIngresar.click()

        label_usuario = self.browser.find_element_by_id('username')

        self.assertIn('Juan Daniel', label_usuario.text)

    def test_5_editar(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        login_usuario = self.browser.find_element_by_id('id_username_login')
        login_usuario.send_keys('juan645')

        login_clave = self.browser.find_element_by_id('id_password_login')
        login_clave.send_keys('clave123')

        botonIngresar = self.browser.find_element_by_id('btn_login')
        botonIngresar.submit()

        time.sleep(4)

        self.browser.find_element_by_id('id_editar').click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Juan Daniel Editado')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(os.path.abspath('persona.jpg'))

        botonGrabar = self.browser.find_element_by_id('id_editar')
        botonGrabar.click()

        span = self.browser.find_element_by_id('username')
        self.assertIn('Juan Daniel Editado', span.text)

    def test_6_comentar(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        login_usuario = self.browser.find_element_by_id('id_username_login')
        login_usuario.send_keys('juan645')

        login_clave = self.browser.find_element_by_id('id_password_login')
        login_clave.send_keys('clave123')

        botonIngresar = self.browser.find_element_by_id('btn_login')
        botonIngresar.submit()

        self.browser.find_element_by_id('id_ircomentar').click()

        nombre = self.browser.find_element_by_id('id_texto')
        nombre.clear()
        nombre.send_keys('Comentario de prueba')

        apellidos = self.browser.find_element_by_id('id_correo')
        apellidos.clear()
        apellidos.send_keys('jd.patino1@uniandes.edu.co')

        botonGrabar = self.browser.find_element_by_id('id_guardar_comentario')
        botonGrabar.click()

        self.browser.get("http://localhost:8000/mostrarTodosComentarios")
        comentarios_json_lista = json.loads(self.browser.find_element_by_tag_name('body').text)
        comentarios_json_string = " ".join(str(x) for x in comentarios_json_lista)
        self.assertIn('Comentario de prueba', comentarios_json_string)