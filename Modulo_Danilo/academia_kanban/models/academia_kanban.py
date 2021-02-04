from odoo import models, fields
class Academia(models.Model):
    _inherit = 'academia'
    priority = fields.Selection([
                                ('0','Bajo'),
                                ('1','Normal'),
                                ('2','Alto')], 'Prioridad',default='1')
    kanban_state = fields.Selection([
                                    ('normal', 'En progreso'),
                                    ('blocked', 'Bloqueado'),
                                    ('done', 'Listo para el siguiente')],'Kanban State', default='normal')