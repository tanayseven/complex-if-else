#!/usr/bin/env bash
poetry run ptw --onpass "notify-send -a \"Tests passing [complex-if-else]\" \"Keep editing\""\
        --onfail "notify-send -u critical -a \"Tests failing [complex-if-else]\" \"Please check the console\""

