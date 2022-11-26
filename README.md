# :bomb: Impulse
## Современный набор инструментов отказа в обслуживании


<p align="center">
  <img src="https://i.ibb.co/rFct6QX/LOGO.png">
</p>

# :computer: Основное окно
<p align="center">
  <img src="https://i.ibb.co/xXcJbVX/2022-11-26-16-12-16.png">
</p>

# :satellite: Методы:
| Метод                |   Цель     | Описание |
| ---------------------| -----------|-------------|
| SMS                  | НОМЕР      | Отправляет огромное количество SMS-сообщений и звонков на одну цель |
| EMAIL                | EMAIL      | Отправляет огромное количество сообщений на электронную почту цели |
| NTP                  | IP:ПОРТ    | Усиление NTP — это тип атаки распределенного отказа в обслуживании (DDoS), при которой злоумышленник использует общедоступные серверы протокола сетевого времени (NTP) для подавления целевого трафика протокола пользовательских дейтаграмм (UDP). |
| SYN                  | IP:ПОРТ    | SYN-флуд (полуоткрытая атака) — это тип атаки типа «отказ в обслуживании» (DDoS), целью которой является сделать сервер недоступным для легитимного трафика за счет использования всех доступных ресурсов сервера. |
| UDP                  | IP:ПОРТ    | UDP-флуд — это тип атаки типа «отказ в обслуживании», при которой большое количество пакетов протокола пользовательских дейтаграмм (UDP) отправляется на целевой сервер с целью подавить способность этого устройства обрабатывать и отвечать. Брандмауэр, защищающий целевой сервер, также может выйти из строя в результате переполнения UDP, что приведет к отказу в обслуживании легитимного трафика. |
| POD (Пинг смерти)    | IP         | Пинг смерти(Ping of Death, также известный как PoD) — это тип атаки типа «отказ в обслуживании» (DoS), при которой злоумышленник пытается вывести из строя, дестабилизировать или заморозить целевой компьютер или службу, отправляя искаженные или слишком большие пакеты с помощью простой команды ping. |
| ICMP                 | IP:ПОРТ    | Ping-флуд, также известный как ICMP-флуд, — это распространенная атака типа «отказ в обслуживании» (DoS), при которой злоумышленник выводит из строя компьютер жертвы, подавляя его эхо-запросами ICMP, также известными как эхо-запросы. |
| HTTP                 | URL        | HTTP Flood — это тип атаки распределенного отказа в обслуживании (DDoS), при которой злоумышленник манипулирует нежелательными HTTP- и POST-запросами для атаки на веб-сервер или приложение. В этих атаках часто используются взаимосвязанные компьютеры, которые были захвачены с помощью вредоносных программ, таких как троянские кони. |
| Slowloris            | IP:ПОРТ    | Slowloris — это программа атаки типа «отказ в обслуживании», которая позволяет злоумышленнику перегрузить целевой сервер, открывая и поддерживая множество одновременных HTTP-соединений между злоумышленником и целью. |
| Memcached            | IP:ПОРТ    | Атака распределенного отказа в обслуживании (DDoS) memcached — это тип кибератаки, при которой злоумышленник пытается перегрузить целевую жертву интернет-трафиком. Злоумышленник подделывает запросы к уязвимому серверу UDP memcached*, который затем переполняет целевую жертву интернет-трафиком, потенциально перегружая ресурсы жертвы. В то время как интернет-инфраструктура цели перегружена, новые запросы не могут быть обработаны, а обычный трафик не может получить доступ к интернет-ресурсу, что приводит к отказу в обслуживании. |

# :gift: Установка:
* Windows:
  * Скачайте Python 3.8 от [сюда](https://www.python.org/downloads/release/python-38)
  * Запустите установщик, и нажмите `add python to PATH`
  * Скачайте Impulse(можно с [оффициального сайта](https://github.com/LimerBoy/Impulse), но на английском
  * Откройте командную строку, или Windows PowerShell в папке Impulse
  * Запустите эту команду: `pip install -r requirements.txt`
  * И эту: `python impulse.py --help`

* Linux:
  * `sudo apt update`
  * `sudo apt install python3 python3-pip git -y`
  * `git clone https://github.com/RimYT/LimerBoyImpulseRussian`
  * `cd Impulse/`
  * `pip3 install -r requirements.txt`
  * `python3 impulse.py --help`

* Termux:
  * `pkg update`
  * `pkg install python3 python3-pip git -y`
  * `git clone [https://github.com/LimerBoy/Impulse](https://github.com/RimYT/LimerBoyImpulseRussian)`
  * `cd Impulse/`
  * `pip3 install -r requirements.txt`
  * `python3 impulse.py --help`

# :phone: Пример SMS и Call(отправка звонков) флуда(спама):
```python3 impulse.py --method SMS --time 20 --threads 15 --target +380123456789```

<p align="center">
  <img src="https://i.ibb.co/Ycsr8ns/2022-11-26-16-16-47.png">
</p>

# :lock: Авторские права:
ВНИМАНИЕ! Я НЕ ПРЕТЕНДУЮ НА АВТОРСТВО! Я ЛИШЬ ПЕРЕВЁЛ ПРЕКРАСНЫЙ ПРОЕКТ ["LimerBoy"](https://github.com/LimerBoy/Impulse)! ССЫЛКА НА ОФФИЦИАЛЬНЫЙ ПРОЕКТ НАХОДИТСЯ [ЗДЕСЬ](https://github.com/LimerBoy/Impulse)

ATTENTION! I DO NOT CLAIM AUTHORITY! I JUST TRANSLATED A GREAT PROJECT ["LimerBoy"](https://github.com/LimerBoy/Impulse)! LINK TO THE OFFICIAL PROJECT IS [HERE](https://github.com/LimerBoy/Impulse)

# :moneybag: Донат автору(не мне):
**BTC:** `1GvEsEEdD8kfbSia6QR3Hk1G4fzy2mwZE4`  
**ETH:** `0x4f62ce9632efF28f175aAAdd58B14A0AC053A952`  
**XMR:** `487sRQv2gBXHVPc59Lkz5j7bgJ28Qy8nPW6hUvRyFWxM84cWzEnmVcWf6MWEQ59BwrP4viyoz6gfqhDPb1yiUx2SUViKVwd`  

# :moneybag: Донат переводчику(мне):
Спасибо, мне очень приятно, если ты решишь задонатить мне, задонатить ты сможешь [здесь](https://www.donationalerts.com/r/rim_yt)(DonationAlerts)
