"""MastodonProfileStatsEntity class."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import CONF_URL

from .const import ATTRIBUTION, DOMAIN, NAME, VERSION
from .coordinator import MastodonProfileStatsUpdateCoordinator


class MastodonProfileStatsEntity(CoordinatorEntity):
    """MastodonProfileStatsEntity class."""

    _attr_attribution = ATTRIBUTION

    def __init__(self, coordinator: MastodonProfileStatsUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            name=NAME,
            model=VERSION,
            manufacturer=NAME,
            configuration_url=coordinator.config_entry.data.get(CONF_URL),
        )
