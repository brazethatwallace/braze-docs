---
nav_title: Otimizar com BrazeAI<sup>TM</sup>
article_title: Otimizando testes A/B com BrazeAI<sup>TM</sup>
page_order: 1.6
description: "Saiba como o recurso Otimizar com BrazeAI<sup>TM</sup> seleciona e distribui automaticamente as variantes com melhor desempenho em Campaigns de envio único e envio múltiplo."
search_rank: 10
toc_headers: h2
---

# Otimizando testes A/B com BrazeAI<sup>TM</sup> {#optimizing-ab-tests-with-brazeai}

> Ative **Otimizar com BrazeAI<sup>TM</sup>** para otimizar automaticamente uma Campaign com múltiplas variantes. O método de otimização depende de a Campaign ser enviada uma única vez ou várias vezes.

## Pré-requisitos {#prerequisites}

Para usar **Otimizar com BrazeAI<sup>TM</sup>**, sua Campaign deve incluir pelo menos duas variantes de mensagem.

Para uma Campaign com vários envios, você também deve:

- Definir pelo menos um evento de conversão.
- Definir a janela de reelegibilidade para 24 horas ou mais.

## Ativar a otimização {#turn-on-optimization}

Na etapa **Públicos-alvo**, acesse **Testes A/B** e ative **Optimize with BrazeAI<sup>TM</sup>**.

## Campaigns de envio único {#single-send-campaigns}

Para uma Campaign de envio único, a Braze envia uma parte inicial do público para cada variante. Depois que a duração do experimento terminar, o BrazeAI<sup>TM</sup> seleciona a variante com melhor desempenho e a envia para o público restante.

A Braze aplica as configurações recomendadas quando você ativa a otimização. Para alterar essas configurações, abra **Controles avançados**:

- **Meta de otimização:** selecione a métrica que o BrazeAI<sup>TM</sup> usa para comparar variantes. As metas disponíveis dependem do canal.
- **Duração do experimento:** selecione 4 horas, 24 horas, 72 horas ou insira uma duração personalizada.
- **Distribuição de variantes:** altere a porcentagem atribuída a cada variante ou grupo de controle.

A duração padrão do experimento é de 4 horas. Se você otimizar para um evento de conversão primária, o padrão é de 24 horas.

### Metas de otimização padrão por canal {#default-optimization-goals-by-channel}

| Canal | Meta padrão |
|---|---|
| Notificações por push | *Opens* |
| E-mail | *Unique Clicks* |
| SMS, MMS, RCS e WhatsApp | *Clicks* |
| Outros canais compatíveis | *conversão primária Event - A* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metas de otimização padrão por canal" }

## Campaigns com múltiplos envios {#multi-send-campaigns}

Para Campaigns recorrentes, baseadas em ação e disparadas por API or interface de programação do aplicativo (API) que enviam várias vezes, o BrazeAI<sup>TM</sup> otimiza continuamente a distribuição do seu público. Após o prazo inicial de conversão, a Braze analisa o desempenho a cada 12 horas e envia mais usuários para as variantes com melhor desempenho.

A distribuição inicial pode ser uniforme enquanto o BrazeAI<sup>TM</sup> coleta dados de desempenho. A distribuição muda conforme a otimização identifica tendências de desempenho.

Abra **Controles avançados** para adicionar ou remover um grupo de controle. Um grupo de controle fornece uma linha de base para medir o desempenho da Campaign e não recebe uma mensagem.

## Relatórios {#reporting}

Após a conclusão de um experimento de envio único, ou depois que uma campanha de envios múltiplos tiver coletado dados suficientes, a página **Campaign Analytics** mostra o aumento produzido pela otimização.

![Análise de campanha mostrando o aumento com Optimize with BrazeAI<sup>TM</sup>, incluindo métricas de comparação após a janela do experimento.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

Para saber mais, consulte [Análise de testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Perguntas frequentes {#frequently-asked-questions}

### Por que não consigo ativar a otimização com BrazeAI<sup>TM</sup>? {#why-cant-i-turn-on-optimize-with-brazeai}

A otimização não está disponível quando:

- A Campaign tem menos de duas variantes ativas.
- Uma Campaign de envio múltiplo não tem eventos de conversão.
- Uma Campaign de envio múltiplo tem uma janela de reelegibilidade inferior a 24 horas.

### Por que minhas variantes têm contagens de envio semelhantes no início? {#why-do-my-variants-have-similar-send-counts-at-first}

BrazeAI<sup>TM</sup> começa com uma distribuição inicial para coletar dados de desempenho. A distribuição é ajustada ao longo do tempo conforme as tendências de desempenho são identificadas.

### Uma Campaign de envio múltiplo pode parar de otimizar sem selecionar uma variante? {#can-a-multi-send-campaign-stop-optimizing-without-selecting-one-variant}

Sim. A otimização é interrompida quando BrazeAI<sup>TM</sup> tem 95% de confiança de que continuar o experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.