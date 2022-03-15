#coding=utf-8
from openerp.osv import fields,osv

class player (osv.osv):
    _name='player.player'
    _columns = {
        #cac thuoc tinh cua lop player
        'name':fields.char('Tên cầu thủ', size=25, required=True, translate=True),
        'portfolio':fields.integer('Tổng số danh hiệu'),
        'coach':fields.char('HLV',size=100, required=True, translate=True),
        'name_club':fields.char('Tên Câu Lạc Bộ',size=100, required=True, translate=True),
        'pos':fields.selection([('td','Tiền đạo'),('tv','Tiền vệ'),
                                 ('hv','Hậu vệ'),('gk','Thủ môn')],'Vị trí'),
        'birthday':fields.datetime('Ngày sinh'),
        'active':fields.boolean('Đang hoạt động ?'),
        'notes':fields.text('Lưu ý')
    }
    _defaults={
        'portfolio':0,
        'active':True
    }
player() #tao 1 the hien cho lop player_player
