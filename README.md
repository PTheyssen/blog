# Notes for using hakyll

When making changes to site.hs need to recompile with:

``` shell
cabal new-install --overwrite-policy=always
```


Build the site:
``` shell
site build
```

Preview the site: (localhost:8000)
``` shell
site watch
```



### Misc 

When making changes to css need to:
- make sure firefox is not caching previous result
