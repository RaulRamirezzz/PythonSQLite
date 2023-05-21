import sqlite3

conexion = sqlite3.connect('Ejemplo.db')
c= conexion.cursor()

c.execute("INSERT INTO acciones VALUES('10/oct/2016', 'compra', 'INV', 100, 15.43)")
c.execute("INSERT INTO acciones VALUES('16/ene/2017', 'venta', 'INV', 2100, 20.25)")
c.execute("INSERT INTO acciones VALUES('22/sep/2016', 'compra', 'INV', 300, 10.00)")
c.execute("INSERT INTO acciones VALUES('05/may/2017', 'venta', 'INV', 400, 25.76)")
c.execute("INSERT INTO acciones VALUES('30/dic/2016', 'venta', 'INV', 500, 17.17)")

conexion.commit()
conexion.close()