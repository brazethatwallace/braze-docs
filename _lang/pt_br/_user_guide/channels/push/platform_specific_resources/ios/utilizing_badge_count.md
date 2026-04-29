---
nav_title: Utilizando a contagem de badges
article_title: Utilizando a contagem de badges
page_order: 8

page_type: reference
description: "Este artigo aborda o uso da contagem de badges no iOS para reengajar usuários que não perceberam uma notificação por push ou que desativaram as notificações por push em primeiro plano."
platform: iOS
channel:
- Push
- in-app messages

---

# Utilizando a contagem de badges {#utilizing-badge-count}

> A contagem de badges do iOS exibe o número de notificações não lidas no seu aplicativo, aparecendo como um círculo vermelho no canto superior direito do ícone do app. Nos últimos anos, os badges se tornaram um meio eficaz de reengajar usuários do app.

A contagem de badges pode ser usada para reengajar usuários que não perceberam uma notificação por push ou que desativaram as notificações por push em primeiro plano. Da mesma forma, pode ser usada para notificar seus usuários sobre mensagens não visualizadas, como atualizações no app.

## Contagem de badges com a Braze {#badge-count-with-braze}

Você pode especificar a contagem de badges desejada ao redigir uma notificação por push pelo dashboard da Braze. Isso pode ser definido como um atributo de usuário com envio de mensagens personalizado, permitindo uma lógica de personalização infinita. Se você deseja enviar um push silencioso que atualiza a contagem de badges sem incomodar o usuário, adicione a flag "Content-Available" ao seu push e deixe o conteúdo da mensagem vazio.

{% alert note %}
Quer saber como definir a contagem de badges no Android? O Android gerencia automaticamente os badges do app para push, então não há configurações de personalização para badges na Braze.
{% endalert %}

### Removendo a contagem de badges {#removing-the-badge-count}

Defina a contagem de badges como 0 ou "" para remover a contagem de badges do ícone do app. A Braze também limpa automaticamente o badge quando uma notificação por push é recebida enquanto o app está em primeiro plano.

## Práticas recomendadas {#best-practices}

Para otimizar o poder de reengajamento dos badges, é fundamental que você configure suas definições de badges de forma a simplificar ao máximo a experiência do usuário.

### Mantenha a contagem de badges baixa {#keep-the-badge-count-low}
Pesquisas mostram que, quando a contagem de badges ultrapassa dois dígitos, os usuários geralmente perdem o interesse nas atualizações e muitas vezes param de usar o app completamente.

> Pode haver exceções a essa regra dependendo da natureza do seu app (por exemplo, apps de e-mail e de mensagens em grupo).

### Limite o que a contagem de badges pode representar {#limit-the-things-a-badge-count-can-represent}
Ao usar badges, você quer tornar as notificações o mais claras e diretas possível. Ao limitar o número de coisas que uma notificação de badge pode representar, você proporciona aos seus usuários uma sensação de familiaridade com os recursos e atualizações do seu app.