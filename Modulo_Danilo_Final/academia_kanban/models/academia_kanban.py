from odoo import models, fields
class Academia(models.Model):
    _inherit = 'academia'
    priority = fields.Selection([
                                ('0','Bajo'),
                                ('1','Normal'),
                                ('2','Alto')], 'Prioridad',default='1')
    kanban_state = fields.Selection([
                                    ('normal', 'Ultimo año'),
                                    ('blocked', 'Cursando'),
                                    ('done', 'Finalizado')],'Kanban State', default='normal')