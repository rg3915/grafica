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


![img](https://raw.githubusercontent.com/rg3915/grafica/master/models.png)

[0]: https://github.com/rg3915/django-orm