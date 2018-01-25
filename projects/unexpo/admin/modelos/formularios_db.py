# -*- coding: utf-8 -*-
try:
 from ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Formularios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Formularios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Formularios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Formularios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Formularios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Post-de-Formulario').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Post-de-Formulario').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Post-de-Formulario').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Post-de-Formulario').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Post-de-Formulario').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Formularios').insertar('Rental Prospects', [[{'opcion': 0, 'Logo': 'img-admin', 'opciones': 'archivos', 'name': 'logo', 'value': 0}, {'Rental Prospects': 'text-admin', 'name': 'titulo', 'value': 'Rental Prospects'}, {'1- Name and Last Name': 'text', 'name': 'last_name', 'value': ''}, {'2- Phone Number': 'text-phone', 'name': 'phone', 'value': ''}, {'3- Email Adress': 'text-email', 'name': 'email', 'value': ''}, {'opcion': 1, 'opciones': 'formularios', '4- Size of Apartment': 'select', 'value': 0, 'name': 'size_apartment'}, {'opcion': 0, '5- Does the person have a Section 8 Voucher or any other payment assistance?': 'select', 'opciones': 'main', 'name': 'voucher_payment', 'value': 0}, {'5.1-If so, of how much?': 'number', 'name': 'si_voucher_payment', 'value': '0'}, {'descripcion': '# of Adults & # of Children (+ ages)', '7.-How many people will be living in the apartment?': 'text', 'name': 'live_pest', 'value': ''}, {'8.-Will you have pets living in the apartment?': 'number', 'name': 'pest_in_apartment', 'value': '0'}, {'opcion': 0, 'opciones': 'main', 'name': 'any_evictions', 'value': 0, '9.-Have the person had any evictions?': 'select'}, {'opcion': 0, 'opciones': 'main', '10.- Do you have a criminal record?': 'select', 'value': 0, 'name': 'criminal_record'}, {'If so, when?': 'text', 'name': 'when', 'value': ''}, {'opcion': 0, 'opciones': 'main', 'name': 'what_type', 'value': 0, '11.- If so, what type?': 'select'}, {'Note': 'textarea', 'name': 'note', 'value': ''}]], {'Formulario': 0}, '19/7/2017 16:24:50', [])
db('Opciones').insertar('Antecedentes criminales', ['', 'Misdemeanor', 'Felony'])
db('Opciones').insertar('Tama\xc3\xb1o de los apartamentos', ['', 'Studio', '1 Bedroom 1 Bath', '2 Bedroom 1 Bath (1.5 Bath)', '2 Bedroom 2 Bath', '3 Bedroom 2 Bath'])
db('Post-de-Formulario').insertar('Rental Prospects 1', [{'value': '0', 'name': 'id', 'Formulario': 'hidden-id'}, [{'opcion': 0, 'Logo': 'img-admin', 'opciones': 'archivos', 'name': 'logo', 'value': 0}, {'Rental Prospects': 'text-admin', 'name': 'titulo', 'value': 'Rental Prospects'}, {'1- Name and Last Name': 'text', 'name': 'last_name', 'value': ''}, {'2- Phone Number': 'text-phone', 'name': 'phone', 'value': ''}, {'3- Email Adress': 'text-email', 'name': 'email', 'value': ''}, {'opcion': 1, 'opciones': 'formularios', '4- Size of Apartment': 'select', 'value': 0, 'name': 'size_apartment'}, {'opcion': 0, '5- Does the person have a Section 8 Voucher or any other payment assistance?': 'select', 'opciones': 'main', 'name': 'voucher_payment', 'value': 0}, {'5.1-If so, of how much?': 'number', 'name': 'si_voucher_payment', 'value': 0}, {'descripcion': '# of Adults & # of Children (+ ages)', '7.-How many people will be living in the apartment?': 'text', 'name': 'live_pest', 'value': ''}, {'8.-Will you have pets living in the apartment?': 'number', 'name': 'pest_in_apartment', 'value': 0}, {'opcion': 0, 'opciones': 'main', 'name': 'any_evictions', 'value': 1, '9.-Have the person had any evictions?': 'select'}, {'opcion': 0, 'opciones': 'main', '10.- Do you have a criminal record?': 'select', 'value': 0, 'name': 'criminal_record'}, {'If so, when?': 'text', 'name': 'when', 'value': ''}, {'opcion': 0, 'opciones': 'main', 'name': 'what_type', 'value': 0, '11.- If so, what type?': 'select'}, {'Note': 'textarea', 'name': 'note', 'value': 'ok'}]], {'Post-de-Formulario': 0}, '29/8/2017 23:32:19', [])
db.load=True
db.load=False
