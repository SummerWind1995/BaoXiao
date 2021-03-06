#coding=utf8
ADMIN = 0
COMMOM_USER = 1

ROLE_CHOICE = (
    (ADMIN, u'管理员'),
    (COMMOM_USER, u'普通用户')
)

PAYED = 1
UNPAYED = 0

PAY_STATUS = (
    (PAYED, u'已付'),
    (UNPAYED, u'未付')
)

ACCEPTED = 1
UNACCEPTED = 0

ACCEPT_STATUS = (
    (ACCEPTED, u'已接单'),
    (UNACCEPTED, u'未接单')
)


ITEMS = (
    (u'日常办公用品', u'日常办公用品支出,如复印纸，文具等'),
    (u'书报杂志订阅费', u'购买书报杂志，资料册等支出'),
    (u'印刷费', u'打印，复印费，印刷费，版面费，外单位审稿费，专著出版费等'),
    (u'手续费', u'电汇手续费等手续费'),
    (u'邮电费', u'向邮局，快递公司支出的邮寄费'),
    (u'电话费', u''),
    (u'网络通讯费', u''),
    (u'日常交通费', u'本市出租车，公交车，地铁，运费，租车费等'),
    (u'仪器设备维修费', u'除车辆维修费以外的仪器设备维修费'),
    (u'会议费', u'本校承办的会议计划中所列支的费用（附会议计划）'),
    (u'专用材料费', u'硒鼓，墨盒，实验室用品，消耗性体育用品，专用工具和仪器等'),
    (u'科研协作费', u''),
    (u'委托业务费', u'加工费，测试费，图文制作费'),
    (u'学校管理费', u''),
    (u'基层管理费', u''),
    (u'水电费', u''),
    (u'其他事务费', u''),
    (u'租赁费', u'设备租赁费等'),
    (u'专用设备购置', u'购置单价超过1000元的通用设备或单价超过1500元的专用设备'),
    (u'软件购置费', u'构建信息网络方面的费用，单件8000元以上的．．．'),
    (u'住宿费', u''),
)

FIELDS = (
    'office_supplies',
    'book',
    'printing',
    'handling_charge',
    'post',
    'phone',
    'internet',
    'traffic',
    'maintenance',
    'conference',
    'material',
    'cooperation',
    'thirdpart',
    'school_management',
    'base_management',
    'water_electric',
    'other',
    'rent',
    'specific_facility',
    'software',
    'hotel'
)