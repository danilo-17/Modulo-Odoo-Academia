from odoo import models, fields
class Academia(models.Model):
    _name = 'academia'
    _description = 'colegio'
    Nombre= fields.Char("Nombre Alumnos")
    DNI= fields.Char("DNI")
    Aula = fields.Selection([('aula1', 'Aula 1'), ('aula2','Aula 2'), ('aula3','Aula 3'), ('aula4','Aula 4')], string= 'Aula')
    notaTra= fields.Selection([('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('7','7'), ('8','8'), ('9','9'), ('10','10')], string= 'Nota Anterior Curso')
    notaFa= fields.Selection([('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('7','7'), ('8','8'), ('9','9'), ('10','10')], string= 'Nota Prueba Acceso')