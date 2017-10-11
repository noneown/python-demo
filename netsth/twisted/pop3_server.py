from poplib import POP3_SSL

rec_svr = POP3_SSL('pop.qq.com', 995)
tuser = 'xxxxxxxxxxx@qq.com' #mail address
rec_svr.user(tuser)
rec_svr.pass_('xxxxxxxxxx') #auth code
rsp, msg, size = rec_svr.retr(rec_svr.stat()[0])
sep = msg.index('')
rec_body = msg[sep + 1:]
print rec_body