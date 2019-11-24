# Top Asteroids Challenge - LPC

## Índice

1. [Sobre Top Asteroids](#sobre-top-asteroids)
2. [Gameplay](#gameplay)
3. [Campeonato](#campeonato)
4. [Como Participar](#como-participar)
5. [Regras](#regras)
6. [Manual Gameplay](#manual-gameplay)
7. [Manual Técnico](#manual-técnico)
8. [Instruções Python](#instruções-python)
9. [Instruções Java](#instruções-java)
10. [Instruções C++](#instruções-c++)
11. [Built-ins](#built-ins)
12. [Submissão](#submissão)
13. [Sistema de Pontuação](#sistema-de-pontuação)

## Sobre Top Asteroids

[![Video de Divulgação](http://img.youtube.com/vi/v6_QOcy6lmM/0.jpg)](https://www.youtube.com/watch?v=LRMhr9bu7jQ "Video de Divulgação")

Top Asteroids é uma competição de Bots (ou IAs) promovida pela Wildlife, na qual os participantes enviarão seus algoritmos para competir entre si.

O jogo utilizado no campeonato será uma adaptação com batalha do clássico Asteroids, desenhado para fornecer gameplay competitivo e interessante para os bots.

O repositório com o pacote inicial do participante encontra-se aqui: https://github.com/topfreegames/top-asteroids-challenge

O pacote inicial contem os executáveis do jogo para Windows, OSX e Linux, e a pasta "Bots" onde se encontra a interface para programação dos bots.

## Gameplay

Vence a IA que obtiver mais Pontos acumulados durante uma série de partidas. Pontos são obtidos ao destruir outras naves, ou perdidos ao morrer para um asteroid. Olhar seção "Sistema de Pontuação" para maiores detalhes.

## Campeonato

Ocorrerá um campeonato com premiação para os primeiros lugares. O participante enviará um bot seu para competir contra os de outros participantes em um sistema de eliminatórias.

Os participantes serão divididos em grupos de até 8 competidores, com os quais serão realizadas exatamente 3 partidas para decidir quais bots avançam de fase.

A cada fase os vencedores da fase anterior competirão entre si, seguindo um sistema de eliminatórias, até que se encontre o vencedor.

## Como Participar

* Clone [este repositório git](https://github.com/topfreegames/top-asteroids-challenge) (pacote inicial) ou baixe [este zip](https://github.com/topfreegames/top-asteroids-challenge/archive/master.zip) contendo a última versão. **Fique atento a atualizações**

* Veja o Manual de Gameplay abaixo. Programe seu bot utilizando a interface e exemplos fornecidos no pacote inicial. Use o jogo para testa-lo

* Atente a hora limite de submissão e todas as regras

## Regras

* O participante deverá utilizar a linguagem python3
* O participante pode incluir novos códigos-fonte se julgar necessário
* Para participar, o participante deverá enviar todos códigos-fonte necessários para executar seu bot junto com instruções de como o fazer (se necessário), até a data limite.

O participante será desqualificado se o bot:
* Demorar mais de 30 ticks para responder
* Causar leaks ou exceder a memória (50mb max.)
* Utilizar mais de 2 threads (contando com a principal)
* Inviabilizar o andamento das partidas devido a crashes ou hangs
* Ler ou escrever arquivos
* Manipular prioridade do processo
* Utilizar qualquer tipo de conexão (fora a interface disponibilizada)
* Montar time com outro bot
* Possuir código indecifrável ou mal escrito
* Utilizar má fé para adquirir qualquer vantagem

## Manual Gameplay

O controle da nave é feito por meio dos thrusters. O Main Thruster é mais potente que faz o movimento pra frente e para traz. Os Side Thrusters servem para rotação quando em sentidos alternados e para movimento lateral quando no mesmo sentido.

O canhão da nave somente atira para frente. Possui 3 niveis de charge, onde quanto mais potente mais rapido.

![_](http://i58.tinypic.com/2ch897d.jpg)

**Constantes Globais**

Pode se considerar o movimento da nave como inercial, sem atrito e com colisões elasticas. Nesta tabela estão listados as constantes de gameplay:

Attribute | Value |
----------|-------|
Update Interval | 0.05 s (por tick) |
Ship Mass | 1 kg |
Main Thruster Force | 30kg*m/s2 |
Side Thrusters Force (each) | 15 kg*m/s2 |
Side Thruster Offset | 2 m |
Laser charge time per Slot | 0.5 s |
Laser Speed Charge 1 | 25 m/s |
Laser Speed Charge 2 | 50 m/s |
Laser Speed Charge 3 | 75 m/s |
Laser Lifetime | 3 s |
Meteor Speed After Split | 8 m/s |
Meteor Masses | 9 kg, 3 kg, 1 kg |
Meteor Radius | 4 m, 2 m, 1 m |

**Observar que tempo dentro da simulação é independente do real. Tempo dentro da simulação pode ser inferido utilizando-se os ticks.**

## Manual Técnico

Dentro do pacote estamos disponibilizando a interface para implementação dos bots em 3 linguagens diferentes (Python, Java e C++). O participante só poderá escolher a linguagem python3.

As entidades listadas a seguir possuem representações similares nas 3 linguagens:

**GameState**
Contem toda a representação do estado atual da partida.

Atributos | Tipo | Descrição
----------|------|----------
GameState.timestep | float | Intervalo fixo entre ciclos / ticks do jogo (em segundos)
GameState.tick | int | Ciclo atual do jogo. Pode pular mais de um valor se bot demorar muito para responder. Cada tick corresponde a aproximadamente 0.05 s na simulação física.
GameState.arenaRadius | float | Raio da arena
GameState.ships | mapa/dict uid:Ship | Dicionário contendo todas naves ativas e presentes no jogo
GameState.rocks | mapa/dict uid:Rock | Dicionário contendo todas pedras ativas e presentes no jogo
GameState.lasers | mapa/dict uid:Laser |Dicionário contendo todos lasers ativos e presentes no jogo
[Método] GameState.log(String msg) | | Envia uma mensagem de debug / log para ser mostrada dentro do jogo.


**GameObject**
Contem atributos comuns a todos objetos físicos do jogo.

Atributos | Tipo | Descrição
----------|------|----------
GameObject.uid | int | Identificador único do objeto
GameObject.posx | float | Posição do objeto
GameObject.posy | float | Posição do objeto
GameObject.velx | float | Velocidade do objeto (por segundo)
GameObject.vely | float | Velocidade do objeto (por segundo)
GameObject.radius | float | Raio do objeto

**Ship : GameObject**
atributos herdados de GameObject
+

Atributos | Tipo | Descrição
----------|------|----------
Ship.ang | float | Direção que nave está apontando
Ship.velang | float | Velocidade angular da nave (por segundo)
Ship.charge | float | Força carregada da arma laser
Ship.score | int | Número de abates

**Rock : GameObject**
somente atributos herdados de GameObject

**Laser : GameObject**
atributos herdados de GameObject
+

Atributos | Tipo | Descrição
----------|------|----------
Laser.lifetime | float | Tempo restante para tiro desaparecer (em segundos)
Laser.owner | int | Uid da nave que atirou o laser

**Action**
Especifica as ações que devem ser executadas pelo bot no próximo tick.

Atributos | Tipo | Range | Descrição
----------|------|-------|----------
Action.thrust | float | [-1, 1] | Motor principal. Impulsiona pra frente e pra trás.
Action.sideThrustFront | float | [-1, 1] | Motor principal. Impulsiona a parte frontal para esquerda ou direita.
Action.sideThrustBack | float | [-1, 1] | Motor principal. Impulsiona a parte traseira para esquerda ou direita.
Action.shoot | int | [0, 3] | Dá comando referente a arma laser: 0 = carregar, N = atirar laser com força N

## Instruções Python

Utilize o fonte localizado em "Bots/python/stupid_bot.py" como exemplo para implementar seu bot.

É permitida a alteração do fonte "bot_interface.py" se julgar necessário.

De maneira geral a classe BotBase deve ser extendida e o método Process(GameState) implementado. Informações referentes a nave do bot encontram-se no próprio objeto. O método deve retornar uma Action.

Para instalar o bot, execute o jogo e através do menu "Install New Bot" configure o comando "python" com argumento "-u ./caminho/do/script.py"

**ATENÇÃO:**
_A interface utiliza os pipes std:in, std:out e std:err para realizar a comunicação. Portanto, qualquer  chamada que os utilize pode ocasionar causar erros (puts, System.out, cout, etc...)._

Utilize GameState.log(mensagem) para mostrar mensagens de log dentro da partida. Todos logs gerados podem ser vistos na pasta Logs.

## Instruções Java

Utilize o projeto (da IDE Eclipse) localizado em "Bots/java/JavaBot" como exemplo para implementar seu bot.

É permitida a alteração do pacote "bot_interface" se julgar necessário.

De maneira geral a classe BotBase deve ser estendida e o método Process(GameState) implementado. Informações referentes a nave do bot encontram-se no próprio objeto. O método deve retornar uma Action.

Para compilar, gere um "Jar Executável" com sua classe bot.

Para instalar o bot, execute o jogo e através do menu "Install New Bot" configure o parâmetro comando "java", e argumento "-jar ./caminho/do/jar.jar"

**ATENÇÃO:**
_A interface utiliza os pipes std:in, std:out e std:err para realizar a comunicação. Portanto, qualquer  chamada que os utilize pode ocasionar causar erros (puts, System.out, cout, etc...)._

Utilize GameState.log(mensagem) para mostrar mensagens de log dentro da partida. Todos logs gerados podem ser vistos na pasta Logs.

## Instruções C++

Os fontes para compilação encontram-se em "Bots/cpp/StupidBot/StupidBot". Utilize sua IDE favorita para montar o projeto.

É permitida a alteração dos fontes "bot_interface.x" e "BotBase.x" se julgar necessário.

De maneira geral a classe BotBase deve ser estendida e o método Process() implementado. Informações referentes a nave do bot encontram-se no atributo \*myShip.

Para configurar a ação utilize os atributos thrust, sideThrustFront, sideThrustBack, shoot.

Lembre-se de alterar o main.cpp para carregar sua classe antes de compilar.

Para instalar o bot, execute o jogo e através do menu "Install New Bot" configure o parâmetro comando "./caminho/ate/executavel"

**ATENÇÃO:**
_A interface utiliza os pipes std:in, std:out e std:err para realizar a comunicação. Portanto, qualquer  chamada que os utilize pode ocasionar causar erros (puts, System.out, cout, etc...)._

Utilize GameState->log(mensagem) para mostrar mensagens de log dentro da partida. Todos logs gerados podem ser vistos na pasta Logs.

## Built-ins

Além das interfaces para programação dos bots, o jogo fornece 3 IAs built-ins para o participante testar seus algoritmos.

O easy somente mira no adversário mais próximo e atira. O average faz o mesmo enquanto desvia de ameaças. Já o "Human Bot" permite que o _espectador humano_ controle a nave com AWSD + ESPAÇO .

## Submissão

Em breve...

## Sistema de Pontuação

### Pontuação das Partidas

É considerado uma "partida" uma série de Matches com um grupo definido e fixo de bots. Cada match dura até sobrar somente um bot vivo ou até final da contagem do tempo máximo.

A classificação é dada ao final da série de acordo com contagem de pontos. Os pontos são acumulados ao longo dos Matches e podem adquiridos ou perdidos das seguintes formas:

* **+1 Ponto :** Destruir uma nave com um tiro seu.
* **+1 Ponto :** Por nave inimiga destruída por asteroide.
* **-1 Ponto :** Ser destruído pelo tiro de um adversário.
* **-N Pontos :** Ser destruído por um asteroide. Onde N é o número de naves ainda vivas.

### Pontuação do Torneio

Dependendo do número de competidores, os participantes serão divididos em chaves e um sistema de torneio por chaves será utilizados para selecionar os melhores bots, sempre promovendo pelo menos a metade dos bots com mais pontos de cada grupo para a próxima etapa.

Para cada grupo, será rodado exatamente 3 partidas para selecionar os melhores bots do grupo.

Saiba mais sobre a TFG: www.tfgco.com
