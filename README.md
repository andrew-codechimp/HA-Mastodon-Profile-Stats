# Home Assistant Mastodon Profile Stats Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]

[![Community Forum][forum-shield]][forum]

_Integration to get profile stats from Mastodon instances._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from Mastodon profile API, polled every 60 minutes

## Sensors

| Sensor      | Description                                                                                                                                                                                                               |
| :------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[PROFILE NAME]_[MASTODON INSTANCE]_followers_count`    | Number of followers                                                                                                                                                                                              |
| `[PROFILE NAME]_[MASTODON INSTANCE]_following_count` | Number of following                                                                                                      |
| `[PROFILE NAME]_[MASTODON INSTANCE]_statuses_count`     | Number of posts |

## Installation

### HACS

1. Make sure the [HACS](https://github.com/custom-components/hacs) component is installed and working.
1. Add the project repository `https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats` as a custom repository to HACS, see: https://hacs.xyz/docs/faq/custom_repositories
1. Search for `Mastodon Profile Stats` in HACS and install it under the "Integrations" category.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Mastodon Profile Stats"

### Manual Installation

<details>
<summary>Show detailed instructions</summary>

Installation via HACS is recommended, but a manual setup is supported.

1. Manually copy custom_components/mastodon_profile_stats folder from latest release to custom_components folder in your config folder.
1. Restart Home Assistant.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Mastodon Profile Stats"

</details>

## Configuration is done in the UI

Add a profile via either @profilename@mastodoninstance or the url

Multiple profiles are supported
<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[mastodon_profile_stats]: https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats
[commits-shield]: https://img.shields.io/github/commit-activity/y/andrew-codechimp/HA-Mastodon-Profile-Stats.svg?style=for-the-badge
[commits]: https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/andrew-codechimp/HA-Mastodon-Profile-Stats.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/andrew-codechimp/HA-Mastodon-Profile-Stats.svg?style=for-the-badge
[releases]: https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats/releases
