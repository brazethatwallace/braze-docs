---
nav_title: Entregabilidade para dispositivos Android chineses
article_title: Entregabilidade de push para dispositivos Android chineses
page_order: 10

page_type: reference
description: "Este artigo aborda nuances de entregabilidade de push que você deve conhecer ao direcionar usuários em dispositivos Android fabricados por OEMs chineses."
channel: push

---

# Entregabilidade de push para dispositivos Android chineses {#push-deliverability-for-chinese-android-devices}

> Alguns dispositivos Android fabricados por fabricantes de equipamentos originais (OEMs) chineses, como Xiaomi, OPPO e Vivo, otimizam a duração da bateria por meio de um gerenciamento agressivo do ciclo de vida dos apps. Essa otimização pode ter a consequência indesejada de encerrar o processamento de apps em segundo plano, o que pode reduzir a entregabilidade das suas notificações por push.<br><br>Para garantir que o desempenho de envio de mensagens do seu app funcione como esperado nesses dispositivos, suas equipes de marketing e engenharia devem colaborar e seguir as etapas descritas neste artigo.

## Etapas para desenvolvedores {#steps-for-developers}
Esses OEMs realizam suas otimizações encerrando agressivamente aplicações em segundo plano e impedindo que elas iniciem automaticamente para executar tarefas em background. Como desenvolvedor, você precisará configurar seu app para solicitar que o usuário alivie essas restrições sempre que possível.

Isso pode ser feito fazendo com que seu app inicie automaticamente no dispositivo do usuário final, o que dá ao app permissão para rodar em segundo plano e escutar mensagens da Braze. Infelizmente, como esse é um problema específico de OEMs e não do Android em si, não existem APIs documentadas para exibir o prompt de permissão de inicialização automática para cada OEM.

Para resolver isso, integre uma biblioteca como o [AutoStarter](https://github.com/judemanutd/AutoStarter) na sua aplicação. O AutoStarter oferece suporte a vários fabricantes, proporcionando uma maneira fácil de chamar o gerenciador de permissões de inicialização em uma ampla variedade de dispositivos. Após integrar o AutoStarter, chame `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para exibir o gerenciador de permissões de inicialização no dispositivo do usuário final. Combine essa ação com um prompt incentivando o usuário final a ativar a "inicialização automática" para o seu app. Sua equipe de marketing vai criar essa mensagem — veja a próxima seção!

## Etapas para profissionais de marketing {#steps-for-marketers}
Depois que seus usuários optarem por receber notificações por push, existem etapas adicionais que eles podem seguir para melhorar a entrega de mensagens nesses dispositivos. Recomendamos que você complemente sua [mensagem de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) com uma mensagem no app direcionada a usuários em dispositivos de OEMs chineses com estas etapas adicionais:

- Ativar a "inicialização automática" para o app
- Desativar a otimização de bateria para o app

Para amplificar ainda mais sua mensagem, adicione outros canais para reapresentar informações de notificações por push não abertas por meio de canais fora do app, como SMS, WhatsApp e LINE, e canais dentro do app, como mensagens no app e Content Cards. Seus usuários poderão ver tudo o que possam ter perdido na próxima vez que abrirem o app.