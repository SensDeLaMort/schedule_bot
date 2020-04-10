import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TOKEN
from parser import Parser
from db_handler import Handler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
handler = Handler()

faculties = {'книит' : 'knt', 'био' : 'bf', 'географак' : 'gf',
		'геолог' : 'gl', 'идпо' : 'idpo',
		'искус' : 'ii', 'физрафак' : 'ifk', 'ифиж' : 'ifg',
		'инхим' : 'ih', 'мехмат' : 'mm', 'соцфак' : 'sf',
		'иняз' : 'fi', 'фнбмт' : 'fn', 'фнп' : 'fnp',
		'психфак' : 'fps', 'пписо' : 'fppso',
		'физфак' : 'ff', 'филфак' : 'fp', 'эконом' : 'ef',
		'юрфак' : 'uf'}


def start(update, context):
	update.message.reply_text('ПРИВЕТ, ПИДАРАС!')
	update.message.reply_text('Бля, брат, введи группу и подгруппу существующую. Будь мужиком, твой рот ебать<3')


def reg(update, context):
	uid = update.message.from_user.id
	args = context.args
	if len(args) != 3:
		update.message.reply_text('Ei, eblo tupoe. Tebe skazali tri argumenta vstavit dolbaeb')
		return()
	group = args[0]
	sub = args[1]
	faculty = args[2].lower()
	if not check_faculty(faculty):
		update.message.reply_text('Podebat reshil?')
	else:
		update.message.reply_text(uid)
		update.message.reply_text('Ti BLYAT uveren, chto ti v {0} gruppe, v {1} podgruppe i s ebanogo {2} faculteta'.format(group, sub, faculty))
		print(f'{uid} {group} {sub} {faculty}')
		handler.add_user(uid, group, sub, faculties[faculty])
		update.message.reply_text('Ya tebya zapomnil')


def help(update, context):
	update.message.reply_text('Just type in your faculty')


#def error(update, context):
#    """Log Errors caused by Updates."""
#    	logger.warning('Update "%s" caused error "%s"', update, context.error)


def parse(update, context):
	user = handler.get_user(update.message.from_user.id)
	if user:
		info = Parser()
		update.message.reply_text(info.get_column(user[1], user[2], user[3]))


def check_faculty(faculty):
	return faculty in faculties.keys()


def main():
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("parse", parse))
	dp.add_handler(CommandHandler("register", reg))
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
