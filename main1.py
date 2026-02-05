class Car:
    is_engine_on: bool = False

    def drive(self, city):
        if (self.is_engine_on):
            print(f'Едем в город {city}')
        else:
            print('Двигатель не заведен, стоим')

сar = Car()
# сar.is_engine_on = True
сar.drive('Москва')

# Инкапсуляция - это сокрытие внутренней реализации за счет государствеенных