from ..models import Measurement
from ..models import Variable


#GetAll
def get_measurements():
    measurements=Measurement.objects.all()
    return measurements

#GetByID
def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

#Crear   
def create_measurement(var):
    variable = Variable.objects.get(pk=var['variable'])
    measurement = Measurement(
        variable = variable,
        value = var['value'],
        unit = var['unit'],
        place = var['place'])

    measurement.save()
    return measurement

#Cambiar
def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)

    measurement.variable = Variable.objects.get(pk=new_var["variable"])
    measurement.value = new_var["value"]
    measurement.unit = new_var['unit']
    measurement.place = new_var['place']
    
    measurement.save() 
    return measurement

#Delete
def delete_measurement(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()
    return measurement


