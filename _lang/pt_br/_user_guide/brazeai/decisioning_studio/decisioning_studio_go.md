---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Saiba como configurar e integrar o BrazeAI Decisioning Studio<sup>TM</sup> Go na Braze."
---

# BrazeAI Decisioning Studio™ Go

> Saiba como configurar e integrar o BrazeAI Decisioning Studio™ Go na Braze.

## Sobre o Decisioning Studio Go {#about-decisioning-studio-go}

O Decisioning Studio Go é um agente de decisão com IA para programas de e-mail recorrentes. Em vez de escolher uma única linha de assunto, horário de envio ou imagem vencedora para todo o público, o agente seleciona a melhor combinação para cada destinatário com base no engajamento anterior.

Você define as variantes entre as quais o agente pode escolher — como linhas de assunto, CTAs, imagens, dias de envio e horários de envio. Para cada usuário no seu Segment or segmento, o agente escolhe a opção com maior probabilidade de gerar engajamento, dentro das restrições e do cronograma que você configurar.

Isso difere dos testes A/B no nível de Campaign com [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), que otimiza variantes para o público. O Decisioning Studio Go personaliza no nível individual em cada envio do programa.

### Como funciona {#how-it-works}

O agente divide um Segment or segmento da Braze em dois grupos: um grupo do Decisioning Studio que recebe conteúdo de e-mail otimizado por IA, e um grupo de controle aleatório (mínimo de 5%) que recebe combinações aleatórias das mesmas opções. O grupo de controle aleatório oferece uma medição contínua e comparável do aumento gerado pelo agente; você pode sempre ver como a experiência personalizada se compara ao mesmo conteúdo enviado sem personalização.

Para cada usuário no grupo do Decisioning Studio, o agente escolhe entre as opções que você forneceu: qual criativo enviar (incluindo a linha de assunto, CTA e imagem específicos dentro dele) e quando enviar (dia da semana e horário do dia, respeitando o horário de silêncio e o fuso local do usuário). [Configure seu agente do Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) aborda cada um desses pontos em detalhe.

À medida que os usuários engajam — ou não — o agente aprende. Os relatórios indicam quando o agente ainda está no período de treinamento versus quando está personalizando ativamente, para que você sempre saiba em que estágio o agente se encontra.

### O que você configura {#what-you-configure}

| Configuração | Descrição |
|---|---|
| **Público** | Um único Segment or segmento da Braze como público de entrada. O agente divide automaticamente o Segment or segmento entre o grupo de decisão e o grupo de controle aleatório. |
| **Cronograma** | Frequência de envio (por exemplo, uma única seleção três vezes por semana), dias da semana permitidos, horário de silêncio no fuso local do usuário e adesão às regras de limite de frequência no nível do agente. |
| **Criativos** | Um ou mais criativos base construídos no criador da Braze. Dentro de cada criativo base, você pode marcar uma linha de assunto, CTA e imagem como pontos de personalização usando Liquid tags, e então fornecer uma lista de variantes para cada um. O agente decide qual criativo base e variante usar para cada destinatário. |
| **Restrições** | Limites que impedem o agente de enviar o mesmo criativo base ou a mesma linha de assunto para um usuário mais de uma vez dentro de uma janela que você define. |
| **Revisão e lançamento** | Uma tela de validação final exibe quaisquer alertas a serem tratados antes do lançamento. O agente passa de **Rascunho** para **Ativo** e começa a enviar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuração do Decisioning Studio Go" }

### Quando usar o Decisioning Studio Go {#when-to-use-decisioning-studio-go}

A melhor adequação são programas de e-mail recorrentes com públicos estáveis e conteúdo clicável, como calendários always-on (recompensas, lançamentos de conteúdo, nudges de ciclo de vida), programas evergreen (winbacks, reengajamento) e promoções com múltiplos e-mails. Esses cenários oferecem ao agente volume e variedade suficientes para aprender de forma significativa.

Consulte [Exemplos para Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) para orientações detalhadas de adequação por tipo de programa.

### Onde o Decisioning Studio Go se encaixa no pacote Decisioning Studio {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

O Decisioning Studio Go é o nível de entrada do BrazeAI Decisioning Studio. Ele foi projetado para profissionais de marketing que desejam personalização de e-mail um-para-um sem a complexidade de configuração de uma implementação completa do Decisioning Studio Pro.

O Decisioning Studio Pro acrescenta:
- Otimização para qualquer métrica de negócio (não apenas cliques)
- Conexão com qualquer fonte de dados primários
- Decisão multicanal
- Padrões de orquestração estendidos
- Suporte dedicado da equipe de AI Decisioning Services da Braze

## Próximas etapas {#next-steps}

- [Configure seu agente do Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) e defina público, cronograma, criativos e restrições
- [Analise exemplos para o Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) para confirmar se seu programa é adequado
- Consulte o [FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq) para perguntas frequentes