# grafica

Estudo de modelagem do banco de dados para uma gráfica com Django.


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/grafica.git
cd grafica
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

### Gerando gráfico dos modelos com pygraphviz

https://gist.github.com/rg3915/92ca34f69dde014b38c29bf0f48c0b30


Leia mais [django-orm][0]


### Comandos personalizados

```
python manage.py create_data
```


### Annotate

```
clientes = Cliente.objects.values('uf').annotate(num_cliente=Count('uf')).values('num_cliente','uf')
```

Leia a [doc][1]

Leia [Como otimizar suas consultas no Django - De N a 1 em 20 minutos][2]

Leia também [create_data][3]


![img](https://raw.githubusercontent.com/rg3915/grafica/master/models.png)

[0]: https://github.com/rg3915/django-orm
[1]: https://docs.djangoproject.com/pt-br/2.1/topics/db/aggregation/
[2]: http://pythonclub.com.br/django-introducao-queries.html
[3]: https://github.com/rg3915/crm-django-vuejs/blob/master/backend/create_data.py