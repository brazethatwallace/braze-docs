---
nav_title: "Caso de uso"
article_title: "Caso de uso: Intelligence Suite"
page_order: 10
search_rank: 12
description: "Novo no Intelligence Suite da Braze? Leia este caso de uso sobre como o Intelligent Timing pode ser aproveitado para enviar promoções personalizadas em um Canvas unificado."
tool:
  - Dashboard
---

# Caso de uso: Transforme o comportamento passado no app em ofertas personalizadas no canal certo {#use-case-turn-past-app-behavior-into-personalized-offers-on-the-right-channel}

> Este exemplo mostra como uma marca fictícia usa o Intelligent Timing para aproveitar dados de engajamento passados no app e em mensagens para enviar promoções personalizadas em um Canvas unificado.

Vamos supor que Marvin é um gerente de marketing na SandwichEmperor, uma rede de fast food que frequentemente lança ofertas por tempo limitado. A equipe de Marvin é responsável por entregar mensagens promocionais no app para divulgar um novo item do cardápio por tempo limitado: o Super Sub.

Até agora, cada mensagem para itens por tempo limitado era gerenciada de forma isolada: diferentes testes de copy e abordagens eram enviados separadamente — eles tentavam diferentes ângulos de mensagem para aumentar o engajamento sem entender completamente quando as promoções por tempo limitado são mais populares entre os usuários no app.

Para a nova promoção do Super Sub, Marvin quer um Canvas coordenado que ainda aprenda ao longo do tempo — usando o comportamento que a Braze já captura (sessões, aberturas, cliques) em vez de adivinhar horários de envio ou uma única mensagem vencedora.

Usando o Intelligent Timing, Marvin pode entregar etapas de Mensagem quando cada pessoa tem mais probabilidade de engajar, com base na análise estatística de interações passadas (por exemplo, padrões de sessão e engajamento por canal).

Este passo a passo descreve como Marvin:

- Constrói um Canvas com push, e-mail e SMS em etapas de Mensagem
- Usa o Intelligent Timing nessas etapas para que a entrega se alinhe com os padrões de engajamento inferidos por usuário e canal

## Etapa 1: Definir a métrica de sucesso e criar o Canvas {#step-1-define-the-success-metric-and-build-the-canvas}

Marvin decide o que "sucesso" significa para o Super Sub (por exemplo, pedidos ou um evento personalizado que é disparado quando alguém conclui uma compra do Super Sub ou o adiciona no app).

Em seguida, Marvin cria um Canvas para que novos usuários entrem em uma programação contínua enquanto a oferta estiver ativa.

1. No dashboard da Braze, Marvin navega até **Messaging** > **Canvas**.
2. Ele cria um Canvas e o nomeia "Item limitado - Super Sub".
3. Em seguida, adiciona um evento de conversão e outra variante no Canvas.
4. Ele preenche os detalhes restantes do Canvas e está pronto para mapear a jornada do usuário no construtor de Canvas.

## Etapa 2: Configurar as definições de entrega {#step-2-set-up-delivery-settings}

Na guia **Delivery Settings** da etapa de Mensagem, Marvin planeja usar o Intelligent Timing para analisar as interações passadas dos usuários com o app e cada canal de envio de mensagens, e então selecionar automaticamente o melhor horário para promover o Super Sub para cada usuário. Isso significa que alguns usuários podem receber a promoção à tarde, enquanto outros podem recebê-la à noite.

Ele seleciona **o horário mais popular de uso do app entre todos os usuários** para usuários que não têm interações passadas suficientes para análise.

## Etapa 3: Adicionar postergações e Intelligent Timing às etapas de Mensagem {#step-3-add-delays-and-intelligent-timing-to-message-steps}

Para etapas de Mensagem que usam Intelligent Timing, Marvin segue as orientações do Canvas: ele coloca uma etapa de postergação de pelo menos dois dias corridos entre a entrada (ou uma etapa anterior) e a etapa de Mensagem com Intelligent Timing. Ele prefere dias corridos para postergações ao usar Intelligent Timing, para que a entrega aconteça no dia pretendido no horário ideal de cada usuário.

Em cada etapa de Mensagem de notificação por push, e-mail e SMS, ele abre **Delivery Settings** e escolhe **Using Intelligent Timing**. Ele define um horário de fallback para usuários que não têm histórico de engajamento suficiente para um horário ideal. Ele observa que etapas de Mensagem com múltiplos canais podem enviar ou tentar enviar em horários diferentes por canal, refletindo como alguns clientes engajam mais com e-mail pela manhã e push à noite.

## Etapa 4: Monitorar e otimizar {#step-4-monitor-and-optimize}

Marvin coordena os ativos promocionais do Super Sub em push, e-mail e SMS nas etapas de Mensagem (e em quaisquer etapas subsequentes que suas variantes usem) e lança o Canvas.

Após o lançamento, ele acompanha a análise de dados do Canvas e as contagens de conversão e conclui que o Intelligent Timing continua otimizando quando cada canal é disparado para cada usuário com base nos padrões de engajamento contínuos. Como resultado, Marvin ajudou a SandwichEmperor com sucesso a conectar o desempenho de ofertas por tempo limitado a quando e qual jornada funciona, em vez de apenas qual mensagem promocional avulsa venceu da última vez.