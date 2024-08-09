"""Custom integration to integrate mastodon_profile_stats with Home Assistant.

For more details about this integration, please refer to
https://github.com/andrew-codechimp/ha-mastodon_profile_stats
"""

from __future__ import annotations

from awesomeversion.awesomeversion import AwesomeVersion

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform, CONF_URL
from homeassistant.const import __version__ as HA_VERSION  # noqa: N812
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import MastodonProfileStatsApiClient
from .const import DOMAIN, LOGGER, MIN_HA_VERSION
from .coordinator import MastodonProfileStatsUpdateCoordinator

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
]


async def async_setup(
    hass: HomeAssistant,  # pylint: disable=unused-argument
    config: ConfigType,  # pylint: disable=unused-argument
) -> bool:
    """Integration setup."""

    if AwesomeVersion(HA_VERSION) < AwesomeVersion(MIN_HA_VERSION):  # pragma: no cover
        msg = (
            "This integration requires at least HomeAssistant version "
            f" {MIN_HA_VERSION}, you are running version {HA_VERSION}."
            " Please upgrade HomeAssistant to continue use this integration."
        )
        LOGGER.critical(msg)
        return False

    LOGGER.warning(
        "This integration has been discontinued, "
        "please remove the integration, delete within HACS and use the official "
        "integration https://www.home-assistant.io/integrations/mastodon"
    )

    return True


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up this integration using UI."""
    hass.data.setdefault(DOMAIN, {})

    hass.data[DOMAIN][entry.entry_id] = coordinator = (
        MastodonProfileStatsUpdateCoordinator(
            hass=hass,
            config_entry=entry,
            client=MastodonProfileStatsApiClient(
                session=async_get_clientsession(hass), url=entry.data[CONF_URL]
            ),
        )
    )
    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    if unloaded := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry.data)
    await async_setup_entry(hass, entry.data)
