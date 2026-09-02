---
nav_title: Vincular usuários do Web SDK or kit de desenvolvimento de software entre domínios
article_title: Vincular usuários do Web SDK or kit de desenvolvimento de software entre domínios por ID de dispositivo
page_order: 1
page_type: reference
description: "Passe o ID de dispositivo do Braze Web SDK or kit de desenvolvimento de software do site de marketing da Kitchenerie para um domínio de loja separado, para que a atividade anônima compartilhe um único perfil de usuário."
---

# Vincular usuários do Web SDK or kit de desenvolvimento de software entre domínios por ID de dispositivo {#link-cross-domain-web-sdk-users-through-device-id}

> Passe o ID de dispositivo do Braze Web SDK or kit de desenvolvimento de software pela URL de destino quando dois domínios não podem compartilhar cookies, para que sessões anônimas em ambos os sites sejam mapeadas para o mesmo perfil de usuário na Braze.

## Sobre este exemplo {#about-this-example}

A Kitchenerie, uma varejista fictícia de utensílios de cozinha, hospeda um site de marketing (`kitchenerie.com`) e uma loja (`kitchenerie.shop`). Cada domínio tem sua própria integração do Braze Web SDK or kit de desenvolvimento de software. Cookies do navegador não são compartilhados entre domínios, então a Braze atribui IDs de dispositivo separados — e perfis anônimos separados — quando o mesmo usuário navega do site de marketing para a loja.

Este padrão:

1. Lê o ID de dispositivo no domínio de origem com `getDeviceId` após a inicialização do SDK or kit de desenvolvimento de software
2. Anexa-o aos links de saída como um parâmetro de consulta (por exemplo, `brazeDeviceId`)
3. No domínio de destino, lê esse parâmetro e o passa para `braze.initialize` por meio da opção `deviceId`

A transferência é mais importante para usuários anônimos. Depois que o usuário faz login na loja, `changeUser` com um `external_id` se torna o identificador durável entre dispositivos. Consulte [Definir IDs de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).

Ambos os domínios devem usar a mesma chave de API or interface de programação do aplicativo (API) do espaço de trabalho da Braze e o mesmo endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software para que os eventos sejam registrados em um único perfil.

## Considerações {#considerations}

- O ID de dispositivo é por navegador. Este padrão não vincula atividades entre navegadores, dispositivos ou perfis diferentes. Use `external_id` por meio de `changeUser` para identidade autenticada entre dispositivos.
- Recupere o ID de dispositivo somente após o Web SDK or kit de desenvolvimento de software ser inicializado no domínio de origem. Chamar `getDeviceId` antes de `initialize` não retorna um valor.
- O Web SDK or kit de desenvolvimento de software lê `deviceId` uma única vez em `initialize`. Não existe um `setDeviceId` pós-inicialização que altere o ID de dispositivo ativo. Leia o parâmetro da URL no domínio de destino antes de chamar `initialize`.
- Visitas diretas, favoritos ou referências de terceiros para a loja sem `brazeDeviceId` devem recorrer à atribuição padrão de ID de dispositivo — comportamento esperado quando não há um ID do domínio de origem para herdar.
- Parâmetros de consulta aparecem no histórico do navegador e nos logs do servidor.
- Parâmetros de consulta podem vazar por meio de cabeçalhos de referência. O ID de dispositivo não é IPI por si só, mas remova o parâmetro após o consumo se sua equipe de privacidade exigir (consulte a Etapa 2).
- Teste de ponta a ponta. Confirme que os eventos do Domínio 2 usam o ID de dispositivo esperado com inspeção de rede.
- Adapte nomes de host, seletores de links e tratamento de erros ao seu site. Teste em seu ambiente de desenvolvimento antes de ir para produção.

## Configuração {#setup}

### Etapa 1: Anexar o ID de dispositivo aos links entre domínios no domínio de origem {#step-1-append-the-device-id-to-cross-domain-links-on-the-source-domain}

Em `kitchenerie.com` (Domínio 1), inicialize o Web SDK or kit de desenvolvimento de software normalmente e, em seguida, anexe o ID de dispositivo atual aos links que apontam para `kitchenerie.shop` (Domínio 2).

Escolha um nome de parâmetro de consulta que não colida com o seu site (este exemplo usa `brazeDeviceId`). A mesma ideia se aplica a links renderizados pelo servidor, navegação do lado do cliente ou valores de `src` de iframe que você controla.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example, javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

Se a sua versão do SDK or kit de desenvolvimento de software expõe `getDeviceId` de forma síncrona (sem retorno de chamada), chame-o após a inicialização:

```javascript
const deviceId = braze.getDeviceId();
```

Consulte [Guia do repositório do Web SDK or kit de desenvolvimento de software — Obter ID de dispositivo]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#get-device-id) e [Opções de inicialização — `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#initialization-options).

### Etapa 2: Ler o ID de dispositivo e inicializar o Web SDK or kit de desenvolvimento de software no domínio de destino {#step-2-read-the-device-id-and-initialize-the-web-sdk-on-the-destination-domain}

Em `kitchenerie.shop` (Domínio 2), leia `brazeDeviceId` da query string antes de `initialize` e passe-o nas opções de inicialização quando presente.

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

Quando o usuário fizer login, chame `changeUser` com o `external_id` dele para que a atividade futura seja vinculada ao perfil identificado.

### Etapa 3: Verificar a transferência {#step-3-verify-the-handoff}

1. Abra o Domínio 1 em um navegador onde você não está logado.
2. Siga um link entre domínios para o Domínio 2.
3. Na guia de rede do navegador, confirme que o Domínio 2 envia eventos com o mesmo ID de dispositivo usado pelo Domínio 1.
4. Repita com uma visita direta ao Domínio 2 (sem parâmetro de consulta) e confirme que um novo ID de dispositivo é atribuído.

## Artigos relacionados {#related-articles}

- [Guia do repositório do Web SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)
- [Integração multidomínio para o Braze Web SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Definir IDs de usuário por meio do Braze SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)
- [Usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)
- [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Armazenamento do Web SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/storage)