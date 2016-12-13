import web
from web import form
from datos import Clientes
from datos import Peliculas
render=web.template.render('templates')

urls = (
    '/(.*)', 'index'
)
db = web.database(dbn='mysql', db='pelis', user='root', pw='utec')
Clientes = Clientes()  
Clientes.read()
peliculas=Peliculas()
peliculas.read()

myform = form.Form( 
    form.Dropdown('Cliente', Clientes.getClientes()), 
    form.Dropdown('Pelicula',peliculas.getPeliculas()), 
    form.Dropdown('Formato', ["Blueray","DVD"]),
    form.Dropdown('Tiempo', ["1","2","3","4","5","6","7"])
    
    ) 
class index:
    def GET(self,results):
        form = myform()
        registros=db.select('renta')
        return render.index(form,registros)
        
    def POST(self,results): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            total=0
            if form.d.Formato=="Blueray":
                total=20
            elif form.d.Formato=="DVD":
                total=10
            total=int(form.d.Tiempo)*total
            db.insert('renta',cliente=form.d.Cliente, pelicula=form.d.Pelicula, formato=form.d.Formato, tiempo=form.d.Tiempo,total=total)
            
            datos=db.select('renta')
            return render.index(form,datos)


if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()