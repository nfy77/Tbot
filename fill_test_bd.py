import sqlite3

def create_test_tables(connect, cursor): 
    cursor.execute("""CREATE TABLE IF NOT EXISTS test_head(
                   test_id INTEGER primary key,
                   type TEXT,
                   text_id INTEGER
                   )""")
    connect.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS test_ques(
                   ques_id INTEGER,
                   test_id INTEGER,
                   text_id INTEGER,
                   PRIMARY KEY(ques_id,test_id)                   
                   )""")
    connect.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS test_answ(
                   answ_id INTEGER,
                   ques_id INTEGER,
                   test_id INTEGER,                   
                   score INTEGER,
                   text_id INTEGER,
                   PRIMARY KEY(answ_id,ques_id,test_id)
                   )""")
    connect.commit()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS test_text(
                   text_id INTEGER primary key,
                   text TEXT
                   )""")
    connect.commit()    

def insert_test_head(connect, cursor, test_id, test_type, text_id):
    try:
        sqlite_insert = """INSERT INTO test_head
                           (test_id, type, text_id)
                            VALUES (?, ?, ?);"""
    
        data_tuple = (test_id, test_type, text_id)
        cursor.execute(sqlite_insert, data_tuple)
        connect.commit()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_test_text(connect, cursor, text_id, text):
    try:
        sqlite_insert = """INSERT INTO test_text
                           (text_id, text)
                           VALUES (?, ?);"""
    
        data_tuple = (text_id, text)
        cursor.execute(sqlite_insert, data_tuple)
        connect.commit()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_test_ques(connect, cursor, ques_id, test_id, text_id):
    try:
        sqlite_insert = """INSERT INTO test_ques
                           (ques_id, test_id, text_id)
                           VALUES (?, ?, ?);"""
    
        data_tuple = (ques_id, test_id, text_id)
        cursor.execute(sqlite_insert, data_tuple)
        connect.commit()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def insert_test_answ(connect, cursor, answ_id, ques_id, test_id, score, text_id):
    try:
        sqlite_insert = """INSERT INTO test_answ
                           (answ_id, ques_id, test_id, score, text_id)
                           VALUES (?, ?, ?, ?, ?);"""
    
        data_tuple = (answ_id, ques_id, test_id, score, text_id)
        cursor.execute(sqlite_insert, data_tuple)
        connect.commit()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        
# Объявление и инициализация объектов БД
# подключение к бд
connect = sqlite3.connect('bd.db')
cursor = connect.cursor()

create_test_tables(connect, cursor)

#Шкала депрессии Бека
insert_test_head(connect, cursor, 1000, 'Шкала депрессии Бека', 9000000)
insert_test_text(connect, cursor, 9000000, """Шкала депрессии Бека (Beck Depression Inventory) предложена А.Т. Беком в 1961 г. и разработана на ос­нове клинических наблюдений, позволив­ших выявить ограниченный набор наиболее реле­вантных и значимых симптомов депрессии и наиболее часто предъявляемых пациентами жалоб. После соотнесения этого списка параметров с клиниче­скими описаниями депрессии, содержащимися в соотвествующей литературе, был разработан опросник, включающий в себя 21 категорию симпто­мов и жалоб.
В этом опроснике содержатся группы утверждений. Внимательно прочитайте каждую группу утверждений. Затем определите в каждой группе одно утверждение, которое лучше всего соответствует тому, как Вы себя чувствовали НА ЭТОЙ НЕДЕЛЕ И СЕГОДНЯ. Поставьте галочку около выбранного утверждения. Если несколько утверждений из одной группы кажутся Вам одинаково хорошо подходящими, то поставьте галочки около каждого из них. Прежде, чем сделать свой выбор, убедитесь, что Вы прочли Все утверждения в каждой группе""")
#1
insert_test_ques(connect, cursor, 1, 1000, 9000010)
insert_test_text(connect, cursor, 9000010, """Настроение""")
insert_test_answ(connect, cursor, 1, 1, 1000, 0, 9000011)
insert_test_text(connect, cursor, 9000011, """Я не чувствую себя расстроенным, печальным.""")
insert_test_answ(connect, cursor, 2, 1, 1000, 1, 9000012)
insert_test_text(connect, cursor, 9000012, """Я расстроен.""")
insert_test_answ(connect, cursor, 3, 1, 1000, 2, 9000013)
insert_test_text(connect, cursor, 9000013, """Я все время расстроен и не могу от этого отключиться.""")
insert_test_answ(connect, cursor, 4, 1, 1000, 3, 9000014)
insert_test_text(connect, cursor, 9000014, """Я настолько расстроен и несчастлив, что не могу это выдержать.""")
#2
insert_test_ques(connect, cursor, 2, 1000, 9000020)
insert_test_text(connect, cursor, 9000020, """Пессимизм""")
insert_test_answ(connect, cursor, 1, 2, 1000, 0, 9000021)
insert_test_text(connect, cursor, 9000021, """Я не тревожусь о своем будущем.""")
insert_test_answ(connect, cursor, 2, 2, 1000, 1, 9000022)
insert_test_text(connect, cursor, 9000022, """Я чувствую, что озадачен будушим.""")
insert_test_answ(connect, cursor, 3, 2, 1000, 2, 9000023)
insert_test_text(connect, cursor, 9000023, """Я чувствую, что меня ничего не ждет в будущем.""")
insert_test_answ(connect, cursor, 4, 2, 1000, 3, 9000024)
insert_test_text(connect, cursor, 9000024, """Мое будущее безнадежно, и ничто не может измениться к лучшему.""")
#3
insert_test_ques(connect, cursor, 3, 1000, 9000030)
insert_test_text(connect, cursor, 9000030, """Чувство несостоятельности""")
insert_test_answ(connect, cursor, 1, 3, 1000, 0, 9000031)
insert_test_text(connect, cursor, 9000031, """Я не чувствую себя неудачником.""")
insert_test_answ(connect, cursor, 2, 3, 1000, 1, 9000032)
insert_test_text(connect, cursor, 9000032, """Я чувствую, что терпел больше неудач, чем другие люди.""")
insert_test_answ(connect, cursor, 3, 3, 1000, 2, 9000033)
insert_test_text(connect, cursor, 9000033, """Когда я оглядываюсь на свою жизнь, я вижу в ней много неудач.""")
insert_test_answ(connect, cursor, 4, 3, 1000, 3, 9000034)
insert_test_text(connect, cursor, 9000034, """Я чувствую, что как личность я - полный неудачник.""")
#4
insert_test_ques(connect, cursor, 4, 1000, 9000040)
insert_test_text(connect, cursor, 9000040, """Неудовлетворенность""")
insert_test_answ(connect, cursor, 1, 4, 1000, 0, 9000041)
insert_test_text(connect, cursor, 9000041, """Я получаю столько же удовлетворения от жизни, как раньше.""")
insert_test_answ(connect, cursor, 2, 4, 1000, 1, 9000042)
insert_test_text(connect, cursor, 9000042, """Я не получаю столько же удовлетворения от жизни, как раньше.""")
insert_test_answ(connect, cursor, 3, 4, 1000, 2, 9000043)
insert_test_text(connect, cursor, 9000043, """Я больше не получаю удовлетворения ни от чего.""")
insert_test_answ(connect, cursor, 4, 4, 1000, 3, 9000044)
insert_test_text(connect, cursor, 9000044, """Я полностью не удовлетворен жизнью. и мне все надоело.""")
#5
insert_test_ques(connect, cursor, 5, 1000, 9000050)
insert_test_text(connect, cursor, 9000050, """Чувство вины""")
insert_test_answ(connect, cursor, 1, 5, 1000, 0, 9000051)
insert_test_text(connect, cursor, 9000051, """Я не чувствую себя в чем-нибудь виноватым.""")
insert_test_answ(connect, cursor, 2, 5, 1000, 1, 9000052)
insert_test_text(connect, cursor, 9000052, """Достаточно часто я чувствую себя виноватым.""")
insert_test_answ(connect, cursor, 3, 5, 1000, 2, 9000053)
insert_test_text(connect, cursor, 9000053, """Большую часть времени я чувствую себя виноватым.""")
insert_test_answ(connect, cursor, 4, 5, 1000, 3, 9000054)
insert_test_text(connect, cursor, 9000054, """Я постоянно испытываю чувство вины.""")
#6
insert_test_ques(connect, cursor, 6, 1000, 9000060)
insert_test_text(connect, cursor, 9000060, """Ощущение, что буду наказан""")
insert_test_answ(connect, cursor, 1, 6, 1000, 0, 9000061)
insert_test_text(connect, cursor, 9000061, """Я не чувствую, что могу быть наказанным за что-либо.""")
insert_test_answ(connect, cursor, 2, 6, 1000, 1, 9000062)
insert_test_text(connect, cursor, 9000062, """Я чувствую, что могу быть наказан.""")
insert_test_answ(connect, cursor, 3, 6, 1000, 2, 9000063)
insert_test_text(connect, cursor, 9000063, """Я ожидаю, что могу быть наказан.""")
insert_test_answ(connect, cursor, 4, 6, 1000, 3, 9000064)
insert_test_text(connect, cursor, 9000064, """Я чувствую себя уже наказанным.""")
#7
insert_test_ques(connect, cursor, 7, 1000, 9000070)
insert_test_text(connect, cursor, 9000070, """Отвращение к самому себе""")
insert_test_answ(connect, cursor, 1, 7, 1000, 0, 9000071)
insert_test_text(connect, cursor, 9000071, """Я не разочаровался в себе.""")
insert_test_answ(connect, cursor, 2, 7, 1000, 1, 9000072)
insert_test_text(connect, cursor, 9000072, """Я разочаровался в себе.""")
insert_test_answ(connect, cursor, 3, 7, 1000, 2, 9000073)
insert_test_text(connect, cursor, 9000073, """Я себе противен.""")
insert_test_answ(connect, cursor, 4, 7, 1000, 3, 9000074)
insert_test_text(connect, cursor, 9000074, """Я себя ненавижу.""")
#8
insert_test_ques(connect, cursor, 8, 1000, 9000080)
insert_test_text(connect, cursor, 9000080, """Идеи самообвинения""")
insert_test_answ(connect, cursor, 1, 8, 1000, 0, 9000081)
insert_test_text(connect, cursor, 9000081, """Я знаю, что я не хуже других.""")
insert_test_answ(connect, cursor, 2, 8, 1000, 1, 9000082)
insert_test_text(connect, cursor, 9000082, """Я критикую себя за ошибки и слабости.""")
insert_test_answ(connect, cursor, 3, 8, 1000, 2, 9000083)
insert_test_text(connect, cursor, 9000083, """Я все время обвиняю себя за свои поступки.""")
insert_test_answ(connect, cursor, 4, 8, 1000, 3, 9000084)
insert_test_text(connect, cursor, 9000084, """Я виню себя во всем плохом, что происходит.""")
#9
insert_test_ques(connect, cursor, 9, 1000, 9000090)
insert_test_text(connect, cursor, 9000090, """Суицидальные мысли""")
insert_test_answ(connect, cursor, 1, 9, 1000, 0, 9000091)
insert_test_text(connect, cursor, 9000091, """Я никогда не думал покончить с собой.""")
insert_test_answ(connect, cursor, 2, 9, 1000, 1, 9000092)
insert_test_text(connect, cursor, 9000092, """Ко мне приходят мысли покончить с собой, но я не буду их осуществлять.""")
insert_test_answ(connect, cursor, 3, 9, 1000, 2, 9000093)
insert_test_text(connect, cursor, 9000093, """Я хотел бы покончить с собой.""")
insert_test_answ(connect, cursor, 4, 9, 1000, 3, 9000094)
insert_test_text(connect, cursor, 9000094, """Я бы убил себя, если бы представился случай.""")
#10
insert_test_ques(connect, cursor, 10, 1000, 9000100)
insert_test_text(connect, cursor, 9000100, """Слезливость""")
insert_test_answ(connect, cursor, 1, 10, 1000, 0, 9000101)
insert_test_text(connect, cursor, 9000101, """Я плачу не больше, чем обычно.""")
insert_test_answ(connect, cursor, 2, 10, 1000, 1, 9000102)
insert_test_text(connect, cursor, 9000102, """Сейчас я плачу чаще, чем раньше.""")
insert_test_answ(connect, cursor, 3, 10, 1000, 2, 9000103)
insert_test_text(connect, cursor, 9000103, """Теперь я все время плачу.""")
insert_test_answ(connect, cursor, 4, 10, 1000, 3, 9000104)
insert_test_text(connect, cursor, 9000104, """Раньше я мог плакать, а сейчас не могу, даже если мне хочется.""")
#11
insert_test_ques(connect, cursor, 11, 1000, 9000110)
insert_test_text(connect, cursor, 9000110, """Раздражительность""")
insert_test_answ(connect, cursor, 1, 11, 1000, 0, 9000111)
insert_test_text(connect, cursor, 9000111, """Сейчас я раздражителен не более, чем обычно.""")
insert_test_answ(connect, cursor, 2, 11, 1000, 1, 9000112)
insert_test_text(connect, cursor, 9000112, """Я более легко раздражаюсь, чем раньше.""")
insert_test_answ(connect, cursor, 3, 11, 1000, 2, 9000113)
insert_test_text(connect, cursor, 9000113, """Теперь я постоянно чувствую, что раздражен.""")
insert_test_answ(connect, cursor, 4, 11, 1000, 3, 9000114)
insert_test_text(connect, cursor, 9000114, """Я стал равнодушен к вещам, которые меня раньше раздражали.""")
#12
insert_test_ques(connect, cursor, 12, 1000, 9000120)
insert_test_text(connect, cursor, 9000120, """Нарушение социальных связей""")
insert_test_answ(connect, cursor, 1, 12, 1000, 0, 9000121)
insert_test_text(connect, cursor, 9000121, """Я не утратил интереса к другим людям.""")
insert_test_answ(connect, cursor, 2, 12, 1000, 1, 9000122)
insert_test_text(connect, cursor, 9000122, """Я меньше интересуюсь другими людьми, чем раньше.""")
insert_test_answ(connect, cursor, 3, 12, 1000, 2, 9000123)
insert_test_text(connect, cursor, 9000123, """Я почти потерял интерес к другим людям.""")
insert_test_answ(connect, cursor, 4, 12, 1000, 3, 9000124)
insert_test_text(connect, cursor, 9000124, """Я полностью утратил интерес к другим людям.""")
#13
insert_test_ques(connect, cursor, 13, 1000, 9000130)
insert_test_text(connect, cursor, 9000130, """Нерешительность""")
insert_test_answ(connect, cursor, 1, 13, 1000, 0, 9000131)
insert_test_text(connect, cursor, 9000131, """Я откладываю принятие решения иногда, как и раньше.""")
insert_test_answ(connect, cursor, 2, 13, 1000, 1, 9000132)
insert_test_text(connect, cursor, 9000132, """Я чаще, чем раньше, откладываю принятие решения.""")
insert_test_answ(connect, cursor, 3, 13, 1000, 2, 9000133)
insert_test_text(connect, cursor, 9000133, """Мне труднее принимать решения, чем раньше.""")
insert_test_answ(connect, cursor, 4, 13, 1000, 3, 9000134)
insert_test_text(connect, cursor, 9000134, """Я больше не могу принимать решения.""")
#14
insert_test_ques(connect, cursor, 14, 1000, 9000140)
insert_test_text(connect, cursor, 9000140, """Образ тела""")
insert_test_answ(connect, cursor, 1, 14, 1000, 0, 9000141)
insert_test_text(connect, cursor, 9000141, """Я не чувствую, что выгляжу хуже, чем обычно.""")
insert_test_answ(connect, cursor, 2, 14, 1000, 1, 9000142)
insert_test_text(connect, cursor, 9000142, """Меня тревожит, что я выгляжу старым и непривлекательным.""")
insert_test_answ(connect, cursor, 3, 14, 1000, 2, 9000143)
insert_test_text(connect, cursor, 9000143, """Я знаю, что в моей внешности произошли существенные изменения, делающие меня непривлекательным.""")
insert_test_answ(connect, cursor, 4, 14, 1000, 3, 9000144)
insert_test_text(connect, cursor, 9000144, """Я знаю, что выгляжу безобразно.""")
#15
insert_test_ques(connect, cursor, 15, 1000, 9000150)
insert_test_text(connect, cursor, 9000150, """Утрата работоспособности""")
insert_test_answ(connect, cursor, 1, 15, 1000, 0, 9000151)
insert_test_text(connect, cursor, 9000151, """Я могу работать так же хорошо, как и раньше.""")
insert_test_answ(connect, cursor, 2, 15, 1000, 1, 9000152)
insert_test_text(connect, cursor, 9000152, """Мне необходимо сделать дополнительное усилие, чтобы начать делать что-нибудь.""")
insert_test_answ(connect, cursor, 3, 15, 1000, 2, 9000153)
insert_test_text(connect, cursor, 9000153, """Я с трудом заставляю себя делать что-либо.""")
insert_test_answ(connect, cursor, 4, 15, 1000, 3, 9000154)
insert_test_text(connect, cursor, 9000154, """Я совсем не могу выполнять никакую работу.""")
#16
insert_test_ques(connect, cursor, 16, 1000, 9000160)
insert_test_text(connect, cursor, 9000160, """Нарушение сна""")
insert_test_answ(connect, cursor, 1, 16, 1000, 0, 9000161)
insert_test_text(connect, cursor, 9000161, """Я сплю так же хорошо, как и раньше.""")
insert_test_answ(connect, cursor, 2, 16, 1000, 1, 9000162)
insert_test_text(connect, cursor, 9000162, """Сейчас я сплю хуже, чем раньше.""")
insert_test_answ(connect, cursor, 3, 16, 1000, 2, 9000163)
insert_test_text(connect, cursor, 9000163, """Я просыпаюсь на 1-2 часа раньше, и мне трудно заснуть опять.""")
insert_test_answ(connect, cursor, 4, 16, 1000, 3, 9000164)
insert_test_text(connect, cursor, 9000164, """Я просыпаюсь на несколько часов раньше обычного и больше не могу заснуть.""")
#17
insert_test_ques(connect, cursor, 17, 1000, 9000170)
insert_test_text(connect, cursor, 9000170, """Утомляемость""")
insert_test_answ(connect, cursor, 1, 17, 1000, 0, 9000171)
insert_test_text(connect, cursor, 9000171, """Я устаю не больше, чем обычно.""")
insert_test_answ(connect, cursor, 2, 17, 1000, 1, 9000172)
insert_test_text(connect, cursor, 9000172, """Теперь я устаю быстрее, чем раньше.""")
insert_test_answ(connect, cursor, 3, 17, 1000, 2, 9000173)
insert_test_text(connect, cursor, 9000173, """Я устаю почти от всего, что я делаю.""")
insert_test_answ(connect, cursor, 4, 17, 1000, 3, 9000174)
insert_test_text(connect, cursor, 9000174, """Я не могу ничего делать из-за усталости.""")

insert_test_ques(connect, cursor, 18, 1000, 9000180)
insert_test_text(connect, cursor, 9000180, """Утрата аппетита""")
insert_test_answ(connect, cursor, 1, 18, 1000, 0, 9000181)
insert_test_text(connect, cursor, 9000181, """Мой аппетит не хуже, чем обычно.""")
insert_test_answ(connect, cursor, 2, 18, 1000, 1, 9000182)
insert_test_text(connect, cursor, 9000182, """Мой аппетит стал хуже, чем раньше.""")
insert_test_answ(connect, cursor, 3, 18, 1000, 2, 9000183)
insert_test_text(connect, cursor, 9000183, """Мой аппетит теперь значительно хуже.""")
insert_test_answ(connect, cursor, 4, 18, 1000, 3, 9000184)
insert_test_text(connect, cursor, 9000184, """У меня вообще нет аппетита.""")

insert_test_ques(connect, cursor, 19, 1000, 9000190)
insert_test_text(connect, cursor, 9000190, """Потеря веса""")
insert_test_answ(connect, cursor, 1, 19, 1000, 0, 9000191)
insert_test_text(connect, cursor, 9000191, """В последнее время я не похудел или потеря веса была незначительной.""")
insert_test_answ(connect, cursor, 2, 19, 1000, 1, 9000192)
insert_test_text(connect, cursor, 9000192, """За последнее время я потерял более 2 кг.""")
insert_test_answ(connect, cursor, 3, 19, 1000, 2, 9000193)
insert_test_text(connect, cursor, 9000193, """Я потерял более 5 кг.""")
insert_test_answ(connect, cursor, 4, 19, 1000, 3, 9000194)
insert_test_text(connect, cursor, 9000194, """Я потерял более 7 кr.""")

insert_test_ques(connect, cursor, 20, 1000, 9000200)
insert_test_text(connect, cursor, 9000200, """Охваченность телесными ощущениями""")
insert_test_answ(connect, cursor, 1, 20, 1000, 0, 9000201)
insert_test_text(connect, cursor, 9000201, """Я беспокоюсь о своем здоровье не больше, чем обычно.""")
insert_test_answ(connect, cursor, 2, 20, 1000, 1, 9000202)
insert_test_text(connect, cursor, 9000202, """Меня тревожат проблемы моего физического здоровья, такие, как боли, расстройство желудка, запоры и т.д.""")
insert_test_answ(connect, cursor, 3, 20, 1000, 2, 9000203)
insert_test_text(connect, cursor, 9000203, """Я очень обеспокоен своим физическим состоянием, и мне трудно думать о чем-либо другом.""")
insert_test_answ(connect, cursor, 4, 20, 1000, 3, 9000204)
insert_test_text(connect, cursor, 9000204, """Я настолько обеспокоен своим физическим состоянием, что больше ни о чем не могу думать.""")

insert_test_ques(connect, cursor, 21, 1000, 9000210)
insert_test_text(connect, cursor, 9000210, """Утрата либидо""")
insert_test_answ(connect, cursor, 1, 21, 1000, 0, 9000211)
insert_test_text(connect, cursor, 9000211, """В последнее время я не замечал изменения своего интереса к сексу.""")
insert_test_answ(connect, cursor, 2, 21, 1000, 1, 9000212)
insert_test_text(connect, cursor, 9000212, """Меня меньше занимают проблемы секса, чем раньше.""")
insert_test_answ(connect, cursor, 3, 21, 1000, 2, 9000213)
insert_test_text(connect, cursor, 9000213, """Сейчас я значительно меньше интересуюсь сексуальными проблемами, чем раньше.""")
insert_test_answ(connect, cursor, 4, 21, 1000, 3, 9000214)
insert_test_text(connect, cursor, 9000214, """Я полностью утратил сексуальный интерес.""")

cursor.close()
connect.close()





class SQL_DB():
    def __init__(self, database_file):
        """Подключаемся к Базе Данных и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor=self.connection.cursor()

    def client_exists(self, user_id):
        """Проверяем есть ли клиент уже в базе данных"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'clients' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    def get_user_id (self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'clients' WHERE 'user_id'= ?", (user_id,))
        return result.fetchall()[0]

    def add_client(self, user_id):
        """Добавляем нового клиента в базу"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'clients' ('user_id') VALUES (?)", (user_id,))

    def set_client_name(self, user_id, client_name):
        with self.connection:
            return self.cursor.execute("UPDATE 'clients' SET 'client_name' = ? WHERE 'user_id' = ?",
                                       (client_name, user_id,)) and self.connection.commit()

    def set_client_phone(self, user_id, cl_phone):
        with self.connection:
            return self.cursor.execute("UPDATE 'clients' SET 'Телефон' = ?  WHERE 'user_id' = ?", 
                                       (user_id, cl_phone,)) and self.connection.commit()

    def set_client_email(self, user_id, cl_email):
        with self.connection:
            return self.cursor.execute("UPDATE 'clients' SET 'Email' = ? WHERE 'user_id' = ?", 
                                       (user_id, cl_email,)) and self.connection.commit()
            
            
