from odoo import api, fields, models
class Academia_User(models.Model):
    _name = 'academia'
    _inherit = ['academia','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Fecha inscripcion')
    cursos=fields.Char("Cursos")
    trabajo_fin=fields.Boolean('TFG')
    contacto=fields.Char("Numero de telefono")
    email=fields.Char("Email")
    horas_curso = fields.Integer('Horas total del curso')
    def do_marcar(self):
        if self.trabajo_fin>5:
            raise Exception('Has aprobado')
        else:
            return False