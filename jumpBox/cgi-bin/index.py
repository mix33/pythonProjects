import cgi
import MySQLdb as sql
#import MySQLdb as sql

data = cgi.FieldStorage()
##########cpu###########
if data.has_key('userTime'):
	value_usrtime = data['userTime'].value
else:
	value = 'usrtime not found'
if data.has_key('systemTime'):
	value_systime = data['systemTime'].value
else:
	value = 'systime not found'
if data.has_key('waitIo'):
	value_waitio = data['waitIo'].value
else:
	value = 'waitIo not found'
if data.has_key('idle'):
	value_idle = data['idle'].value
else:
	value = 'idle not found'
######memory############
if data.has_key('total'):
	value_total = data['total'].value
else:
	value = 'total not found'
if data.has_key('used'):
	value_used = data['used'].value
else:
	value = 'used not found'
if data.has_key('free'):
	value_free = data['free'].value
else:
	value = 'free not found'
if data.has_key('buffers'):
	value_buffers = data['buffers'].value
else:
	value = 'buffers not found'
if data.has_key('cached'):
	value_cached = data['cached'].value
else:
	value = 'cached not found'
#####random disk#######
if data.has_key('device'):
	value_device = data['device'].value
else:
	value = 'device not found'
if data.has_key('mountpoint'):
	value_mountpoint = data['mountpoint'].value
else:
	value = 'mountpoint not found'
if data.has_key('fstype'):
	value_fstype = data['fstype'].value
else:
	value = 'fstype not found'
if data.has_key('opts'):
	value_opts = data['opts'].value
else:
	value = 'opts not found'
if data.has_key('read_ct'):
	value_read_ct = data['read_ct'].value
else:
	value = 'read_ct not found'
if data.has_key('read_bt'):
	value_read_bt = data['read_bt'].value
else:
	value = 'read_bt not found'
if data.has_key('read_t'):
	value_read_t = data['read_t'].value
else:
	value = 'read_t not found'
######random ps########
if data.has_key('ps_name'):
	value_ps_name = data['ps_name'].value
else:
	value = 'ps_name not found'
if data.has_key('ps_cwd'):
	value_ps_cwd = data['ps_cwd'].value
else:
	value = 'ps_cwd not found'
if data.has_key('ps_time'):
	value_ps_time = data['ps_time'].value
else:
	value = 'ps_time not found'
if data.has_key('ptime'):
	value_ptime = data['ptime'].value
else:
	value = 'ptime not found'
#######################################################

values = [value_usrtime, value_systime, value_waitio, value_idle]
values_m = [value_total,value_used,value_free,value_buffers,value_cached]
values_d = [value_device,value_mountpoint,value_fstype,value_opts,value_read_ct,value_read_bt,value_read_t]
values_p = [value_ps_name,value_ps_cwd,value_ps_time,value_ptime]
con = sql.connect(user = 'root',passwd = 'asdqwe123',db = 'cpu',host = 'localhost')
cur = con.cursor()
###will return error table exists while still can be written####
cur.execute("create table if not exists cpu(id int primary key auto_increment, cpu char(50), systime char(50), waitio char(50), idle char(50))")
cur.execute("create table if not exists memory(id int primary key auto_increment, total char(50), used char(50), free char(50), buffers char(50), cached char(50))")
cur.execute("create table if not exists disk(id int primary key auto_increment, device char(50), mountpoint char(50), fstype char(50), opts char(50), readcount char(50), readbytes char(50), readtime char(50))")
cur.execute("create table if not exists process(id int primary key auto_increment, name char(50), path char(50), status char(50), time char(50))")
##################################################
cur.execute("insert into cpu(cpu,systime,waitio, idle) values(%s,%s,%s,%s)", values)
cur.execute("insert into memory(total,used,free,buffers,cached) values(%s,%s,%s,%s,%s)", values_m)
cur.execute("insert into disk(device,mountpoint,fstype,opts,readcount,readbytes,readtime) values(%s,%s,%s,%s,%s,%s,%s)", values_d)
cur.execute("insert into process(name,path,status,time) values(%s,%s,%s,%s)", values_p)



con.commit()
cur.close()
con.close()
