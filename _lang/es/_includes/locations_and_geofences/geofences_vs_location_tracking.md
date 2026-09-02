En Braze, las geovallas y el seguimiento de ubicación tienen propósitos diferentes:

| | Seguimiento de ubicación | Geovallas |
|---|---|---|
| Propósito | Segmentar usuarios según dónde estuvieron | Desencadenar mensajería cuando los usuarios entran o salen de un área |
| Uso típico | `Most Recent Location` y filtros relacionados | Campaigns en tiempo real al entrar o salir de una geovalla |
| Cuándo se evalúa la ubicación | Se actualiza cuando la aplicación está abierta (inicio de sesión); refleja la última ubicación conocida del usuario | Monitoreado por el sistema operativo cuando los permisos de ubicación lo permiten, incluso cuando la aplicación está en segundo plano o cerrada |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Location tracking compared to geofences" }

- **Seguimiento de ubicación:** Recopila y almacena la ubicación más reciente de cada usuario en su perfil. Usas estos datos para segmentación retrospectiva; por ejemplo, el filtro `Most Recent Location` se dirige a usuarios según dónde abrieron tu aplicación por última vez, no necesariamente donde se encuentran en tiempo real.
- **Geovallas:** Define límites virtuales alrededor de una latitud, longitud y radio. Cuando un usuario entra o sale de un límite, Braze puede desencadenar acciones como enviar una Campaign. Las geovallas requieren configuración adicional del SDK or kit de desarrollo de software más allá del seguimiento de ubicación básico.

Ambas características requieren que los usuarios otorguen permisos de ubicación. Si un usuario desactiva el seguimiento de ubicación, los datos de ubicación almacenados previamente no se eliminan automáticamente de su perfil, pero no se recopilan nuevos datos de ubicación.