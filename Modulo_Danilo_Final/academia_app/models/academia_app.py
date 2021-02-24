from odoo import models, fields
class Academia(models.Model):
    _name = 'academia'
    _description = 'colegio'
    Nombre= fields.Char("Nombre",required=True)
    apellido= fields.Char("Apellidos",required=True)
    DNI= fields.Char("DNI",help="Ejemplo:85697452E")
    Aula = fields.Selection([('aula1', 'Inglés'), ('aula2','Francés'), ('aula3','Portugés'), ('aula4','Alemán')], string= 'Aula')
    notaTra= fields.Selection([('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('7','7'), ('8','8'), ('9','9'), ('10','10')], string= 'Nota Anterior Curso')
    notaFa= fields.Selection([('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('7','7'), ('8','8'), ('9','9'), ('10','10')], string= 'Nota Prueba Acceso')
    
 