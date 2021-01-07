import random 
from time import sleep 
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("http://www.servelelecciones.cl/")

DELAY_QUERY = 0.3


driver.find_element_by_xpath('//li[@ng-click="divEnChile(vistaVertical)"]').click()
sleep(DELAY_QUERY)


seleccion = driver.find_element_by_name("filtro")
seleccion_region = seleccion.find_element_by_id("selRegion")
opciones_region = [x for x in seleccion_region.find_elements_by_tag_name("option")]

lista_uwu = [0, 1, 2, 3, 4 ,5 ,6 ,7]
print(lista_uwu[1:7])
#Son 16 regiones. con 6 workers, deben ser 2, 3 y 1.
#opciones_region[1:7]
#opciones_region[7:13]
#opciones_region[13:17]

for region in opciones_region[1:]:
    break
    print(region.get_attribute("text"))
    region.click()
    sleep(DELAY_QUERY)
    seleccion_comunas = seleccion.find_element_by_id("selComunas")
    opciones_comuna = [x for x in seleccion_comunas.find_elements_by_tag_name("option")]

    for comuna in opciones_comuna[1:]:
        print(comuna.get_attribute("text"))
        comuna.click()
        sleep(DELAY_QUERY)
        seleccion_circ = seleccion.find_element_by_id("selCircunscripcionElectorales")
        opciones_circ = [x for x in seleccion_circ.find_elements_by_tag_name("option")]

        for circ in opciones_circ[1:]:
            print(circ.get_attribute("text"))
            circ.click()
            sleep(DELAY_QUERY)
            seleccion_local = seleccion.find_element_by_id("selLocalesVotacion")
            opciones_local = [x for x in seleccion_local.find_elements_by_tag_name("option")]
            for local in opciones_local[1:]:
                print(local.get_attribute("text"))
                local.click()
                sleep(DELAY_QUERY)
                seleccion_mesa = seleccion.find_element_by_id("selMesasReceptoras")
                opciones_mesa = [x for x in seleccion_mesa.find_elements_by_tag_name("option")]

                for mesa in opciones_mesa[1:]:
                    sleep(DELAY_QUERY*2)
                    print(mesa.get_attribute("text"))
                    tabla = driver.find_element_by_xpath('//table[@class="table table-striped table-condensed table-hover"]')
                    a = tabla.find_element_by_css_selector('tbody')
                    b = tabla.find_element_by_css_selector('tfoot')
                    a_scopes = a.find_elements_by_xpath('//tr[@class="nivelUno ng-scope"]')
                    b_scopes = b.find_elements_by_xpath('//tr[@ng-repeat="item in rows.resumen"]')
                    #Apruebo
                    print(a_scopes[1].text.split(" "))
                    #Rechazo
                    print(a_scopes[3].text.split(" "))
                    #Nulos
                    print(b_scopes[0].text.split(" "))
                    #Blancos
                    print(b_scopes[1].text.split(" "))
                    #Total
                    print(b_scopes[2].text.split(" "))

                    

                #break

            #break

        #break
        
    #break

