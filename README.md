# whingepool-alert
This script will check a whirlpool thread perioidcally for the latest post and fire a Discord webhook if it sees a fresh post.

I threw it together quickly hence the few bad bits of code and the Whirlpool API is very limiting (Can't even pull posts!).

## Installation
Basically update the API Key, thread, forum ID etc and throw this in a systemd unit file so it runs constantly.
