# PluginSettingContext

This "package" is a dependency for *your* package(s). It allows your users to enable/disable a key
binding by simply changing your package's settings. And all it requires you to do is to add:

```json
"context": [
    { "key": "package_setting.SettingsFileName.setting_to_enable_this_key_binding" }
]
```

That's it!

To make things clearer, here's when it's decomposed:

1. `package_setting.`: this prefix is needed and the exact same in every cases.
2. `SettingsFileName`: this part might be a bit more confusing. It the name of the setting file *without the extension* in which you write custom settings for the package. It usually is the same as the package name. It also usually have the extension `.sublime-settings`.
3. `setting_to_enable_this_key_binding`: simply the setting's name. It can be a bit more than that though, keep reading to get more :wink:

## Overview

A `YourPackage.sublime-settings` file:

```json
{
    "enabled_shortcut_my_super_command": true
}
```

```json
[
    {
        "keys": ["ctrl+l"],
        "command": "my_super_command",
        "context": [
            { "key": "package_setting.SettingsFileName.enabled_shortcut_my_super_command" }
        ]
    }
]
```

And this shortcut will work. But if you set `YourPackage.sublime-settings`'s content to:

```json
{
    "enabled_shortcut_my_super_command": false
}
```

You guessed it: this key binding wouldn't work any more. Pretty handy, right?

## Further infos

In the overview's example, the `operator: equal` and `operand: true` is implicit, but you can of
course change it:

```json
[
    {
        "keys": ["ctrl+l"],
        "command": "my_super_command",
        "context": [
            { "key": "package_setting.SettingsFileName.enabled_shortcut_my_super_command",
              "operand": "not_equal",
              "operator": "a string for example!"}
        ]
    }
]
```

The `key` is quiet clever too. Have a look:

In `Hello.sublime-settings`:

```json
{
    "my_setting": {
        "my_key": ["my", "list", {
            "and": "it goes on and",
            "on": true
        }]
    }
}
```

And your key binding:

```json
[
    {
        "keys": ["ctrl+l"],
        "command": "my_super_command",
        "context": [
            { "key": "package_setting.SettingsFileName.my_setting.my_key.2.on"}
        ]
    }
]
```

And it works!

## How to use it

### If you want to use this in your package

If you want to use this feature in your *package*, just [add it as a dependency],[]. So, for example

In your `dependencies.json`

```json
{
    "*": {
        "*": [
            "PackageSettingContext"
        ]
    }
}
```

### If you want to use this in your regular keymap

What you can do is actually set this as a dependency to your `User` package. Create the file
`Packages/User/dependencies.json`, and set the same content as above


[add it as a dependency]: https://packagecontrol.io/docs/dependencies
