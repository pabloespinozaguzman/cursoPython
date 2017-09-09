class cliente(object):
    estado_cuenta= None
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __len__(self):
        return self.edad

    def __str__(self):
        # return self.nombre + '' + self.apellidos
        # return ''.join((self.nombre, self.apellidos),)
        # dato = 'cliente: %s %s' % (self.nombre, self.apellidos)
        return self.getNombres()

    def getNombres(self):
        return ''.join((self.nombre, self.apellidos), )

    @property
    def nombres(self):
        return ''.join((self.nombre, self.apellidos), )

if __file__ == '__main__':
    cliente = cliente('Jose','Ramirez', edad='28')
    print(cliente.edad)
    print(cliente.nombres, len(cliente))