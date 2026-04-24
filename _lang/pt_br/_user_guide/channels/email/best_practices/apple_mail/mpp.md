---
nav_title: Proteção de Privacidade do Apple Mail
article_title: Proteção de Privacidade do Apple Mail para iOS 15
page_order: 1
description: "Este artigo de referência aborda a atualização de privacidade da Proteção de Privacidade do Apple Mail, quem será afetado por ela e algumas próximas etapas para se preparar para o recurso."
channel:
  - email

---

# Proteção de Privacidade do Apple Mail

> Este artigo aborda a Proteção de Privacidade do Apple Mail (MPP), quem ela afeta e como se preparar para seu impacto nas métricas de entregabilidade de e-mail.

## O que é a atualização da Proteção de Privacidade do Apple Mail?

A Proteção de Privacidade do Apple Mail (MPP) é uma atualização de privacidade disponível para usuários do app Apple Mail no iOS 15, iPadOS 15, macOS Monterey e watchOS 8, lançada em meados de setembro de 2021. Para usuários que fazem opt-in na MPP (o que prevemos que a maioria dos usuários fará), os e-mails passam a ser pré-carregados por meio de servidores proxy, armazenando imagens em cache e dificultando o uso de pixels de rastreamento para métricas como [rastreamento de abertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel).

As marcas devem esperar que a MPP resulte em problemas relacionados às métricas de entregabilidade de e-mail e em questões com campanhas e Canvas pré-existentes que são disparados com base nessas métricas. Para entender o impacto na entregabilidade de e-mail, consulte [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/).

### Quem será afetado?

Qualquer destinatário que use o app nativo Apple Mail em:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

Isso se aplica a todos os usuários que conectaram sua conta de e-mail ao app Apple Mail e fizeram opt-in no recurso de segurança, independentemente do serviço de e-mail (Gmail, Outlook, Yahoo, AOL, etc.). Esse impacto não se limita a assinantes que recebem e-mails em endereços Apple/iCloud/me.com.

{% alert important %}
Embora essas atualizações na entregabilidade de e-mail sejam significativas, a MPP não altera fundamentalmente nenhuma das regras que regem o e-mail e a entregabilidade. Em vez disso, ela impactará como medimos o sucesso e quais ferramentas e funcionalidades de e-mail poderão ser usadas daqui em diante.
{% endalert %}

## Como se preparar para a MPP?

O tempo é essencial para marcas que estão apenas começando a pensar em como responder à MPP e seu potencial impacto no marketing por e-mail e nos esforços gerais de engajamento com o cliente. Recomendamos que os usuários façam o seguinte:

- Avaliem o risco que a MPP representa para seus esforços de marketing
- Elaborem um plano de resposta direcionado à MPP que aborde ajustes de automação na plataforma da Braze, fortaleça as melhores práticas de entregabilidade e desenvolva um conjunto mais amplo de métricas para medir o desempenho.
- Implementem esse plano de resposta o mais rápido possível

Para uma visão geral detalhada de como se preparar para a Proteção de Privacidade do Apple Mail, confira nosso [post no blog](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare).