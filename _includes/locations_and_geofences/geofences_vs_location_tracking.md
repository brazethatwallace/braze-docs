In Braze, geofences and location tracking serve different purposes:

| | Location tracking | Geofences |
|---|---|---|
| Purpose | Segment users based on where they were | Trigger messaging when users enter or exit an area |
| Typical use | `Most Recent Location` and related filters | Real-time campaigns on geofence enter or exit |
| When location is evaluated | Updated when the app is open (session start); reflects the user's last known location | Monitored by the OS when location permissions allow, including when the app is in the background or closed |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Location tracking compared to geofences" }

- **Location tracking:** Collect and store each user's most recent location on their profile. You use this data for backward-looking segmentation—for example, the `Most Recent Location` filter targets users based on where they last opened your app, not necessarily where they are in real time.
- **Geofences:** Define virtual boundaries around a latitude, longitude, and radius. When a user enters or exits a boundary, Braze can trigger actions such as sending a campaign. Geofences require additional SDK setup beyond basic location tracking.

Both features require users to grant location permissions. If a user opts out of location tracking, previously stored location data isn't automatically removed from their profile, but new location data isn't collected.
