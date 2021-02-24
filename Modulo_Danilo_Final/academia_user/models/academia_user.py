from odoo import api, fields, models
class Academia_User(models.Model):
    _name = 'academia'
    _inherit = ['academia','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Fecha inscripcion')
    cursos = fields.Selection([('nivel1', 'B1'), ('nivel2','B2'), ('nivele3','C1'), ('nivel','C2')], string= 'Nivel')
    trabajo_fin=fields.Boolean('ESO')
    fNumerosa=fields.Boolean('Familia Numerosa')
    desempleado=fields.Boolean('Desempleado')
    sEscolar=fields.Boolean('Seguro Académico')
    contacto=fields.Char("Numero de telefono",required=True)
    email=fields.Char("Email",required=True)
    horas_curso = fields.Integer('Horas total del curso')
    def do_marcar(self):
        if self.trabajo_fin>5:
            raise Exception('¿Cursó la ESO?')
        else:
            return False
    def de_marcar(self):
        if self.fNumerosa:
            raise Exception('¿Familia numerosa?')
        else:
            return False
    def de_marcar(self):
        if self.desempleado:
            raise Exception('¿Desempleado?')
        else:
            return False
    def de_marcar(self):
        if self.sEscolar:
            raise Exception('¿Seguro Escolar?')
        else:
            return False