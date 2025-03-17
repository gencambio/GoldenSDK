
class Cuenta:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cuenta = self.session.get("cuenta")
        if not cuenta:
            ceunta= self.session["cuenta"] = {}
        
        self.cuenta  = cuenta

    
    def agregar(self, gasto):
        if(str(gasto.id)not in self.cuenta.keys()):
            self.cuenta[gasto.id]={
                "gasto_id": gasto.id,
                "concepto": gasto.conceptonombre,
                "costo" : str(gasto.costo),
                "categoria" : gasto.categoria,
                "proveedor" : gasto.proveedor,
                
            }
        
        self.guardar_carro()

    def guardar_carro(self):
        self.session["cuenta"] = self.cuenta
        self.session.modified = True    

   
            