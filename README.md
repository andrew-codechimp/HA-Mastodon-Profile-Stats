# Home Assistant Mastodon Profile Stats Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
[![Community Forum][forum-shield]][forum]

[![BuyMeACoffee](https://img.shields.io/badge/-buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee&style=for-the-badge)](https://www.buymeacoffee.com/codechimp)


Integration to get profile stats from Mastodon instances (multiple supported).

*Please :star: this repo if you find it useful*

![Mastodon Profile Stats](https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats/blob/main/images/screenshot-device.png "Mastodon Profile Stats")


**This integration will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from Mastodon profile API, polled every 60 minutes

## Sensors

| Sensor      | Description                                                                                                                                                                                                               |
| :------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[PROFILE NAME]_[MASTODON INSTANCE]_followers`    | Number of followers                                                                                                                                                                                              |
| `[PROFILE NAME]_[MASTODON INSTANCE]_following` | Number of following                                                                                                      |
| `[PROFILE NAME]_[MASTODON INSTANCE]_statuses`     | Number of posts |

## Installation

### HACS

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=andrew-codechimp&repository=HA-Mastodon-Profile-Stats&category=Integration)

Or  
Search for `Mastodon Profile Stats` in HACS and install it under the "Integrations" category.  
Restart Home Assistant  
In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Mastodon Profile Stats"  

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

Multiple profiles are supported and the stats are updated every 60 minutes
<!---->

If you find this useful and want to show your support  

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/codechimp)

## Translations

You can help by adding missing translations when you are a native speaker. Or add a complete new language when there is no language file available.

Mastodon Profile Stats uses Crowdin to make contributing easy.

## Changing or adding to existing language

First register and join the translation project

- If you don’t have a Crowdin account yet, create one at [https://crowdin.com](https://crowdin.com)
- Go to the [Mastodon Profile Stats Crowdin project page](https://crowdin.com/project/mastodon-profile-stats)
- Click Join.

Next translate a string

- Select the language you want to contribute to from the dashboard.
- Click Translate All.
- Find the string you want to edit, missing translation are marked red.
- Fill in or modify the translation and click Save.
- Repeat for other translations.

Mastodon Profile Stats will automatically pull in latest changes to translations every day and create a Pull Request. After that is reviewed by a maintainer it will be included in the next release of Battery Notes.

## Adding a new language

Create an [Issue](https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats/issues/new?template=new_language_request.yml&title=New+Language) requesting a new language. We will do the necessary work to add the new translation to the integration and Crowdin site, when it's ready for you to contribute we'll comment on the issue you raised.


## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[mastodon_profile_stats]: https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats
[commits-shield]: https://img.shields.io/github/commit-activity/y/andrew-codechimp/HA-Mastodon-Profile-Stats.svg?style=for-the-badge
[commits]: https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/t/custom-component-mastodon-profile-stats/601024
[license-shield]: https://img.shields.io/github/license/andrew-codechimp/HA-Mastodon-Profile-Stats.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/andrew-codechimp/HA-Mastodon-Profile-Stats.svg?style=for-the-badge
[releases]: https://github.com/andrew-codechimp/HA-Mastodon-Profile-Stats/releases
