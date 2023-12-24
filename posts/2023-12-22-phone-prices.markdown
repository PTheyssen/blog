---
title: Scraping Phone Prices
author: Philipp Theyssen
---

My Iphone 7 has really seen better days, thats why I recently started
looking for a new phone. 

I somehow want to stay with an Iphone, purely out of convenience.

I like to keep it minimal and have some nice apps,

even recently discovered flat habits / org-roam.

(Though eventually I should probably take the opensource android plunge)



Anyways, I think buying refurbed nowadays is a great option.

Though, I was really unsure about the price variations, and
wanted to record some historic prices for the models I am interested in.


## Models
- Iphone SE
- Iphone 12
- Iphone 13


As a first protopye I chose only a single website for to check the prices, of course in Germany there are websites like Idealo, which do exactly this but, but obviously thats less fun than writing you own webscraper.


## Quick python script

- 



## Update: retrieve actual phone parameters
The problem was that 






## Setting up a systemd timer in nixos

```nix
  systemd.timers."scrape-phone-prices" = {
    wantedBy = [ "timers.target" ];
    timerConfig = {
      OnBootSec = "30m";
      OnUnitActiveSec = "30m";
      Unit = "scrape-phone-prices.service";
    };
  };

  systemd.services."scrape-phone-prices" = {
    wantedBy = [ "multi-user.target" ];
    path = [
      pkgs.nix
      pkgs.bash
      (pkgs.python3.withPackages (ps: with ps; [
        numpy
        requests
        beautifulsoup4
      ]))
    ];
    script = ''
       python3 /home/pt/repos/phone-prices/scrape-phone-prices.py
    '';
    serviceConfig = {
      Type = "oneshot";
      User = "pt";
    };
  };
```



## Recorded Price Data

<img src="../images/prices-22-12-2023.svg" style="width:950px"/>


## Use Pyautogui for whats app
Ugly solution (though fascinating) sending whats app message to myself,
by opening new tab in browser.


## Using telegram bot (seems pretty easy to setup)


### Future (next in series)
- having custom price alert solution in place (fun + in futuer lots of possible savings)
- I really would like to move this to azure (azure functions),
- store sqlite file in azure storage account, ideally using terraform
