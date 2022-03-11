### Integração Zabbix Telegram 

### Requisitos 

```
python3

pyTelegramBotAPI
```

Download: https://pypi.org/project/pyTelegramBotAPI/0.3.0/

### Testando script 

Crie uma váriavel de ambiente: 

```export BOT_TOKEN=SEU_TOKEN_AQUI```

Pegue o id do chat do Telegram:

```curl https://api.telegram.org/bot_SEU_TOKEN_AQUI/getUpdates | jq```

Feito isso, execute o seguinte comando:

```python3 telegram.py ID_AQUI Testando Alerta```

### Tutorial de como integrar o Telegram ao Zabbix 

https://medium.com/@araujo.emerson28/zabbix-integra%C3%A7%C3%A3o-com-o-telegram-6e3a48bdab50