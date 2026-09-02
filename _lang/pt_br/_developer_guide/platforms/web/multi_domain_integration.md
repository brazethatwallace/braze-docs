---
nav_title: Integração multidomínio
article_title: Integração multidomínio para o SDK or kit de desenvolvimento de software da Braze para web
platform: Web
page_order: 23
page_type: reference
description: "Saiba como implementar o SDK or kit de desenvolvimento de software da Braze para web em vários domínios, incluindo estratégia de chave de API or interface de programação do aplicativo (API), configuração de push e comportamento de sessão."
---

# Integração multidomínio {#multi-domain-integration}

> Saiba como integrar o SDK or kit de desenvolvimento de software da Braze para web em vários domínios web.

Quando sua implementação abrange vários domínios, os limites de origem do navegador afetam a forma como o SDK or kit de desenvolvimento de software da Braze para web armazena e lê o estado do usuário.

## Escolha uma estratégia de app e chave de API or interface de programação do aplicativo (API) {#choose-an-app-and-api-key-strategy}

Você pode usar uma única chave de API or interface de programação do aplicativo (API) do SDK or kit de desenvolvimento de software para web em vários domínios, mas, na maioria dos casos, usar chaves de API or interface de programação do aplicativo (API) separadas mapeadas para apps separados no mesmo espaço de trabalho oferece mais controle.

| Estratégia | Recomendada quando | Compensações |
|---|---|---|
| **Apps separados (recomendado)** | Você deseja direcionamento, relatórios e controle de Campaign independentes por domínio | Requer o gerenciamento de duas integrações de app |
| **App único** | Você trata ambos os domínios como uma única propriedade operacionalmente | Disparos de sessão e relatórios por domínio são mais difíceis de separar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Opções de estratégia de app e chave de API or interface de programação do aplicativo (API)" }

Com apps separados em um espaço de trabalho, você pode usar filtros de app para uma segmentação mais limpa e direcionamento de mensagens por domínio.

## Configure notificações por push em um domínio {#configure-push-notifications-on-one-domain}

Para domínios raiz separados, o registro de web push é isolado por domínio.

- Escolha um domínio como seu domínio de notificações por push.
- Não registre push em ambos os domínios raiz para a mesma jornada de usuário, pois isso pode criar comportamentos conflitantes de solicitação e inscrição.

## Identifique usuários de forma consistente entre domínios {#identify-users-consistently-across-domains}

Por padrão, cada domínio raiz armazena seu próprio estado do SDK or kit de desenvolvimento de software. Para associar a atividade ao mesmo perfil de usuário da Braze entre domínios:

- Chame [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) com o mesmo `external_id` em cada domínio após o login.
- Mantenha ambos os apps no mesmo espaço de trabalho se estiver usando chaves de API or interface de programação do aplicativo (API) separadas.

Para orientações gerais sobre IDs de usuário, consulte [Definir IDs de usuário pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Planeje o comportamento de eventos e disparos por domínio {#plan-event-and-trigger-behavior-by-domain}

A forma como você modela eventos e disparos depende da sua estratégia de app:

- **App único entre domínios:** Registre eventos personalizados específicos do domínio para que você possa distinguir o comportamento por site na segmentação e nos disparos.
- **Apps separados:** Prefira filtros de app para direcionamento e análise de dados específicos por domínio.

## Entenda o comportamento de sessão entre domínios {#understand-session-behavior-across-domains}

Por padrão, o tempo limite de sessão do SDK or kit de desenvolvimento de software para web é de 30 minutos de inatividade. Para domínios raiz separados usando um único app/chave de API or interface de programação do aplicativo (API):

- Cada domínio inicia e encerra sessões de forma independente.
- Um usuário navegando entre ambos os domínios pode criar sessões sobrepostas.
- Disparos de início de sessão podem ser acionados em ambos os domínios.

Para detalhes sobre o ciclo de vida básico de sessões, consulte [Rastrear sessões pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).