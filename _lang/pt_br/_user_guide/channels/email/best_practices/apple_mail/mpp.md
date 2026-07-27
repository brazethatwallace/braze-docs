---
nav_title: Proteção de privacidade de e-mail da Apple
article_title: Proteção de privacidade de e-mail da Apple para iOS 15
page_order: 1
description: "Este artigo de referência aborda a atualização da proteção de privacidade de e-mail da Apple, quem será afetado por ela e algumas etapas para se preparar para o recurso."
channel:
  - email

---

# Proteção de privacidade de e-mail da Apple {#apples-mail-privacy-protection}

> Este artigo aborda a Proteção de Privacidade de E-mail (MPP) da Apple, quem ela afeta e como se preparar para seu impacto nas métricas de entregabilidade de e-mail.

## O que é a atualização da proteção de privacidade de e-mail da Apple? {#what-is-apples-mail-privacy-protection-update}

A Proteção de Privacidade de E-mail (MPP) da Apple é uma atualização de privacidade disponível para usuários do app Apple Mail no iOS 15, iPadOS 15, macOS Monterey e watchOS 8, lançada em meados de setembro de 2021. Para os usuários que fizerem aceitação do MPP (o que prevemos que a maioria dos usuários fará), os e-mails agora serão pré-carregados usando servidores proxy, armazenando imagens em cache e dificultando a capacidade de aproveitar os pixels de rastreamento para métricas como [rastreamento de abertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement).

As marcas devem esperar que o MPP resulte em problemas com relação às métricas de entregabilidade de e-mail e problemas com Campaigns e Canvas pré-existentes que disparam com base nessas métricas. Para entender o impacto na entregabilidade de e-mail, consulte [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting).

### Quem será afetado por isso? {#who-will-this-affect}

Qualquer destinatário que esteja usando o app Apple Mail nativo em:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

Isso se aplica a todos os usuários que conectaram suas contas de e-mail ao app Apple Mail e fizeram aceitação do recurso de segurança, independentemente do serviço de e-mail (Gmail, Outlook, Yahoo, AOL, etc.). Esse impacto não se limita a assinantes que recebem e-mails em endereços Apple/iCloud/me.com.

{% alert important %}
Embora essas atualizações na entregabilidade de e-mail sejam significativas, o MPP não altera fundamentalmente nenhuma das regras que regem o e-mail e a entregabilidade. Em vez disso, ele impactará como medimos o sucesso e quais ferramentas e funcionalidades de e-mail poderão ser usadas daqui em diante.
{% endalert %}

## Como se preparar para o MPP? {#how-to-prepare-for-mpp}

O tempo é essencial para marcas que estão apenas começando a pensar em como responder ao MPP e seu potencial impacto no marketing por e-mail e nos esforços gerais de engajamento do cliente. Recomendamos que os usuários façam o seguinte:

- Avaliem o risco que o MPP representa para seus esforços de marketing
- Elaborem um plano de resposta direcionado ao MPP que aborde ajustes de automação na plataforma da Braze, fortaleça as melhores práticas de entregabilidade e desenvolva um conjunto mais amplo de métricas para medir o desempenho.
- Implementem esse plano de resposta o mais rápido possível

Para uma visão geral detalhada de como se preparar para a Proteção de Privacidade de E-mail da Apple, confira nosso [post no blog](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare).