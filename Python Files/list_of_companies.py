my_list = (
    """01.1 Отглеждане на едногодишни растения""",
    """01.2 Отглеждане на многогодишни насаждения""",
    """01.3 Дейности на разсадници, без горските""",
    """01.4 Животновъдство""",
    """01.5 Комбинирано растениевъдно-животновъдно стопанствово""",
    """01.6 Спомагателни дейности в селското стопанство""",
    """01.7 Лов и спомагателни дейности""",
    """02.1 Възпроизводство на гори""",
    """02.2 Дърводобив""",
    """02.3 Събиране на диворастящи и недървесни продукти""",
    """02.4 Спомагателни дейности в горското стопанство""",
    """03.1 Риболов""",
    """03.2 Развъждане и отглеждане на риба и други водни организми""",
    """05.1 Добив на антрацитни и черни въглища""",
    """05.2 Добив на кафяви и лигнитни въглища""",
    """06.1 Добив на нефт""",
    """06.2 Добив на природен газ""",
    """07.1 Добив на железни руди""",
    """07.2 Добив на уранови, ториеви и руди на цветни метали""",
    """08.1 Добив на скални материали, пясък и глина""",
    """08.9 Добив на други неметални материали и суровини""",
    """09.1 Спомагателни дейности в добива на нефт и природен газ""",
    """
    09.9 Спомагателни дейности в добива, без добива на нефт и природен газ
  """,
    """
    10.1 Производство и преработка на месо; производство на месни продукти, без
    готови ястия
  """,
    """
    10.2 Преработка и консервиране на риба и други водни животни, без готови
    ястия
  """,
    """
    10.3 Преработка и консервиране на плодове и зеленчуци, без готови ястия
  """,
    """10.4 Производство на растителни и животински масла и мазнини""",
    """10.5 Производство на мляко и млечни продукти""",
    """
    10.6 Производство на мелничарски продукти, нишесте и нишестени продукти
  """,
    """10.7 Производство на хлебни и тестени изделия""",
    """10.8 Производство на други хранителни продукти""",
    """10.9 Производство на готови храни за животни""",
    """11.0 Производство на напитки""",
    """12.0 Производство на тютюневи изделия""",
    """13.1 Подготовка и предене на текстилни влакна""",
    """13.2 Производство на тъкани""",
    """13.3 Облагородяване на прежди, платове и облекло""",
    """13.9 Производство на други текстилни изделия""",
    """14.1 Производство на облекло, без кожухарско""",
    """14.2 Производство на облекло и изделия от кожухарски кожи""",
    """14.3 Производство на други трикотажни изделия""",
    """
    15.1 Обработка на кожи; производство на изделия за пътуване и сарашки
    изделия
  """,
    """15.2 Производство на обувки""",
    """16.1 Разкрояване, рендосване и импрегниране на дървен материал""",
    """
    16.2 Производство на изделия от дървен материал, корк, слама и материали за
    плетене
  """,
    """17.1 Производство на влакнести полуфабрикати, хартия и картон""",
    """17.2 Производство на изделия от хартия и картон""",
    """18.1 Печатна дейност""",
    """18.2 Възпроизвеждане на записани носители""",
    """19.1 Производство на кокс и продукти на коксуването""",
    """
    19.2 Производство на рафинирани нефтопродукти и брикети от въглища и торф
  """,
    """20.1 Производство на основни химични вещества""",
    """20.2 Производство на пестициди и други агрохимикали""",
    """
    20.3 Производство на бои, лакове и подобни продукти, печатарско мастило и
    китове
  """,
    """
    20.4 Производство на почистващи, миещи, тоалетни и козметични препарати
  """,
    """20.5 Производство на други химични продукти""",
    """20.6 Производство на изкуствени и синтетични влакна""",
    """21.1 Производство на лекарствени вещества""",
    """21.2 Производство на лекарствени продукти""",
    """22.1 Производство на изделия от каучук""",
    """22.2 Производство на изделия от пластмаси""",
    """23.1 Производство на стъкло и изделия от стъкло""",
    """23.2 Производство на огнеупорни изделия""",
    """23.3 Производство на керамични изделия за строителството""",
    """23.4 Производство на други порцеланови и керамични изделия""",
    """23.5 Производство на цимент, вар и гипс""",
    """23.6 Производство на изделия от бетон, гипс и цимент""",
    """
    23.7 Рязане, профилиране и обработване на строителни и декоративни скални
    материали
  """,
    """23.9 Производство на изделия от други неметални минерали""",
    """24.1 Производство на чугун, стомана и феросплави""",
    """24.2 Производство на тръби, кухи профили и фитинги за тях от стомана""",
    """
    24.3 Производство на други продукти при първичната преработка на стомана
  """,
    """24.4 Производство на основни благородни и други цветни метали""",
    """24.5 Леене на метали""",
    """25.1 Производство на метални изделия за строителството""",
    """
    25.2 Производство на котли за централно отопление и радиатори с
    неелектрическо загряване; производство на цистерни, резервоари и контейнери
    от метал
  """,
    """25.3 Производство на парни котли, без котли за централно отопление""",
    """25.4 Производство на въоръжение и боеприпаси""",
    """25.5 Коване, щамповане и валцуване на метал; прахова металургия""",
    """25.6 Друго металообработване""",
    """25.7 Производство на кухненски прибори, инструменти и железария""",
    """25.9 Производство на други метални изделия""",
    """26.1 Производство на електронни елементи и печатни платки""",
    """26.2 Производство на компютърна техника""",
    """26.3 Производство на радио-, телевизионна и далекосъобщителна техника""",
    """26.4 Производство на битова електроника""",
    """
    26.5 Производство на уреди и апарати за измерване, изпитване и навигация;
    производство на часовници
  """,
    """
    26.6 Производство на излъчващи електромедицински и терапевтични апарати
  """,
    """26.7 Производство на оптични уреди и елементи и фотографска техника""",
    """26.8 Производство на магнитни и оптични носители, незаписани""",
    """
    27.1 Производство на електрически двигатели, генератори и трансформатори и
    апарати за управление и разпределение на електрическа енергия
  """,
    """27.2 Производство на акумулаторни батерии и акумулатори""",
    """
    27.3 Производство на изолирани проводници и електроинсталационни изделия
  """,
    """27.4 Производство на лампи и осветители""",
    """27.5 Производство на битови уреди""",
    """27.9 Производство на други електрически съоръжения""",
    """28.1 Производство на машини с общо предназначение""",
    """28.2 Производство на други машини с общо предназначение""",
    """28.3 Производство на машини за селското и горското стопанство""",
    """28.4 Производство на обработващи машини""",
    """28.9 Производство на други машини със специално предназначение""",
    """29.1 Производство на автомобили и техните двигатели""",
    """
    29.2 Производство на купета и каросерии за автомобили; производство на
    ремаркета и полуремаркета
  """,
    """29.3 Производство на части и принадлежности за автомобили""",
    """30.1 Строителство на плавателни съдове""",
    """30.2 Производство на локомотиви, мотриси и вагони""",
    """
    30.3 Производство на въздухоплавателни и космически средства и техните
    двигатели
  """,
    """30.4 Производство на бойни бронирани транспортни машини""",
    """30.9 Производство на други превозни средства""",
    """31.0 Производство на мебели""",
    """32.1 Производство на бижута и подобни изделия""",
    """32.2 Производство на музикални инструменти""",
    """32.3 Производство на спортни стоки""",
    """32.4 Производство на игри и детски играчки""",
    """32.5 Производство на медицински и зъболекарски инструменти и средства""",
    """32.9 Разнообразни производства, некласифицирани другаде""",
    """33.1 Ремонт на метални изделия, машини и оборудване""",
    """33.2 Инсталиране на машини и оборудване""",
    """35.1 Производство, пренос и разпределение на електрическа енергия""",
    """
    35.2 Производство и разпределение на газообразни горива по
    газоразпределителните мрежи
  """,
    """35.3 Производство и разпределение на топлинна енергия""",
    """36.0 Събиране, пречистване и доставяне на води""",
    """37.0 Събиране, отвеждане и пречистване на отпадъчни води""",
    """38.1 Събиране на отпадъци""",
    """38.2 Обработване и обезвреждане на отпадъци""",
    """38.3 Рециклиране на материали""",
    """39.0 Възстановяване и други услуги по управление на отпадъци""",
    """41.1 Дейности по реализиране на инвестиционни проекти за сгради""",
    """41.2 Строителство на жилищни и нежилищни сгради""",
    """42.1 Строителство на пътища, вкл. релсови""",
    """42.2 Строителство на преносни и разпределителни проводи и мрежи""",
    """42.9 Строителство на други съоръжения""",
    """43.1 Разчистване и подготовка на строителната площадка""",
    """43.2 Изграждане на инсталации""",
    """43.3 Довършителни строителни дейности""",
    """43.9 Други специализирани строителни дейности""",
    """45.1 Търговия с автомобили""",
    """45.2 Техническо обслужване и ремонт на автомобили""",
    """45.3 Търговия с части и принадлежности за автомобили""",
    """
    45.4 Търговия с мотоциклети и с части за тях, техническо обслужване и ремонт
    на мотоциклети
  """,
    """46.1 Търговия на едро чрез посредничество""",
    """46.2 Tърговия на едро със селскостопански суровини и живи животни""",
    """46.3 Търговия на едро с хранителни стоки, напитки и тютюневи изделия""",
    """46.4 Търговия на едро с нехранителни потребителски стоки""",
    """46.5 Търговия на едро с компютърна и комуникационна техника""",
    """
    46.6 Търговия на едро с други машини и оборудване със стопанско
    предназначение и части за тях
  """,
    """
    46.7 Търговия на едро с неселскостопански междинни продукти, отпадъци и
    скрап
  """,
    """46.9 Неспециализирана търговия на едро""",
    """47.1 Търговия на дребно в неспециализирани магазини""",
    """
    47.2 Търговия на дребно в специализирани магазини с хранителни стоки,
    напитки и тютюневи изделия
  """,
    """47.3 Търговия на дребно с автомобилни горива и смазочни материали""",
    """
    47.4 Търговия на дребно в специализирани магазини с компютърна и
    комуникационна техника и битова електроника
  """,
    """
    47.5 Търговия на дребно в специализирани магазини с текстил, железария,
    стоки за обзавеждане и битови електроуреди
  """,
    """
    47.6 Търговия на дребно в специализирани магазини със стоки, предназначени
    за свободното време
  """,
    """
    47.7 Търговия на дребно в специализирани магазини с други нехранителни стоки
  """,
    """47.8 Търговия на дребно на открити щандове и пазари""",
    """47.9 Търговия на дребно извън търговски обекти""",
    """49.1 Пътнически железопътен транспорт, междуселищен""",
    """49.2 Товарен железопътен транспорт""",
    """49.3 Друг пътнически сухопътен транспорт""",
    """49.4 Товарен автомобилен транспорт и услуги по преместване""",
    """49.5 Тръбопроводен транспорт""",
    """50.1 Пътнически морски и крайбрежен транспорт""",
    """50.2 Товарен морски и крайбрежен транспорт""",
    """50.3 Пътнически транспорт по вътрешни водни пътища""",
    """50.4 Товарен транспорт по вътрешни водни пътища""",
    """51.1 Пътнически въздушен транспорт""",
    """51.2 Товарен въздушен транспорт; космически транспорт""",
    """52.1 Складиране и съхраняване на товари""",
    """52.2 Спомагателни дейности в транспорта""",
    """53.1 Дейност на пощи, предоставящи универсална пощенска услуга""",
    """53.2 Други пощенски и куриерски дейности""",
    """55.1 Хотели и подобни места за настаняване""",
    """55.2 Туристическо и друго краткосрочно настаняване""",
    """55.3 Къмпинги и терени за каравани и къмпинг-автомобили""",
    """55.9 Други места за настаняване""",
    """56.1 Дейност на ресторанти и заведения за бързо обслужване""",
    """56.2 Приготвяне и доставяне на храна""",
    """56.3 Дейност на питейни заведения""",
    """58.1 Издаване на книги, периодични издания и друга издателска дейност""",
    """58.2 Издаване на програмни продукти""",
    """
    59.1 Производство и разпространение на филми и телевизионни предавания
  """,
    """59.2 Звукозаписване и издаване на музика""",
    """60.1 Създаване и излъчване на радиопрограми""",
    """60.2 Създаване и излъчване на телевизионни програми""",
    """61.1 Далекосъобщителна дейност чрез фиксирани мрежи""",
    """61.2 Далекосъобщителна дейност по безжичен път""",
    """61.3 Спътникова далекосъобщителна дейност""",
    """61.9 Други далекосъобщителни дейности""",
    """62.0 Дейности в областта на информационните технологии""",
    """63.1 Обработка на данни, хостинг и подобни дейности; web-портали""",
    """63.9 Други информационни услуги""",
    """64.1 Парично посредничество""",
    """64.2 Дейност на холдингови дружества""",
    """64.3 Фондове за инвестиране и подобни финансови субекти""",
    """
    64.9 Предоставяне на други финансови услуги, без застраховане и допълнително
    пенсионно осигуряване
  """,
    """65.1 Застраховане""",
    """65.2 Презастраховане""",
    """65.3 Допълнително пенсионно осигуряване""",
    """
    66.1 Спомагателни дейности във финансовите услуги, без застраховане и
    допълнително пенсионно осигуряване
  """,
    """
    66.2 Спомагателни дейности в застраховането и допълнителното пенсионно
    осигуряване
  """,
    """66.3 Управление на фондове""",
    """68.1 Покупка и продажба на собствени недвижими имоти""",
    """68.2 Даване под наем и експлоатация на собствени недвижими имоти""",
    """68.3 Посредническа дейност по операции с недвижими имоти""",
    """69.1 Юридически дейности""",
    """69.2 Счетоводни и одиторски дейности; данъчни консултации""",
    """70.1 Дейност на централни офиси""",
    """70.2 Консултантски дейности в областта на управлението""",
    """71.1 Архитектурни и инженерни дейности""",
    """71.2 Технически изпитвания и анализи""",
    """
    72.1 Научноизследователска и развойна дейност в областта на естествените,
    медицинските, селскостопанските и техническите науки
  """,
    """
    72.2 Научноизследователска и развойна дейност в областта на обществените и
    хуманитарните науки
  """,
    """73.1 Рекламна дейност""",
    """73.2 Проучване на пазари и изследване на общественото мнение""",
    """74.1 Специализирани дейности в областта на дизайна""",
    """74.2 Дейности в областта на фотографията""",
    """74.3 Преводаческа дейност""",
    """74.9 Други професионални дейности, некласифицирани другаде""",
    """75.0 Ветеринарномедицинска дейност""",
    """77.1 Даване под наем и оперативен лизинг на автомобили""",
    """77.2 Даване под наем и оперативен лизинг на лични и домакински вещи""",
    """
    77.3 Даване под наем и оперативен лизинг на други машини и оборудване със
    стопанско предназначение
  """,
    """
    77.4 Оперативен лизинг на интелектуална собственост и сходни продукти, без
    обектите на авторско право
  """,
    """78.1 Посредническа дейност на агенции по наемане на работа""",
    """78.2 Предоставяне на работна сила за временна заетост""",
    """78.3 Други дейности по предоставяне на работна сила""",
    """79.1 Туристическа агентска и операторска дейност""",
    """79.9 Други дейности, свързани с пътувания и резервации""",
    """
    80.1 Частна охранителна дейност, без използване на технически системи за
    сигурност
  """,
    """80.2 Дейности в областта на технически системи за сигурност""",
    """80.3 Дейности по разследване и издирване""",
    """81.1 Комплексно обслужване на сгради""",
    """81.2 Дейности по почистване""",
    """81.3 Оформяне и поддържане на озеленени площи""",
    """82.1 Административни и спомагателни офис дейности""",
    """82.2 Дейност на телефонни центрове за услуги""",
    """82.3 Организиране на конгреси и търговски изложения""",
    """
    82.9 Спомагателно обслужване на стопанската дейност, некласифицирано другаде
  """,
    """84.1 Държавно управление с общ, икономически и социален характер""",
    """84.2 Услуги на държавното управление за обществото като цяло""",
    """84.3 Държавно обществено осигуряване""",
    """85.1 Предучилищно образование""",
    """85.2 Начално образование (първи етап на основното образование)""",
    """
    85.3 Прогимназиално (втори етап на основното образование) и средно
    образование
  """,
    """85.4 Образование след завършено средно образование""",
    """85.5 Други образователни дейности""",
    """85.6 Спомагателни дейности в областта на образованието""",
    """86.1 Дейност на болници""",
    """86.2 Извънболнична лекарска практика""",
    """86.9 Други дейности по хуманно здравеопазване""",
    """87.1 Дейност на заведения със здравни грижи""",
    """
    87.2 Социални грижи с настаняване за лица с умствена изостаналост,
    психичноболни и зависими от наркотици
  """,
    """
    87.3 Социални грижи с настаняване за възрастни лица и хора с физически
    увреждания
  """,
    """87.9 Други социални грижи с настаняване""",
    """
    88.1 Социална работа без настаняване за възрастни лица и хора с увреждания
  """,
    """88.9 Друга социална работа без настаняване""",
    """90.0 Артистична и творческа дейност""",
    """91.0 Други дейности в областта на културата""",
    """92.0 Организиране на хазартни игри""",
    """93.1 Дейности в областта на спорта""",
    """93.2 Дейности, свързани с развлечения и отдих""",
    """
    94.1 Дейност на бизнес организации, организации на работодатели и
    професионални организации
  """,
    """94.2 Дейност на синдикални организации""",
    """94.9 Дейност на други организации с нестопанска цел""",
    """95.1 Ремонт на компютърна и комуникационна техника""",
    """95.2 Ремонт на лични и домакински вещи""",
    """96.0 Други персонални услуги""",
    """97.0 Дейности на домакинства като работодатели на домашен персонал""",
    """
    98.1 Недиференцирани дейности на домакинства по производство на стоки за
    собствено потребление
  """,

    """
    98.2 Недиференцирани дейности на домакинства по производство на услуги за
    собствено потребление
  """,
    """99.0 Дейности на екстериториални организации и служби"""
)
