"""Profile helper for MastodonProfileStats."""

from urllib.parse import urlparse

class MastodonProfile:
    """MastodonProfileStats Profile helper class."""

    def __init__(
        self,
        profile_url: str
    ) -> None:
        """Initialize the profile class."""
        self.profile_url = profile_url

    @property
    def native_value(self) -> str:
        """Return the native value of the profile."""
        return self.profile_url

    @property
    def apiurl(self) -> str:
        """Return the api url for profile."""

        # https://mastodon.online/@codechimp
        # https://mastodon.online/api/v1/accounts/lookup?acct=codechimp

        url_components = urlparse(self.profile_url)
        api = (url_components.scheme + '://' +
               url_components.netloc +
               '/api/v1/accounts/lookup?acct=' + url_components.path[2:])

        return api

    @property
    def profile_name(self) -> str:
        """Return the profile name."""

        # https://mastodon.online/@codechimp

        url_components = urlparse(self.profile_url)
        profile = url_components.path[2:]

        return profile
