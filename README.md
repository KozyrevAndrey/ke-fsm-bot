### Инструкция по запуску 

Бот запускается в зависимости от системы при помощи команды `python3 appbot.py` 

Написан бот в async стиле. 
Используется aiogram 2 версии, так как в момент написания 3 версии еще не существовало.

Для сохранения состояний бот использует FSM. Сообщения сохраняются в оперативной памяти, формируются после всех шагов и отправляются в необходимую группу. 

Мысли по улучшениям:
- Вместо FSM(Final State Machine) использовать Redis;
- Подключить Докер для упрощения запуска и развертывания;

Работал бот на pm2. 
Ссылка на пакет в npm `https://www.npmjs.com/package/pm2`

